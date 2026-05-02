# Profile: Student / Lifelong Learner

## Description
For students, bootcamp attendees, and lifelong learners who need to organize courses, connect concepts across subjects, track exercises, and build a personal knowledge base from formal and informal learning.

---

## Folder Structure

```
01_Courses/
  [CourseName]/
    Lectures/
    Exercises/
    Summaries/
    [CourseName].md       ← course hub note
02_Concepts/
  [Subject]/              ← e.g. Mathematics, Programming, History
03_Projects/
  [ProjectName]/
    Notes/
    [ProjectName].md
04_Resources/
  Books/
  Links/
  Cheatsheets/
05_Exams/
  [CourseName]/
    Flashcards/
    Past-Exams/
06_Daily/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Courses folder | `01_Courses` | `01_Cursos` | `01_Courses` |
| Concepts folder | `02_Concepts` | `02_Conceptos` | `02_Concepts` |
| Projects folder | `03_Projects` | `03_Proyectos` | `03_Projects` |
| Resources folder | `04_Resources` | `04_Recursos` | `04_Resources` |
| Exams folder | `05_Exams` | `05_Exámenes` | `05_Exams` |
| Daily folder | `06_Daily` | `06_Diario` | `06_Daily` |
| Lectures subfolder | `Lectures` | `Clases` | `Lectures` |
| Exercises subfolder | `Exercises` | `Ejercicios` | `Exercises` |
| Summaries subfolder | `Summaries` | `Resúmenes` | `Summaries` |
| Flashcards subfolder | `Flashcards` | `Tarjetas` | `Flashcards` |

---

## Hub Notes to Create

1. **`01_Courses/[CourseName]/[CourseName].md`** — one per course
   - Links to: all lectures, exercises, summaries, exam prep
   - Fields: subject, professor/source, start date, status (active/complete)

2. **`02_Concepts/Concepts.md`** — concepts master index
   - Links to: all concept notes, organized by subject

3. **`04_Resources/Resources.md`** — resources hub
   - Links to: key books, useful links, cheatsheets

---

## Routing Rules

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `lecture-note` | `01_Courses/[course]/Lectures/` | clase, lecture, lesson, módulo, unit |
| `exercise` | `01_Courses/[course]/Exercises/` | ejercicio, exercise, practice, problem, tarea |
| `summary` | `01_Courses/[course]/Summaries/` | resumen, summary, recap, overview |
| `concept` | `02_Concepts/[subject]/` | concepto, concept, definition, qué es |
| `project-note` | `03_Projects/[project]/Notes/` | proyecto, project, trabajo, assignment |
| `resource` | `04_Resources/[type]/` | libro, book, link, artículo, reference |
| `flashcard` | `05_Exams/[course]/Flashcards/` | flashcard, tarjeta, memorizar, remember |
| `daily` | `06_Daily/` | hoy, today, daily, study session |

---

## Link Rules

| Note type | Auto-link to |
|---|---|
| `lecture-note` | Course hub, relevant concepts if they already exist in `02_Concepts/` |
| `exercise` | Lecture note it relates to, concept it practices |
| `concept` | Other concepts in same subject, lectures where it appeared |
| `summary` | All lecture notes of that module, related concepts |
| `project-note` | Relevant concepts, course hub if related |
| `flashcard` | Concept note it tests, lecture where it appeared |
| `daily` | Active courses (link to current lecture), any exercises due |

**Key learning principle:** Every concept note should link to at least one place where it was used (a lecture, exercise, or project). Concepts without applications are flagged by /link-finder.

---

## Diagnostic Questions that lead to this profile

User answers that suggest Student profile:
- "I'm studying / in school / taking courses"
- "I want to organize my class notes"
- "I take a lot of courses online (Udemy, Coursera, etc.)"
- "I need to connect concepts across subjects"
- "I prepare for exams and want to review efficiently"
