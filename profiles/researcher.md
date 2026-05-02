# Profile: Researcher / Writer

## Description
For academics, writers, journalists, and knowledge workers who need to connect ideas, build arguments from sources, and develop original thinking through a Zettelkasten-style approach.

---

## Folder Structure

```
00_Inbox/                 ← raw captures, unprocessed
01_Literature/
  Books/
  Papers/
  Articles/
  Podcasts/
02_Permanent/
  Concepts/
  Arguments/
  Questions/
  Contradictions/
03_Projects/
  [ProjectName]/          ← essay, thesis, book, article
    Outline/
    Drafts/
    [ProjectName].md
04_References/
  Authors/
  Sources/
05_Daily/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Inbox folder | `00_Inbox` | `00_Entrada` | `00_Inbox` |
| Literature folder | `01_Literature` | `01_Literatura` | `01_Literature` |
| Permanent folder | `02_Permanent` | `02_Permanente` | `02_Permanent` |
| Projects folder | `03_Projects` | `03_Proyectos` | `03_Projects` |
| References folder | `04_References` | `04_Referencias` | `04_References` |
| Concepts subfolder | `Concepts` | `Conceptos` | `Concepts` |
| Arguments subfolder | `Arguments` | `Argumentos` | `Arguments` |
| Questions subfolder | `Questions` | `Preguntas` | `Questions` |

---

## Hub Notes to Create

1. **`00_Inbox/Inbox.md`** — processing queue
   - Lists all unprocessed notes with links, to be reviewed and moved

2. **`02_Permanent/Map-of-Content.md`** — MOC (Map of Content)
   - The master index of all permanent concepts, grouped by theme
   - This is the most important note in a Zettelkasten vault

3. **`03_Projects/[ProjectName]/[ProjectName].md`** — one per writing project
   - Links to: all permanent notes used, outline, drafts

---

## Routing Rules

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `literature-note` | `01_Literature/[source-type]/` | leí, read, libro, book, paper, article, podcast |
| `permanent-note` | `02_Permanent/Concepts/` | idea permanente, concepto, concept, insight |
| `argument` | `02_Permanent/Arguments/` | argumento, claim, because, porque, therefore |
| `question` | `02_Permanent/Questions/` | pregunta, question, ¿, wonder, curious |
| `contradiction` | `02_Permanent/Contradictions/` | but, pero, contradice, contradicts, tension |
| `project-note` | `03_Projects/[project]/` | writing, essay, thesis, draft, borrador |
| `raw-capture` | `00_Inbox/` | (default for unclassified input) |

**Important rule for this profile:** Every note starts in `00_Inbox/` unless the user explicitly classifies it. Inbox is reviewed weekly.

---

## Link Rules

| Note type | Auto-link to |
|---|---|
| `literature-note` | All permanent concepts mentioned or implied in it |
| `permanent-note` | 3-5 existing permanent notes that relate (search by keywords) |
| `argument` | The concept it supports, contradicting arguments if they exist |
| `question` | Related concepts, related arguments |
| `project-note` | All permanent notes referenced in the project |
| `contradiction` | Both sides of the tension (link to each concept) |

**Zettelkasten linking principle:** Every permanent note must link to at least 2 other permanent notes. Isolated notes are flagged as orphans by /link-finder.

---

## Diagnostic Questions that lead to this profile

User answers that suggest Researcher profile:
- "I research topics / write essays or articles"
- "I read a lot and want to connect ideas"
- "I want to build a knowledge base over time"
- "I'm a student / academic / journalist / writer"
- "I want ideas to link to each other"
