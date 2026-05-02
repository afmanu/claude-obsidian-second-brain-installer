# Profile: Personal / Life OS

## Description
For individuals who want to organize their personal life — habits, goals, journaling, relationships, health, finances, and personal growth — in one integrated system.

---

## Folder Structure

```
01_Journal/
  Daily/
  Weekly/
  Monthly/
02_Goals/
  [Year]/
    Annual/
    Quarterly/
03_Areas/
  Health/
    Habits/
    Workouts/
    Nutrition/
  Finance/
    Budget/
    Investments/
  Relationships/
    People/
    Conversations/
  Growth/
    Skills/
    Reading/
04_Projects/
  [ProjectName]/
05_Reflections/
  Lessons/
  Gratitude/
  Values/
06_Resources/
  Books/
  Quotes/
  Inspiration/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Journal folder | `01_Journal` | `01_Diario` | `01_Journal` |
| Goals folder | `02_Goals` | `02_Objetivos` | `02_Goals` |
| Areas folder | `03_Areas` | `03_Áreas` | `03_Areas` |
| Projects folder | `04_Projects` | `04_Proyectos` | `04_Projects` |
| Reflections folder | `05_Reflections` | `05_Reflexiones` | `05_Reflections` |
| Resources folder | `06_Resources` | `06_Recursos` | `06_Resources` |
| Habits subfolder | `Habits` | `Hábitos` | `Habits` |
| Relationships subfolder | `Relationships` | `Relaciones` | `Relationships` |
| Lessons subfolder | `Lessons` | `Lecciones` | `Lessons` |

---

## Hub Notes to Create

1. **`02_Goals/[Year]/Annual/[Year]-Goals.md`** — annual goals hub
   - Links to: quarterly breakdowns, relevant projects and areas

2. **`03_Areas/Areas.md`** — life areas hub (like a life wheel)
   - Links to: Health, Finance, Relationships, Growth
   - Each area has a current status and focus

3. **`05_Reflections/Reflections.md`** — reflections hub
   - Links to: Lessons, Gratitude, Values notes

---

## Routing Rules

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `daily-journal` | `01_Journal/Daily/` | hoy, today, diario, daily, morning, mañana |
| `weekly-review` | `01_Journal/Weekly/` | esta semana, weekly, review, semana |
| `goal` | `02_Goals/[year]/` | objetivo, goal, want to, quiero, propósito |
| `habit` | `03_Areas/Health/Habits/` | hábito, habit, routine, rutina, cada día |
| `finance-note` | `03_Areas/Finance/` | dinero, money, gasto, expense, inversión |
| `person-note` | `03_Areas/Relationships/People/` | persona, person, [name], conocí, met |
| `lesson` | `05_Reflections/Lessons/` | aprendí, lesson, learned, me di cuenta, realized |
| `gratitude` | `05_Reflections/Gratitude/` | agradezco, grateful, thankful, gracias |
| `book-note` | `06_Resources/Books/` | libro, book, leí, read, reading |
| `quote` | `06_Resources/Quotes/` | cita, quote, dijo, said, frase |

---

## Link Rules

| Note type | Auto-link to |
|---|---|
| `daily-journal` | Weekly review of that week (if exists), any habits or goals mentioned |
| `weekly-review` | All daily journal entries of that week, relevant goal progress |
| `goal` | Relevant life area (Health, Finance, etc.), quarterly breakdown |
| `habit` | Health area hub, daily journal entries where it appears |
| `lesson` | Reflections hub, relevant goal or area it applies to |
| `person-note` | Relationships hub, any shared projects or conversations |
| `book-note` | Related lessons or insights extracted from it |
| `finance-note` | Finance area hub, relevant goal if budget-related |

**Personal OS principle:** The Weekly Review note is the connective tissue — it links daily journals, goal progress, and area check-ins into one coherent picture of the week.

---

## Diagnostic Questions that lead to this profile

User answers that suggest Personal profile:
- "I want to organize my personal life / habits / goals"
- "I journal daily or want to start"
- "I want to track health, finance, relationships"
- "I'm building a life system / personal OS"
- "I want to reflect and grow as a person"
