# Profile: Entrepreneur / Business Owner

## Description
For founders, entrepreneurs, and business owners who need to manage strategy, products, customers, marketing, team, and operations — all from one knowledge base.

---

## Folder Structure

```
01_Strategy/
  Vision/
  Goals/
  Decisions/
  Competitors/
02_Products/
  [ProductName]/
    Roadmap/
    Features/
    Feedback/
    [ProductName].md
03_Customers/
  Segments/
  Feedback/
  Cases/
04_Marketing/
  Campaigns/
  Content/
  Channels/
05_Team/
  People/
  Processes/
  Culture/
06_Finance/
  Metrics/
  Expenses/
  Revenue/
07_Learning/
  Books/
  Insights/
08_Daily/
```

### Language Mapping
| Element | english | spanish | mixed |
|---|---|---|---|
| Strategy folder | `01_Strategy` | `01_Estrategia` | `01_Strategy` |
| Products folder | `02_Products` | `02_Productos` | `02_Products` |
| Customers folder | `03_Customers` | `03_Clientes` | `03_Customers` |
| Marketing folder | `04_Marketing` | `04_Marketing` | `04_Marketing` |
| Team folder | `05_Team` | `05_Equipo` | `05_Team` |
| Finance folder | `06_Finance` | `06_Finanzas` | `06_Finance` |
| Learning folder | `07_Learning` | `07_Aprendizaje` | `07_Learning` |
| Daily folder | `08_Daily` | `08_Diario` | `08_Daily` |
| Roadmap subfolder | `Roadmap` | `Hoja de Ruta` | `Roadmap` |
| Decisions subfolder | `Decisions` | `Decisiones` | `Decisions` |

---

## Hub Notes to Create

1. **`01_Strategy/Strategy.md`** — strategy hub
   - Vision statement, current OKRs/goals, top 3 priorities
   - Links to: Decisions, Competitors

2. **`02_Products/[ProductName]/[ProductName].md`** — one per product
   - Links to: Roadmap, customer feedback, marketing campaigns

3. **`03_Customers/Customers.md`** — customer hub
   - Links to: Segments, Feedback, Cases

4. **`04_Marketing/Marketing.md`** — marketing hub
   - Links to: active campaigns, content pillars, channels

5. **`06_Finance/Finance.md`** — finance hub
   - Links to: key metrics, revenue sources, expense categories

---

## Routing Rules

| Note type | Destination folder | Trigger keywords |
|---|---|---|
| `decision` | `01_Strategy/Decisions/` | decidí, decided, choice, elegí, strategic |
| `product-idea` | `02_Products/[product]/Features/` | feature, idea, mejora, improvement, build |
| `customer-feedback` | `03_Customers/Feedback/` | feedback, cliente dijo, user said, complaint |
| `campaign` | `04_Marketing/Campaigns/` | campaña, campaign, launch, ad, post |
| `content-idea` | `04_Marketing/Content/` | contenido, content, post, artículo, video |
| `team-note` | `05_Team/People/` | equipo, team, hire, contratar, onboarding |
| `process` | `05_Team/Processes/` | proceso, SOP, process, workflow, how-to |
| `metric` | `06_Finance/Metrics/` | métrica, metric, KPI, revenue, MRR, churn |
| `learning` | `07_Learning/Insights/` | aprendí, insight, book, learned, lesson |
| `daily` | `08_Daily/` | hoy, today, daily, weekly |

---

## Link Rules

| Note type | Auto-link to |
|---|---|
| `decision` | Strategy hub, affected product/team area |
| `product-idea` | Product hub, relevant customer feedback if exists |
| `customer-feedback` | Customer hub, relevant product if mentioned |
| `campaign` | Marketing hub, relevant product |
| `metric` | Finance hub, relevant product or campaign |
| `learning` | Strategy hub (if strategic insight), relevant product/team area |
| `daily` | Active decisions, key metrics if mentioned |

---

## Diagnostic Questions that lead to this profile

User answers that suggest Entrepreneur profile:
- "I run / am building a business or startup"
- "I manage a team and products"
- "I need to track strategy, marketing, and operations"
- "I'm a founder / CEO / COO"
- "I want to connect customers, products, and strategy"
