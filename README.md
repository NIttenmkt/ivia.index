# IVIA — AI Visibility Index

IVIA (AI Visibility Index) is an open two-layer framework for measuring how entities are recognized, cited, and described within AI-generated responses and traditional search results.

IVIA is part of the SAGEO methodology (Search AI & Generative Engine Optimization), developed by Nitten Marketing SpA (Santiago, Chile) and first validated in April 2026 on the domain nittenmkt.cl.

**IVIA measures visibility where traditional SEO cannot: inside AI-generated answers.**

---

## Why IVIA exists

Traditional SEO metrics measure ranking and traffic.
IVIA measures something different:

- Whether an entity appears in AI-generated responses and search results
- How often and how prominently it is mentioned
- Whether it is described correctly and aligned with its real value proposition
- Whether it appears in high-intent queries

As generative AI systems replace traditional search for many queries, visibility shifts from ranking to inclusion. IVIA is an attempt to make that shift measurable. In AI systems, entities are not ranked — they are selected.

---

## Structure: two independent layers (v2.0)

IVIA v2.0 separates measurement into two distinct layers with different formulas. Both share the same four dimensions and the same F and C scales, but differ in PR normalization — because the precision standard in a generative response (AI) differs from that of an organic result (SERP).

| Layer | Systems evaluated | PR normalization |
|-------|-------------------|-----------------|
| `CAPA_IVIA_IA` | ChatGPT · Claude · Gemini · Perplexity | PR ÷ 4 |
| `CAPA_IPS_SERP` | Google · Microsoft Bing | PR ÷ 5 |

---

## The four dimensions

Dimensions are shared across both layers.

| Dimension | Code | What it measures | Scale |
|-----------|------|-----------------|-------|
| Presence | P | Does the entity appear? | 0–1 |
| Frequency | F | How intensely is it mentioned per response? | 0–3, normalized ÷3 |
| Precision | PR | Is the entity described correctly and aligned with its real value proposition? | 1–5 (see below) |
| Context | C | What type of query triggered the appearance? | 0.3 / 0.7 / 1.0 |

**Context weights:**
- Informational query → `0.3`
- Comparative query → `0.7`
- Transactional query → `1.0`

**Precision scale v2.0 (1–5):**
- `1` — Incorrect
- `2` — Incorrect attributes
- `3` — Partially correct
- `4` — Correct and aligned with actual positioning
- `5` — Correct with entity's own terminology

**Frequency scale:**
- `0` — Absent
- `1` — Mentioned once / low visibility
- `2` — Detailed / visible and contextualized
- `3` — Dominant / Top 3 with high prominence

---

## Scoring model

### CAPA_IVIA_IA (language models)

```
IVIA_IA = [(P × 0.20) + ((F/3) × 0.30) + ((PR/4) × 0.30) + (C × 0.20)] × 100
```

