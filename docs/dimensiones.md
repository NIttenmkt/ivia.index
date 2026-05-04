---
title: "IVIA — Dimensiones"
description: "Definición operativa de las cuatro dimensiones del índice IVIA"
version: "1.0"
date: "2026-05-01"
author: "Nitten Marketing SpA"
related:
  - calculo.md
  - limitaciones.md
---

# IVIA — Las cuatro dimensiones

## Presencia (P)

**Qué mide:** si la entidad aparece mencionada en la respuesta generada.

**Cómo se mide:**
```
P = número de queries donde la entidad aparece / total de queries evaluadas
```

**Escala:** 0–1 continuo.

**Nota:** P es la dimensión más binaria del índice. Una entidad que aparece en 3 de 10 queries tiene P = 0.3. No distingue entre una mención breve y un análisis extenso; eso lo captura F.

---

## Frecuencia (F)

**Qué mide:** la intensidad de aparición dentro de cada respuesta donde la entidad está presente.

**Escala discreta:**
| Valor | Descripción |
|-------|-------------|
| 0 | No aparece |
| 1 | Mencionada una vez |
| 2 | Mencionada varias veces o con detalle |
| 3 | Dominante en la respuesta |

**Para el cálculo:** normalizar dividiendo por 3.
```
F_normalizada = F_discreta / 3
```

**Nota de robustez:** esta es la dimensión con menor resolución del índice. Una escala discreta de 0-3 introduce poca variabilidad. En versiones futuras se evaluará una escala continua o una escala de 0-5.

---

## Precisión (PR)

**Qué mide:** el grado de exactitud con que el modelo describe la entidad respecto a su propuesta de valor real.

**Escala cualitativa:**
| Valor | Descripción |
|-------|-------------|
| 0 | Incorrecto o ausente |
| 0.5 | Parcialmente correcto (menciona la entidad pero con atributos incorrectos o incompletos) |
| 1.0 | Correcto y alineado con el posicionamiento real de la entidad |

**Criterio de evaluación:** la descripción generada se compara con la propuesta de valor documentada de la entidad (sitio web, documentación oficial, casos de estudio). No se evalúa si la descripción es favorable, sino si es fiel.

**Advertencia:** PR es la dimensión más subjetiva del índice y la más susceptible al sesgo del evaluador. El protocolo recomendado desde v1.1 es el uso de al menos tres evaluadores independientes con desviación máxima aceptable de 0.25 puntos. Ver [limitaciones.md](limitaciones.md).

---

## Contexto (C)

**Qué mide:** la relevancia de la consulta en la que aparece la entidad, ponderada por su proximidad a una intención de decisión o contratación.

**Ponderaciones:**
| Tipo de query | Valor C |
|--------------|---------|
| Informacional ("¿qué es AEO?") | 0.3 |
| Comparativa ("¿qué agencias hacen AEO en Chile?") | 0.7 |
| Transaccional ("necesito contratar una agencia AEO") | 1.0 |

**Nota:** las ponderaciones actuales (0.3 / 0.7 / 1.0) son el resultado de un juicio experto, no de calibración estadística. Representan la hipótesis de que la intención transaccional produce citaciones tres veces más valiosas comercialmente que la intención informacional. Esta hipótesis puede ser revisada con evidencia acumulada en versiones futuras.
