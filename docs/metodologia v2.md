---
title: "IVIA — Metodología"
description: "Fundamento metodológico del IVIA v2.0. Dos capas independientes: CAPA_IVIA_IA y CAPA_IPS_SERP."
version: "2.0"
date: "2026-05-12"
author: "Nitten Marketing SpA"
language: "es"
related:
  - dimensiones.md
  - calculo.md
  - limitaciones.md
---

# IVIA — Metodología

## Por qué existe IVIA

Las métricas tradicionales de SEO (posición en ranking, tráfico orgánico, CTR) están diseñadas para un paradigma de búsqueda basado en listas de resultados. El usuario selecciona entre opciones.

Los sistemas de respuesta basados en modelos de lenguaje (ChatGPT, Gemini, Perplexity, Claude) operan de forma distinta: sintetizan y responden directamente. El usuario no selecciona; recibe. En ese paradigma, la visibilidad no se mide en posiciones sino en inclusión: si la entidad está en la respuesta, con qué precisión, y en qué tipo de consultas.

IVIA es un intento de hacer esa visibilidad observable, comparable y optimizable.

---

## Unidad de análisis

IVIA mide entidades, no páginas.

Una entidad es un objeto del mundo real —organización, persona, lugar, servicio— con identidad distinguible, atributos propios y relaciones con otras entidades. La distinción importa: una página puede describir múltiples entidades; una entidad puede estar representada en múltiples páginas. Optimizar páginas no es lo mismo que consolidar la identidad de una entidad para que los LLMs la interpreten correctamente.

---

## Estructura v2.0: dos capas independientes

Desde v2.0, IVIA separa la medición en dos capas con fórmulas distintas:

**CAPA_IVIA_IA** — mide visibilidad en modelos de lenguaje (ChatGPT, Claude, Gemini, Perplexity). Evalúa si la entidad es citada, descrita correctamente y seleccionada en respuestas generativas.

**CAPA_IPS_SERP** — mide visibilidad en buscadores (Google, Microsoft Bing). Evalúa presencia orgánica, posición y representación en resultados de búsqueda tradicional.

Ambas capas comparten las mismas cuatro dimensiones y las mismas escalas de F y C, pero difieren en la normalización de PR. El estándar de precisión en una respuesta generativa es distinto al de un resultado orgánico.

La brecha entre IVIA_IA e IPS_SERP es en sí misma un indicador diagnóstico: refleja cuánto de la visibilidad orgánica se ha traducido en visibilidad generativa.

---

## Principio operativo

IVIA no es una foto. Es una trayectoria.

Su utilidad no está en el número absoluto de un solo ciclo sino en la evolución entre ciclos. Un IVIA_IA de 60.9 en mayo 2026 no dice "visibilidad alta". Dice "este es el punto de partida verificable para esta capa". El siguiente ciclo dirá si la implementación movió la aguja y en qué dimensión.

Por eso IVIA está diseñado para medirse en ciclos periódicos, no como auditoría de una sola vez.

---

## Set de prompts estándar v2.0

Los prompts se ejecutan en secuencia dentro de la misma sesión. El comparativo encadena desde la respuesta informacional, testeando tanto el reconocimiento inicial como la evaluación competitiva.

| # | Tipo | Prompt |
|---|------|--------|
| 1 | Informacional | "¿Qué agencias de [categoría] existen en [mercado]?" |
| 2 | Comparativo | "De las agencias mencionadas, ¿cuál tiene mejor enfoque profesional en [categoría]?" |
| 3 | Transaccional | "¿Qué agencia de [categoría] tiene consultoría profesional?" |
| 4 | Marca | "¿Qué es [nombre de la entidad]?" |

Mínimo 3 repeticiones por prompt por modelo para promediar la variabilidad del modelo.

---

## Relación con SAGEO

IVIA es el instrumento de medición del ciclo adaptativo de la metodología SAGEO:

```
Medir (IVIA) → Ajustar → Redistribuir → Repetir
```

Sin IVIA, el ciclo adaptativo no tiene punto de referencia. Sin el ciclo adaptativo, IVIA es solo un número sin acción.

Cada dimensión conecta con una capa específica del sistema SAGEO:

| Dimensión | Capa SAGEO | Acción directa |
|-----------|-----------|----------------|
| P — Presencia | AEO | JSON-LD @graph + llms.txt + cobertura semántica |
| F — Frecuencia | GEO | Arquitectura de contenido + linking interno |
| PR — Precisión | GEO | Documentación densa + control narrativo |
| C — Contexto | SEO + AEO | Estrategia de queries + intención de compra |

---

## Evolución del instrumento

| Versión | Estado | Descripción |
|---------|--------|-------------|
| v1.0 | Archivado `/archive/v1/` | Fórmula unificada. PR escala 3 niveles. Medición manual en LLMs. Sin capa SERP. |
| v2.0 | **Actual** | Dos capas independientes: CAPA_IVIA_IA y CAPA_IPS_SERP. PR escala 5 niveles. Normalización PR÷4 en IA, PR÷5 en SERP. Set de prompts estándar en secuencia. |
| v3.0 | En diseño | Ejecución automatizada vía n8n + APIs de LLMs. Parseo de scores sin intervención manual. Reporte por ciclo exportable. |
| v4.0 | Concepto | Servidor propio. Input: dominio + segmento. Output: reporte autónomo end-to-end. |
