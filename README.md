---
title: AI Labour Market Aggregator (ALMA)
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.56.0
app_file: app.py
pinned: false
license: mit
short_description: Central hub for AI and tech job discovery
---

# 🤖 AI Labour Market Aggregator (ALMA)

> **One dashboard. Every AI and tech job board worth visiting. Filtered by role, ranked by relevance, visualised in real time.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56-FF4B4B)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![Deployed](https://img.shields.io/badge/🤗-HF%20Spaces-yellow)](https://huggingface.co/spaces)

---

## Table of Contents

- [Overview](#overview)
- [The Problem ALMA Solves](#the-problem-alma-solves)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Dashboard Walkthrough](#dashboard-walkthrough)
  - [Header Strip](#header-strip)
  - [Left Panel — Job Listings](#left-panel--job-listings)
  - [Centre Panel — Analytics](#centre-panel--analytics)
  - [Right Panel — Job Details](#right-panel--job-details)
- [Supported AI Roles](#supported-ai-roles)
- [Job Board Categories](#job-board-categories)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment on Hugging Face Spaces](#deployment-on-hugging-face-spaces)
- [How to Use ALMA (Practical Walkthrough)](#how-to-use-alma-practical-walkthrough)
- [Design Decisions](#design-decisions)
- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Roadmap](#roadmap)
- [Author](#author)
- [License](#license)

---

## Overview

**ALMA** (AI Labour Market Aggregator) is a single-page Streamlit dashboard that aggregates the AI and tech job market into one interactive view. Instead of opening 15 browser tabs across Indeed, LinkedIn, Reed, Welcome to the Jungle, Otta, and a dozen company career pages, you pick an AI role from a dropdown and ALMA surfaces the listings, the salary benchmarks, the most requested skills, the geographic distribution of opportunities, and direct links to every relevant job board, all on one screen.

It is built for three audiences:

1. **Job seekers** moving into or across AI roles who want a one-click launchpad to every relevant board and company career page.
2. **Students and early-career engineers** trying to understand the market before applying. What roles exist, what they pay, what skills they demand, and where the opportunities are concentrated.
3. **Recruiters, researchers, and analysts** who need a fast snapshot of AI hiring trends broken down by role, geography, and skill demand.

ALMA is intentionally minimal. No login, no tracking, no lead capture. Pick a role. See the market. Click through to apply.

---

## The Problem ALMA Solves

Looking for an AI or ML role in 2026 means:

- **15+ job boards** that all matter but none of which cover everything (Indeed, LinkedIn, Reed, Totaljobs, Otta, Welcome to the Jungle, Hiring.cafe, Wellfound, Dice, Built In, Y Combinator Jobs, AI-specific boards like AI Jobs Board and ML Jobs List, and on and on)
- **Salary opacity.** Most listings hide the range. Most aggregators don't benchmark by role and geography
- **Skills mismatch between job titles and actual job descriptions.** "Data Scientist" at one company is "ML Engineer" at another
- **Geographic fragmentation.** UK boards miss US roles, US boards miss European roles, and almost nobody indexes diversity-focused boards
- **No visibility into trends.** You don't know if "LLM Engineer" postings are up 40% this quarter or down 15%

ALMA collapses this into one view. You see the listings, the KPIs, the skill demand, the location breakdown, and the trend line. And you have a curated launchpad of 70+ job boards organised by category and geography, one click away.

---

## Key Features

| Capability | Details |
|------------|---------|
| **Role Selector** | Pick from the full catalogue of AI and ML roles (Data Scientist, ML Engineer, AI Research Engineer, NLP Engineer, Computer Vision Engineer, MLOps Engineer, Prompt Engineer, AI Product Manager, and more) |
| **Dark / Light Theme** | Professional dark mode by default with a one-click switch to a polished light theme. Both themes use carefully calibrated colour palettes for accessibility |
| **KPI Strip** | Four live KPI cards: Total Listings, Average UK Salary, Top Location, Remote Availability, each with a quarter-over-quarter delta |
| **Job Listings Panel** | 20 curated listings per role with company, role title, salary range, location, type, and work mode, all filterable by type (Full-time, Contract, Remote) and mode (Onsite, Hybrid, Remote) |
| **Most Requested Skills** | Horizontal bar chart ranking the top skills employers are asking for in the selected role |
| **Location Distribution** | Donut chart showing geographic distribution of listings by country with country count in the centre |
| **AI Demand Trends** | Multi-line time-series chart covering 9 AI fields over multiple years (Machine Learning, NLP, Computer Vision, MLOps, Generative AI, Deep Learning, and more) showing demand index evolution |
| **Job Board Directory** | 70+ curated job board and company career page links, organised into 13 categories from AI-Specific to UK Enterprise to Diversity-Focused boards |
| **Detailed Job Cards** | Full overview of each listing: salary, location, work mode, type, experience level, posted date, required skills, full description, application guidance, and direct apply/visit links |
| **Quick Search Launchpad** | One-click search of the selected role on Indeed, LinkedIn, Reed, and Totaljobs |
| **Responsive Layout** | Three-column layout sized for desktop work. Collapsible on narrower screens |
| **Pure-Python Stack** | No backend API. No database. All data served from `data.py`. Refresh monthly, deploy anywhere |

---

## Tech Stack

```
Frontend & Orchestration:  Streamlit 1.56
Visualisation:             Plotly (interactive charts)
Data Layer:                Pure Python module (data.py)
Styling:                   Custom CSS with CSS variables for theming
Fonts:                     IBM Plex Mono (numerics), Outfit (body)
Deployment:                Hugging Face Spaces (Streamlit SDK)
```

No database. No backend API. No ML models at runtime. ALMA is deliberately lightweight. The data is maintained manually as a Python module that's refreshed on a regular cadence, which keeps the app fast, reliable, and free to run.

---

## Dashboard Walkthrough

ALMA's interface is a single page divided into four regions. Here's what each one does.

---

### Header Strip

A fixed top bar with the ALMA logo, a live UTC timestamp, and a status indicator showing the feed is active. Sits above every other element and re-renders the current time on each reload.

---

### Left Panel — Job Listings

The narrow left column shows the current selected role name plus a count badge of total listings, followed by two filter dropdowns:

- **Type:** All, Full-time, Contract, Remote
- **Mode:** All Modes, Onsite, Hybrid, Remote

Below the filters is a scrollable list of 20 curated listings for the selected role. Each listing card shows:

- Company name (bold)
- Role title
- Salary range (colour-coded accent)
- Location (city, country)
- Type pill (Full-time blue, Contract amber, Remote purple)

Clicking the **Select** button on any card promotes that listing to the Right Panel for full detail.

---

### Centre Panel — Analytics

The largest panel, containing five stacked sections.

**KPI Strip (four cards)**

| KPI | What It Shows |
|-----|---------------|
| **Total Listings** | Number of listings currently aggregated for this role, plus month-over-month growth |
| **Avg. Salary (UK)** | Median UK salary benchmark for the role, with quarter-over-quarter change |
| **Top Location** | Highest-share city or country for this role, with its percentage of total listings |
| **Remote Available** | Percentage of listings offering full remote, with quarter-over-quarter change |

Each KPI card has a top-edge accent stripe in a distinct colour and uses IBM Plex Mono for the numeric value to give it that analytical-dashboard feel.

**Skills and Location Charts (side by side)**

Left: **Most Requested Skills** — horizontal bar chart ranking the top skills employers are asking for in the selected role. Skills are extracted from the listing data and ranked by frequency. Each bar is coloured from the ALMA palette and labelled with a percentage on the right.

Right: **Location Distribution** — donut chart with the country count in the centre, showing the geographic distribution of listings. Each slice is clickable and labelled with country name and percentage.

**AI Field Demand Trends (global)**

A multi-line time-series chart below the two side-by-side charts. Tracks demand index across 9 AI fields over a multi-year window:

- Machine Learning
- Natural Language Processing
- Computer Vision
- MLOps / ML Infrastructure
- Generative AI / LLMs
- Deep Learning
- AI Research
- Data Science
- AI Product Management

Each field has a distinct colour and line style (dash, dot, dashdot, etc.) so they remain readable when overlapping. The legend is placed below the chart horizontally. This is the single most useful chart in the app for anyone planning a multi-year career bet. You can see whether a field is rising, flat, or cooling.

**Explore More Tech Jobs (curated link directory)**

This is the hidden gem of ALMA. 70+ curated job board and company career page links, organised into 13 categories, each category presented as a horizontal strip of clickable chips. Categories include AI-Specific boards, UK Job Boards, UK Tech Boards, USA boards, Canada, Europe, Top AI Companies (direct career pages), UK Tech Careers, UK Enterprise & Finance, Global Companies, Startups & Scale-ups, Diversity & Inclusion boards, and Contract & Freelance platforms.

Each chip opens the relevant board or career page in a new tab. The links are dynamically filtered by the selected role where applicable — for example, selecting "ML Engineer" versus "Data Scientist" may surface a different set of company pages.

---

### Right Panel — Job Details

The narrow right column shows the full detail view for whichever listing is currently selected in the Left Panel.

Sections rendered top to bottom:

- **Header:** "Job Details" label with a counter showing "N of M" for the current listing
- **Company + Role Title:** Large company name, accent-coloured role title below
- **Overview table:** Salary, Location, Work Mode, Type, Experience level, Posted date
- **Required Skills:** Tag cloud of skills extracted from the listing
- **Description:** Full job description paragraph
- **How to Apply:** Tailored guidance for the selected role
- **Search Now button:** Primary gradient call-to-action that opens the apply URL
- **Visit Company Website link:** Secondary link to the company's main site
- **Also Search On:** Quick-launch chips for Indeed, LinkedIn, Reed, and Totaljobs, each pre-filled with the selected role as the search query

---

## Supported AI Roles

ALMA covers the full modern AI and ML role spectrum. The role list is dynamic and defined in `data.py`, but typically includes:

- Data Scientist
- Machine Learning Engineer
- AI Research Engineer / Research Scientist
- NLP Engineer
- Computer Vision Engineer
- MLOps Engineer
- Deep Learning Engineer
- Applied Scientist
- Prompt Engineer
- AI Product Manager
- Data Engineer (ML-adjacent)
- AI Ethics / Responsible AI roles

Each role has its own curated listings, salary benchmarks, skill rankings, and trend data.

---

## Job Board Categories

The "Explore More Tech Jobs" section organises 70+ external links into 13 categories:

| Category | What's Inside |
|----------|---------------|
| **🤖 AI & ML Specific** | AI-only boards (AI Jobs Board, ML Jobs List, AI-Jobs.net, etc.) |
| **🇬🇧 UK Job Boards** | Indeed UK, Reed, Totaljobs, CV-Library, Guardian Jobs |
| **💻 UK Tech Boards** | Otta, Hired.com, CWJobs, Technojobs |
| **🇺🇸 United States** | LinkedIn US, Indeed US, Built In, Dice, Wellfound |
| **🇨🇦 Canada** | Canadian-specific boards and listings |
| **🇪🇺 Germany & Europe** | Welcome to the Jungle, European tech boards |
| **🏢 Top AI Companies** | Direct career pages for OpenAI, Anthropic, DeepMind, xAI, Meta AI, etc. |
| **🇬🇧 UK Tech Careers** | Direct career pages for UK tech companies |
| **🏛️ UK Enterprise & Finance** | Banks, consulting, and large enterprise career pages |
| **🌍 Global Companies** | Google, Microsoft, Amazon, IBM, and other global tech |
| **🚀 Startups & Scale-ups** | Y Combinator Jobs, early-stage specialist boards |
| **🌈 Diversity & Inclusion** | Diversity-focused boards and inclusion-first platforms |
| **📝 Contract & Freelance** | Upwork, Toptal, contractor-focused UK boards |

Each category is rendered as a horizontal strip of colour-coded chips. Hovering a chip highlights it. Clicking opens the link in a new tab.

---

## Data Sources

The underlying job data and salary benchmarks are informed by publicly available APIs and industry reports, including:

- **Adzuna** (UK and international listings API)
- **Jooble** (aggregated listings)
- **JSearch** (RapidAPI listings)
- **USAJobs** (US federal listings)

The data layer is currently maintained as a curated Python module (`data.py`) that is refreshed on a monthly cadence to keep listings, salary benchmarks, and trend data current. This is a deliberate design choice. Live API calls would make the app slower and introduce rate-limit risk without meaningfully improving the user experience for what is primarily a discovery and navigation tool.

The long-term plan is to move to a scheduled background refresh that writes to a cached snapshot, keeping the user-facing experience fast while the data stays current.

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip or conda
- Approximately 200 MB free disk space for dependencies

### Quick Install

```bash
# Clone the repository
git clone https://github.com/[your-username]/alma.git
cd alma

# Install dependencies
pip install -r requirements.txt
```

---

## Running Locally

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

To run on a specific port:

```bash
streamlit run app.py --server.port 8080
```

To expose it over your network:

```bash
streamlit run app.py --server.address 0.0.0.0
```

---

## Deployment on Hugging Face Spaces

ALMA is deployed on Hugging Face Spaces using the Streamlit SDK. The YAML configuration at the top of this README is what Spaces reads to launch the app.

To deploy your own copy:

1. Create a new Space on Hugging Face, selecting **Streamlit** as the SDK
2. Clone the Space repository locally
3. Copy `app.py`, `data.py`, and `requirements.txt` into the repo root
4. Keep the YAML frontmatter at the top of `README.md` intact
5. Push to the Space's remote. HF will build and deploy automatically

Build time is typically 2 to 4 minutes. ALMA has a lightweight dependency footprint compared to ML-heavy apps.

---

## How to Use ALMA (Practical Walkthrough)

Here's a typical session, start to finish.

**Step 1 — Pick your role.** Open ALMA and select your target role from the dropdown at the top. The entire dashboard updates instantly.

**Step 2 — Read the KPIs.** Scan the four KPI cards. Is the listing count strong? What's the UK salary benchmark? What's the top location? How much is remote?

**Step 3 — Check the skills.** Look at the Most Requested Skills chart. If you see skills you don't have, that's your study list. If you see skills you do have, highlight them on your CV.

**Step 4 — Check the geography.** The Location Distribution donut tells you where to focus. If 40% of listings are in London, that's where the competition is, but also where the salaries are highest. If 15% are in Berlin, that's a good target if you have an EU work permit.

**Step 5 — Read the trend.** The AI Field Demand Trends chart is the long-term signal. Is your target field rising or cooling? Is there an adjacent field that's rising faster?

**Step 6 — Browse listings.** Scroll the Left Panel and click Select on anything interesting. The Right Panel gives you the full job spec, required skills, and direct apply links.

**Step 7 — Launch broad searches.** Scroll to the "Explore More Tech Jobs" section. Click through to the boards relevant to your geography and situation. Bookmark the ones that resonate.

**Step 8 — Quick search on aggregators.** From the Right Panel, use the "Also Search On" chips to search the selected role on Indeed, LinkedIn, Reed, and Totaljobs with one click each.

---

## Design Decisions

A handful of deliberate choices shape how ALMA feels to use.

| Decision | Choice | Why |
|----------|--------|-----|
| **Static data, not live API** | Curated Python module refreshed monthly | Live APIs would add latency and rate-limit risk. Discovery tools don't need real-time freshness to be useful |
| **Three-column layout** | Listings, Analytics, Details side by side | Lets you compare listings without losing the analytical context. Mimics how traders and analysts actually work |
| **Dark mode by default** | Professional dark palette with bright accents | Most users browse jobs after work. Dark mode is easier on the eyes. Light mode is one click away |
| **No login / no tracking** | Pure frontend, no user state | Job seekers hate lead-capture walls. ALMA respects that. No email required, no cookies, no retargeting |
| **70+ links curated manually** | Organised by category and geography | Quality over quantity. Every link has been checked. No dead links, no low-quality spam boards |
| **One-click search launchpad** | Pre-filled search URLs for 4 major boards | The highest-value action is "find me more of this role on Indeed." ALMA makes it a single click |
| **Salary shown in IBM Plex Mono** | Fixed-width font for all numeric values | Keeps salary ranges visually aligned and scannable. Mimics the aesthetic of financial dashboards |
| **Two custom fonts only** | IBM Plex Mono + Outfit | One for numbers, one for everything else. Keeps the visual language consistent |

---

## Repository Structure

```
.
├── README.md              # This file (with HF Spaces YAML frontmatter)
├── app.py                 # Main Streamlit dashboard
├── data.py                # Job listings, skills, locations, KPIs, trends, links
├── requirements.txt       # Python dependencies
└── LICENSE                # MIT License
```

ALMA is split into two files: `app.py` handles the UI, layout, and styling. `data.py` owns all data generation, curated links, and benchmark values. This clean split means the data refresh workflow is simple. Update `data.py`, redeploy. The app code doesn't move.

---

## Dependencies

```
streamlit>=1.56.0
plotly>=5.20.0
pandas>=2.0.0
```

Install everything with:

```bash
pip install -r requirements.txt
```

ALMA's dependency footprint is deliberately tiny. Fast installs, fast cold starts, easy to deploy anywhere.

---

## Roadmap

Features that may land in future versions:

- **Live API integration** — Adzuna, Jooble, JSearch, and USAJobs with cached snapshots
- **Salary percentile view** — 25th, 50th, 75th, 90th by role and geography
- **Remote-only mode** — Hide everything that isn't full remote
- **Saved searches** — Bookmark role + filter combinations for one-click recall
- **Email digest** — Optional weekly email of new listings matching saved searches
- **Skills gap analyser** — Upload your CV and see which skills you're missing for your target role
- **Company insights** — Glassdoor rating, Crunchbase funding, and Wellfound team size inline on each listing
- **Resume keyword matcher** — Auto-highlight which listings match your resume keywords
- **Interview preparation links** — Per-role interview prep resources
- **Export to CSV** — Download the current filtered listing set

---

## Author

**Collins Lemeke**

ALMA was built to solve a problem I kept hitting myself — fragmented AI job search across 15+ boards with no unified view of salaries, skills, and trends. Instead of opening tabs endlessly, I wanted one screen that showed me the market.

For questions, feedback, or feature requests, open a GitHub issue or reach out via Hugging Face.

---

## License

MIT License. Free to use, modify, and distribute. See [LICENSE](LICENSE) for full terms.

---

> *Built with Streamlit and Plotly. Designed for AI job seekers, students, and recruiters who want the full picture of the market on one screen.*
