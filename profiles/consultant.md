# Profile: Consultant / Project Manager

## Description
For consultants, freelancers, and project managers who work with multiple clients and need to track projects, meetings, deliverables, and knowledge per client.

---

## Folder Structure

```
01_Clients/
  [ClientName]/
    Projects/
    Meetings/
    Proposals/
    Contacts/
    [ClientName].md       ← client hub note
02_Services/
  [ServiceName].md        ← service hub note
03_Operations/
  Finance/
  Legal/
  Processes/
  Templates/
04_Knowledge/
  Methodologies/
  Learnings/
  References/
05_Daily/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Clients folder | `01_Clients` | `01_Clientes` | `01_Clients` |
| Services folder | `02_Services` | `02_Servicios` | `02_Services` |
| Operations folder | `03_Operations` | `03_Operaciones` | `03_Operations` |
| Knowledge folder | `04_Knowledge` | `04_Conocimiento` | `04_Knowledge` |
| Daily folder | `05_Daily` | `05_Diario` | `05_Daily` |
| Meetings subfolder | `Meetings` | `Reuniones` | `Meetings` |
| Projects subfolder | `Projects` | `Proyectos` | `Projects` |
| Proposals subfolder | `Proposals` | `Propuestas` | `Proposals` |
| Learnings subfolder | `Learnings` | `Aprendizajes` | `Learnings` |

---

## Hub Notes to Create

1. **`01_Clients/[ClientName]/[ClientName].md`** — one per client
   - Links to: all projects, meetings, proposals for that client
   - Fields: status (active/inactive), service, start date, key contacts

2. **`02_Services/[ServiceName].md`** — one per service offered
   - Links to: clients using this service, relevant methodologies

3. **`03_Operations/Operations.md`** — operations hub
   - Links to: Finance, Legal, Processes, Templates

4. **`04_Knowledge/Knowledge.md`** — knowledge hub
   - Links to: Methodologies, Learnings, References

---

## Routing Rules

When capturing a note, route it based on type:

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `meeting` | `01_Clients/[client]/Meetings/` | reunion, call, meeting, cliente, zoom |
| `project` | `01_Clients/[client]/Projects/` | proyecto, entregable, deliverable, milestone |
| `proposal` | `01_Clients/[client]/Proposals/` | propuesta, oferta, presupuesto, quote |
| `process` | `03_Operations/Processes/` | proceso, workflow, procedimiento, SOP |
| `template` | `03_Operations/Templates/` | plantilla, template, formato |
| `learning` | `04_Knowledge/Learnings/` | aprendí, insight, lesson, learned |
| `methodology` | `04_Knowledge/Methodologies/` | método, framework, approach, estrategia |
| `daily` | `05_Daily/` | hoy, today, daily, diario |

If no type matches, ask the user: "Is this related to a client, an operation, or general knowledge?"

---

## Link Rules

When creating a note, automatically add these wikilinks:

| Note type | Auto-link to |
|---|---|
| `meeting` | Client hub (`[[01_Clients/[client]/[client]]]`), active project if mentioned |
| `project` | Client hub, service used (`[[02_Services/[service]]]`) |
| `proposal` | Client hub, service hub |
| `learning` | Relevant methodology if exists, related client if applicable |
| `process` | Operations hub, related service if applicable |
| `daily` | Any meetings of that day (search by date), active projects |

---

## Diagnostic Questions that lead to this profile

User answers that suggest Consultant profile:
- "I manage projects for clients"
- "I work with multiple clients"
- "I need to track deliverables and meetings per client"
- "I'm a freelancer / consultant / agency"
- "I sell services"
