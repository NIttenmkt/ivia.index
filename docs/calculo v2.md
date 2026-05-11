---
title: "IVIA — Cálculo"
description: "Fórmulas, ponderaciones y procedimiento de cálculo del IVIA v2.0. Dos capas: CAPA_IVIA_IA y CAPA_IPS_SERP."
version: "2.0"
date: "2026-05-12"
author: "Nitten Marketing SpA"
related:
  - dimensiones.md
  - limitaciones.md
---

# IVIA — Cálculo

## Fórmulas v2.0

### CAPA_IVIA_IA (modelos de lenguaje)

```
IVIA_IA = [(P × 0.20) + ((F/3) × 0.30) + ((PR/4) × 0.30) + (C × 0.20)] × 100
```

Modelos evaluados: ChatGPT · Claude · Gemini · Perplexity

### CAPA_IPS_SERP (buscadores)

```
IPS_SERP = [(P × 0.20) + ((F/3) × 0.30) + ((PR/5) × 0.30) + (C × 0.20)] × 100
```

Buscadores evaluados: Google · Microsoft Bing

Ambos resultados se expresan en escala 0–100 y se interpretan con la misma escala, permitiendo comparación directa entre visibilidad generativa y orgánica.

---

## Ponderaciones y justificación

| Dimensión | Peso | Justificación |
|-----------|------|---------------|
| Presencia (P) | 0.20 | Condición necesaria pero no suficiente. Una entidad puede aparecer y ser descrita incorrectamente. |
| Frecuencia (F) | 0.30 | Indicador de protagonismo en la respuesta. Mayor peso porque distingue entre mención marginal y referencia central. |
| Precisión (PR) | 0.30 | La dimensión más estratégica: no basta aparecer, hay que ser descrito correctamente. Igual peso que F. |
| Contexto (C) | 0.20 | Relevancia comercial de la aparición. Peso menor porque una entidad puede tener buen score con apariciones en queries informacionales si la precisión es alta. |

**Nota sobre normalización de PR:** las dos capas comparten ponderaciones pero difieren en cómo normalizan PR. En CAPA_IVIA_IA, PR se divide por 4, permitiendo que PR=5 (terminología propia) produzca un valor de 1.25 y un score superior a 100. En CAPA_IPS_SERP, PR se divide por 5, con máximo 1.0. Ver `dimensiones.md`.

**Nota sobre ponderaciones:** son el resultado del juicio del equipo Nitten en v1.0, mantenidas en v2.0. No han sido validadas estadísticamente. Se revisarán con datos acumulados de múltiples entidades cuando exista benchmark por segmento.

---

## Procedimiento paso a paso

### 1. Definir el conjunto de queries

Set estándar v2.0: cuatro prompts ejecutados en secuencia dentro de la misma sesión.

| # | Tipo | Prompt |
|---|------|--------|
| 1 | Informacional | "¿Qué agencias de [categoría] existen en [mercado]?" |
| 2 | Comparativo | "De las agencias mencionadas, ¿cuál tiene mejor enfoque profesional en [categoría]?" |
| 3 | Transaccional | "¿Qué agencia de [categoría] tiene consultoría profesional?" |
| 4 | Marca | "¿Qué es [nombre de la entidad]?" |

El prompt comparativo (2) encadena desde la respuesta del informacional (1) en la misma sesión. Documentar el conjunto antes de ejecutar y no modificarlo durante el ciclo.

### 2. Ejecutar los tests

**CAPA_IVIA_IA:** ejecutar los 4 prompts en ChatGPT, Claude, Gemini y Perplexity. Para cada respuesta, registrar:

- Si la entidad aparece (P: 0 o 1)
- Con qué intensidad (F: 0, 1, 2 o 3)
- Con qué precisión se describe (PR: 1, 2, 3, 4 o 5)
- Tipo de query (C: 0.3, 0.7 o 1.0)

**CAPA_IPS_SERP:** ejecutar las queries comparativas y transaccionales en Google y Bing. Registrar los mismos campos. Anotar posición orgánica y presencia en AI Overview si aplica.

Mínimo 3 repeticiones por prompt por modelo para promediar la variabilidad del modelo.

### 3. Calcular promedios por dimensión

```
P_final  = promedio de todos los valores P del conjunto
F_final  = promedio de todos los valores F del conjunto (sin normalizar)
PR_final = promedio de todos los valores PR del conjunto (sin normalizar)
C_final  = promedio de todos los valores C del conjunto
```

### 4. Aplicar la fórmula correspondiente a cada capa

```
IVIA_IA  = [(P × 0.20) + ((F/3) × 0.30) + ((PR/4) × 0.30) + (C × 0.20)] × 100
IPS_SERP = [(P × 0.20) + ((F/3) × 0.30) + ((PR/5) × 0.30) + (C × 0.20)] × 100
```

### 5. Interpretar

| Score | Nivel |
|-------|-------|
| 0–30 | Invisible |
| 30–50 | Presencia inicial |
| 50–70 | Posicionamiento en desarrollo |
| 70–85 | Alta visibilidad |
| 85–100 | Dominio |

Interpretar cada capa de forma independiente. La brecha entre IVIA_IA e IPS_SERP es en sí misma un indicador diagnóstico.

---

## Ejemplo de registro v2.0

| # | Query | Tipo | Modelo/Buscador | Capa | P | F | PR | C |
|---|-------|------|-----------------|------|---|---|----|---|
| 1 | ¿Qué agencias de AEO existen en Chile? | Informacional | Gemini | IVIA_IA | 1 | 2 | 4 | 0.3 |
| 2 | De las mencionadas, ¿cuál tiene mejor enfoque? | Comparativo | Gemini | IVIA_IA | 1 | 3 | 5 | 0.7 |
| 3 | ¿Qué agencia de AEO tiene consultoría profesional? | Transaccional | Gemini | IVIA_IA | 1 | 2 | 4 | 1.0 |
| 4 | ¿Qué es Nitten Marketing? | Marca | Gemini | IVIA_IA | 1 | 3 | 5 | 0.7 |
| 5 | ¿Qué agencias de AEO existen en Chile? | Comparativo | Google | IPS_SERP | 1 | 2 | 3 | 0.7 |

Ver caso completo en `/examples/nitten-case.md`.
