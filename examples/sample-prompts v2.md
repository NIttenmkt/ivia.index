---
title: "IVIA — Prompts de ejemplo para evaluación"
description: "Set estándar v2.0 y prompts de referencia para medir IVIA en diferentes sectores. Cuatro tipos de intención en secuencia: informacional, comparativo encadenado, transaccional y marca."
version: "2.0"
date: "2026-05-12"
author: "Nitten Marketing SpA"
related:
  - calculo.md
  - metodologia.md
---

# IVIA — Prompts de ejemplo para evaluación

## Set estándar v2.0

El set estándar es fijo y se ejecuta en secuencia dentro de la misma sesión de chat. El prompt comparativo (2) encadena desde la respuesta del informacional (1): no se abre una sesión nueva entre ambos.

| # | Tipo | Prompt genérico | C |
|---|------|-----------------|---|
| 1 | Informacional | "¿Qué [categoría] existen en [mercado]?" | 0.3 |
| 2 | Comparativo | "De los/las mencionados/as, ¿cuál tiene mejor enfoque profesional en [categoría]?" | 0.7 |
| 3 | Transaccional | "¿Qué [categoría] tiene consultoría/atención profesional?" | 1.0 |
| 4 | Marca | "¿Qué es [nombre de la entidad]?" | 0.7 |

**Por qué el encadenamiento:** el comparativo encadenado testa dos cosas en un solo ciclo: si la entidad aparece en el reconocimiento inicial (prompt 1) y cómo es evaluada en contexto competitivo (prompt 2). Refleja el flujo real de un usuario que descubre opciones y luego compara.

---

## Ejemplos por sector

### Agencias de marketing

**Set estándar aplicado:**

| # | Tipo | Prompt |
|---|------|--------|
| 1 | Informacional | "¿Qué agencias de AEO existen en Chile?" |
| 2 | Comparativo | "De las agencias mencionadas, ¿cuál tiene mejor enfoque profesional en AEO?" |
| 3 | Transaccional | "¿Qué agencia de AEO tiene consultoría profesional?" |
| 4 | Marca | "¿Qué es Nitten Marketing?" |

**Prompts adicionales opcionales:**

*Informacionales (C = 0.3)*
- "¿Qué agencias de marketing digital en [país] trabajan con visibilidad en IA?"
- "¿Qué hace una agencia especializada en AEO y GEO?"

*Comparativos (C = 0.7)*
- "¿Existen agencias que trabajen AEO y GEO de forma integrada? ¿Cómo lo están haciendo?"
- "Estoy evaluando contratar una agencia de marketing digital que entienda IA. ¿Qué opciones me recomiendas en [ciudad]?"

*Transaccionales (C = 1.0)*
- "Necesito contratar una agencia que me ayude a aparecer en respuestas de ChatGPT y Gemini. ¿Cuál recomiendas?"
- "¿Qué agencia de AEO en [país] tiene experiencia en el sector salud?"

---

### Sector salud

**Set estándar aplicado:**

| # | Tipo | Prompt |
|---|------|--------|
| 1 | Informacional | "¿Qué centros médicos existen en [comuna/ciudad]?" |
| 2 | Comparativo | "De los centros mencionados, ¿cuál tiene mejor reputación y disponibilidad?" |
| 3 | Transaccional | "Necesito agendar una ecografía ginecológica en [zona]. ¿Cuál recomiendas?" |
| 4 | Marca | "¿Qué es [nombre del centro médico]?" |

**Prompts adicionales opcionales:**

*Informacionales (C = 0.3)*
- "¿Qué especialidades médicas debería tener una clínica familiar?"
- "¿Qué es un centro médico de atención primaria?"

*Comparativos (C = 0.7)*
- "¿Qué centros médicos en [zona] atienden sin previa cita?"
- "¿Cuáles son los mejores centros médicos en [ciudad] con convenio Fonasa?"

*Transaccionales (C = 1.0)*
- "Busco cardiólogo en [zona]. ¿Dónde puedo agendar?"
- "Necesito un chequeo médico completo cerca de [ubicación]. ¿Qué centro recomiendas?"

---

### Sector legal

**Set estándar aplicado:**

| # | Tipo | Prompt |
|---|------|--------|
| 1 | Informacional | "¿Qué estudios de abogados existen en [ciudad] especializados en [área]?" |
| 2 | Comparativo | "De los estudios mencionados, ¿cuál tiene mejor trayectoria en [área]?" |
| 3 | Transaccional | "Necesito un abogado especialista en [área] en [ciudad]. ¿A quién contacto?" |
| 4 | Marca | "¿Qué es [nombre del estudio]?" |

---

## Notas para el evaluador

**Sobre el encadenamiento:**
- Los prompts 1 y 2 se ejecutan en la misma sesión sin cerrarla entre medio
- Si el prompt 1 no menciona a la entidad, el prompt 2 igualmente se ejecuta: registrar P=0 en prompt 1 y evaluar si la entidad aparece espontáneamente en el comparativo

**Sobre el prompt informacional:**
- No incluir el nombre de la entidad (mide aparición orgánica)
- El prompt de disciplina pura ("¿Qué es el AEO?") no es válido como informacional en v2.0: es un control de conocimiento del modelo, no un indicador de presencia

**Sobre el prompt de marca:**
- Siempre incluye el nombre de la entidad (evalúa precisión descriptiva, no presencia orgánica)
- Asignar C = 0.7 (comparativo), no 1.0, porque la intención es informarse sobre la entidad, no contratar

**Sobre la ejecución:**
- Ejecutar cada prompt al menos 3 veces en el mismo modelo y promediar
- Registrar la respuesta completa, no solo si apareció o no
- Anotar si el modelo usó terminología propia de la entidad (campo `own_language`)
- Registrar con qué otras entidades apareció (campo `appeared_with`)

**Sobre la evaluación de PR:**
- Evaluar PR contra la propuesta de valor documentada de la entidad, no contra preferencias del evaluador
- Usar la escala 1–5: 1=incorrecto · 2=atributos incorrectos · 3=parcialmente correcto · 4=correcto y alineado · 5=correcto con terminología propia
- En caso de duda entre dos valores adyacentes, registrar el inferior y documentar la razón

**Sobre CAPA_IPS_SERP:**
- Ejecutar los prompts comparativos y transaccionales en Google y Bing en modo incógnito
- Registrar posición orgánica y si hay AI Overview activo
- Anotar el snippet exacto mostrado en AI Overview si aplica
