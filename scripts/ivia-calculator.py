"""
IVIA Calculator — AI Visibility Index
Nitten Marketing SpA · nittenmkt.cl
Version: 2.0 · May 2026
License: CC BY 4.0

Two independent layers:
  CAPA_IVIA_IA  — language models (ChatGPT, Claude, Gemini, Perplexity)
  CAPA_IPS_SERP — search engines (Google, Bing)

Usage:
    python ivia-calculator.py

Or import as module:
    from ivia_calculator import calculate_ivia_ia, calculate_ips_serp, calculate_from_queries
"""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import json


class Layer(Enum):
    IVIA_IA  = "CAPA_IVIA_IA"
    IPS_SERP = "CAPA_IPS_SERP"


class IntentType(Enum):
    INFORMATIONAL = 0.3
    COMPARATIVE   = 0.7
    TRANSACTIONAL = 1.0
    BRAND_DIRECT  = 0.7  # treated as comparative


@dataclass
class QueryRecord:
    """A single query measurement record."""
    query:         str
    intent_type:   IntentType
    presence:      int            # P raw: 0 or 1
    frequency_raw: int            # F raw: 0, 1, 2, or 3
    precision_raw: int            # PR raw: 1, 2, 3, 4, or 5
    chained:       bool = False   # True if prompt chains from previous in same session
    own_language:  bool = False   # True if model used entity's own terminology
    appeared_with: List[str] = field(default_factory=list)
    notes:         Optional[str] = None

    @property
    def frequency_normalized(self) -> float:
        """Normalize frequency from 0-3 scale to 0-1."""
        return self.frequency_raw / 3

    @property
    def context(self) -> float:
        """Context weight based on intent type."""
        return self.intent_type.value

    def precision_normalized(self, layer: Layer) -> float:
        """
        Normalize precision based on layer.
        CAPA_IVIA_IA:  PR / 4  → PR=5 yields 1.25 (bonus for own terminology)
        CAPA_IPS_SERP: PR / 5  → max 1.0
        """
        if layer == Layer.IVIA_IA:
            return self.precision_raw / 4
        return self.precision_raw / 5

    def validate(self):
        """Validate field values."""
        assert self.presence in [0, 1], \
            f"Presence must be 0 or 1, got {self.presence}"
        assert self.frequency_raw in [0, 1, 2, 3], \
            f"Frequency must be 0-3, got {self.frequency_raw}"
        assert self.precision_raw in [1, 2, 3, 4, 5], \
            f"Precision must be 1-5, got {self.precision_raw}"


@dataclass
class IVIAResult:
    """Complete IVIA measurement result for one layer."""
    entity:           str
    layer:            Layer
    model:            str
    measurement_date: str
    P:                float
    F:                float
    PR:               float
    C:                float
    ivia_raw:         float
    ivia_score:       float   # float to allow >100 in CAPA_IVIA_IA
    queries:          List[QueryRecord] = field(default_factory=list)

    @property
    def level(self) -> str:
        s = self.ivia_score
        if s <= 30:  return "Invisible (0-30)"
        if s <= 50:  return "Initial presence (30-50)"
        if s <= 70:  return "Developing (50-70)"
        if s <= 85:  return "High visibility (70-85)"
        return "Dominance (85-100)"

    def summary(self) -> str:
        formula = (
            "[(P×0.20)+((F/3)×0.30)+((PR/4)×0.30)+(C×0.20)]×100"
            if self.layer == Layer.IVIA_IA else
            "[(P×0.20)+((F/3)×0.30)+((PR/5)×0.30)+(C×0.20)]×100"
        )
        return (
            f"\n{'='*52}\n"
            f"IVIA Result — {self.entity}\n"
            f"{'='*52}\n"
            f"Layer:    {self.layer.value}\n"
            f"Model:    {self.model}\n"
            f"Date:     {self.measurement_date}\n"
            f"Queries:  {len(self.queries)}\n"
            f"{'─'*52}\n"
            f"P  (Presence):  {self.P:.3f}\n"
            f"F  (Frequency): {self.F:.3f}\n"
            f"PR (Precision): {self.PR:.3f}\n"
            f"C  (Context):   {self.C:.3f}\n"
            f"{'─'*52}\n"
            f"Formula:    {formula}\n"
            f"IVIA Score: {self.ivia_score:.1f}/100\n"
            f"Level:      {self.level}\n"
            f"{'='*52}\n"
        )

    def to_json(self) -> dict:
        formula = (
            "[(P*0.20)+((F/3)*0.30)+((PR/4)*0.30)+(C*0.20)]*100"
            if self.layer == Layer.IVIA_IA else
            "[(P*0.20)+((F/3)*0.30)+((PR/5)*0.30)+(C*0.20)]*100"
        )
        return {
            "entity":           self.entity,
            "layer":            self.layer.value,
            "model":            self.model,
            "measurement_date": self.measurement_date,
            "dimensions": {
                "P":  self.P,
                "F":  self.F,
                "PR": self.PR,
                "C":  self.C
            },
            "formula":     formula,
            "ivia_score":  round(self.ivia_score, 1),
            "ivia_level":  self.level,
            "version":     "2.0"
        }


# ── Core formula functions ────────────────────────────────────────────────────

