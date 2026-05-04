# IVIA — AI Visibility Index

**IVIA** (AI Visibility Index) is an experimental framework for measuring how entities are recognized, cited, and described within AI-generated responses.

It was developed as part of the **SAGEO methodology** by Nitten Marketing SpA (Santiago, Chile) and first validated in April 2026 on the domain [nittenmkt.cl](https://nittenmkt.cl).

---

## Why IVIA exists

Traditional SEO metrics measure ranking and traffic.  
IVIA measures something different:

- Whether an entity **appears** in AI-generated responses
- **How often** it is mentioned
- Whether it is **described correctly**
- Whether it appears in **high-intent queries**

As generative AI systems replace traditional search for many queries, visibility shifts from *ranking* to *inclusion*. IVIA is an attempt to make that shift measurable.

---

## The four dimensions

| Dimension | Code | What it measures | Scale |
|-----------|------|-----------------|-------|
| Presence | P | Does the entity appear in AI responses? | 0–1 |
| Frequency | F | How intensely is it mentioned per response? | 0–3, normalized /3 |
| Precision | PR | Is the entity described correctly and aligned with its real value proposition? | 0 / 0.5 / 1 |
| Context | C | What type of query triggered the appearance? | 0.3 / 0.7 / 1.0 |

**Context weights:**
- Informational query → `0.3`
- Comparative query → `0.7`
- Transactional query → `1.0`

**Precision scores:**
- `0` — Incorrect or absent
- `0.5` — Partially correct
- `1.0` — Correct and aligned with actual positioning

---

## Formula

```
IVIA = (P × 0.20) + (F × 0.30) + (PR × 0.30) + (C × 0.20)
```

Result expressed on a 0–100 scale (multiply by 100).

---

## Interpretation scale

| Score | Level | Implication |
|-------|-------|-------------|
| 0–30 | Invisible | Entity not interpretable by generative systems |
| 30–50 | Initial presence | Appears but with imprecise descriptions or low-value queries |
| 50–70 | Developing | Verifiable citation in specific queries. Main gap: high-intent queries and secondary models |
| 70–85 | High visibility | Consistent presence, precise descriptions across multiple models |
| 85–100 | AI dominance | Reference entity in its category for generative systems |

---

## Status

`v1.0 — Exploratory`

IVIA is an exploratory instrument. It is not a standardized metric and has not been validated by third parties. Its value is directional, not statistically precise. See [/docs/limitaciones.md](/docs/limitaciones.md) for a full declaration of limitations.

---

## First validated case

**Entity:** Nitten Marketing SpA · nittenmkt.cl  
**Period:** July 2025 – April 2026  
**IVIA result:** 64/100 (Developing)  

See [/examples/nitten-case.md](/examples/nitten-case.md) for the full documented case including prompt protocols, raw scores, and analysis.

---

## Use cases

- Evaluate AI visibility of brands and organizations
- Track evolution across implementation cycles
- Compare entities in the same market segment
- Establish a baseline before and after semantic infrastructure work

---

## Related framework

IVIA is the measurement instrument of **SAGEO** (Search AI & Generative Engine Optimization), a four-layer methodology for digital visibility in the AI era:

```
SEO (TOFU) → AEO (MOFU) → GEO (MOFU→BOFU) → ASO (BOFU)
```

Full methodology documentation: [nittenmkt.cl/aeo/](https://nittenmkt.cl/aeo/)  
Case study paper: [nittenmkt.cl/aeo-como-sistema/](https://nittenmkt.cl/aeo-como-sistema/)

---

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)

You are free to use, adapt, and build upon this framework for any purpose, including commercial, as long as you give appropriate credit to Nitten Marketing SpA.

---

## How to cite

```
Nitten Marketing SpA. (2026). IVIA — AI Visibility Index (v1.0).
GitHub. https://github.com/nitten/ivia-index
```

Or use the [CITATION.cff](CITATION.cff) file for automated citation tools.

---

## Author

**Nitten Marketing SpA**  
Santiago, Chile  
[nittenmkt.cl](https://nittenmkt.cl) · agencia@nittenmkt.cl
Initial release — IVIA v0.1

*Developed by the Nitten team. Consolidated and presented by Maximiliano Acuña, OCC.*

---

*Algoritmos que atraen. Activaciones que venden.*
