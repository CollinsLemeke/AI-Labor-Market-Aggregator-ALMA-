---
title: AI Labour Market Intelligence
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.55.0
app_file: app.py
pinned: true
license: mit
---

# AI Labour Market Intelligence Dashboard

Real-time analytics of global AI job demand. Built by Collins @ AI Nexus, University of Greater Manchester.

## Features
- Role-based filtering across 14 AI job categories
- Live job listings with direct application links
- Skills frequency analysis via DistilBERT NER
- Location distribution analytics
- Dark/Light theme toggle
- Data from Adzuna, Jooble, JSearch & USAJobs APIs

## Tech Stack
- **Frontend**: Streamlit with custom CSS
- **Storage**: DuckDB + Parquet
- **NLP**: DistilBERT (skill extraction)
- **Data**: Adzuna, Jooble, RapidAPI JSearch, USAJobs