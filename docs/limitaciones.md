---
title: "IVIA — Limitaciones"
description: "Declaración explícita de limitaciones del índice IVIA v1.0"
version: "1.0"
date: "2026-05-01"
author: "Nitten Marketing SpA"
related:
  - metodologia.md
  - dimensiones.md
---

# IVIA — Limitaciones

Esta sección existe porque un instrumento de medición sin declaración de limitaciones no es un instrumento: es una afirmación. Las siguientes limitaciones se declaran sin atenuantes.

## 1. Dependencia del diseño de los prompts

El IVIA varía según cómo se formulen las queries de evaluación. Un conjunto de queries sesgado hacia la fortaleza de la entidad producirá un IVIA inflado. Un conjunto sesgado hacia queries genéricas producirá un IVIA deflado.

**Mitigación actual:** documentar el conjunto de queries antes de ejecutar los tests y no modificarlo durante el ciclo de medición.

**Mitigación propuesta (v1.1):** involucrar a un evaluador externo sin conocimiento previo de la entidad para diseñar al menos el 50% del conjunto de queries.

---

## 2. Variabilidad entre modelos de lenguaje

El IVIA calculado en Gemini puede diferir significativamente del calculado en ChatGPT o Perplexity. Los modelos tienen corpora de entrenamiento distintos, ciclos de actualización distintos y comportamientos distintos ante las mismas queries.

**Estado actual:** IVIA v1.0 ha sido validado principalmente en Gemini. Los resultados en otros modelos no están documentados.

**Mitigación propuesta (v2.0):** versiones segmentadas por modelo (IVIA-G para Gemini, IVIA-C para ChatGPT, IVIA-P para Perplexity) con normalización cross-model.

---

## 3. Naturaleza no determinística de las respuestas

El mismo prompt en el mismo modelo puede producir respuestas diferentes en ejecuciones distintas. Esto introduce variabilidad que no es controlable por la entidad evaluada.

**Mitigación actual:** ejecutar cada query al menos 3 veces y usar el promedio.

---

## 4. Subjetividad de la dimensión PR (Precisión)

La evaluación de si una descripción generada es "correcta" implica un juicio que puede variar entre evaluadores. En v1.0, PR fue evaluada por un único evaluador del equipo.

**Mitigación propuesta (v1.1):** protocolo de tres evaluadores independientes. Desviación máxima aceptable entre evaluadores: 0.25 puntos. Si se supera, el prompt se descarta y rediseña.

Los tres evaluadores recomendados: un miembro del equipo, un cliente activo de la entidad evaluada, y un profesional externo del sector sin relación comercial con la entidad.

---

## 5. Ponderaciones no validadas estadísticamente

Los pesos de la fórmula (P×0.20, F×0.30, PR×0.30, C×0.20) son el resultado de un juicio experto, no de calibración estadística. Representan hipótesis razonables sobre la importancia relativa de cada dimensión, pero pueden no ser óptimos.

**Mitigación propuesta (v2.0):** revisión de ponderaciones basada en datos acumulados de múltiples entidades medidas bajo el mismo protocolo.

---

## 6. Ausencia de grupo de control

IVIA no tiene un mecanismo para aislar el efecto de la implementación de infraestructura de otros factores concurrentes (antigüedad del dominio, publicaciones en redes, cambios en los modelos de IA). Los resultados son correlacionados, no causalmente demostrados.

---

## 7. Instrumento no validado externamente

IVIA es un instrumento propietario sin validación por terceros ni comparabilidad con otros estudios. Es internamente consistente pero no estandarizado. Cualquier uso en investigación debe declarar estas limitaciones explícitamente.

---

## Declaración de uso responsable

IVIA no debe usarse para afirmar causalidad, hacer comparaciones con entidades que no han seguido el mismo protocolo de medición, o proyectar resultados futuros con certeza. Su valor es la dirección del ajuste, no la precisión estadística.
