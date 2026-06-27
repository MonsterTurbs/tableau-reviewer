from pathlib import Path
import re
import textwrap


OUT_MD = Path("Tagalog_Lesson_Reviewer.md")
OUT_PDF = Path("Tagalog_Lesson_Reviewer.pdf")


CONTENT = r"""# Tagalog Lesson Reviewer: Tableau Full Course

Source: plain.txt transcript + table of content.txt timestamps

Layunin ng reviewer na ito: maintindihan ng beginner ang buong flow ng Tableau course mula basic data concepts hanggang final Tableau project. Hindi ito literal na salin ng transcript. Inayos ito bilang study notes: malinaw, practical, at madaling balikan.

## Paano gamitin ang reviewer

- Basahin muna ang "Important terms" sa bawat section.
- Sundan ang timestamp kung gusto mong bumalik sa video/transcript.
- Tandaan ang pattern: concept muna, example, kailan gagamitin, at common mistake.
- Sagutan ang quiz sa dulo pagkatapos basahin.

# 00:00 - Intro

Ang course ay ginawa para dalhin ang learner mula zero knowledge hanggang kaya nang gumawa ng Tableau dashboards. Ang focus ay hindi lang pag-click sa tool, kundi pag-intindi kung paano gumagana ang data visualization, BI, data modeling, calculations, charts, dashboards, at project delivery.

Practical idea: kung beginner ka, huwag mong kabisaduhin lahat ng buttons agad. Mas mahalaga munang maintindihan kung bakit kailangan ang chart, anong data ang ginagamit, at paano makakatulong ang dashboard sa decision maker.

Important terms:
- Tableau: tool para gumawa ng charts, dashboards, at interactive data stories.
- Dashboard: collection ng charts at controls na nagbibigay ng quick view sa important metrics.
- Visualization: graphical representation ng data tulad ng bar chart, line chart, map, o table.
- BI or Business Intelligence: proseso ng paggamit ng data para makagawa ng better decisions.

Summary: Ang course ay practical Tableau training na nakasentro sa concepts, hands-on practice, at real project workflow.

Reviewer notes:
- Hindi sapat ang marunong mag-drag and drop. Kailangan maintindihan ang data.
- Goal ng dashboard: gawing madaling makita ang sagot sa business question.
- Ang best Tableau developer ay marunong mag-isip bilang analyst, designer, at project implementer.

# 03:20 - Tableau Course Structure

Ang course ay may 15 major sections. Nagsisimula sa basics: ano ang BI, data visualization, at Tableau. Pagkatapos, tatalakayin ang Tableau products, architecture, environment setup, data combining, metadata, organizing data, filtering, parameters, actions, calculations, charts, dashboards, at final project.

Simple flow ng learning:
1. Understand data and BI.
2. Understand Tableau ecosystem.
3. Prepare Tableau environment.
4. Build correct data sources.
5. Clean and organize fields.
6. Filter, calculate, and make charts.
7. Combine charts into dashboards.
8. Deliver a project from requirements to final dashboard.

Practical example: Kung sales manager ang user, hindi mo agad sisimulan sa kulay ng dashboard. Una mong tatanungin: anong tanong ang kailangang sagutin? Total sales? Profit? Monthly trend? Top products? From there, pipili ka ng data source, calculations, charts, at dashboard layout.

Summary: Ang course structure ay parang real Tableau project lifecycle: concept, setup, data source, analysis, visualization, dashboard, delivery.

# 08:35 - #1 Section: Tableau Basics

## 08:37 - Big Data Terms

Sa modern world, halos lahat ng ginagawa natin ay gumagawa ng data: online searches, purchases, emails, social media, phones, smart devices, machines, cars, at factories. Kapag sobra na ang dami, bilis, at klase ng data, pumapasok ang idea ng Big Data.

Important terms:
- Raw data: hilaw na data. Rows, numbers, text, logs, o files na hindi pa nalilinis at mahirap intindihin.
- Big Data: data na malaki ang volume, mabilis ang dating, at iba-iba ang format.
- 3 V's of Big Data: Volume, Velocity, Variety.
- Volume: dami ng data.
- Velocity: bilis ng generation at processing ng data.
- Variety: iba't ibang uri ng data, tulad ng structured, semi-structured, at unstructured.
- IoT or Internet of Things: mga device na connected sa internet at nagpapadala ng data.
- Data architecture: blueprint kung paano i-store, i-process, at i-access ang data.
- Data engineering: paggawa ng pipelines para kunin, linisin, baguhin, at ilipat ang data.
- ETL: Extract, Transform, Load. Kumuha ng data, ayusin ito, at ilagay sa target storage.
- Data modeling: pag-aayos ng entities/tables at relationships para maintindihan kung paano konektado ang data.
- Data mining: paghahanap ng patterns, trends, at hidden knowledge.
- Machine learning: paggamit ng historical data at algorithms para gumawa ng predictions.
- Data science: combination ng programming, math/statistics, at domain knowledge para kumuha ng insights.
- Data visualization: pag-convert ng raw numbers sa visuals para mas madaling maintindihan.

Layman's explanation: Ang raw data ay parang crude oil. May value siya, pero hindi pa agad magagamit. Kailangan munang linisin, ayusin, i-model, i-analyze, at ipakita sa paraan na madaling maintindihan.

Practical example: May online store ka. Raw data mo ay bawat order, click, product view, customer location, at payment record. Hindi mo agad malalaman kung aling product ang patok hangga't hindi mo ito nililinis, pinagsasama, at ginagawang chart.

Summary: Big Data is not just "maraming data." Ito ay data na kailangang i-handle nang maayos dahil malaki, mabilis, at iba-iba ang format.

Reviewer notes:
- Structured data: tables, rows, columns.
- Semi-structured data: XML, JSON, server logs.
- Unstructured data: videos, images, audio, free text.
- Data becomes valuable only when converted into insight.

## 16:54 - What is Business Intelligence (BI)

Business Intelligence or BI ay proseso ng pagkuha ng raw data, pag-analyze nito, at pag-present ng result para makatulong sa business decisions. Sa transcript, may example ng shops sa iba't ibang cities na may data tungkol sa sales, inventory, products, staff cost, at iba pa. Ang managers ay may tanong tulad ng "What happened?" at "What will happen?"

Important terms:
- Decision makers: managers, finance, HR, operations, o leaders na kailangang magdesisyon.
- Data analyst: naglilinis, nagko-connect, at nag-aaggregate ng data para masagot ang business questions.
- Data scientist: gumagamit ng mining, machine learning, at models para gumawa ng predictions o discover unknown insights.
- BI: bridge sa pagitan ng raw data at business decisions.

Layman's explanation: Ang BI ay parang dashboard ng kotse. Hindi mo tinitingnan ang raw engine signals. Tinitingnan mo ang speed, fuel, warning lights, at direction. Ganito rin sa business: hindi raw tables ang kailangan ng manager, kundi malinaw na indicators.

Practical example: Instead na spreadsheet na may libo-libong sales rows, gumawa ng dashboard na may total sales, profit, monthly trend, top products, at filters by city.

Summary: BI turns data into understandable information so people can decide faster and smarter.

## 19:34 - What is Data Visualization

Data visualization ay pag-convert ng numbers at raw data into charts, graphs, maps, at other visuals. Malakas ito dahil mas mabilis mag-process ang tao ng visual information kaysa plain text o spreadsheet.

Important terms:
- Data viz or data visualization: paggamit ng graphical elements para ipakita ang data.
- Storytelling: pagbuo ng malinaw na narrative mula sa data.
- Pattern: paulit-ulit o meaningful na behavior sa data.
- Trend: direction over time, tulad ng pataas o pababang sales.

Layman's explanation: Kapag puro numbers ang tinitingnan mo, mahirap makita kung ano ang nangyayari. Kapag ginawang chart, biglang nakikita ang mataas, mababa, outlier, at pattern.

Practical example: Kung may monthly sales table, mahirap makita agad kung kailan bumagsak ang sales. Sa line chart, makikita mo agad kung anong buwan nagkaroon ng drop.

Summary: Data visualization makes complex data easier to read, remember, and act on.

## 22:50 - Excel vs BI-Tools

Excel is useful and familiar, pero kapag lumalaki ang data at organization, lumalabas ang limitations. Modern BI tools like Tableau and Power BI are better for automation, large data, security, governance, sharing, at interactive dashboards.

Key comparison:
- Excel: madalas manual export/import, maraming file versions, limited capacity, harder security.
- Tableau/BI tools: direct connection sa sources, scheduled refresh, centralized sharing, role-based access, interactive dashboards.

Important terms:
- Automation: automatic refresh o update ng data/report.
- Capacity: kaya bang mag-handle ng malaking data volume.
- Security: control kung sino ang makakakita ng data.
- Row-level security or RLS: bawat user ay nakakakita lang ng rows na allowed sa role niya.
- Single source of truth: isang trusted report/dashboard imbes na maraming conflicting spreadsheet versions.

Practical example: Sa Excel, may "report_final.xlsx", "report_final_v2.xlsx", at "report_final_REAL.xlsx". Sa Tableau Server/Cloud, isang dashboard lang ang published at refreshed automatically.

Summary: Excel is great for small/manual work. BI tools are better for scalable, secure, automated, and shared analytics.

## 31:28 - Top 3 BI-Tools

Karaniwang top BI tools sa market ay Tableau, Power BI, at Qlik. Lahat ay ginagamit para gumawa ng business dashboards at visual analysis, pero may kanya-kanyang strengths, licensing, ecosystem, at user experience.

Reviewer notes:
- Tableau: strong sa visual analytics at interactive exploration.
- Power BI: strong sa Microsoft ecosystem at enterprise adoption.
- Qlik: known for associative data model and exploration.

Summary: Hindi tool name ang pinakamahalaga. Ang mahalaga ay kung kaya nitong sagutin ang business requirement nang reliable at understandable.

## 32:22 - What is Tableau

Tableau ay visual analytics platform na ginagamit para kumonekta sa data, gumawa ng charts, dashboards, stories, at mag-share ng insights. Ang target users nito ay hindi lang programmers. Puwede rin ang analysts at business users dahil drag-and-drop ang core interaction.

Important terms:
- Drag and drop analysis: pagbuo ng view sa pamamagitan ng paglagay ng fields sa rows, columns, marks, filters, at iba pa.
- Workbook: Tableau file na may data source, worksheets, dashboards, at stories.
- Worksheet: isang single visualization.
- Dashboard: combination ng multiple worksheets and controls.
- Story: sequence ng sheets/dashboards para magkwento ng analysis.

Summary: Tableau helps users explore data visually and communicate insights through dashboards.

## 34:50 - Why Tableau

Malakas ang Tableau dahil visual, interactive, mabilis sa data exploration, may maraming charting capability, may malaking community, at may ecosystem ng products para development, sharing, hosting, at viewing.

Main reasons:
- Madaling gumawa ng charts with drag and drop.
- Interactive dashboards with filters, parameters, and actions.
- Handles large data through live/extract connections.
- Strong community and learning resources.
- Useful across departments: sales, finance, HR, operations, logistics, marketing.

Practical example: Gumawa ka ng dashboard with sales forecast and product clusters. Kapag nag-click ang user sa isang segment, magbabago ang related charts. Ito ang interactive analysis na mahirap gawin sa static spreadsheet.

Summary: Tableau is powerful because it combines visual exploration, interactivity, scalability, and shareability.

# 39:54 - #2 Chapter: Tableau Products

## 39:54 - Tableau Development Products

May dalawang major categories ng Tableau products: development tools at sharing tools. Development tools ang ginagamit para gumawa ng data sources, charts, dashboards, at data preparation.

Development products:
- Tableau Desktop: paid full authoring tool. Para sa professional Tableau development.
- Tableau Public Desktop: free authoring tool, pero public ang publishing at may limitations.
- Tableau Prep: tool para linisin, i-transform, at ihanda ang data bago gamitin sa analysis.

Decision guide:
- Kung data preparation/cleaning ang main task, use Tableau Prep.
- Kung kailangan ng private/professional work, server/database/cloud connections, use Tableau Desktop.
- Kung learning or public portfolio lang at okay na public ang data, use Tableau Public.

Summary: Piliin ang development product base sa privacy, data source type, data size, at purpose.

## 43:36 - Tableau Sharing Process

Sharing process:
1. Gumawa ng data source at visuals sa Tableau Desktop/Public.
2. Gumawa ng worksheets, dashboards, or stories.
3. I-publish o i-share gamit ang Tableau Server, Tableau Cloud, Tableau Public, Tableau Reader, or Tableau Mobile.

Important terms:
- Developer/Creator: gumagawa ng workbook/dashboard.
- Consumer/Viewer: tumitingin at nakikipag-interact sa dashboard.
- Publish: pag-upload ng workbook/dashboard sa sharing platform.
- Collaborate: sabay-sabay na access, comments, sharing, permissions, refresh, at governance.

Practical example: Analyst builds sales dashboard in Tableau Desktop, publishes to Tableau Server, then managers open it in browser or Tableau Mobile.

Summary: Tableau workflow is build, publish, consume, and manage.

## 54:26 - Tableau Hosting: On-Prem, IaaS, SaaS

May tatlong common hosting models:
- On-premises: ikaw/organization ang nagma-manage ng hardware, software, security, updates, and operations.
- IaaS or Infrastructure as a Service: cloud provider ang may hardware, pero ikaw pa rin ang magse-setup/manage ng Tableau Server software.
- SaaS or Software as a Service: Tableau Cloud. Provider ang nagma-manage ng infrastructure and software.

Important terms:
- Infrastructure: servers, storage, networking, operating systems.
- Patching: updating software/security fixes.
- Scalability: ability to handle more users/data.
- Robustness: stable and reliable operation.

Decision guide:
- Need full control and strict internal hosting? On-prem.
- Want cloud hardware but still manage server software? IaaS.
- Want less admin work and managed platform? SaaS/Tableau Cloud.

Summary: Hosting choice is a tradeoff between control, responsibility, cost, security, and maintenance effort.

## 1:00:24 - Tableau Sharing Products

Sharing products:
- Tableau Server: private enterprise platform installed/managed by organization.
- Tableau Cloud: hosted SaaS platform managed by Tableau.
- Tableau Public: public platform for sharing visualizations to the world.
- Tableau Reader: free desktop viewer for packaged workbooks.
- Tableau Mobile: mobile app for viewing/interacting with Server or Cloud dashboards.

Decision guide:
- Public data and no strict refresh/privacy? Tableau Public.
- Private organization sharing and you manage infrastructure? Tableau Server.
- Private organization sharing but prefer managed hosting? Tableau Cloud.
- Send packaged file directly to someone? Tableau Reader, but no automatic refresh.
- Need phone/tablet access? Tableau Mobile with Server/Cloud.

Summary: Sharing product depends on audience, privacy, refresh needs, and management responsibility.

# 1:12:03 - #3 Section: Tableau Architecture

## 1:12:46 - Live vs Extract

Kapag connected ang Tableau sa data, may dalawang main connection types:
- Live connection: Tableau queries the source directly. Mas fresh ang data, pero performance depends sa source/database/network.
- Extract connection: kinokopya ang snapshot/subset ng data into Tableau extract. Mas mabilis kadalasan, pero kailangan i-refresh para maging updated.

Important terms:
- Data freshness: gaano ka-updated ang data.
- Performance: bilis ng dashboard.
- Extract: optimized copy ng data used by Tableau.

Decision guide:
- Need real-time or near real-time data? Live.
- Need faster dashboard and okay ang scheduled refresh? Extract.
- If source is slow but data does not need instant freshness, extract is usually practical.

Summary: Live favors freshness. Extract favors performance and portability.

## 1:14:48 - Tableau File Types

Tableau file types depend on whether they contain workbook, data source, extract, or packaged assets.

Important file types:
- .twb: Tableau Workbook. Contains workbook metadata, not the actual local data files.
- .twbx: Packaged Workbook. Contains workbook plus packaged data/assets.
- .tds: Tableau Data Source. Contains data source connection metadata.
- .tdsx: Packaged Data Source. Contains data source plus extract/local data assets.
- .hyper: Tableau extract data file.

Layman's explanation: .twb is like recipe instructions; .twbx is recipe plus ingredients packed together.

Summary: Use packaged files when sending work to someone who needs the data included.

## 1:19:16 - Tableau Desktop Architecture

Tableau Desktop has layers:
- Data source layer: connect to data, define relationships/joins/unions, set metadata.
- Worksheet layer: build one chart or visual.
- Dashboard layer: combine worksheets into one interactive screen.
- Story layer: arrange sheets/dashboards in sequence to explain a narrative.

Important terms:
- Data pane: list of fields in Tableau.
- Marks card: controls color, size, label, detail, tooltip, and mark type.
- Rows/Columns shelves: where fields define the structure of the view.
- Analytics pane: tools like reference lines, trend lines, forecasts.

Summary: Desktop architecture moves from data connection to single visual to dashboard to story.

## 1:26:39 - Tableau Server Architecture

Tableau Server has components that handle access, rendering, queries, metadata, extracts, caching, and background jobs.

Important components:
- Gateway: first entry point for web requests.
- Application Server: handles login, permissions, and general web application logic.
- VizQL Server: converts user actions into queries and renders visual output.
- Data Server: manages data connections, metadata, and security filtering.
- Repository: stores metadata like users, permissions, workbooks, schedules, and server info.
- File Store: stores extracts and files used by server.
- Cache Server: stores frequently used results/assets to improve speed.
- Backgrounder: runs scheduled jobs like extract refreshes and subscriptions.

Example flow: User opens a sales dashboard in browser. Gateway receives request, Application Server checks login, VizQL builds the view, Data Server gets needed data, Repository provides metadata/permissions, then the dashboard is returned to the browser.

Summary: Server architecture exists so many users can securely view, refresh, and interact with dashboards.

# 1:48:37 - #4 Section: Prepare the Environment

## 1:48:44 - Download & Install Tableau Public

For learning, Tableau Public is enough because it is free and includes many authoring features. Limitation: published work is public, so do not use confidential data.

Reviewer notes:
- Install Tableau Public Desktop.
- Use it for practice and portfolio.
- Never upload private company/customer data to public platforms.

## 1:50:06 - Create Tableau Public Account

Create account to publish visualizations online. This lets you store and share public dashboards.

Summary: Tableau Public account is useful for practice, sharing, and portfolio building.

## 1:51:26 - Get Training Datasets

Training datasets usually include tables like Orders, Customers, Products, and Locations. These are connected using keys like Customer ID and Product ID.

Important terms:
- Key field: common field used to connect tables.
- Orders table: often a fact table with transactions.
- Customers/Products tables: often dimension tables with descriptive info.
- Locale issue: decimal separator may differ by region, e.g. comma vs dot.

Practical example: Orders has Product ID. Products table also has Product ID. That common key lets Tableau relate the transaction to product name/category.

## 1:57:18 - Publish First Viz

Publishing means uploading the workbook/dashboard to Tableau Public/Server/Cloud so others can view it.

Reviewer notes:
- Check data privacy before publishing.
- Test the visualization after publishing.
- Make sure filters and interactions still work.

## 1:59:33 - Tour into the Tableau Interface

Main parts of Tableau interface:
- Start page: open/connect to data.
- Data source page: build data model and inspect fields.
- Worksheet: create one visualization.
- Dashboard: combine worksheets.
- Data pane: fields categorized as dimensions/measures.
- Marks card: controls appearance and detail.
- Show Me: suggests chart types based on selected fields.
- Status bar: shows marks, rows, columns, and basic view info.

Summary: Learn where things are: data source page for data, worksheet for charts, dashboard for layout.

# 2:13:01 - #5 Section: Combining Data

## 2:13:51 - Basics Data Modeling

Data modeling is organizing data into tables/entities and defining relationships between them. Sa BI, magandang data model ang foundation ng reliable dashboard.

Important terms:
- Entity: object or concept represented by a table, e.g. Customer, Product, Order.
- Fact table: table with events/transactions and numeric measures, e.g. Orders.
- Dimension table: descriptive table, e.g. Customers, Products.
- Star schema: one fact table in center connected to dimension tables.
- Snowflake schema: dimension tables are further normalized into related tables.
- Cardinality: relationship count, e.g. one-to-many, many-to-one.

Practical example: Orders is fact table. Customers and Products are dimensions. Orders connect to Customers via Customer ID and to Products via Product ID.

Summary: Good data modeling prevents wrong numbers and makes analysis easier.

## 2:19:57 - Logical & Physical Layers

Tableau data model has two layers:
- Logical layer: default layer where tables are connected using relationships. Tables stay separate.
- Physical layer: inside a logical table, where you can use joins and unions. Tables can be merged.

Important terms:
- Relationship: flexible link between logical tables.
- Join: physically combines columns from tables.
- Union: stacks rows from tables with same structure.
- Data blending: combines data sources at visualization level.

Summary: Use logical layer for relationships. Go to physical layer when you need joins/unions inside one logical table.

## 2:25:07 - Joins

Joins combine tables side by side using a common key. Common join types:
- Inner join: keeps only matching rows from both tables.
- Left join: keeps all rows from left table and matching rows from right.
- Right join: keeps all rows from right table and matching rows from left.
- Full outer join: keeps all rows from both tables.

Common risk: Joins can duplicate rows or lose rows if join type/key is wrong. This can make measures like Sales, Profit, or Average incorrect.

Practical example: If customers without orders are removed by an inner join, your customer count becomes wrong.

Summary: Joins are useful but static and can change row-level data. Validate counts after joining.

## 2:33:59 - Union

Union stacks tables vertically. Use it when tables have the same columns/structure.

Requirements:
- Same or compatible fields.
- Usually same business meaning.
- Best for appending similar files/tables, e.g. Orders_2022 + Orders_2023.

Practical example: If you have one CSV per month with same columns, union them into one Orders table.

Summary: Join adds columns. Union adds rows.

## 2:40:54 - Relationships

Relationships are Tableau's recommended default method for connecting logical tables. They keep tables separate and let Tableau decide how to query based on fields used in the view.

Settings to understand:
- Relationship key: common field, e.g. Customer ID.
- Cardinality: one/many on each side.
- Referential integrity: whether records always match or only some match.

Best practice from transcript: if unsure, many-to-many is safer for correctness. For better performance, configure correct one/many cardinality when you are sure.

Summary: Relationships are flexible and reduce risk of duplicated/lost data compared with joins.

## 2:57:28 - Data Blending

Data blending combines data from different data sources at the visualization level. One source becomes primary, another secondary.

Important terms:
- Primary data source: first source used in the worksheet, often blue check/indicator.
- Secondary data source: supporting source used after primary, often orange indicator.
- Blend relationship: fields used to connect the sources.

When to use:
- Tables are in different data sources and cannot be joined/related normally.
- You need worksheet-level combination.

Limitation: It is less flexible than relationships in a single data source and can be harder to manage.

Summary: Use data blending when combining across separate data sources at worksheet level.

## 3:15:57 - Summary: Combining Methods

Combining methods:
- Joins: physical layer, side-by-side columns, can duplicate/lose data.
- Union: physical layer, stack rows, for same structure.
- Relationships: logical layer, flexible, Tableau-recommended default.
- Data blending: visualization level, for separate data sources.

Decision guide:
- Same entity split into multiple files/years? Union.
- Need to physically merge columns in one logical table? Join.
- Different entities in same data model? Relationship.
- Different data sources and worksheet-level mix? Data blending.

Reviewer notes:
- Always validate row counts, distinct counts, and totals.
- Prefer relationships when possible.
- Joins are not bad, but they require stronger checking.

# 3:28:46 - #6 Section: Tableau Metadata

## 3:29:42 - Data Types

Metadata means information about your fields: name, data type, role, geographic role, default aggregation, etc. Tableau guesses metadata when you connect data, but you must check it.

Main data types:
- String: text, names, categories.
- Number whole: integers like quantity or customer count.
- Number decimal: values with decimals like price or discount.
- Date: date only.
- Date & time: date plus time.
- Boolean: true/false.
- Geographic: location fields assigned a geographic role.

Important warning: Keys used in joins/relationships must have matching data types. Customer ID as string cannot properly match Customer ID as number without correction.

Summary: Wrong data type can break relationships, calculations, filters, and charts.

## 3:48:35 - Geographic & Image Roles

Geographic role tells Tableau a field is a location such as Country, State, City, Postal Code, Latitude, or Longitude. This enables map views.

Image role lets Tableau use image URLs or image fields in visualization contexts where supported.

Practical example: If "Germany" is just a string, Tableau treats it as text. If assigned Country/Region geographic role, Tableau can place it on a map.

Summary: Roles add meaning beyond the raw data type.

## 3:53:18 - Dimensions & Measures

Dimensions are fields used to slice, group, filter, or organize data. Measures are numeric fields used for calculations and aggregation.

Examples:
- Dimensions: Category, Country, Customer Name, Order Date.
- Measures: Sales, Profit, Quantity, Discount.

Important difference:
- Dimensions define level of detail.
- Measures answer "how much/how many."

Practical example: "Sales by Category" uses Category as dimension and Sales as measure.

Summary: Dimension = by what. Measure = what number.

## 4:10:57 - Discrete vs Continuous

Discrete fields create distinct headers or categories. Continuous fields create axes and ranges.

Important terms:
- Discrete: separate values, often blue pill in Tableau.
- Continuous: ongoing range, often green pill in Tableau.

Examples:
- Discrete date: Year as separate headers: 2021, 2022, 2023.
- Continuous date: timeline axis from one date to another.
- Discrete numeric bin: score groups like 0-10, 10-20.
- Continuous measure: Sales axis.

Summary: Discrete creates categories/headers. Continuous creates axes/ranges.

## 4:25:34 - Summary: Tableau Metadata

Reviewer notes:
- Check data types immediately after connection.
- Set geographic roles for maps.
- Understand dimensions/measures before building charts.
- Blue vs green pills affect chart structure.

# 4:27:16 - #7 Section: Renaming & Aliases

## 4:27:50 - Naming Conventions

Good naming makes Tableau easier to understand and maintain. Use clear, consistent names for fields, tables, sheets, dashboards, and calculations.

Best practices:
- Use business-friendly field names.
- Avoid cryptic names like "SUM_SLS_23_Q".
- Use consistent capitalization.
- Name calculations based on result, e.g. "Sales Current Year", not "Calc 1".

Summary: Clear names reduce confusion for both developers and users.

## 4:38:28 - Renaming

Renaming can be done for fields, tables, worksheets, dashboards, and calculated fields. In Tableau, renaming display names does not always rename the original database column; it often changes how Tableau shows it.

Practical example: Rename "Cust_ID" to "Customer ID" for readability.

Reviewer note: Rename fields in a way that matches business language, not just technical database names.

## 4:48:46 - Aliases

Aliases change how field values are displayed. They are useful for coded values.

Practical example:
- Original value: "DE"
- Alias: "Germany"
- Original value: "US"
- Alias: "United States"

Summary: Rename fields for column names. Use aliases for values inside a field.

# 4:57:26 - #8 Section: Organizing Data

## 4:58:13 - Hierarchy

Hierarchy groups dimensions into drill-down paths. Common example: Country > State > City > Postal Code.

Use case: Let users start high level then drill down into details.

Practical example: Sales by Country, then expand to City without building a separate chart.

Summary: Hierarchies organize dimensions into natural levels.

## 5:16:03 - Groups

Groups combine dimension members into custom categories.

Practical example: Group several small product subcategories into "Others" or group selected countries into "Europe Focus Markets."

Summary: Groups are manual business-friendly buckets.

## 5:28:57 - Cluster Group

Clusters are automatic groupings based on patterns in data. Tableau can cluster marks using variables/measures.

Practical example: Customers can be clustered by Sales and Profit into high-value, low-profit, or average segments.

Summary: Groups are manual. Clusters are data-driven.

## 5:38:37 - Sets

Sets define a subset of members based on condition or manual selection. Sets can be dynamic and update when data changes.

Important terms:
- Set: selected subset of dimension members.
- In/Out: whether a member belongs to a set.
- Combined set: result of combining sets using logic like union/intersection/difference.

Use cases:
- Top 10 customers by sales.
- Customers with Profit > 1000.
- Products in selected campaign.

Summary: Sets are powerful for comparisons, dynamic membership, and advanced interactivity.

## 6:02:25 - Bins & Histograms

Bins divide a measure into equal-sized groups. Histograms show how many data points fall into each bin.

Important terms:
- Bin: interval group, e.g. score 0-10, 10-20.
- Histogram: chart showing distribution of values across bins.
- Distribution: how values are spread.
- Outlier: unusual value far from the rest.

Practical example: Customer scores from 0 to 100 can be binned by 10s. Histogram shows whether most customers are low, medium, or high score.

Summary: Bins create groups from measures. Histograms reveal distribution, peaks, valleys, and outliers.

# 6:12:55 - #9 Section: Filtering & Sorting Data

## 6:13:40 - Understand Tableau Filters

Filters remove or keep subsets of data for a purpose. Tableau has several filter types and an order of operations.

Common filter types:
- Extract filter: limits data included in extract.
- Data source filter: limits data for the whole data source.
- Context filter: creates a filtered context before other dependent filters.
- Dimension filter: filters categorical fields.
- Measure filter: filters aggregated numeric values.
- Table calculation filter: filters after table calculations.
- User filter/security filter: filters by user permission or role.

Important idea: Not all filters happen at the same time. Order matters.

Summary: Filters control what data enters the analysis and what users can explore.

## 6:25:11 - How to Create Filters

Ways to create filters:
- Drag a field to Filters shelf.
- Right-click field and choose filter/show filter.
- Use filter cards in the view.
- Use context filters for performance/dependent filtering.
- Use Top N filters for ranking.
- Use relative date filters for dynamic periods.

Practical examples:
- Show only year 2023.
- Show only Category = Technology.
- Show Top 10 customers by Sales.
- Show orders from the last 30 days.

Reviewer notes:
- Check whether filtering should happen globally or only on one sheet.
- Use "Apply to worksheets" carefully.
- Test totals after filtering.

## 6:48:05 - Customizing Filters

Filter cards can be customized for user experience.

Common options:
- Single value list/dropdown.
- Multiple values list/dropdown.
- Wildcard match.
- Slider for ranges.
- Relative date filter.
- Top tab for Top N.
- Include/exclude values.
- Show All option.
- Customize title and labels.

Best practices:
- Use dropdowns to save space.
- Use relevant values only when filter choices depend on other filters.
- Avoid too many visible filters; they overwhelm users.
- Name filters clearly.
- Hide technical fields from end users.

Summary: Filtering is not just data logic. It is also dashboard usability.

# 8:03:50 - #10 Section: Tableau Parameters

Parameters are user-controlled variables. They replace static values in calculations, filters, reference lines, titles, bins, and more.

Important terms:
- Parameter: value chosen by user, like a variable.
- Dynamic calculation: calculation changes based on selected parameter value.
- Reference line: line in chart used as threshold/target.
- Swap measure/dimension: using parameter to let user choose what field is shown.

Use cases from transcript:
- Dynamic threshold in KPI colors.
- Dynamic reference line.
- Parameter-driven filters.
- Switch between dimensions.
- Switch between measures.
- Dynamic titles/text.
- Dynamic bin size for histograms.

Practical example: Instead of hardcoding "Profit < 10000 = Red", create a Profit Threshold parameter. User can choose 5000, 10000, or 20000.

Summary: Parameters make one view flexible enough to answer multiple requirements.

Reviewer notes:
- Parameter alone does nothing; it must be used in calculation/filter/reference line/etc.
- Always show parameter control if users need to change it.
- Update titles/tooltips so users know what parameter is selected.

# 8:32:09 - #11 Section: Tableau Actions

Actions make dashboards interactive. A user action like hover, select, or menu click can trigger a change.

Important terms:
- Source sheet: sheet where action starts.
- Target sheet: sheet affected by the action.
- Trigger: hover, select, or menu.
- Filter action: clicking a mark filters another view.
- Highlight action: clicking/hovering highlights related marks.
- URL action: opens a webpage.
- Go to Sheet action: navigates to another sheet/dashboard.
- Set action: changes set membership.
- Parameter action: changes parameter value.

Practical example: Click a product category in a bar chart, and the sales trend chart filters to that category.

Summary: Actions turn dashboards from static reports into guided exploration tools.

# 9:05:56 - #12 Section: Tableau Calculations

Calculations create new fields from existing data. They are essential for custom logic, KPIs, transformations, labels, and advanced charts.

Important terms:
- Calculated field: custom field created using formula.
- Function: built-in operation like SUM, IF, LEFT, DATEPART.
- Syntax: rules for writing valid formula.
- Aggregation: summarizing values like SUM, AVG, MIN, MAX, COUNT.

Practical example: Create Profit Ratio = SUM([Profit]) / SUM([Sales]).

Reviewer notes:
- Break complex calculations into smaller intermediate fields when useful.
- Test calculations in a simple table before using in complex charts.
- Check level of detail: row-level, aggregate, table calculation, or LOD.

## 9:31:33 - Types of Tableau Calculations

Four major calculation types:
- Row-level calculation: computed for each row before aggregation.
- Aggregate calculation: computed after values are aggregated in the view.
- Table calculation: computed based on the table/view result, e.g. running total, percent of total.
- LOD expression: controls calculation level of detail independent of the view.

Decision guide:
- Need per-row logic? Row-level.
- Need SUM/AVG level in current view? Aggregate.
- Need running total/rank/percent across view? Table calculation.
- Need fixed granularity regardless of view? LOD.

Summary: Choose calculation type based on when and at what detail the result should be computed.

## 9:53:53 - Number Functions

Number functions manipulate numeric values.

Examples:
- ROUND: round number.
- CEILING/FLOOR: move number up/down to whole boundary.
- ABS: absolute value.
- SQRT: square root.
- POWER: exponent.

Use case: clean decimals, format KPI values, calculate ratios, or create thresholds.

## 10:04:12 - String Functions

String functions manipulate text.

Examples:
- LEFT/RIGHT/MID: extract part of text.
- LEN: length of text.
- FIND/CONTAINS: search text.
- REPLACE: replace text.
- SPLIT: split text by delimiter.
- UPPER/LOWER: change case.
- TRIM: remove extra spaces.

Practical example: Extract product code from "ABC-123-Monitor" using SPLIT or MID.

Summary: String functions clean and reshape text fields.

## 11:27:55 - Date Functions

Date functions work with dates and time.

Examples:
- TODAY: current date.
- NOW: current date and time.
- DATEPART: get part like year/month/day.
- DATETRUNC: truncate date to month/year level.
- DATEDIFF: difference between dates.
- DATEADD: add interval to date.

Practical example: Show orders from current year by using DATEPART('year', [Order Date]) = DATEPART('year', TODAY()).

Summary: Date functions are needed for trends, periods, aging, and dynamic time filters.

## 12:17:31 - Null Functions

Null means missing or unknown value. Nulls can affect averages, counts, calculations, and charts.

Common functions:
- ISNULL: checks if value is null.
- IFNULL: replaces null with alternative value.
- ZN: converts null numeric values to zero.

Important warning: Replacing null with zero is not always correct. Null can mean "unknown", while zero means "known value of nothing."

Summary: Handle nulls intentionally, especially before aggregates.

## 12:30:33 - Logical Functions

Logical functions let calculations make decisions.

Examples:
- IF / THEN / ELSEIF / ELSE / END
- CASE / WHEN / THEN / ELSE / END
- AND, OR, NOT
- IN

Practical example:
IF SUM([Sales]) > 200000 THEN "Green"
ELSEIF SUM([Sales]) > 100000 THEN "Orange"
ELSE "Red"
END

Summary: Logical functions create categories, KPIs, flags, and conditional formatting.

## 13:16:13 - Aggregate Functions

Aggregate functions summarize many rows.

Examples:
- SUM: total.
- AVG: average.
- MIN/MAX: smallest/largest.
- COUNT: count values.
- COUNTD: count distinct values.
- MEDIAN: middle value.

Practical example: SUM(Sales) by Category shows total sales per category.

Summary: Aggregates answer business questions at the level of the view.

## 13:35:24 - Attribute Function ATTR()

ATTR returns a value if all underlying rows have the same value. If multiple values exist, Tableau may show an asterisk.

Use case: safely display dimensions in aggregate contexts.

Layman's explanation: ATTR asks, "Is there exactly one value here? If yes, show it. If not, signal that there are multiple."

Summary: ATTR helps avoid misleading dimension display when multiple values exist.

## 13:59:29 - Fixed

FIXED LOD calculates at a specified level, regardless of the view's current dimensions.

Example:
{ FIXED [Customer ID] : SUM([Sales]) }

Meaning: calculate total sales per customer, even if the current chart is by Category or Year.

Use case: customer-level metrics, cohort logic, stable denominators.

## 14:08:55 - Exclude

EXCLUDE removes a dimension from the calculation level, based on current view.

Example:
{ EXCLUDE [Category] : SUM([Sales]) }

Meaning: calculate sales while ignoring Category in the view.

Summary: EXCLUDE is useful when you want broader totals while the view has more detail.

## 14:14:26 - Include

INCLUDE adds a dimension to the calculation level, even if it is not displayed in the view.

Example:
{ INCLUDE [Order ID] : SUM([Sales]) }

Meaning: compute with Order ID detail included, then aggregate to the view.

Summary: INCLUDE is useful when calculation needs more detail than what the chart shows.

# 15:02:51 - #13 Section: Tableau Charts

The course builds many chart types. The key lesson is not to memorize 63 charts, but to choose the right chart for the question.

Major chart families and uses:
- Bar charts: compare categories.
- Line charts: show trends over time.
- Area charts: show trend plus volume.
- Pie/donut charts: show simple part-to-whole, but use carefully.
- Treemap: part-to-whole with many categories.
- Scatter plot: relationship between two measures.
- Histogram: distribution of one measure.
- Box plot: distribution and outliers.
- Maps: geographic analysis.
- Heat map/highlight table: intensity across categories.
- Bullet chart: actual vs target.
- Gantt chart: duration/timeline.
- Waterfall chart: positive/negative contribution to total.
- KPI cards: quick key numbers.
- Sparkline: compact trend line.
- Bar-in-bar: compare current vs previous or actual vs target.
- Dual-axis chart: combine two measures in one view, with caution.

Decision guide by question:
- "Which category is higher?" Use bar chart.
- "How did it change over time?" Use line chart.
- "Where is it happening?" Use map.
- "How are values distributed?" Use histogram or box plot.
- "How are two measures related?" Use scatter plot.
- "What is current vs target?" Use bullet chart or bar-in-bar.
- "What makes up the total?" Use stacked bar, treemap, or limited pie/donut.

Important chart tips:
- Sort bars when comparing.
- Use labels only where helpful.
- Avoid too many colors.
- Use consistent colors for same meanings.
- Do not use pie charts with too many slices.
- Always match chart type to the business question.

Summary: Good chart selection starts from the question, not from what looks fancy.

Reviewer notes:
- A simple chart that answers the question is better than a complex chart that confuses users.
- Test readability at dashboard size, not just full worksheet size.
- Use tooltips for supporting details, not for hiding the main answer.

# 17:55:35 - #14 Section: Tableau Dashboards

Dashboard building means arranging multiple charts, filters, text, legends, images, and controls into one usable screen.

Important terms:
- Tiled layout: objects snap into structured containers.
- Floating layout: objects can be placed freely.
- Container: layout object that groups and controls spacing of dashboard items.
- Horizontal container: items side by side.
- Vertical container: items stacked top to bottom.
- Padding: spacing inside or outside objects.
- Dashboard action: interaction between objects.

Best practices:
- Start with purpose and user question.
- Use containers to keep layout clean.
- Keep spacing consistent.
- Put KPIs at the top if users need quick overview.
- Put filters where users can find them, but avoid clutter.
- Use actions to make charts interactive.
- Test the dashboard in presentation/viewer mode.

Practical example: Sales dashboard may have KPIs at top, monthly sales trend in the middle, product/category comparison below, and a collapsible filter panel on the side.

Summary: A dashboard is not just a pile of charts. It is a designed decision-making interface.

# 18:22:08 - #15 Section: Tableau Project

The final project shows a real workflow from requirements to dashboard delivery.

Project phases:
1. Analyze user requirements.
2. Decide charts for each requirement.
3. Design dashboard mockup.
4. Prepare data source.
5. Build calculated fields.
6. Build charts.
7. Plan dashboard containers.
8. Build dashboard layout.
9. Format, clean, and test.
10. Add interactivity and navigation.
11. Deliver final dashboards.

Example project requirements:
- Show KPI cards for sales/profit/quantity or customers.
- Compare current year vs previous year.
- Show monthly trends using sparklines.
- Show subcategory comparisons using bar-in-bar.
- Show data distribution using histogram.
- Show top 10 customers by profit.
- Allow filtering by product and location information.
- Make charts interactive.
- Add navigation icons between sales and customer dashboards.

Important project lessons:
- Do not rush into building charts without a plan.
- Translate every requirement into a chart or dashboard element.
- Use one consistent mockup/design for related dashboards.
- Reuse structure when making a second dashboard.
- Test calculations in simple tables before relying on them in visuals.
- Test filters, parameters, actions, and navigation.

Summary: Real Tableau work is structured. Requirements drive chart choices, chart choices drive layout, and testing protects correctness.

# Final Reviewer Cheat Sheet

Core concepts:
- BI: using data to support decisions.
- Data visualization: turning data into visuals.
- Tableau: visual analytics platform.
- Worksheet: one chart.
- Dashboard: multiple charts/controls in one screen.
- Dimension: category/grouping field.
- Measure: numeric field.
- Discrete: separate headers/categories.
- Continuous: axis/range.
- Relationship: flexible logical table connection.
- Join: physical side-by-side merge.
- Union: vertical row stacking.
- Data blending: worksheet-level combination across sources.
- Parameter: user-controlled variable.
- Action: user interaction that changes dashboard behavior.
- Calculation: custom field/formula.
- LOD: calculation with controlled level of detail.

Common mistakes to avoid:
- Publishing private data to Tableau Public.
- Trusting Tableau's guessed data types without checking.
- Joining tables without validating duplicates/lost records.
- Using too many filters on a dashboard.
- Choosing a chart because it looks advanced, not because it answers the question.
- Replacing nulls with zero without understanding meaning.
- Making calculations directly in complex visuals without testing.
- Building dashboards before understanding requirements.

# Practice Quiz

1. Ano ang ibig sabihin ng BI?
2. Ano ang difference ng raw data at insight?
3. Ibigay ang 3 V's of Big Data.
4. Kailan mas practical gamitin ang Tableau kaysa Excel?
5. Ano ang difference ng Tableau Desktop at Tableau Public?
6. Ano ang difference ng live connection at extract connection?
7. Ano ang .twbx?
8. Ano ang role ng VizQL Server?
9. Ano ang difference ng logical layer at physical layer?
10. Ano ang difference ng join at union?
11. Bakit recommended ang relationships sa Tableau?
12. Kailan ginagamit ang data blending?
13. Ano ang dimension? Magbigay ng example.
14. Ano ang measure? Magbigay ng example.
15. Ano ang difference ng discrete at continuous?
16. Ano ang alias sa Tableau?
17. Para saan ang hierarchy?
18. Ano ang difference ng group at set?
19. Ano ang histogram?
20. Bakit mahalaga ang order of operations sa filters?
21. Ano ang parameter?
22. Bakit hindi sapat gumawa lang ng parameter control?
23. Ano ang dashboard action?
24. Ibigay ang apat na types ng Tableau calculations.
25. Kailan gagamit ng FIXED LOD?
26. Ano ang ginagawa ng IFNULL o ZN?
27. Anong chart ang bagay para sa trend over time?
28. Anong chart ang bagay para sa distribution?
29. Ano ang purpose ng containers sa dashboard?
30. Bakit kailangan magsimula sa requirements sa Tableau project?

# Answer Key

1. Business Intelligence: paggamit ng data analysis at reporting para makagawa ng better decisions.
2. Raw data ay hilaw at mahirap intindihin; insight ay meaningful understanding/actionable finding mula sa data.
3. Volume, Velocity, Variety.
4. Kapag kailangan ng automation, large data handling, security, centralized sharing, at interactive dashboards.
5. Desktop is paid/professional/private authoring tool; Public is free but intended for public publishing/learning.
6. Live queries source directly for freshness; extract uses copied optimized data for performance.
7. Packaged workbook containing workbook plus data/assets.
8. It converts user interactions into queries and renders visualizations.
9. Logical layer uses relationships and keeps tables separate; physical layer uses joins/unions and can merge tables.
10. Join adds columns side by side; union stacks rows vertically.
11. Relationships are flexible and reduce risk of duplicate/lost rows compared with joins.
12. When combining different data sources at worksheet/visualization level.
13. Dimension is grouping/category field, e.g. Category, Country, Customer Name.
14. Measure is numeric field for calculation, e.g. Sales, Profit, Quantity.
15. Discrete creates separate headers/categories; continuous creates axis/range.
16. Alias changes displayed value names, e.g. DE shown as Germany.
17. Hierarchy creates drill-down levels like Country > City > Postal Code.
18. Group is manual grouping of members; set is subset membership that can be dynamic/condition-based.
19. Chart showing distribution of values across bins.
20. Because filters happen at different stages and can affect results/performance differently.
21. User-controlled variable value used in calculations, filters, reference lines, titles, etc.
22. Parameter must be connected to a calculation/filter/reference line/etc. to affect the view.
23. Interaction triggered by user action, such as filter, highlight, URL, navigation, set, or parameter action.
24. Row-level, aggregate, table calculation, and LOD expression.
25. When calculation must stay at a specified granularity regardless of current view.
26. They handle null values; IFNULL replaces null, ZN converts null numeric values to zero.
27. Line chart.
28. Histogram or box plot.
29. Containers organize layout, alignment, spacing, and structure.
30. Requirements define what questions to answer, which charts to build, and how the dashboard should work.
"""


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class SimplePDF:
    def __init__(self):
        self.pages = []
        self.width = 595
        self.height = 842
        self.left = 54
        self.right = 54
        self.top = 54
        self.bottom = 54
        self.y = self.height - self.top
        self.current = []
        self.page_no = 0
        self.add_page()

    def add_page(self):
        if hasattr(self, "current") and self.current:
            self._footer()
            self.pages.append("\n".join(self.current))
        self.page_no += 1
        self.current = []
        self.y = self.height - self.top

    def _footer(self):
        footer = f"Page {self.page_no}"
        self.current.append("BT /F1 8 Tf 0.35 0.35 0.35 rg")
        self.current.append(f"1 0 0 1 {self.width - self.right - 38} 28 Tm ({footer}) Tj ET")

    def ensure(self, needed):
        if self.y - needed < self.bottom:
            self.add_page()

    def draw_line(self, text, size=10, font="F1", indent=0, color="0 0 0", leading=None):
        if leading is None:
            leading = size + 4
        self.ensure(leading)
        x = self.left + indent
        self.current.append(f"BT /{font} {size} Tf {color} rg 1 0 0 1 {x:.2f} {self.y:.2f} Tm ({pdf_escape(text)}) Tj ET")
        self.y -= leading

    def space(self, pts):
        self.ensure(pts)
        self.y -= pts

    def finish(self):
        self._footer()
        self.pages.append("\n".join(self.current))

        objects = []
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        kids = []
        page_obj_ids = []
        content_obj_ids = []
        for i, stream in enumerate(self.pages):
            page_id = 3 + i * 2
            content_id = page_id + 1
            page_obj_ids.append(page_id)
            content_obj_ids.append(content_id)
            kids.append(f"{page_id} 0 R")
        objects.append(f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(self.pages)} >>")
        for page_id, content_id, stream in zip(page_obj_ids, content_obj_ids, self.pages):
            objects.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.width} {self.height}] "
                f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> "
                f"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> >> >> "
                f"/Contents {content_id} 0 R >>"
            )
            data = stream.encode("latin-1", errors="replace")
            objects.append(f"<< /Length {len(data)} >>\nstream\n{stream}\nendstream")

        out = ["%PDF-1.4\n%\xE2\xE3\xCF\xD3\n"]
        offsets = [0]
        for i, obj in enumerate(objects, start=1):
            offsets.append(sum(len(part.encode("latin-1", errors="replace")) for part in out))
            out.append(f"{i} 0 obj\n{obj}\nendobj\n")
        xref = sum(len(part.encode("latin-1", errors="replace")) for part in out)
        out.append(f"xref\n0 {len(objects)+1}\n")
        out.append("0000000000 65535 f \n")
        for off in offsets[1:]:
            out.append(f"{off:010d} 00000 n \n")
        out.append(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n")
        OUT_PDF.write_bytes("".join(out).encode("latin-1", errors="replace"))


def wrap_lines(text, size, indent=0, bullet_prefix=""):
    usable = 595 - 54 - 54 - indent
    avg = size * 0.50
    width_chars = max(28, int(usable / avg))
    if bullet_prefix:
        subsequent = " " * len(bullet_prefix)
        return textwrap.wrap(
            text,
            width=width_chars,
            initial_indent=bullet_prefix,
            subsequent_indent=subsequent,
            break_long_words=False,
            break_on_hyphens=False,
        )
    return textwrap.wrap(text, width=width_chars, break_long_words=False, break_on_hyphens=False) or [""]


def render_markdown_to_pdf(md: str):
    pdf = SimplePDF()
    for raw in md.splitlines():
        line = raw.rstrip()
        label_icons = {
            "[GUIDE]": ":)",
            "[SIMPLE]": ":D",
            "[EXAMPLE]": "->",
            "[DECIDE]": "?",
            "[WATCH OUT]": "!",
            "[MEMORY HOOK]": "*",
            "[TAKEAWAY]": "=",
            "[CHECK]": "OK",
            "[QUIZ]": "??",
            "[PRACTICE]": ">>",
            "[SCAN]": "--",
            "[STUDY]": "::",
        }
        for label, icon in label_icons.items():
            if line.startswith(label) and not line.startswith(f"{label} {icon}"):
                line = line.replace(label, f"{label} {icon}", 1)
                break
        if not line:
            pdf.space(5)
            continue
        if line.startswith("# "):
            if pdf.y < 700 and pdf.page_no > 1:
                pdf.add_page()
            pdf.space(4)
            for part in wrap_lines(line[2:], 18):
                pdf.draw_line(part, size=18, font="F2", color="0.05 0.12 0.20", leading=23)
            pdf.space(6)
        elif line.startswith("## "):
            pdf.space(7)
            for part in wrap_lines(line[3:], 13):
                pdf.draw_line(part, size=13, font="F2", color="0.08 0.20 0.32", leading=17)
            pdf.space(2)
        elif re.match(r"^\d+\. ", line):
            for part in wrap_lines(line, 10.2, indent=18):
                pdf.draw_line(part, size=10.2, indent=18, leading=14)
        elif line.startswith("- "):
            text = line[2:]
            wrapped = wrap_lines(text, 10.2, indent=18, bullet_prefix="- ")
            for part in wrapped:
                pdf.draw_line(part, size=10.2, indent=18, leading=14)
        else:
            font = "F2" if line.endswith(":") or line in {"Source: plain.txt transcript + table of content.txt timestamps"} else "F1"
            for part in wrap_lines(line, 10.2):
                pdf.draw_line(part, size=10.2, font=font, leading=14)
    pdf.finish()


def main():
    if OUT_MD.exists():
        content = OUT_MD.read_text(encoding="utf-8")
    else:
        content = CONTENT
        OUT_MD.write_text(content, encoding="utf-8")
    render_markdown_to_pdf(content)
    print(f"Wrote {OUT_MD}")
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    main()
