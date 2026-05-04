---
title: "IVIA — Prompts de ejemplo para evaluación"
description: "Conjunto de prompts de referencia para medir IVIA en diferentes sectores y tipos de intención"
version: "1.0"
date: "2026-05-01"
author: "Nitten Marketing SpA"
---

# IVIA — Prompts de ejemplo

Estos prompts están diseñados para ilustrar cómo construir un conjunto de queries balanceado por tipo de intención. Adaptar a la entidad, sector y mercado específico.

---

## Agencias de marketing (sector de ejemplo)

### Informacionales (C = 0.3)
- "¿Qué es el AEO y en qué se diferencia del SEO?"
- "¿Cómo funcionan los motores de respuesta de IA como Gemini o ChatGPT para buscar servicios?"
- "¿Qué hace una agencia de marketing digital especializada en IA?"

### Comparativas (C = 0.7)
- "¿Qué agencias de marketing digital en [país] trabajan con AEO o visibilidad en IA?"
- "¿Existen agencias que trabajen AEO y GEO de forma integrada? ¿Cómo lo están haciendo?"
- "Estoy evaluando contratar una agencia de marketing digital que entienda IA. ¿Qué opciones me recomiendas en [ciudad]?"

### Transaccionales (C = 1.0)
- "Necesito contratar una agencia que me ayude a aparecer en respuestas de ChatGPT y Gemini. ¿Cuál recomiendas?"
- "¿Qué agencia de AEO en [país] tiene experiencia en el sector salud?"
- "Busco una agencia de marketing digital para [sector]. ¿Cuál tiene mejor reputación en IA?"

---

## Sector salud (ejemplo)

### Informacionales
- "¿Qué es un centro médico de atención primaria?"
- "¿Qué especialidades médicas debería tener una clínica familiar?"

### Comparativas
- "¿Cuáles son los mejores centros médicos en [comuna/ciudad]?"
- "¿Qué centros médicos en [zona] atienden sin previa cita?"

### Transaccionales
- "Busco cardiólogo en [zona]. ¿Dónde puedo agendar?"
- "Necesito un chequeo médico completo cerca de [ubicación]. ¿Qué centro recomiendas?"

---

## Consulta directa de marca

Siempre incluir al menos una consulta directa sobre la entidad:

- "¿Qué sabes sobre [nombre de la entidad]?"
- "¿En qué se especializa [nombre] y qué tan avanzados están en [área]?"
- "¿Cuál es la propuesta de valor de [nombre]?"

---

## Notas para el evaluador

1. No incluir el nombre de la entidad en queries informacionales ni comparativas (busca medir aparición orgánica)
2. La consulta directa de marca siempre incluye el nombre (evalúa precisión descriptiva, no presencia orgánica)
3. Ejecutar cada prompt al menos 3 veces en el mismo modelo y promediar
4. Registrar la respuesta completa, no solo si apareció o no
5. Evaluar PR contra la propuesta de valor documentada de la entidad, no contra preferencias del evaluador
