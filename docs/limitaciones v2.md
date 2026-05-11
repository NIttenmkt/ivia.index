---
title: "IVIA — Limitaciones"
description: "Declaración explícita de limitaciones del índice IVIA v2.0. Dos capas: CAPA_IVIA_IA y CAPA_IPS_SERP."
version: "2.0"
date: "2026-05-12"
author: "Nitten Marketing SpA"
related:
  - metodologia.md
  - dimensiones.md
---

# IVIA — Limitaciones

Esta sección existe porque un instrumento de medición sin declaración de limitaciones no es un instrumento: es una afirmación. Las siguientes limitaciones se declaran sin atenuantes.

---

## 1. Dependencia del diseño de los prompts

El IVIA varía según cómo se formulen las queries de evaluación. Un conjunto de queries sesgado hacia la fortaleza de la entidad producirá un IVIA inflado. Un conjunto sesgado hacia queries genéricas producirá un IVIA deflado.

**Mitigación v2.0 (implementada):** set de prompts estándar de cuatro queries en secuencia fija (informacional, comparativo encadenado, transaccional, marca). El conjunto se documenta antes de ejecutar los tests y no se modifica durante el ciclo de medición.

**Mitigación propuesta (v3.0):** evaluador externo sin conocimiento previo de la entidad para validar el conjunto de queries antes de cada ciclo.

---

## 2. Variabilidad entre modelos de lenguaje

Los modelos tienen corpora de entrenamiento distintos, ciclos de actualización distintos y comportamientos distintos ante las mismas queries. El IVIA_IA calculado en Gemini puede diferir del calculado en ChatGPT, Claude o Perplexity.

**Mitigación v2.0 (implementada):** CAPA_IVIA_IA evalúa los cuatro modelos principales (ChatGPT, Claude, Gemini, Perplexity) en cada ciclo y promedia los resultados. El score por modelo se registra de forma separada en el dataset para trazabilidad.

---

## 3. Naturaleza no determinística de las respuestas

El mismo prompt en el mismo modelo puede producir respuestas diferentes en ejecuciones distintas. Esto introduce variabilidad que no es controlable por la entidad evaluada.

**Mitigación actual:** ejecutar cada query al menos 3 veces por modelo y usar el promedio. Registrar las variaciones en el dataset.

---

## 4. Subjetividad de la dimensión PR (Precisión)

La evaluación de si una descripción generada es "correcta y alineada con el posicionamiento real" implica un juicio que puede variar entre evaluadores. En v1.0, PR fue evaluada por un único evaluador del equipo.

**Mitigación v2.0 (parcial):** PR ahora usa una escala de 5 niveles (1–5) con descriptores explícitos por nivel, lo que reduce el margen de interpretación subjetiva respecto a la escala de 3 niveles de v1.0.

**Mitigación propuesta (v3.0):** protocolo de tres evaluadores independientes. Desviación máxima aceptable entre evaluadores: 0.25 puntos. Si se supera, el prompt se descarta y rediseña. Evaluadores recomendados: un miembro del equipo, un cliente activo de la entidad evaluada, y un profesional externo del sector sin relación comercial.

---

## 5. Ponderaciones no validadas estadísticamente

Los pesos de la fórmula (P×0.20, F×0.30, PR×0.30, C×0.20) son el resultado de juicio experto, no de calibración estadística. Representan hipótesis razonables sobre la importancia relativa de cada dimensión, pero pueden no ser óptimos.

**Mitigación propuesta:** revisión de ponderaciones basada en datos acumulados de múltiples entidades medidas bajo el mismo protocolo. El benchmark `ivia-benchmarks.md` en desarrollo permitirá esta revisión cuando existan al menos 4 casos documentados por segmento.

---

## 6. Comparabilidad limitada entre CAPA_IVIA_IA y CAPA_IPS_SERP

Ambas capas comparten escala 0–100 y dimensiones, pero miden fenómenos distintos con normalizaciones de PR diferentes (÷4 en IA, ÷5 en SERP). La comparación directa de scores entre capas es válida como indicador de brecha, pero no implica equivalencia metodológica exacta.

**Uso correcto:** la brecha entre capas es un diagnóstico de cuánto de la visibilidad orgánica se ha traducido en visibilidad generativa. No es una afirmación de que un canal supera al otro en términos absolutos.

---

## 7. Ausencia de grupo de control

IVIA no tiene un mecanismo para aislar el efecto de la implementación de infraestructura de otros factores concurrentes (antigüedad del dominio, publicaciones en redes, cambios en los modelos de IA). Los resultados son correlacionados, no causalmente demostrados.

---

## 8. Instrumento no validado externamente

IVIA es un instrumento propietario sin validación por terceros ni comparabilidad con otros estudios. Es internamente consistente pero no estandarizado. Cualquier uso en investigación debe declarar estas limitaciones explícitamente.

---

## Declaración de uso responsable

IVIA no debe usarse para afirmar causalidad, hacer comparaciones con entidades que no han seguido el mismo protocolo de medición, o proyectar resultados futuros con certeza. Su valor es la dirección del ajuste, no la precisión estadística.
