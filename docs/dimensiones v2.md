---
title: "IVIA — Dimensiones"
description: "Definición operativa de las cuatro dimensiones del índice IVIA v2.0. Compartidas entre CAPA_IVIA_IA y CAPA_IPS_SERP."
version: "2.0"
date: "2026-05-12"
author: "Nitten Marketing SpA"
related:
  - calculo.md
  - limitaciones.md
---

# IVIA — Las cuatro dimensiones

Las cuatro dimensiones son compartidas entre CAPA_IVIA_IA y CAPA_IPS_SERP. Las escalas de F y C son idénticas en ambas capas. La escala de PR comparte definición pero tiene normalización distinta según la capa.

---

## Presencia (P)

**Qué mide:** si la entidad aparece mencionada en la respuesta generada o en los resultados de búsqueda.

**Cómo se mide:**
```
P = número de queries donde la entidad aparece / total de queries evaluadas
```

**Escala:** 0–1 continuo.

**Nota:** P es la dimensión más binaria del índice. Una entidad que aparece en 3 de 10 queries tiene P = 0.3. No distingue entre una mención breve y un análisis extenso; eso lo captura F. P es la condición necesaria: sin presencia, las otras dimensiones no aplican.

---

## Frecuencia (F)

**Qué mide:** la intensidad de aparición dentro de cada respuesta o resultado donde la entidad está presente.

**Escala discreta (compartida entre capas):**

| Valor | En CAPA_IVIA_IA | En CAPA_IPS_SERP |
|-------|-----------------|------------------|
| `0` | No aparece | Ausente |
| `1` | Mencionada una vez | Baja visibilidad (segunda página o baja relevancia) |
| `2` | Mencionada varias veces o con detalle | Visible y contextualizada (primera página) |
| `3` | Dominante en la respuesta | Top 3 / alta prominencia |

**Para el cálculo:** normalizar dividiendo por 3 en ambas capas.
```
F_normalizada = F_discreta / 3
```

---

## Precisión (PR)

**Qué mide:** el grado de exactitud con que el modelo o buscador describe la entidad respecto a su propuesta de valor real.

**Escala v2.0 (1–5):**

| Valor | Descripción |
|-------|-------------|
| `1` | Incorrecto |
| `2` | Atributos incorrectos |
| `3` | Parcialmente correcto |
| `4` | Correcto y alineado con el posicionamiento real |
| `5` | Correcto con terminología propia de la entidad |

**Criterio de evaluación:** la descripción generada se compara con la propuesta de valor documentada de la entidad (sitio web, documentación oficial, casos de estudio). No se evalúa si la descripción es favorable, sino si es fiel.

**Normalización diferenciada por capa:**

| Capa | Normalización | Máximo | Nota |
|------|--------------|--------|------|
| CAPA_IVIA_IA | PR ÷ 4 | 1.25 (PR=5) | Bonus por terminología propia |
| CAPA_IPS_SERP | PR ÷ 5 | 1.0 (PR=5) | Sin bonus, máximo 1.0 |

En CAPA_IVIA_IA, PR=5 produce un valor de 1.25, reflejando el beneficio estratégico de que el modelo adopte el lenguaje propio de la entidad. Scores de IVIA_IA superiores a 100 son posibles en casos de dominio total y son comportamiento esperado.

**Advertencia:** PR es la dimensión más subjetiva del índice y la más susceptible al sesgo del evaluador. Ver `limitaciones.md`.

---

## Contexto (C)

**Qué mide:** la relevancia de la consulta según su proximidad a una intención de decisión o contratación.

**Ponderaciones (compartidas entre capas):**

| Tipo de query | Valor C | Ejemplo |
|---------------|---------|---------|
| Informacional | `0.3` | "¿Qué agencias de AEO existen en Chile?" |
| Comparativa | `0.7` | "De las agencias mencionadas, ¿cuál tiene mejor enfoque?" |
| Transaccional | `1.0` | "¿Qué agencia de AEO tiene consultoría profesional?" |

**Nota:** las ponderaciones (0.3 / 0.7 / 1.0) son el resultado de juicio experto, no de calibración estadística. Representan la hipótesis de que la intención transaccional produce citaciones tres veces más valiosas comercialmente que la intención informacional. Esta hipótesis será revisada con evidencia acumulada en versiones futuras.
