# Profile: Developer / Technical

## Description
For software developers, engineers, and technical specialists who need to organize code knowledge, solutions, architectures, and learning across languages, frameworks, and projects.

---

## Folder Structure

```
01_Projects/
  [ProjectName]/
    Architecture/
    Decisions/
    [ProjectName].md      ← project hub note
02_Codebase/
  Languages/
    Python/
    JavaScript/
    [Language]/
  Frameworks/
    React/
    FastAPI/
    [Framework]/
03_Solutions/
  Bugs/
  Patterns/
  Snippets/
04_Learning/
  Courses/
  Concepts/
  Books/
05_Daily/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Projects folder | `01_Projects` | `01_Proyectos` | `01_Projects` |
| Codebase folder | `02_Codebase` | `02_Código` | `02_Codebase` |
| Solutions folder | `03_Solutions` | `03_Soluciones` | `03_Solutions` |
| Learning folder | `04_Learning` | `04_Aprendizaje` | `04_Learning` |
| Daily folder | `05_Daily` | `05_Diario` | `05_Daily` |
| Bugs subfolder | `Bugs` | `Bugs` | `Bugs` |
| Patterns subfolder | `Patterns` | `Patrones` | `Patterns` |
| Concepts subfolder | `Concepts` | `Conceptos` | `Concepts` |
| Decisions subfolder | `Decisions` | `Decisiones` | `Decisions` |

---

## Hub Notes to Create

1. **`01_Projects/[ProjectName]/[ProjectName].md`** — one per project
   - Links to: Architecture decisions, active tasks, tech stack used

2. **`02_Codebase/Codebase.md`** — codebase hub
   - Links to: all languages and frameworks used

3. **`03_Solutions/Solutions.md`** — solutions hub
   - Links to: Bugs, Patterns, Snippets

4. **`04_Learning/Learning.md`** — learning hub
   - Links to: Courses, Concepts, Books

---

## Routing Rules

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `bug-fix` | `03_Solutions/Bugs/` | bug, fix, error, issue, solved, arreglé |
| `pattern` | `03_Solutions/Patterns/` | pattern, approach, patrón, arquitectura |
| `snippet` | `03_Solutions/Snippets/` | snippet, función, helper, utility, code |
| `concept` | `04_Learning/Concepts/` | concepto, concept, learned, aprendí |
| `architecture` | `01_Projects/[project]/Architecture/` | arquitectura, design, structure, decision |
| `decision` | `01_Projects/[project]/Decisions/` | decided, decidí, chose, elegí, ADR |
| `course-note` | `04_Learning/Courses/[course]/` | curso, course, lecture, clase, módulo |
| `daily` | `05_Daily/` | hoy, today, daily, standup |

---

## Link Rules

| Note type | Auto-link to |
|---|---|
| `bug-fix` | Language/framework it's about (`[[02_Codebase/Languages/Python]]`), project if applicable |
| `pattern` | Related language/framework, related project if applicable |
| `concept` | Related language or framework, related solution if exists |
| `architecture` | Project hub, relevant patterns from Solutions |
| `decision` | Project hub, architecture note if exists |
| `course-note` | Learning hub, related concepts if they exist |
| `daily` | Active project notes, any decisions made that day |

---

## Diagnostic Questions that lead to this profile

User answers that suggest Developer profile:
- "I write code / build software"
- "I work with multiple languages or frameworks"
- "I need to remember solutions to bugs and patterns"
- "I want to track architecture decisions"
- "I'm a developer / engineer / CTO"
