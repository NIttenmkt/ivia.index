---
title: "IVIA — Caso validado: Nitten Marketing SpA"
description: "Segunda medición IVIA aplicada al dominio nittenmkt.cl bajo metodología v2.0. Dos capas independientes: CAPA_IVIA_IA 60.9/100 · CAPA_IPS_SERP 75.0/100."
entity: "Nitten Marketing SpA"
domain: "nittenmkt.cl"
period: "Julio 2025 – Mayo 2026"
measurement_date: "2026-05-12"
models_tested:
  - ChatGPT
  - Claude
  - Gemini
  - Perplexity
  - Google
  - Bing
ivia_ia_result: 60.9
ips_serp_result: 75.0
ivia_level: "Posicionamiento en desarrollo (IVIA_IA) · Alta visibilidad (IPS_SERP)"
version: "2.0"
related:
  - metodologia.md
  - limitaciones.md
---

# IVIA — Caso validado: Nitten Marketing SpA

## Historial de mediciones

| Ciclo | Fecha | Metodología | IVIA_IA | IPS_SERP | Nivel |
|-------|-------|-------------|---------|----------|-------|
| S(0) | 22 feb 2026 | Pre-IVIA | 0 / 100 | — | Invisible |
| Ciclo 1 | 29 abr 2026 | IVIA v1.0 | 64 / 100 | — | Posicionamiento en desarrollo |
| Ciclo 2 | 12 may 2026 | IVIA v2.0 | 60.9 / 100 | 75.0 / 100 | IVIA_IA: en desarrollo · IPS_SERP: alta visibilidad |

**Nota sobre la variación Ciclo 1 → Ciclo 2:** la diferencia de 64 → 60.9 en IVIA_IA no indica retroceso. Refleja el cambio de metodología: v2.0 evalúa 4 modelos (vs. Gemini en v1.0), el promedio cross-model es más conservador y más representativo. Los modelos donde Nitten tiene menor presencia (Gemini en queries genéricas) pesan igual que los de mayor presencia (ChatGPT, Claude).

---

## Contexto del caso

- **Entidad:** Nitten Marketing SpA
- **Dominio:** nittenmkt.cl
- **Sector:** Marketing digital y BTL — Santiago, Chile
- **Período de implementación:** Julio 2025 – Mayo 2026
- **Fecha de medición:** 12 de mayo de 2026
- **Antigüedad del dominio:** menos de 12 meses
- **Inversión publicitaria para las queries objetivo:** ninguna

Este caso documenta la primera medición bajo metodología IVIA v2.0 aplicada al dominio de Nitten, utilizado como laboratorio de implementación de SAGEO antes de ofrecer el servicio a clientes externos.

---

## Infraestructura implementada antes de la medición

- JSON-LD con @graph completo (Organization, WebPage, FAQPage, Service, DefinedTermSet, SpeakableSpecification) vía WPCode tipo PHP
- llms.txt en la raíz del dominio con rutas a documentos semánticos
- llms-full.txt (en implementación)
- Biblioteca /aeo/ con documentos .md con frontmatter YAML y referencias cruzadas
- nitten-context.xml (sitemap híbrido AI)
- Presencia verificada en GBP, Clutch, Sortlist y LinkedIn
- ai-brief.md, servicios-ia.json, knowledge-index.json, openapi.yaml
- Core Web Vitals aprobada. PageSpeed Insights mobile: 90+

---

## CAPA_IVIA_IA — Resultados por modelo

### Scores por modelo

| Modelo | IVIA Promedio | % Presencia | Precisión promedio | % Top 3 |
|--------|--------------|-------------|-------------------|---------|
| ChatGPT | 107.5 | 75% | Alta | 75% |
| Perplexity | 93.5 | 100% | Alta | 100% |
| Claude | 53.0 | 50% | Media | 50% |
| Gemini | 48.5 | 25% | Media | 25% |
| **Global** | **60.9** | **62.5%** | — | — |

### Registro de scores por query y modelo

