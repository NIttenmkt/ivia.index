"""
IVIA Calculator — AI Visibility Index
Nitten Marketing SpA · nittenmkt.cl
Version: 1.0 · May 2026
License: CC BY 4.0

Usage:
    python ivia-calculator.py

Or import as module:
    from ivia_calculator import calculate_ivia, calculate_from_queries
"""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import json


class IntentType(Enum):
    INFORMATIONAL = 0.3
    COMPARATIVE = 0.7
    TRANSACTIONAL = 1.0
    BRAND_DIRECT = 0.7  # treated as comparative


@dataclass
class QueryRecord:
    """A single query measurement record."""
    query: str
    intent_type: IntentType
    presence: int          # P raw: 0 or 1
    frequency_raw: int     # F raw: 0, 1, 2, or 3
    precision: float       # PR: 0, 0.5, or 1.0
    notes: Optional[str] = None

    @property
    def frequency_normalized(self) -> float:
        """Normalize frequency from 0-3 scale to 0-1."""
        return self.frequency_raw / 3

    @property
    def context(self) -> float:
        """Context weight based on intent type."""
        return self.intent_type.value

    def validate(self):
        """Validate field values."""
        assert self.presence in [0, 1], f"Presence must be 0 or 1, got {self.presence}"
        assert self.frequency_raw in [0, 1, 2, 3], f"Frequency must be 0-3, got {self.frequency_raw}"
        assert self.precision in [0, 0.5, 1.0], f"Precision must be 0, 0.5 or 1.0, got {self.precision}"


@dataclass
class IVIAResult:
    """Complete IVIA measurement result."""
    entity: str
    model: str
    measurement_date: str
    P: float
    F: float
    PR: float
    C: float
    ivia_raw: float
    ivia_score: int
    queries: List[QueryRecord] = field(default_factory=list)

    @property
    def level(self) -> str:
        if self.ivia_score <= 30:
            return "Invisible (0-30)"
        elif self.ivia_score <= 50:
            return "Initial presence (30-50)"
        elif self.ivia_score <= 70:
            return "Developing (50-70)"
        elif self.ivia_score <= 85:
            return "High visibility (70-85)"
        else:
            return "AI dominance (85-100)"

    def summary(self) -> str:
        return (
            f"\n{'='*50}\n"
            f"IVIA Result — {self.entity}\n"
            f"{'='*50}\n"
            f"Model:    {self.model}\n"
            f"Date:     {self.measurement_date}\n"
            f"Queries:  {len(self.queries)}\n"
            f"{'─'*50}\n"
            f"P  (Presence):  {self.P:.2f}\n"
            f"F  (Frequency): {self.F:.2f}\n"
            f"PR (Precision): {self.PR:.2f}\n"
            f"C  (Context):   {self.C:.2f}\n"
            f"{'─'*50}\n"
            f"IVIA Score: {self.ivia_score}/100\n"
            f"Level:      {self.level}\n"
            f"{'='*50}\n"
        )

    def to_json(self) -> dict:
        return {
            "entity": self.entity,
            "model": self.model,
            "measurement_date": self.measurement_date,
            "dimensions": {
                "P": self.P,
                "F": self.F,
                "PR": self.PR,
                "C": self.C
            },
            "formula": "(P*0.20)+(F*0.30)+(PR*0.30)+(C*0.20)",
            "ivia_score": self.ivia_score,
            "ivia_level": self.level,
            "version": "1.0"
        }


def calculate_ivia(P: float, F: float, PR: float, C: float) -> float:
    """
    Calculate IVIA from dimension values.

    Args:
        P:  Presence (0-1)
        F:  Frequency normalized (0-1)
        PR: Precision (0, 0.5, or 1.0)
        C:  Context weight (0.3, 0.7, or 1.0)

    Returns:
        IVIA score as float (0-1)
    """
    return (P * 0.20) + (F * 0.30) + (PR * 0.30) + (C * 0.20)


def calculate_from_queries(
    entity: str,
    queries: List[QueryRecord],
    model: str = "unknown",
    measurement_date: str = "2026-01-01"
) -> IVIAResult:
    """
    Calculate IVIA from a list of QueryRecord objects.

    Args:
        entity: Name of the entity being evaluated
        queries: List of QueryRecord measurements
        model: AI model used (e.g. 'gemini', 'chatgpt')
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
    PR_avg = sum(q.precision for q in queries) / len(queries)
    C_avg  = sum(q.context for q in queries) / len(queries)

    ivia_raw = calculate_ivia(P_avg, F_avg, PR_avg, C_avg)
    ivia_score = round(ivia_raw * 100)

    return IVIAResult(
        entity=entity,
        model=model,
        measurement_date=measurement_date,
        P=round(P_avg, 3),
        F=round(F_avg, 3),
        PR=round(PR_avg, 3),
        C=round(C_avg, 3),
        ivia_raw=round(ivia_raw, 4),
        ivia_score=ivia_score,
        queries=queries
    )


# ─── EXAMPLE: Nitten Marketing SpA case (April 2026) ──────────────────────────

if __name__ == "__main__":

    nitten_queries = [
        QueryRecord(
            query="Evaluating a digital marketing agency in Chile focused on AI positioning",
            intent_type=IntentType.COMPARATIVE,
            presence=0,
            frequency_raw=0,
            precision=0,
            notes="Does not appear. Gemini names Best Solution, Postedin, Adinfluence"
        ),
        QueryRecord(
            query="Agencies working AEO and GEO in an integrated way",
            intent_type=IntentType.COMPARATIVE,
            presence=1,
            frequency_raw=1,
            precision=1.0,
            notes="Appears 2nd. Correct description. Gemini uses 'Arquitectura de Respuesta'"
        ),
        QueryRecord(
            query="What do you know about Nitten Marketing in Chile?",
            intent_type=IntentType.BRAND_DIRECT,
            presence=1,
            frequency_raw=2,
            precision=1.0,
            notes="Full structured analysis. Strengths and gaps coherent with real positioning"
        ),
        QueryRecord(
            query="agencias AEO en Chile (Google AI Overviews)",
            intent_type=IntentType.TRANSACTIONAL,
            presence=1,
            frequency_raw=1,
            precision=1.0,
            notes="Position #1 organic. Cited first in AI Overviews"
        ),
    ]

    result = calculate_from_queries(
        entity="Nitten Marketing SpA",
        queries=nitten_queries,
        model="gemini",
        measurement_date="2026-04-29"
    )

    print(result.summary())
    print("JSON output:")
    print(json.dumps(result.to_json(), indent=2, ensure_ascii=False))