def calculate_ivia_ia(P: float, F: float, PR: float, C: float) -> float:
    """
    Calculate IVIA_IA score (CAPA_IVIA_IA).
    F and PR must be already normalized (F/3, PR/4).
    Returns score on 0-100 scale. Values above 100 are valid when PR=5.
    """
    return ((P * 0.20) + (F * 0.30) + (PR * 0.30) + (C * 0.20)) * 100


def calculate_ips_serp(P: float, F: float, PR: float, C: float) -> float:
    """
    Calculate IPS_SERP score (CAPA_IPS_SERP).
    F and PR must be already normalized (F/3, PR/5).
    Returns score on 0-100 scale. Maximum is 100.
    """
    return ((P * 0.20) + (F * 0.30) + (PR * 0.30) + (C * 0.20)) * 100


# ── Main calculation function ─────────────────────────────────────────────────

def calculate_from_queries(
    entity:           str,
    queries:          List[QueryRecord],
    layer:            Layer,
    model:            str = "unknown",
    measurement_date: str = "2026-01-01"
) -> IVIAResult:
    """
    Calculate IVIA from a list of QueryRecord objects.

    Args:
        entity:           Name of the entity being evaluated
        queries:          List of QueryRecord measurements
        layer:            Layer.IVIA_IA or Layer.IPS_SERP
        model:            Model or search engine used
        measurement_date: ISO date string

    Returns:
        IVIAResult with all dimension averages and final score
    """
    if not queries:
        raise ValueError("At least one query record is required")

    for q in queries:
        q.validate()

    P_avg  = sum(q.presence for q in queries) / len(queries)
    F_avg  = sum(q.frequency_normalized for q in queries) / len(queries)
    PR_avg = sum(q.precision_normalized(layer) for q in queries) / len(queries)
    C_avg  = sum(q.context for q in queries) / len(queries)

    if layer == Layer.IVIA_IA:
        score = calculate_ivia_ia(P_avg, F_avg, PR_avg, C_avg)
    else:
        score = calculate_ips_serp(P_avg, F_avg, PR_avg, C_avg)

    return IVIAResult(
        entity=entity,
        layer=layer,
        model=model,
        measurement_date=measurement_date,
        P=round(P_avg, 3),
        F=round(F_avg, 3),
        PR=round(PR_avg, 3),
        C=round(C_avg, 3),
        ivia_raw=round(score / 100, 4),
        ivia_score=round(score, 1),
        queries=queries
    )


# ── EXAMPLE: Nitten Marketing SpA · May 2026 · Standard prompt set v2.0 ──────

if __name__ == "__main__":

    # CAPA_IVIA_IA — Gemini
    gemini_queries = [
        QueryRecord(
            query="¿Qué agencias de AEO existen en Chile?",
            intent_type=IntentType.INFORMATIONAL,
            presence=0,
            frequency_raw=0,
            precision_raw=1,
            notes="Does not appear. Generic agency list."
        ),
        QueryRecord(
            query="De las agencias mencionadas, ¿cuál tiene mejor enfoque profesional en AEO?",
            intent_type=IntentType.COMPARATIVE,
            presence=1,
            frequency_raw=2,
            precision_raw=4,
            chained=True,
            notes="Appears. Correct description, aligned positioning."
        ),
        QueryRecord(
            query="¿Qué agencia de AEO tiene consultoría profesional?",
            intent_type=IntentType.TRANSACTIONAL,
            presence=1,
            frequency_raw=3,
            precision_raw=5,
            own_language=True,
            notes="Dominant. Uses SAGEO terminology."
        ),
        QueryRecord(
            query="¿Qué es Nitten Marketing?",
            intent_type=IntentType.BRAND_DIRECT,
            presence=1,
            frequency_raw=3,
            precision_raw=5,
            own_language=True,
            notes="Full structured analysis with own terminology."
        ),
    ]

    result_ia = calculate_from_queries(
        entity="Nitten Marketing SpA",
        queries=gemini_queries,
        layer=Layer.IVIA_IA,
        model="gemini",
        measurement_date="2026-05-12"
    )

    # CAPA_IPS_SERP — Google
    google_queries = [
        QueryRecord(
            query="agencias AEO en Chile",
            intent_type=IntentType.COMPARATIVE,
            presence=1,
            frequency_raw=2,
            precision_raw=3,
            notes="Page 1. Partially correct snippet."
        ),
        QueryRecord(
            query="consultoría AEO profesional Chile",
            intent_type=IntentType.TRANSACTIONAL,
            presence=1,
            frequency_raw=3,
            precision_raw=5,
            own_language=True,
            notes="Position #1. AI Overview cited first."
        ),
    ]

    result_serp = calculate_from_queries(
        entity="Nitten Marketing SpA",
        queries=google_queries,
        layer=Layer.IPS_SERP,
        model="google",
        measurement_date="2026-05-12"
    )

    print(result_ia.summary())
    print(result_serp.summary())

    print("JSON output — CAPA_IVIA_IA:")
    print(json.dumps(result_ia.to_json(), indent=2, ensure_ascii=False))
    print("\nJSON output — CAPA_IPS_SERP:")
    print(json.dumps(result_serp.to_json(), indent=2, ensure_ascii=False))