PR normalization ÷4 allows PR=5 (entity's own terminology) to produce a value above 1.0, reflecting the strategic benefit of a model adopting the entity's own language. Scores above 100 are possible in cases of total dominance and are expected behavior.

### CAPA_IPS_SERP (search engines)

```
IPS_SERP = [(P × 0.20) + ((F/3) × 0.30) + ((PR/5) × 0.30) + (C × 0.20)] × 100
```

PR normalization ÷5 sets a maximum of 1.0 with no bonus. In SERP, maximum precision equates to correct position and aligned representation.

Both results are expressed on a 0–100 scale and interpreted using the same scale, enabling direct comparison between generative and organic visibility.

---

## Standard prompt set v2.0

Prompts are executed in sequence within the same session. The comparative prompt chains from the informational response, testing both initial recognition and competitive evaluation.

| # | Type | Prompt |
|---|------|--------|
| 1 | Informational | "What [category] agencies exist in [market]?" |
| 2 | Comparative | "Of the agencies mentioned, which has the strongest professional approach in [category]?" |
| 3 | Transactional | "Which [category] agency offers professional consulting?" |
| 4 | Brand | "What is [entity name]?" |

Minimum: 3 repetitions per prompt per model to average model variability.

---

## Interpretation scale

Valid for both layers.

| Score | Level | Implication |
|-------|-------|-------------|
| 0–30 | Invisible | Entity not interpretable by the evaluated systems |
| 30–50 | Initial presence | Appears but with imprecise descriptions or low-value queries |
| 50–70 | Developing | Verifiable citation in specific queries. Main gap: high-intent queries and other models |
| 70–85 | High visibility | Consistent presence, precise descriptions across multiple models or search engines |
| 85–100 | Dominance | Reference entity in its category for generative systems |

---

## Version history

| Version | Date | Status | Key changes |
|---------|------|--------|-------------|
| v1.0 | Mar 2026 | Archived · `/archive/v1/` | Single unified formula. PR 3-level scale (0 / 0.5 / 1.0). Manual measurement in LLMs only. No independent SERP layer. |
| v2.0 | May 2026 | **Current** | Two independent layers: CAPA_IVIA_IA and CAPA_IPS_SERP. PR 5-level scale (1–5). PR÷4 normalization in IA, PR÷5 in SERP. Models evaluated separately from search engines. Standardized 4-prompt sequential set. |
| v3.0 | In design | — | Automated execution via n8n + LLM APIs. Automated score parsing without manual validation. Exportable cycle report. |

---

## Status

**v2.0 — Active**

IVIA is an evolving framework. Current results should be interpreted as directional rather than statistically definitive. See `/docs/limitaciones.md` for a full declaration of limitations.

v1.0 is archived at `/archive/v1/` with tag `v1.0`. Methodological traceability is preserved intentionally.

---

## Validated case

**Entity:** Nitten Marketing SpA · nittenmkt.cl
**Period:** February – May 2026
**S(0):** 0/100 (both layers) — February 22, 2026

| Layer | Score | Level |
|-------|-------|-------|
| IVIA_IA (LLMs) | 60.9 / 100 | Developing |
| IPS_SERP (search engines) | 75.0 / 100 | High visibility |

The gap between layers — higher SERP than IA — is one of the key diagnostic signals of the system. It indicates strong organic positioning not yet fully translated into generative citation.

See `/examples/nitten-case.md` for the full documented case including prompt protocols, raw scores, and analysis.

---

## Use cases

- Evaluate AI visibility of brands and organizations
- Track evolution across implementation cycles
- Compare entities in the same market segment
- Establish a baseline before and after semantic infrastructure work
- Diagnose gaps between generative visibility (IVIA_IA) and organic visibility (IPS_SERP)

---

## Conceptual shift

IVIA is based on a structural change:

> Search engines rank documents.
> AI systems generate answers.

Visibility is no longer about ranking pages, but about being included in generated responses. The gap between IVIA_IA and IPS_SERP is the measurable expression of that shift for any given entity.

---

## Related framework

IVIA is the measurement instrument of SAGEO (Search AI & Generative Engine Optimization), a four-layer methodology for digital visibility in the AI era:

```
SEO (TOFU) → AEO (MOFU) → GEO (MOFU→BOFU) → ASO (BOFU)
```

Full methodology documentation: [nittenmkt.cl/aeo/](https://nittenmkt.cl/aeo/)
Case study paper: [nittenmkt.cl/aeo-como-sistema/](https://nittenmkt.cl/aeo-como-sistema/)

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to use, adapt, and build upon this framework for any purpose, including commercial, as long as you give appropriate credit to Nitten Marketing SpA.

---

## How to cite

```
Nitten Marketing SpA. (2026). IVIA — AI Visibility Index (v2.0).
GitHub. https://github.com/NIttenmkt/ivia.index
```

Or use the `CITATION.cff` file for automated citation tools.

---

## Author

**Nitten Marketing SpA**
Santiago, Chile
[nittenmkt.cl](https://nittenmkt.cl) · agencia@nittenmkt.cl

Developed by the Nitten team. Consolidated and presented by Maximiliano Acuña, OCC.

*Algoritmos que atraen. Activaciones que venden.*
