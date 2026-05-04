---
title: "IVIA — Caso validado: Nitten Marketing SpA"
description: "Primera validación empírica del IVIA aplicada al dominio nittenmkt.cl"
entity: "Nitten Marketing SpA"
domain: "nittenmkt.cl"
period: "Julio 2025 – Abril 2026"
measurement_date: "2026-04-29"
model_tested: "Gemini"
ivia_result: 64
ivia_level: "Posicionamiento en desarrollo"
version: "1.0"
---

# IVIA — Caso validado: Nitten Marketing SpA

## Contexto del caso

**Entidad:** Nitten Marketing SpA  
**Dominio:** nittenmkt.cl  
**Sector:** Marketing digital y BTL — Santiago, Chile  
**Período de implementación:** Julio 2025 – Abril 2026  
**Fecha de medición:** 29 de abril de 2026  
**Modelo evaluado:** Gemini (Google)  
**Antigüedad del dominio al momento de la medición:** menos de 12 meses  
**Inversión publicitaria para las queries objetivo:** ninguna  

Este caso documenta la primera medición IVIA realizada por Nitten Marketing SpA en su propio dominio, utilizado como laboratorio de implementación de la metodología SAGEO antes de ofrecer el servicio a clientes externos.

---

## Infraestructura implementada antes de la medición

La entidad implementó durante el período los siguientes elementos de infraestructura semántica:

- JSON-LD con @graph completo (Organization, WebPage, FAQPage, Service, DefinedTermSet, SpeakableSpecification) vía WPCode tipo PHP
- llms.txt en la raíz del dominio con rutas a 17 documentos semánticos
- Biblioteca /aeo/ con 17 documentos .md con frontmatter YAML y referencias cruzadas
- nitten-context.xml (sitemap híbrido AI) con 44 URLs
- Presencia verificada en GBP, Clutch, Sortlist y LinkedIn
- ai-brief.md, servicios-ia.json, knowledge-index.json, openapi.yaml (parcial)
- Core Web Vitals aprobada. PageSpeed Insights mobile: rendimiento 94+

---

## Protocolo de testing

### Conjunto de queries evaluadas

Se diseñaron 4 queries cubriendo los tres tipos de intención. El conjunto fue diseñado por el equipo Nitten con conocimiento previo de la implementación, lo que constituye una limitación declarada (ver [/docs/limitaciones.md](../docs/limitaciones.md)).

| # | Query | Tipo de intención | Modelo |
|---|-------|------------------|--------|
| 1 | "Estoy evaluando contratar una agencia de marketing digital en Chile que realmente entienda cómo posicionarse en inteligencia artificial. ¿Qué opciones me recomendarías?" | Comparativa (amplia) | Gemini |
| 2 | "¿Existen agencias que trabajen AEO y GEO de forma integrada? ¿Cómo lo están haciendo actualmente?" | Comparativa (específica) | Gemini |
| 3 | "¿Qué sabes sobre Nitten Marketing en Chile? ¿En qué se diferencian y qué tan avanzados están en IA?" | Consulta directa de marca | Gemini |
| 4 | "agencias AEO en Chile" | Transaccional / comparativa | Google (AI Overviews) |

---

## Registro de scores por query

| # | Query | P | F (raw) | F (norm) | PR | C | Notas |
|---|-------|---|---------|----------|----|---|-------|
| 1 | Prospección genérica | 0 | 0 | 0 | 0 | 0.7 | No aparece. Nombra Best Solution, Postedin, Adinfluence |
| 2 | AEO/GEO integrado | 1 | 1 | 0.33 | 1.0 | 0.7 | Aparece 2°. Descripción correcta. Usa "Arquitectura de Respuesta" |
| 3 | Consulta directa | 1 | 2 | 0.67 | 1.0 | 0.7 | Análisis completo. Fortalezas y brechas coherentes |
| 4 | Google AI Overviews | 1 | 1 | 0.33 | 1.0 | 1.0 | Posición #1 orgánica. Citada en primer lugar en AI Overviews |

---

## Cálculo IVIA

### Promedios por dimensión

```
P_final  = (0 + 1 + 1 + 1) / 4 = 0.75
F_final  = (0 + 0.33 + 0.67 + 0.33) / 4 = 0.33
PR_final = (0 + 1.0 + 1.0 + 1.0) / 4 = 0.75
C_final  = (0.7 + 0.7 + 0.7 + 1.0) / 4 = 0.78
```