| Modelo | Tipo | Query | P | F | PR | C | Score |
|--------|------|-------|---|---|----|---|-------|
| Gemini | Informacional | ¿Qué es el AEO en Chile? | 0 | 0 | 1 | 0.3 | 6.0 |
| Gemini | Comparativo | Mejores agencias de AEO en Chile | 0 | 0 | 3 | 1.0 | 42.5 |
| Gemini | Comparativo | ¿Cuál agencia de AEO tiene consultoría profesional? | 0 | 0 | 1 | 0.7 | 14.0 |
| Gemini | Marca | ¿Qué es Nitten Marketing? | 1 | 3 | 4 | 0.7 | 94.0 |
| Perplexity | Informacional | ¿Qué es el AEO en Chile? | 0 | 0 | 1 | 0.3 | 6.0 |
| Perplexity | Comparativo | Mejores agencias de AEO en Chile | 1 | 2 | 4 | 0.7 | 84.0 |
| Perplexity | Transaccional | ¿Cuál agencia de AEO tiene consultoría profesional? | 1 | 3 | 5 | 0.3 | 93.5 |
| Perplexity | Marca | ¿Qué es Nitten Marketing? | 1 | 3 | 5 | 0.3 | 93.5 |
| Claude | Informacional | ¿Qué es el AEO en Chile? | 0 | 0 | 1 | 0.3 | 6.0 |
| Claude | Comparativo | Mejores agencias de AEO en Chile | 1 | 3 | 5 | 0.3 | 93.5 |
| Claude | Transaccional | ¿Cuál agencia de AEO tiene consultoría profesional? | 0 | 0 | 1 | 0.3 | 6.0 |
| Claude | Marca | ¿Qué es Nitten Marketing? | 1 | 3 | 5 | 1.0 | 107.5 |
| ChatGPT | Informacional | ¿Qué es el AEO en Chile? | 0 | 0 | 1 | 0.3 | 6.0 |
| ChatGPT | Comparativo | Mejores agencias de AEO en Chile | 1 | 3 | 5 | 1.0 | 107.5 |
| ChatGPT | Transaccional | ¿Cuál agencia de AEO tiene consultoría profesional? | 1 | 3 | 5 | 1.0 | 107.5 |
| ChatGPT | Marca | ¿Qué es Nitten Marketing? | 1 | 3 | 5 | 1.0 | 107.5 |

**Nota sobre PR:** escala 1–5. Normalización PR÷4 en CAPA_IVIA_IA. PR=5 produce valor 1.25 en la fórmula.

### Cálculo IVIA_IA global

```
IVIA_IA = [(P×0.20) + ((F/3)×0.30) + ((PR/4)×0.30) + (C×0.20)] × 100

Por dimensión:
P  — Presencia:  56.3
F  — Frecuencia: 54.2
PR — Precisión:  71.9
C  — Contexto:   59.4

IVIA_IA global: 60.9 / 100
Nivel: Posicionamiento en desarrollo (50–70)
```

---

## CAPA_IPS_SERP — Resultados por buscador

| Buscador | Query | P | F | PR | C | Score |
|----------|-------|---|---|----|---|-------|
| Google | Agencias AEO en Chile | 1 | 2 | 3 | 0.3 | 64.0 |
| Bing | Agencias AEO en Chile | 1 | 3 | 5 | 0.3 | 86.0 |

### Cálculo IPS_SERP global

```
IPS_SERP = [(P×0.20) + ((F/3)×0.30) + ((PR/5)×0.30) + (C×0.20)] × 100

IPS_SERP global: 75.0 / 100
Nivel: Alta visibilidad (70–85)
```

---

## Análisis de brecha entre capas

| Capa | Score | Nivel |
|------|-------|-------|
| IPS_SERP | 75.0 | Alta visibilidad |
| IVIA_IA | 60.9 | Posicionamiento en desarrollo |
| **Brecha** | **14.1 puntos** | SERP supera a IA |

La brecha positiva SERP→IA indica que la visibilidad orgánica está más consolidada que la generativa. El posicionamiento técnico (Schema, Core Web Vitals, estructura semántica) se tradujo más rápido en resultados de búsqueda tradicional que en citación por LLMs. Es el patrón esperado en implementaciones tempranas.

---

## Observación metodológica detectada en este ciclo

Cambios fuertes de estructura generan latencia en Gemini orgánico y Google SERP, pero no en AI Overview. Hipótesis: AI Overview opera con pipeline de indexación distinto, posiblemente caché propio o snapshot más estable. Esta hipótesis será evaluada en el Ciclo 3.

---

## Nota sobre el set de prompts de este ciclo

Este ciclo utilizó un set de prompts previo a la estandarización v2.0. El set incluyó un prompt informacional de definición de disciplina ("¿Qué es el AEO en Chile?") que, por diseño, no puede producir aparición de ninguna agencia. Su utilidad es como control, no como indicador de presencia.

A partir del Ciclo 3 (julio 2026), se aplicará el set estándar v2.0:
1. Informacional: "¿Qué agencias de AEO existen en Chile?"
2. Comparativo encadenado: "De las agencias mencionadas, ¿cuál tiene mejor enfoque profesional?"
3. Transaccional: "¿Qué agencia de AEO tiene consultoría profesional?"
4. Marca: "¿Qué es Nitten Marketing?"

---

## Limitaciones de este caso

- Set de prompts diseñado por el equipo evaluado (sesgo de selección)
- PR evaluada por un único evaluador (sesgo de evaluador único)
- Muestra de 2 queries en CAPA_IPS_SERP (Google y Bing)
- Sin grupo de control para aislar el efecto de la implementación SAGEO

Ver `/docs/limitaciones.md` para declaración completa.

---

## Próximos pasos

- [ ] Ciclo 3 con set de prompts estándar v2.0 (julio 2026)
- [ ] Protocolo de tres evaluadores para PR
- [ ] Ampliar CAPA_IPS_SERP con más queries y tipos de intención
- [ ] Registrar CAPA_AOG (AI Overview Google) como capa adicional