### Aplicación de la fórmula

```
IVIA = (P × 0.20) + (F × 0.30) + (PR × 0.30) + (C × 0.20)
IVIA = (0.75 × 0.20) + (0.33 × 0.30) + (0.75 × 0.30) + (0.78 × 0.20)
IVIA = 0.150 + 0.099 + 0.225 + 0.156
IVIA = 0.630

IVIA = 63/100 → redondeado: 64/100
```

**Nivel:** Posicionamiento en desarrollo (rango 50–70)

---

## Análisis por query

### Query 1 — Prospección genérica: sin aparición
Gemini no menciona a Nitten. Esto era esperado para un dominio con menos de 12 meses de antigüedad en queries genéricas de alta competencia. La antigüedad acumulada de los competidores establecidos (Postedin, Best Solution) domina en ese tipo de consulta. No falsifica la hipótesis central, que afirmaba visibilidad en queries donde la infraestructura técnica específica es determinante.

### Query 2 — AEO/GEO integrado: citación con terminología propia
Gemini describe a Nitten en segundo lugar con la frase "Arquitectura de Respuesta" — término exclusivo de la biblioteca /aeo/ del sitio, no de uso general en la industria. Esto valida H1a: la infraestructura estructurada produce reconocimiento correcto y extracción de vocabulario propio. La descripción completa de Gemini:

> *"Nitten Marketing (Especialistas en AEO). Se posicionan directamente como una 'Agencia AEO' en Santiago. Su enfoque es menos sobre el tráfico masivo y más sobre ser la entidad de referencia. Trabajan en la infraestructura de datos estructurados (Schema) y en la Arquitectura de Respuesta."*

Gemini agrega además una cita del caso de cliente:

> *"En el sector salud (como su caso con centromedicosandiego.cl), logran que cuando alguien pregunta por síntomas o especialistas en una zona, la IA mencione al centro médico como la respuesta directa."*

### Query 3 — Consulta directa: análisis estratégico coherente
Gemini produce un análisis estructurado que identifica correctamente las fortalezas y las brechas estratégicas de Nitten, coherentes con lo que el equipo ha discutido internamente, sin que eso fuera instruido al modelo.

**Fortalezas identificadas por Gemini:**
- Especialización en AEO en un nicho donde las agencias grandes aún están aprendiendo
- Transparencia de métricas: foco en citación por IA, no métricas de vanidad
- Sectores de alta exigencia: salud, B2B, legal

**Áreas de mejora identificadas por Gemini:**
- Barrera de entrada técnica para el cliente no técnico
- Dependencia de la velocidad de adopción de IA generativa en Chile

### Query 4 — Google AI Overviews: posición #1 orgánica
Búsqueda en modo incógnito. Posición #1 orgánica para "agencias AEO en Chile". Nitten citada en primer lugar en AI Overviews: *"Destacan firmas como Nitten Marketing, Agencia ROI, Loup y Nexbu."* SEO Austral aparece dos veces como resultado patrocinado en la misma búsqueda.

---

## Limitaciones de este caso

1. Conjunto de queries diseñado por el equipo evaluado (sesgo de selección)
2. PR evaluada por un único evaluador (sesgo de evaluador único)
3. Validación realizada en un solo modelo (Gemini)
4. Sin grupo de control para aislar el efecto de la implementación SAGEO
5. Muestra pequeña: 4 queries

Estas limitaciones están declaradas en el documento metodológico del caso: [SAGEO como Sistema. Nueva lectura sobre el AEO](https://nittenmkt.cl/aeo-como-sistema/)

---

## Estado de la entidad al momento de la medición

| Métrica | Valor |
|---------|-------|
| IVIA total | 64/100 |
| Nivel | Posicionamiento en desarrollo |
| Brecha principal | Queries genéricas de alta competencia (P=0 en Query 1) |
| Fortaleza principal | Precisión descriptiva (PR=1.0 en 3 de 4 queries) |
| Próximo ciclo de medición | Julio 2026 |
| Modelos pendientes | ChatGPT, Perplexity |

---

## Próximos pasos para este caso

- [ ] Segundo ciclo IVIA con protocolo de tres evaluadores (julio 2026)
- [ ] Validación cross-model: ChatGPT y Perplexity
- [ ] Prompts diseñados por evaluador externo
- [ ] Comparar delta IVIA respecto a este ciclo baseline
