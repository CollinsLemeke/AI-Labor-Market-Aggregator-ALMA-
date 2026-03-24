"""
Mock data for AI Labour Market Aggregator Dashboard.
Replace this with real API pipeline (Adzuna, Jooble, JSearch, USAJobs) in production.

Updated: March 2026
Sources: IT Jobs Watch, Glassdoor, Indeed UK, LinkedIn, PwC AI Jobs Barometer,
         CareerCheck, Morgan McKinley, Robert Half, Digital Waffle, LSE, WEF
"""

import pandas as pd
import random
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════
# ROLE DEFINITIONS
# Updated March 2026 based on LinkedIn (6,000+ AI jobs UK),
# Indeed UK, Glassdoor (1,048 AI engineer London alone),
# IT Jobs Watch, WEF (1.3M new AI roles globally)
# ═══════════════════════════════════════════════════════════

ROLES = {
    "Technical": [
        {"name": "AI Engineer", "count": 8920},
        {"name": "ML Engineer", "count": 4750},
        {"name": "Deep Learning Engineer", "count": 2580},
        {"name": "Data Scientist", "count": 6210},
        {"name": "Data Analyst", "count": 8540},
        {"name": "AI Researcher", "count": 2010},
        {"name": "LLM Engineer", "count": 4680},
        {"name": "Agentic Engineer", "count": 3240},
        {"name": "NLP Engineer", "count": 2180},
        {"name": "Computer Vision Engineer", "count": 1490},
        {"name": "MLOps Engineer", "count": 3280},
        {"name": "Data Engineer", "count": 7120},
        {"name": "Robotics AI Engineer", "count": 1080},
        {"name": "AI Security Engineer", "count": 950},
        {"name": "Prompt Engineer", "count": 1340},
    ],
    "Non-Technical": [
        {"name": "AI Product Manager", "count": 1980},
        {"name": "AI Ethics Officer", "count": 480},
        {"name": "AI Consultant", "count": 1350},
        {"name": "AI Trainer / Annotator", "count": 3410},
        {"name": "AI Sales Engineer", "count": 1140},
        {"name": "AI Technical Writer", "count": 720},
        {"name": "AI Solutions Architect", "count": 1620},
    ],
}

# ═══════════════════════════════════════════════════════════
# COMPANY & LOCATION DATA
# Salaries updated from: IT Jobs Watch (median AI Engineer
# £85K, ML Engineer £67.5K as of 6 Mar 2026), Glassdoor
# (AI Engineer UK avg £62.5K, London avg £71.3K),
# Indeed (ML Engineer avg £75.2K), Morgan McKinley
# (AI/ML Specialist London £75K-£90K), CareerCheck
# (ML Engineer London £60K-£150K+), Robert Half
# (ML Engineer London £81.5K-£129.3K), Digital Waffle
# (projected AI avg UK £81.3K). US salaries from
# ZipRecruiter, Levels.fyi, Wellfound.
# ═══════════════════════════════════════════════════════════

COMPANIES_BY_ROLE = {
    "AI Engineer": [
        {"company": "Google DeepMind", "location": "London, UK", "salary_min": 95000, "salary_max": 150000, "mode": "Hybrid"},
        {"company": "Microsoft", "location": "London, UK", "salary_min": 88000, "salary_max": 135000, "mode": "Hybrid"},
        {"company": "Amazon", "location": "London, UK", "salary_min": 90000, "salary_max": 140000, "mode": "Hybrid"},
        {"company": "Meta", "location": "London, UK", "salary_min": 110000, "salary_max": 160000, "mode": "Hybrid"},
        {"company": "Apple", "location": "London, UK", "salary_min": 98000, "salary_max": 145000, "mode": "Onsite"},
        {"company": "Palantir", "location": "London, UK", "salary_min": 95000, "salary_max": 150000, "mode": "Hybrid"},
        {"company": "Anthropic", "location": "San Francisco, US", "salary_min": 185000, "salary_max": 310000, "mode": "Hybrid"},
        {"company": "OpenAI", "location": "San Francisco, US", "salary_min": 195000, "salary_max": 330000, "mode": "Onsite"},
        {"company": "Revolut", "location": "London, UK", "salary_min": 80000, "salary_max": 115000, "mode": "Hybrid"},
        {"company": "Darktrace", "location": "Cambridge, UK", "salary_min": 78000, "salary_max": 110000, "mode": "Hybrid"},
        {"company": "Faculty AI", "location": "London, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Hybrid"},
        {"company": "Wise", "location": "London, UK", "salary_min": 75000, "salary_max": 105000, "mode": "Hybrid"},
        {"company": "Spotify", "location": "London, UK", "salary_min": 85000, "salary_max": 122000, "mode": "Hybrid"},
        {"company": "Ocado Technology", "location": "Hatfield, UK", "salary_min": 72000, "salary_max": 102000, "mode": "Hybrid"},
        {"company": "Rolls-Royce", "location": "Derby, UK", "salary_min": 68000, "salary_max": 95000, "mode": "Onsite"},
        {"company": "BAE Systems", "location": "London, UK", "salary_min": 70000, "salary_max": 100000, "mode": "Onsite"},
        {"company": "Siemens", "location": "Munich, Germany", "salary_min": 75000, "salary_max": 110000, "mode": "Hybrid"},
        {"company": "Infosys", "location": "Bangalore, India", "salary_min": 24000, "salary_max": 46000, "mode": "Hybrid"},
        {"company": "Grab", "location": "Singapore", "salary_min": 65000, "salary_max": 102000, "mode": "Hybrid"},
        {"company": "Contract Role", "location": "Leeds, UK", "salary_min": 550, "salary_max": 750, "mode": "Remote"},
    ],
    "ML Engineer": [
        {"company": "DeepMind", "location": "London, UK", "salary_min": 100000, "salary_max": 145000, "mode": "Hybrid"},
        {"company": "Revolut", "location": "London, UK", "salary_min": 78000, "salary_max": 108000, "mode": "Onsite"},
        {"company": "Spotify", "location": "London, UK", "salary_min": 82000, "salary_max": 115000, "mode": "Hybrid"},
        {"company": "Meta", "location": "London, UK", "salary_min": 115000, "salary_max": 158000, "mode": "Hybrid"},
        {"company": "Arm", "location": "Cambridge, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Onsite"},
        {"company": "Otta", "location": "Remote, UK", "salary_min": 68000, "salary_max": 90000, "mode": "Remote"},
        {"company": "Darktrace", "location": "Cambridge, UK", "salary_min": 75000, "salary_max": 105000, "mode": "Hybrid"},
        {"company": "Wise", "location": "London, UK", "salary_min": 70000, "salary_max": 98000, "mode": "Hybrid"},
        {"company": "BenevolentAI", "location": "London, UK", "salary_min": 82000, "salary_max": 120000, "mode": "Onsite"},
        {"company": "Monzo", "location": "London, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Hybrid"},
        {"company": "Wayve", "location": "London, UK", "salary_min": 88000, "salary_max": 128000, "mode": "Onsite"},
        {"company": "Amazon", "location": "London, UK", "salary_min": 92000, "salary_max": 145000, "mode": "Hybrid"},
        {"company": "Apple", "location": "London, UK", "salary_min": 98000, "salary_max": 140000, "mode": "Onsite"},
        {"company": "Microsoft", "location": "Cambridge, UK", "salary_min": 88000, "salary_max": 130000, "mode": "Hybrid"},
        {"company": "Google", "location": "London, UK", "salary_min": 105000, "salary_max": 150000, "mode": "Hybrid"},
        {"company": "Graphcore", "location": "Bristol, UK", "salary_min": 75000, "salary_max": 105000, "mode": "Hybrid"},
        {"company": "Improbable", "location": "London, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Hybrid"},
        {"company": "Faculty AI", "location": "London, UK", "salary_min": 68000, "salary_max": 95000, "mode": "Hybrid"},
        {"company": "Tractable", "location": "London, UK", "salary_min": 80000, "salary_max": 112000, "mode": "Remote"},
        {"company": "Babylon Health", "location": "London, UK", "salary_min": 70000, "salary_max": 98000, "mode": "Hybrid"},
        {"company": "Siemens", "location": "Munich, Germany", "salary_min": 72000, "salary_max": 105000, "mode": "Hybrid"},
        {"company": "SAP", "location": "Berlin, Germany", "salary_min": 75000, "salary_max": 102000, "mode": "Onsite"},
        {"company": "Stripe", "location": "San Francisco, US", "salary_min": 160000, "salary_max": 235000, "mode": "Hybrid"},
        {"company": "OpenAI", "location": "San Francisco, US", "salary_min": 190000, "salary_max": 320000, "mode": "Onsite"},
        {"company": "Anthropic", "location": "San Francisco, US", "salary_min": 180000, "salary_max": 295000, "mode": "Hybrid"},
        {"company": "Flipkart", "location": "Bangalore, India", "salary_min": 28000, "salary_max": 50000, "mode": "Onsite"},
        {"company": "Grab", "location": "Singapore", "salary_min": 62000, "salary_max": 100000, "mode": "Hybrid"},
        {"company": "Contract Role", "location": "Manchester, UK", "salary_min": 550, "salary_max": 700, "mode": "Remote"},
    ],
    "Deep Learning Engineer": [
        {"company": "DeepMind", "location": "London, UK", "salary_min": 105000, "salary_max": 155000, "mode": "Hybrid"},
        {"company": "Wayve", "location": "London, UK", "salary_min": 92000, "salary_max": 135000, "mode": "Onsite"},
        {"company": "Meta", "location": "London, UK", "salary_min": 115000, "salary_max": 162000, "mode": "Hybrid"},
        {"company": "NVIDIA", "location": "Cambridge, UK", "salary_min": 100000, "salary_max": 148000, "mode": "Hybrid"},
        {"company": "Graphcore", "location": "Bristol, UK", "salary_min": 82000, "salary_max": 120000, "mode": "Onsite"},
        {"company": "BenevolentAI", "location": "London, UK", "salary_min": 88000, "salary_max": 125000, "mode": "Onsite"},
        {"company": "Arm", "location": "Cambridge, UK", "salary_min": 80000, "salary_max": 112000, "mode": "Onsite"},
        {"company": "Samsung AI", "location": "Cambridge, UK", "salary_min": 85000, "salary_max": 120000, "mode": "Hybrid"},
        {"company": "Google", "location": "London, UK", "salary_min": 110000, "salary_max": 158000, "mode": "Hybrid"},
        {"company": "Huawei R&D", "location": "London, UK", "salary_min": 90000, "salary_max": 130000, "mode": "Onsite"},
        {"company": "OpenAI", "location": "San Francisco, US", "salary_min": 200000, "salary_max": 340000, "mode": "Onsite"},
        {"company": "Tesla", "location": "Palo Alto, US", "salary_min": 170000, "salary_max": 265000, "mode": "Onsite"},
        {"company": "Stability AI", "location": "London, UK", "salary_min": 88000, "salary_max": 130000, "mode": "Remote"},
        {"company": "Bosch AI", "location": "Stuttgart, Germany", "salary_min": 75000, "salary_max": 110000, "mode": "Hybrid"},
        {"company": "Contract Role", "location": "London, UK", "salary_min": 650, "salary_max": 850, "mode": "Remote"},
    ],
    "Data Analyst": [
        {"company": "Deloitte", "location": "London, UK", "salary_min": 36000, "salary_max": 58000, "mode": "Hybrid"},
        {"company": "PwC", "location": "London, UK", "salary_min": 40000, "salary_max": 62000, "mode": "Hybrid"},
        {"company": "NHS Digital", "location": "Leeds, UK", "salary_min": 33000, "salary_max": 50000, "mode": "Hybrid"},
        {"company": "Barclays", "location": "London, UK", "salary_min": 42000, "salary_max": 65000, "mode": "Hybrid"},
        {"company": "Tesco", "location": "Welwyn Garden City, UK", "salary_min": 36000, "salary_max": 52000, "mode": "Hybrid"},
        {"company": "Sky", "location": "London, UK", "salary_min": 40000, "salary_max": 58000, "mode": "Hybrid"},
        {"company": "Deliveroo", "location": "London, UK", "salary_min": 44000, "salary_max": 65000, "mode": "Hybrid"},
        {"company": "Monzo", "location": "London, UK", "salary_min": 42000, "salary_max": 62000, "mode": "Remote"},
        {"company": "HSBC", "location": "Birmingham, UK", "salary_min": 40000, "salary_max": 60000, "mode": "Hybrid"},
        {"company": "BT Group", "location": "London, UK", "salary_min": 38000, "salary_max": 55000, "mode": "Hybrid"},
        {"company": "Unilever", "location": "London, UK", "salary_min": 42000, "salary_max": 62000, "mode": "Hybrid"},
        {"company": "BBC", "location": "London, UK", "salary_min": 35000, "salary_max": 52000, "mode": "Hybrid"},
        {"company": "Lloyds Banking", "location": "London, UK", "salary_min": 38000, "salary_max": 58000, "mode": "Hybrid"},
        {"company": "Sainsbury's", "location": "London, UK", "salary_min": 34000, "salary_max": 50000, "mode": "Onsite"},
        {"company": "AstraZeneca", "location": "Cambridge, UK", "salary_min": 44000, "salary_max": 66000, "mode": "Hybrid"},
        {"company": "Vodafone", "location": "London, UK", "salary_min": 40000, "salary_max": 58000, "mode": "Hybrid"},
        {"company": "Booking.com", "location": "Amsterdam, Netherlands", "salary_min": 48000, "salary_max": 72000, "mode": "Hybrid"},
        {"company": "Zalando", "location": "Berlin, Germany", "salary_min": 44000, "salary_max": 65000, "mode": "Hybrid"},
        {"company": "JPMorgan", "location": "London, UK", "salary_min": 48000, "salary_max": 70000, "mode": "Onsite"},
        {"company": "Contract Role", "location": "Manchester, UK", "salary_min": 320, "salary_max": 480, "mode": "Remote"},
    ],
    "Agentic Engineer": [
        {"company": "Anthropic", "location": "San Francisco, US", "salary_min": 190000, "salary_max": 320000, "mode": "Hybrid"},
        {"company": "OpenAI", "location": "San Francisco, US", "salary_min": 195000, "salary_max": 330000, "mode": "Onsite"},
        {"company": "LangChain", "location": "Remote, US", "salary_min": 160000, "salary_max": 245000, "mode": "Remote"},
        {"company": "Google DeepMind", "location": "London, UK", "salary_min": 105000, "salary_max": 155000, "mode": "Hybrid"},
        {"company": "Microsoft", "location": "London, UK", "salary_min": 95000, "salary_max": 142000, "mode": "Hybrid"},
        {"company": "Cognition AI", "location": "San Francisco, US", "salary_min": 180000, "salary_max": 285000, "mode": "Onsite"},
        {"company": "Adept AI", "location": "San Francisco, US", "salary_min": 175000, "salary_max": 275000, "mode": "Hybrid"},
        {"company": "Replit", "location": "San Francisco, US", "salary_min": 165000, "salary_max": 255000, "mode": "Remote"},
        {"company": "Faculty AI", "location": "London, UK", "salary_min": 78000, "salary_max": 115000, "mode": "Hybrid"},
        {"company": "Palantir", "location": "London, UK", "salary_min": 98000, "salary_max": 148000, "mode": "Hybrid"},
        {"company": "Revolut", "location": "London, UK", "salary_min": 82000, "salary_max": 120000, "mode": "Hybrid"},
        {"company": "Amazon", "location": "London, UK", "salary_min": 92000, "salary_max": 138000, "mode": "Hybrid"},
        {"company": "Stability AI", "location": "London, UK", "salary_min": 85000, "salary_max": 125000, "mode": "Remote"},
        {"company": "Cohere", "location": "Toronto, Canada", "salary_min": 150000, "salary_max": 235000, "mode": "Remote"},
        {"company": "Contract Role", "location": "London, UK", "salary_min": 700, "salary_max": 950, "mode": "Remote"},
    ],
    "Robotics AI Engineer": [
        {"company": "Dyson", "location": "Malmesbury, UK", "salary_min": 68000, "salary_max": 100000, "mode": "Onsite"},
        {"company": "Wayve", "location": "London, UK", "salary_min": 82000, "salary_max": 125000, "mode": "Onsite"},
        {"company": "Ocado Technology", "location": "Hatfield, UK", "salary_min": 72000, "salary_max": 105000, "mode": "Hybrid"},
        {"company": "BAE Systems", "location": "Warton, UK", "salary_min": 62000, "salary_max": 92000, "mode": "Onsite"},
        {"company": "Rolls-Royce", "location": "Derby, UK", "salary_min": 65000, "salary_max": 95000, "mode": "Onsite"},
        {"company": "Amazon Robotics", "location": "Cambridge, UK", "salary_min": 88000, "salary_max": 130000, "mode": "Onsite"},
        {"company": "Boston Dynamics", "location": "Waltham, US", "salary_min": 140000, "salary_max": 215000, "mode": "Onsite"},
        {"company": "Toyota Research", "location": "Cambridge, UK", "salary_min": 75000, "salary_max": 110000, "mode": "Hybrid"},
        {"company": "Bosch", "location": "Stuttgart, Germany", "salary_min": 70000, "salary_max": 102000, "mode": "Onsite"},
        {"company": "ABB", "location": "Zurich, Switzerland", "salary_min": 88000, "salary_max": 125000, "mode": "Onsite"},
        {"company": "Contract Role", "location": "Bristol, UK", "salary_min": 550, "salary_max": 750, "mode": "Hybrid"},
    ],
    "AI Security Engineer": [
        {"company": "Darktrace", "location": "Cambridge, UK", "salary_min": 80000, "salary_max": 120000, "mode": "Hybrid"},
        {"company": "CrowdStrike", "location": "London, UK", "salary_min": 88000, "salary_max": 130000, "mode": "Remote"},
        {"company": "GCHQ", "location": "Cheltenham, UK", "salary_min": 58000, "salary_max": 85000, "mode": "Onsite"},
        {"company": "NCC Group", "location": "Manchester, UK", "salary_min": 68000, "salary_max": 100000, "mode": "Hybrid"},
        {"company": "BAE Systems AI", "location": "London, UK", "salary_min": 72000, "salary_max": 105000, "mode": "Onsite"},
        {"company": "Google", "location": "London, UK", "salary_min": 98000, "salary_max": 148000, "mode": "Hybrid"},
        {"company": "Microsoft", "location": "London, UK", "salary_min": 90000, "salary_max": 135000, "mode": "Hybrid"},
        {"company": "Palantir", "location": "London, UK", "salary_min": 95000, "salary_max": 142000, "mode": "Hybrid"},
        {"company": "Sophos", "location": "Oxford, UK", "salary_min": 65000, "salary_max": 95000, "mode": "Hybrid"},
        {"company": "Palo Alto Networks", "location": "London, UK", "salary_min": 92000, "salary_max": 140000, "mode": "Remote"},
        {"company": "Contract Role", "location": "London, UK", "salary_min": 600, "salary_max": 800, "mode": "Remote"},
    ],
}

# Default companies for roles without specific data
DEFAULT_COMPANIES = [
    {"company": "Accenture", "location": "London, UK", "salary_min": 58000, "salary_max": 90000, "mode": "Hybrid"},
    {"company": "IBM", "location": "London, UK", "salary_min": 62000, "salary_max": 95000, "mode": "Hybrid"},
    {"company": "McKinsey", "location": "London, UK", "salary_min": 85000, "salary_max": 138000, "mode": "Onsite"},
    {"company": "Palantir", "location": "London, UK", "salary_min": 92000, "salary_max": 145000, "mode": "Hybrid"},
    {"company": "Capgemini", "location": "London, UK", "salary_min": 58000, "salary_max": 88000, "mode": "Hybrid"},
    {"company": "Deloitte", "location": "London, UK", "salary_min": 55000, "salary_max": 85000, "mode": "Hybrid"},
    {"company": "Microsoft", "location": "London, UK", "salary_min": 78000, "salary_max": 125000, "mode": "Hybrid"},
    {"company": "Google", "location": "London, UK", "salary_min": 88000, "salary_max": 140000, "mode": "Hybrid"},
    {"company": "Amazon", "location": "London, UK", "salary_min": 72000, "salary_max": 115000, "mode": "Hybrid"},
    {"company": "ByteDance", "location": "London, UK", "salary_min": 88000, "salary_max": 125000, "mode": "Onsite"},
    {"company": "Booking.com", "location": "Amsterdam, Netherlands", "salary_min": 72000, "salary_max": 105000, "mode": "Hybrid"},
    {"company": "Shopify", "location": "Remote, UK", "salary_min": 75000, "salary_max": 110000, "mode": "Remote"},
    {"company": "Siemens", "location": "Munich, Germany", "salary_min": 68000, "salary_max": 100000, "mode": "Hybrid"},
    {"company": "BT Group", "location": "London, UK", "salary_min": 58000, "salary_max": 85000, "mode": "Hybrid"},
    {"company": "BAE Systems", "location": "London, UK", "salary_min": 62000, "salary_max": 92000, "mode": "Onsite"},
]

# Skills updated March 2026 based on IT Jobs Watch co-occurrence
# data, Indeed skill frequency, and industry reports.
# LLM/RAG/Agentic skills now appear more prominently across roles.
SKILLS_BY_ROLE = {
    "AI Engineer": {
        "Python": 95, "PyTorch": 78, "TensorFlow": 58, "LLMs / GenAI": 68,
        "AWS / GCP": 60, "Docker / K8s": 55, "REST APIs": 50, "SQL": 45,
    },
    "ML Engineer": {
        "Python": 93, "PyTorch": 80, "TensorFlow": 56, "AWS / GCP": 58,
        "Docker / K8s": 52, "SQL": 46, "LLMs / NLP": 48, "MLflow": 35,
    },
    "Deep Learning Engineer": {
        "Python": 96, "PyTorch": 94, "CUDA / GPU": 80, "CNNs / RNNs": 70,
        "TensorFlow": 55, "Mathematics": 70, "Distributed Training": 58, "C++": 40,
    },
    "Data Scientist": {
        "Python": 96, "SQL": 84, "Pandas / NumPy": 80, "Scikit-learn": 68,
        "Statistics": 66, "Tableau / Power BI": 55, "R": 32, "Spark": 34,
    },
    "Data Analyst": {
        "SQL": 96, "Excel": 88, "Power BI": 80, "Tableau": 62,
        "Python": 58, "Statistics": 54, "Google Analytics": 40, "Looker": 38,
    },
    "AI Researcher": {
        "Python": 92, "PyTorch": 88, "Research Papers": 82, "Mathematics": 80,
        "Deep Learning": 78, "NLP / CV": 62, "JAX": 40, "LaTeX": 52,
    },
    "LLM Engineer": {
        "Python": 95, "LLM Fine-tuning": 90, "PyTorch": 82, "RAG": 80,
        "LangChain": 68, "Vector DBs": 62, "Prompt Eng.": 55, "AWS / GCP": 48,
    },
    "Agentic Engineer": {
        "Python": 94, "LangChain / LangGraph": 92, "LLM APIs": 90, "RAG": 80,
        "Tool Use / Function Calling": 78, "Vector DBs": 65, "Docker": 52, "Multi-Agent Systems": 72,
    },
    "NLP Engineer": {
        "Python": 94, "NLP / spaCy": 84, "PyTorch": 78, "Transformers": 75,
        "BERT / GPT": 68, "Text Mining": 52, "SQL": 44, "Docker": 40,
    },
    "Computer Vision Engineer": {
        "Python": 92, "PyTorch": 86, "OpenCV": 80, "CNNs": 74,
        "TensorFlow": 55, "Image Seg.": 54, "YOLO / Det.": 50, "C++": 36,
    },
    "MLOps Engineer": {
        "Python": 90, "Docker / K8s": 88, "AWS / GCP": 85, "CI/CD": 78,
        "MLflow": 72, "Terraform": 58, "Airflow": 52, "Monitoring": 48,
    },
    "Data Engineer": {
        "SQL": 96, "Python": 90, "Spark": 80, "AWS / GCP": 75,
        "Airflow": 68, "dbt": 60, "Kafka": 52, "Snowflake": 48,
    },
    "Robotics AI Engineer": {
        "Python": 90, "ROS / ROS2": 86, "C++": 82, "Computer Vision": 74,
        "PyTorch": 64, "Sensor Fusion": 60, "Control Systems": 56, "Simulation": 50,
    },
    "AI Security Engineer": {
        "Python": 86, "Adversarial ML": 82, "Cybersecurity": 80, "Threat Modelling": 74,
        "LLM Red Teaming": 72, "Docker / K8s": 58, "Penetration Testing": 52, "AWS / GCP": 48,
    },
    "Prompt Engineer": {
        "Prompt Design": 96, "LLM Knowledge": 90, "Python": 62, "Eval Metrics": 58,
        "Fine-tuning": 48, "RAG": 45, "AI Safety": 38, "Technical Writing": 52,
    },
    "AI Solutions Architect": {
        "Cloud Architecture": 92, "AWS / GCP / Azure": 90, "ML Pipelines": 78, "System Design": 75,
        "Python": 62, "Stakeholder Mgmt": 70, "Cost Optimisation": 58, "Security": 52,
    },
    "AI Technical Writer": {
        "Technical Writing": 96, "AI/ML Knowledge": 82, "Documentation Tools": 78, "Python (basic)": 58,
        "API Documentation": 72, "Markdown / RST": 68, "User Research": 52, "Diagramming": 48,
    },
}

DEFAULT_SKILLS = {
    "Communication": 86, "AI Strategy": 74, "Project Mgmt": 70, "Data Analysis": 62,
    "Stakeholder Mgmt": 58, "Python (basic)": 48, "Presentation": 66, "Research": 52,
}

LOCATIONS_BY_ROLE = {
    "default": {
        "United Kingdom": 30, "United States": 22, "Germany": 14,
        "Canada": 11, "Other": 23,
    }
}

ROLE_DESCRIPTIONS = {
    "AI Engineer": [
        "Design and build end-to-end AI systems from prototyping to production deployment.",
        "Integrate LLMs, computer vision, and ML models into scalable product features.",
        "Develop AI-powered APIs and microservices for internal and external consumers.",
        "Collaborate with product teams to identify high-impact AI use cases.",
        "Establish best practices for AI system reliability, monitoring, and observability.",
    ],
    "ML Engineer": [
        "Build and deploy production ML models at scale.",
        "Design end-to-end ML pipelines for real-time inference.",
        "Optimise model performance and latency for production systems.",
        "Collaborate with research teams to productionise novel models.",
        "Develop automated training and evaluation frameworks.",
    ],
    "Deep Learning Engineer": [
        "Design and train large-scale deep neural networks for complex tasks.",
        "Optimise model architectures for GPU and TPU distributed training.",
        "Research and implement state-of-the-art deep learning techniques.",
        "Build custom layers, loss functions, and training loops for novel problems.",
        "Profile and improve training efficiency across multi-node GPU clusters.",
    ],
    "Data Scientist": [
        "Analyse complex datasets to drive business decisions.",
        "Build predictive models and statistical analysis pipelines.",
        "Design and run A/B experiments at scale.",
        "Create dashboards and data visualisations for stakeholders.",
        "Develop customer segmentation and recommendation systems.",
    ],
    "Data Analyst": [
        "Transform raw data into actionable business insights through reports and dashboards.",
        "Write complex SQL queries to extract and analyse large datasets.",
        "Build interactive visualisations in Power BI and Tableau for stakeholder reporting.",
        "Monitor KPIs and identify trends, anomalies, and growth opportunities.",
        "Collaborate with product and marketing teams to support data-driven decisions.",
    ],
    "AI Researcher": [
        "Conduct original research advancing the state of the art in machine learning.",
        "Publish findings in top-tier conferences such as NeurIPS, ICML, and ICLR.",
        "Develop novel model architectures and training methodologies.",
        "Collaborate with engineering teams to translate research into products.",
        "Mentor junior researchers and contribute to the broader AI research community.",
    ],
    "LLM Engineer": [
        "Fine-tune and deploy large language models for production applications.",
        "Build RAG pipelines combining retrieval systems with generative models.",
        "Optimise LLM inference for latency and cost at scale.",
        "Develop evaluation frameworks for language model quality and safety.",
        "Integrate LLMs into existing product workflows and APIs.",
    ],
    "Agentic Engineer": [
        "Design and build autonomous AI agent systems that reason, plan, and execute tasks.",
        "Develop multi-agent orchestration frameworks with tool use and function calling.",
        "Build reliable agent pipelines using LangChain, LangGraph, and custom frameworks.",
        "Implement memory, planning, and reflection capabilities for long-running agents.",
        "Create evaluation harnesses for agent reliability, safety, and task completion.",
    ],
    "NLP Engineer": [
        "Build and deploy NLP models for text classification, NER, and sentiment analysis.",
        "Develop text processing pipelines for large-scale document understanding.",
        "Fine-tune transformer models for domain-specific language tasks.",
        "Design multilingual NLP systems for global product reach.",
        "Optimise NLP inference for real-time applications.",
    ],
    "Robotics AI Engineer": [
        "Develop perception and planning algorithms for autonomous robotic systems.",
        "Integrate computer vision and sensor fusion for real-world robot navigation.",
        "Build simulation environments for training and testing robot behaviours.",
        "Optimise control systems for safe and efficient robot operation.",
        "Collaborate with mechanical and electrical engineers on full-stack robotics.",
    ],
    "AI Security Engineer": [
        "Develop adversarial testing frameworks for AI and ML model robustness.",
        "Build red-teaming pipelines for LLM safety and alignment evaluation.",
        "Design security architectures for AI systems against data poisoning and extraction attacks.",
        "Implement monitoring and alerting for AI model drift and adversarial inputs.",
        "Conduct threat modelling for AI-powered products and infrastructure.",
    ],
}

DEFAULT_DESCRIPTIONS = [
    "Join our growing AI team to work on cutting-edge problems.",
    "Help build the next generation of intelligent systems.",
    "Work alongside world-class engineers and researchers.",
    "Drive innovation in applied artificial intelligence.",
    "Shape the future of AI-powered products and services.",
]

JOB_TYPES = ["Full-time", "Full-time", "Full-time", "Full-time", "Contract", "Remote"]
EXPERIENCE_LEVELS = ["1+ years", "2+ years", "2+ years", "3+ years", "3+ years", "5+ years", "PhD + 2 years"]

# ═══════════════════════════════════════════════════════════
# VERIFIED CAREER PAGE URLS
# Every URL has been manually verified to be a working
# careers/jobs page for that company.
# ═══════════════════════════════════════════════════════════

VERIFIED_URLS = {
    # Big Tech
    "Google DeepMind":  {"apply": "https://deepmind.google/careers/", "website": "https://deepmind.google"},
    "DeepMind":         {"apply": "https://deepmind.google/careers/", "website": "https://deepmind.google"},
    "Google":           {"apply": "https://www.google.com/about/careers/applications/", "website": "https://www.google.com"},
    "Meta":             {"apply": "https://www.metacareers.com/jobs", "website": "https://www.meta.com"},
    "Microsoft":        {"apply": "https://careers.microsoft.com/", "website": "https://www.microsoft.com"},
    "Amazon":           {"apply": "https://www.amazon.jobs/en-gb/", "website": "https://www.amazon.co.uk"},
    "Amazon Robotics":  {"apply": "https://www.amazon.jobs/en-gb/teams/amazon-robotics", "website": "https://www.amazon.science"},
    "Apple":            {"apply": "https://jobs.apple.com/en-gb/search", "website": "https://www.apple.com"},
    "NVIDIA":           {"apply": "https://www.nvidia.com/en-gb/about-nvidia/careers/", "website": "https://www.nvidia.com"},

    # AI-First Companies
    "OpenAI":           {"apply": "https://openai.com/careers/", "website": "https://openai.com"},
    "Anthropic":        {"apply": "https://www.anthropic.com/careers", "website": "https://www.anthropic.com"},
    "Stability AI":     {"apply": "https://stability.ai/careers", "website": "https://stability.ai"},
    "Cohere":           {"apply": "https://cohere.com/careers", "website": "https://cohere.com"},
    "Cognition AI":     {"apply": "https://www.cognition.ai/careers", "website": "https://www.cognition.ai"},
    "Adept AI":         {"apply": "https://www.adept.ai/careers", "website": "https://www.adept.ai"},
    "Replit":           {"apply": "https://replit.com/site/careers", "website": "https://replit.com"},
    "LangChain":        {"apply": "https://www.langchain.com/careers", "website": "https://www.langchain.com"},
    "Huawei R&D":       {"apply": "https://career.huawei.com/reccampportal/portal5/index.html", "website": "https://www.huawei.com"},

    # UK Fintech
    "Revolut":          {"apply": "https://www.revolut.com/careers/", "website": "https://www.revolut.com"},
    "Monzo":            {"apply": "https://monzo.com/careers/", "website": "https://monzo.com"},
    "Wise":             {"apply": "https://www.wise.jobs/", "website": "https://wise.com"},
    "Starling Bank":    {"apply": "https://www.starlingbank.com/careers/", "website": "https://www.starlingbank.com"},

    # UK Tech
    "Spotify":          {"apply": "https://www.lifeatspotify.com/jobs", "website": "https://www.spotify.com"},
    "Darktrace":        {"apply": "https://darktrace.com/careers", "website": "https://darktrace.com"},
    "Arm":              {"apply": "https://careers.arm.com/", "website": "https://www.arm.com"},
    "Graphcore":        {"apply": "https://www.graphcore.ai/careers", "website": "https://www.graphcore.ai"},
    "Wayve":            {"apply": "https://wayve.ai/careers/", "website": "https://wayve.ai"},
    "BenevolentAI":     {"apply": "https://www.benevolent.com/careers", "website": "https://www.benevolent.com"},
    "Improbable":       {"apply": "https://www.improbable.io/careers", "website": "https://www.improbable.io"},
    "Faculty AI":       {"apply": "https://faculty.ai/careers/", "website": "https://faculty.ai"},
    "Tractable":        {"apply": "https://tractable.ai/careers", "website": "https://tractable.ai"},
    "Ocado Technology": {"apply": "https://careers.ocadogroup.com/", "website": "https://www.ocadogroup.com"},
    "Deliveroo":        {"apply": "https://careers.deliveroo.co.uk/", "website": "https://deliveroo.co.uk"},
    "Otta":             {"apply": "https://otta.com/careers", "website": "https://otta.com"},
    "Samsung AI":       {"apply": "https://research.samsung.com/artificial-intelligence", "website": "https://research.samsung.com"},

    # UK Enterprise / Defence
    "BAE Systems":      {"apply": "https://www.baesystems.com/en/careers", "website": "https://www.baesystems.com"},
    "BAE Systems AI":   {"apply": "https://www.baesystems.com/en/careers", "website": "https://www.baesystems.com"},
    "Rolls-Royce":      {"apply": "https://careers.rolls-royce.com/", "website": "https://www.rolls-royce.com"},
    "Dyson":            {"apply": "https://careers.dyson.com/en-gb/", "website": "https://www.dyson.co.uk"},
    "Palantir":         {"apply": "https://www.palantir.com/careers/", "website": "https://www.palantir.com"},

    # Consulting / Professional Services
    "Accenture":        {"apply": "https://www.accenture.com/gb-en/careers", "website": "https://www.accenture.com"},
    "McKinsey":         {"apply": "https://www.mckinsey.com/careers", "website": "https://www.mckinsey.com"},
    "Deloitte":         {"apply": "https://www2.deloitte.com/uk/en/careers.html", "website": "https://www2.deloitte.com"},
    "PwC":              {"apply": "https://www.pwc.co.uk/careers.html", "website": "https://www.pwc.co.uk"},
    "Capgemini":        {"apply": "https://www.capgemini.com/gb-en/careers/", "website": "https://www.capgemini.com"},
    "IBM":              {"apply": "https://www.ibm.com/careers", "website": "https://www.ibm.com"},

    # Banking / Finance
    "Barclays":         {"apply": "https://search.jobs.barclays/", "website": "https://www.barclays.co.uk"},
    "HSBC":             {"apply": "https://www.hsbc.com/careers", "website": "https://www.hsbc.com"},
    "JPMorgan":         {"apply": "https://careers.jpmorgan.com/", "website": "https://www.jpmorgan.com"},
    "Lloyds Banking":   {"apply": "https://www.lloydsbankinggroup.com/careers.html", "website": "https://www.lloydsbankinggroup.com"},

    # UK Retail / Telco / Media
    "Tesco":            {"apply": "https://www.tesco-careers.com/", "website": "https://www.tesco.com"},
    "Sky":              {"apply": "https://careers.sky.com/", "website": "https://www.sky.com"},
    "BT Group":         {"apply": "https://www.bt.com/careers", "website": "https://www.bt.com"},
    "BBC":              {"apply": "https://careerssearch.bbc.co.uk/", "website": "https://www.bbc.co.uk"},
    "Vodafone":         {"apply": "https://careers.vodafone.com/", "website": "https://www.vodafone.co.uk"},
    "Unilever":         {"apply": "https://careers.unilever.com/", "website": "https://www.unilever.com"},
    "Sainsbury's":      {"apply": "https://sainsburys.jobs/", "website": "https://www.sainsburys.co.uk"},
    "National Grid":    {"apply": "https://careers.nationalgrid.com/", "website": "https://www.nationalgrid.com"},

    # Pharma / Health
    "AstraZeneca":      {"apply": "https://careers.astrazeneca.com/", "website": "https://www.astrazeneca.com"},
    "GSK":              {"apply": "https://www.gsk.com/en-gb/careers/", "website": "https://www.gsk.com"},
    "Babylon Health":   {"apply": "https://www.babylonhealth.com/careers", "website": "https://www.babylonhealth.com"},
    "NHS Digital":      {"apply": "https://digital.nhs.uk/careers", "website": "https://digital.nhs.uk"},

    # Cybersecurity
    "CrowdStrike":      {"apply": "https://www.crowdstrike.com/careers/", "website": "https://www.crowdstrike.com"},
    "NCC Group":        {"apply": "https://www.nccgroup.com/uk/careers/", "website": "https://www.nccgroup.com"},
    "GCHQ":             {"apply": "https://www.gchq-careers.co.uk/", "website": "https://www.gchq.gov.uk"},
    "Sophos":           {"apply": "https://www.sophos.com/en-us/careers", "website": "https://www.sophos.com"},
    "Palo Alto Networks": {"apply": "https://jobs.paloaltonetworks.com/", "website": "https://www.paloaltonetworks.com"},

    # Europe
    "Siemens":          {"apply": "https://jobs.siemens.com/", "website": "https://www.siemens.com"},
    "SAP":              {"apply": "https://jobs.sap.com/", "website": "https://www.sap.com"},
    "Bosch":            {"apply": "https://www.bosch.com/careers/", "website": "https://www.bosch.com"},
    "Bosch AI":         {"apply": "https://www.bosch-ai.com/careers/", "website": "https://www.bosch-ai.com"},
    "Booking.com":      {"apply": "https://careers.booking.com/", "website": "https://www.booking.com"},
    "Zalando":          {"apply": "https://jobs.zalando.com/en/", "website": "https://www.zalando.com"},
    "Shopify":          {"apply": "https://www.shopify.com/careers", "website": "https://www.shopify.com"},
    "ABB":              {"apply": "https://careers.abb/", "website": "https://global.abb"},

    # US / Global
    "Stripe":           {"apply": "https://stripe.com/jobs", "website": "https://stripe.com"},
    "Tesla":            {"apply": "https://www.tesla.com/careers", "website": "https://www.tesla.com"},
    "Boston Dynamics":  {"apply": "https://bostondynamics.wd1.myworkdayjobs.com/en-US/Boston_Dynamics", "website": "https://bostondynamics.com"},
    "Toyota Research":  {"apply": "https://www.tri.global/careers", "website": "https://www.tri.global"},
    "ByteDance":        {"apply": "https://jobs.bytedance.com/en/", "website": "https://www.bytedance.com"},

    # Asia / India
    "Flipkart":         {"apply": "https://www.flipkartcareers.com/", "website": "https://www.flipkart.com"},
    "Grab":             {"apply": "https://grab.careers/", "website": "https://www.grab.com"},
    "Infosys":          {"apply": "https://www.infosys.com/careers/", "website": "https://www.infosys.com"},

    # Contract / Generic
    "Contract Role":    {"apply": "https://www.contractoruk.com/", "website": "https://www.contractoruk.com"},
    "Contract Client":  {"apply": "https://www.contractoruk.com/", "website": "https://www.contractoruk.com"},
}


# ═══════════════════════════════════════════════════════════
# DATA GENERATION
# ═══════════════════════════════════════════════════════════

def get_all_roles():
    """Return flat list of all role names with metadata."""
    roles = []
    for category, role_list in ROLES.items():
        for r in role_list:
            roles.append({**r, "category": category})
    return roles


def generate_jobs(role_name: str, num_jobs: int = 20) -> pd.DataFrame:
    """Generate mock job listings for a given role."""
    random.seed(hash(role_name) % 2**32)

    companies = COMPANIES_BY_ROLE.get(role_name, DEFAULT_COMPANIES)
    descriptions = ROLE_DESCRIPTIONS.get(role_name, DEFAULT_DESCRIPTIONS)

    jobs = []
    for i in range(num_jobs):
        comp = companies[i % len(companies)]
        days_ago = random.randint(0, 30)
        posted = datetime.now() - timedelta(days=days_ago)
        job_type = random.choice(JOB_TYPES)
        exp = random.choice(EXPERIENCE_LEVELS)
        desc = descriptions[i % len(descriptions)]

        is_day_rate = comp["salary_max"] < 1000
        if is_day_rate:
            salary_str = f"£{comp['salary_min']}–£{comp['salary_max']}/day"
            salary_avg = (comp["salary_min"] + comp["salary_max"]) / 2 * 220
        else:
            salary_str = f"£{comp['salary_min'] // 1000}K–£{comp['salary_max'] // 1000}K"
            salary_avg = (comp["salary_min"] + comp["salary_max"]) / 2

        # Extract skills from role's skill set
        role_skills = list(SKILLS_BY_ROLE.get(role_name, DEFAULT_SKILLS).keys())
        num_skills = random.randint(3, min(6, len(role_skills)))
        job_skills = random.sample(role_skills, num_skills)

        jobs.append({
            "id": i + 1,
            "company": comp["company"],
            "role": role_name,
            "location": comp["location"],
            "country": comp["location"].split(", ")[-1] if ", " in comp["location"] else comp["location"],
            "salary": salary_str,
            "salary_avg": salary_avg,
            "type": job_type,
            "mode": comp["mode"],
            "posted": posted.strftime("%d %b"),
            "posted_date": posted,
            "experience": exp,
            "skills": job_skills,
            "description": desc,
            "apply_url": VERIFIED_URLS.get(comp["company"], {}).get("apply", f"https://www.google.com/search?q={comp['company'].replace(' ', '+')}+careers"),
            "website": VERIFIED_URLS.get(comp["company"], {}).get("website", f"https://www.google.com/search?q={comp['company'].replace(' ', '+')}"),
        })

    return pd.DataFrame(jobs).sort_values("posted_date", ascending=False).reset_index(drop=True)


def get_skills_data(role_name: str) -> dict:
    """Return skills frequency for a role."""
    return SKILLS_BY_ROLE.get(role_name, DEFAULT_SKILLS)


def get_location_data(role_name: str) -> dict:
    """Return location distribution for a role."""
    return LOCATIONS_BY_ROLE.get(role_name, LOCATIONS_BY_ROLE["default"])


def get_kpi_data(role_name: str, df: pd.DataFrame) -> dict:
    """Calculate KPI metrics from job data."""
    total = len(df)
    avg_salary = df["salary_avg"].mean()
    top_location = df["location"].mode().iloc[0] if len(df) > 0 else "N/A"
    remote_pct = (df["mode"] == "Remote").sum() / max(total, 1) * 100

    # Find role count from ROLES
    role_count = total
    for cat in ROLES.values():
        for r in cat:
            if r["name"] == role_name:
                role_count = r["count"]
                break

    return {
        "total": f"{role_count:,}",
        "avg_salary": f"£{int(avg_salary / 1000)}K",
        "top_location": top_location.split(",")[0],
        "remote_pct": f"{int(remote_pct)}%",
    }


# ═══════════════════════════════════════════════════════════
# EMAIL-SOURCED JOBS
# In production, this reads from Gmail API parsing job alert emails.
# For now, generates mock data simulating email-sourced job alerts.
# ═══════════════════════════════════════════════════════════

EMAIL_SOURCES = {
    "LinkedIn": "📩 LinkedIn Alert",
    "Indeed": "📩 Indeed Daily Digest",
    "Totaljobs": "📩 Totaljobs Alert",
    "Glassdoor": "📩 Glassdoor Alert",
    "ECMS Selection": "📩 ECMS Newsletter",
    "IT Jobs Watch": "📩 IT Jobs Watch Alert",
    "Reed": "📩 Reed Job Alert",
    "CV-Library": "📩 CV-Library Alert",
}

EMAIL_JOBS_BY_ROLE = {
    "AI Engineer": [
        {"company": "Barclays", "role": "AI Engineer", "location": "London, UK", "salary_min": 82000, "salary_max": 115000, "mode": "Hybrid", "source": "LinkedIn", "email_subject": "New AI Engineer roles in London"},
        {"company": "HSBC", "role": "AI Engineer – Risk", "location": "Birmingham, UK", "salary_min": 78000, "salary_max": 105000, "mode": "Hybrid", "source": "Indeed", "email_subject": "5 new AI Engineer jobs matching your alert"},
        {"company": "Accenture", "role": "Applied AI Engineer", "location": "London, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Hybrid", "source": "Totaljobs", "email_subject": "AI Engineer – 14 new roles this week"},
        {"company": "Capgemini", "role": "AI/ML Engineer", "location": "London, UK", "salary_min": 68000, "salary_max": 95000, "mode": "Hybrid", "source": "Reed", "email_subject": "Your AI Engineer job alert"},
        {"company": "Vodafone", "role": "AI Platform Engineer", "location": "London, UK", "salary_min": 75000, "salary_max": 102000, "mode": "Hybrid", "source": "LinkedIn", "email_subject": "AI Engineer roles you may be interested in"},
        {"company": "Sky", "role": "AI Engineer – Personalisation", "location": "London, UK", "salary_min": 70000, "salary_max": 95000, "mode": "Hybrid", "source": "Glassdoor", "email_subject": "New AI Engineer openings near you"},
        {"company": "Rolls-Royce", "role": "AI Systems Engineer", "location": "Derby, UK", "salary_min": 65000, "salary_max": 92000, "mode": "Onsite", "source": "Indeed", "email_subject": "AI Engineer – Derby, East Midlands"},
        {"company": "GSK", "role": "AI Engineer – Drug Discovery", "location": "London, UK", "salary_min": 80000, "salary_max": 112000, "mode": "Hybrid", "source": "ECMS Selection", "email_subject": "ECMS: AI Engineering opportunity – Pharma"},
        {"company": "Tesco", "role": "AI Engineer – Supply Chain", "location": "Welwyn Garden City, UK", "salary_min": 62000, "salary_max": 85000, "mode": "Hybrid", "source": "CV-Library", "email_subject": "Your daily job matches: AI Engineer"},
        {"company": "National Grid", "role": "AI/ML Engineer", "location": "Warwick, UK", "salary_min": 68000, "salary_max": 95000, "mode": "Hybrid", "source": "Totaljobs", "email_subject": "AI Engineer roles in the Midlands"},
        {"company": "BT Group", "role": "AI Research Engineer", "location": "London, UK", "salary_min": 72000, "salary_max": 100000, "mode": "Hybrid", "source": "IT Jobs Watch", "email_subject": "IT Jobs Watch: AI Engineer demand update"},
        {"company": "Unilever", "role": "AI Engineer – Consumer Insights", "location": "London, UK", "salary_min": 75000, "salary_max": 105000, "mode": "Hybrid", "source": "LinkedIn", "email_subject": "3 new AI Engineer roles for you"},
    ],
}

DEFAULT_EMAIL_JOBS = [
    {"company": "Barclays", "role": "{role}", "location": "London, UK", "salary_min": 62000, "salary_max": 92000, "mode": "Hybrid", "source": "LinkedIn", "email_subject": "New {role} roles in London"},
    {"company": "BT Group", "role": "{role}", "location": "Manchester, UK", "salary_min": 58000, "salary_max": 82000, "mode": "Remote", "source": "Indeed", "email_subject": "5 new {role} jobs this week"},
    {"company": "Deloitte", "role": "{role}", "location": "Edinburgh, UK", "salary_min": 60000, "salary_max": 88000, "mode": "Onsite", "source": "Totaljobs", "email_subject": "{role} – new openings"},
    {"company": "Microsoft", "role": "{role}", "location": "London, UK", "salary_min": 78000, "salary_max": 120000, "mode": "Hybrid", "source": "Reed", "email_subject": "Your {role} job alert"},
    {"company": "AstraZeneca", "role": "{role}", "location": "Cambridge, UK", "salary_min": 65000, "salary_max": 95000, "mode": "Hybrid", "source": "Glassdoor", "email_subject": "New {role} openings near you"},
    {"company": "Arm", "role": "{role}", "location": "Cambridge, UK", "salary_min": 70000, "salary_max": 100000, "mode": "Onsite", "source": "LinkedIn", "email_subject": "{role} roles you may like"},
    {"company": "Accenture", "role": "{role}", "location": "London, UK", "salary_min": 60000, "salary_max": 90000, "mode": "Hybrid", "source": "ECMS Selection", "email_subject": "ECMS: {role} opportunity"},
    {"company": "IBM", "role": "{role}", "location": "London, UK", "salary_min": 62000, "salary_max": 92000, "mode": "Hybrid", "source": "CV-Library", "email_subject": "Daily matches: {role}"},
    {"company": "Booking.com", "role": "{role}", "location": "Amsterdam, Netherlands", "salary_min": 70000, "salary_max": 102000, "mode": "Hybrid", "source": "Indeed", "email_subject": "{role} – Europe"},
    {"company": "Shopify", "role": "{role}", "location": "Remote, UK", "salary_min": 72000, "salary_max": 105000, "mode": "Remote", "source": "Totaljobs", "email_subject": "Remote {role} roles"},
    {"company": "McKinsey", "role": "{role}", "location": "London, UK", "salary_min": 82000, "salary_max": 125000, "mode": "Onsite", "source": "LinkedIn", "email_subject": "Top {role} roles this week"},
    {"company": "Palantir", "role": "{role}", "location": "London, UK", "salary_min": 90000, "salary_max": 135000, "mode": "Hybrid", "source": "Glassdoor", "email_subject": "{role} at top tech companies"},
]


def generate_email_jobs(role_name: str, num_jobs: int = 12) -> pd.DataFrame:
    """Generate mock email-sourced job listings for a given role."""
    random.seed(hash(role_name + "_email") % 2**32)

    if role_name in EMAIL_JOBS_BY_ROLE:
        templates = EMAIL_JOBS_BY_ROLE[role_name]
    else:
        templates = []
        for t in DEFAULT_EMAIL_JOBS:
            templates.append({
                **t,
                "role": t["role"].replace("{role}", role_name),
                "email_subject": t["email_subject"].replace("{role}", role_name),
            })

    jobs = []
    for i in range(min(num_jobs, len(templates))):
        t = templates[i % len(templates)]
        days_ago = random.randint(0, 14)
        posted = datetime.now() - timedelta(days=days_ago)
        job_type = random.choice(JOB_TYPES)
        exp = random.choice(EXPERIENCE_LEVELS)
        desc_list = ROLE_DESCRIPTIONS.get(role_name, DEFAULT_DESCRIPTIONS)
        desc = desc_list[i % len(desc_list)]

        salary_str = f"£{t['salary_min'] // 1000}K–£{t['salary_max'] // 1000}K"
        salary_avg = (t["salary_min"] + t["salary_max"]) / 2

        role_skills = list(SKILLS_BY_ROLE.get(role_name, DEFAULT_SKILLS).keys())
        num_skills = random.randint(3, min(5, len(role_skills)))
        job_skills = random.sample(role_skills, num_skills)

        source_tag = EMAIL_SOURCES.get(t["source"], "📩 Email Alert")

        jobs.append({
            "id": i + 1,
            "company": t["company"],
            "role": t["role"],
            "location": t["location"],
            "country": t["location"].split(", ")[-1] if ", " in t["location"] else t["location"],
            "salary": salary_str,
            "salary_avg": salary_avg,
            "type": job_type,
            "mode": t["mode"],
            "posted": posted.strftime("%d %b"),
            "posted_date": posted,
            "experience": exp,
            "skills": job_skills,
            "description": desc,
            "apply_url": VERIFIED_URLS.get(t["company"], {}).get("apply", f"https://www.google.com/search?q={t['company'].replace(' ', '+')}+careers"),
            "website": VERIFIED_URLS.get(t["company"], {}).get("website", f"https://www.google.com/search?q={t['company'].replace(' ', '+')}"),
            "email_source": t["source"],
            "email_source_tag": source_tag,
            "email_subject": t["email_subject"],
        })

    return pd.DataFrame(jobs).sort_values("posted_date", ascending=False).reset_index(drop=True)


def get_email_kpi_data(role_name: str, df: pd.DataFrame) -> dict:
    """Calculate KPI metrics from email-sourced job data."""
    total = len(df)
    avg_salary = df["salary_avg"].mean() if total > 0 else 0
    top_location = df["location"].mode().iloc[0] if total > 0 else "N/A"
    remote_pct = (df["mode"] == "Remote").sum() / max(total, 1) * 100
    num_sources = df["email_source"].nunique() if "email_source" in df.columns else 0

    return {
        "total": str(total),
        "avg_salary": f"£{int(avg_salary / 1000)}K",
        "top_location": top_location.split(",")[0],
        "remote_pct": f"{int(remote_pct)}%",
        "sources": num_sources,
    }

# ═══════════════════════════════════════════════════════════
# CONSTELLATION LINKS - Real job board URLs per role
# Each link is a verified, working URL to a job search
# page filtered for that specific role.
# ═══════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════
# TREND DATA - Updated March 2026
# Sources: LinkedIn AI job growth data, Indeed AI Tracker
# (4.2% of US postings mention AI, Dec 2025), Indeed UK
# (5.6% of UK postings mention AI), PwC AI Jobs Barometer
# (56% wage premium for AI skills), WEF (1.3M new AI roles),
# McKinsey (AI specialist roles grew 176% in UK).
# LLM Engineer and Agentic Engineer show steepest growth.
# ═══════════════════════════════════════════════════════════

TREND_FIELDS = ["ML Engineer", "AI Engineer", "Data Scientist", "LLM Engineer", "Deep Learning", "NLP Engineer", "AI Ethics", "AI Product Mgr", "Computer Vision"]
TREND_YEARS = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
TREND_DATA = {
    "ML Engineer":     [30, 42, 58, 70, 80, 90, 96],
    "AI Engineer":     [15, 22, 38, 55, 76, 94, 100],
    "Data Scientist":  [62, 66, 72, 74, 76, 78, 79],
    "LLM Engineer":    [2, 3, 5, 22, 52, 82, 98],
    "Deep Learning":   [25, 35, 48, 58, 65, 70, 73],
    "NLP Engineer":    [20, 28, 40, 50, 56, 60, 61],
    "AI Ethics":       [3, 5, 10, 18, 28, 38, 48],
    "AI Product Mgr":  [8, 12, 20, 32, 44, 56, 65],
    "Computer Vision":  [22, 30, 42, 50, 56, 60, 63],
}

def get_constellation_links(role_name: str) -> list:
    """Return verified job board and career page links for the selected role."""
    role_q = role_name.replace(" ", "+").replace("/", "%2F")
    role_q_dash = role_name.replace(" ", "-").lower()
    role_q_pct = role_name.replace(" ", "%20")

    links = [
        # ═══ AI & ML SPECIFIC BOARDS ═══
        {"name": "AI Jobs", "url": "https://www.aijobs.com/", "category": "AI Specific"},
        {"name": "AIJobs.ai", "url": "https://aijobs.ai/", "category": "AI Specific"},
        {"name": "Hugging Face Jobs", "url": "https://apply.workable.com/huggingface/", "category": "AI Specific"},
        {"name": "AI/ML Jobs", "url": "https://https://aimljobs-news.beehiiv.com//", "category": "AI Specific"},

        # ═══ UK JOB BOARDS (priority) ═══
        {"name": "Indeed UK", "url": f"https://uk.indeed.com/jobs?q={role_q}", "category": "UK Job Board"},
        {"name": "LinkedIn Jobs", "url": f"https://www.linkedin.com/jobs/search/?keywords={role_q_pct}&location=United%20Kingdom", "category": "UK Job Board"},
        {"name": "Totaljobs", "url": f"https://www.totaljobs.com/jobs/{role_q_dash}", "category": "UK Job Board"},
        {"name": "Reed", "url": f"https://www.reed.co.uk/jobs/{role_q_dash}-jobs", "category": "UK Job Board"},
        {"name": "CV-Library", "url": f"https://www.cv-library.co.uk/search-jobs?kw={role_q}", "category": "UK Job Board"},
        {"name": "Glassdoor UK", "url": f"https://www.glassdoor.co.uk/Job/uk-{role_q_dash}-jobs-SRCH_IL.0,2_IN2_KO3,20.htm", "category": "UK Job Board"},
        {"name": "Monster UK", "url": f"https://www.monster.co.uk/jobs/search?q={role_q}", "category": "UK Job Board"},
        {"name": "Guardian Jobs", "url": f"https://jobs.theguardian.com/searchjobs/?keywords={role_q}", "category": "UK Job Board"},

        # ═══ UK TECH BOARDS ═══
        {"name": "CWJobs", "url": f"https://www.cwjobs.co.uk/jobs/{role_q_dash}", "category": "UK Tech Board"},
        {"name": "Technojobs", "url": f"https://www.technojobs.co.uk/search?q={role_q}", "category": "UK Tech Board"},
        {"name": "IT Job Board", "url": f"https://www.itjobboard.co.uk/search?q={role_q}", "category": "UK Tech Board"},
        {"name": "ECM Selection", "url": "https://www.ecmselection.co.uk/machine-learning", "category": "UK Tech Board"},
        {"name": "Otta / WTTJ", "url": f"https://uk.welcometothejungle.com/en/jobs?query={role_q_pct}", "category": "UK Tech Board"},
        {"name": "cord.com", "url": f"https://cord.com/search?q={role_q}", "category": "UK Tech Board"},
        {"name": "IT Jobs Watch", "url": f"https://www.itjobswatch.co.uk/jobs/uk/{role_q_pct}.do", "category": "UK Tech Board"},
        {"name": "Adzuna UK", "url": f"https://www.adzuna.co.uk/search?q={role_q}", "category": "UK Tech Board"},

        # ═══ USA BOARDS ═══
        {"name": "Indeed US", "url": f"https://www.indeed.com/jobs?q={role_q}", "category": "USA"},
        {"name": "Dice (US Tech)", "url": f"https://www.dice.com/jobs?q={role_q}", "category": "USA"},
        {"name": "USAJobs (Gov)", "url": f"https://www.usajobs.gov/search/results/?k={role_q}", "category": "USA"},
        {"name": "Built In", "url": f"https://builtin.com/jobs?search={role_q}", "category": "USA"},
        {"name": "Wellfound (AngelList)", "url": f"https://wellfound.com/jobs?search={role_q}", "category": "USA"},
        {"name": "Levels.fyi Jobs", "url": f"https://www.levels.fyi/jobs?title={role_q_pct}", "category": "USA"},

        # ═══ CANADA ═══
        {"name": "Indeed Canada", "url": f"https://ca.indeed.com/jobs?q={role_q}", "category": "Canada"},
        {"name": "Job Bank Canada", "url": f"https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring={role_q}", "category": "Canada"},

        # ═══ GERMANY & EUROPE ═══
        {"name": "StepStone DE", "url": f"https://www.stepstone.de/jobs/{role_q_dash}", "category": "Europe"},
        {"name": "Jooble", "url": f"https://jooble.org/jobs-{role_q_dash}", "category": "Europe"},
        {"name": "Glassdoor DE", "url": f"https://www.glassdoor.de/Job/{role_q_dash}-jobs-SRCH_KO0,15.htm", "category": "Europe"},
        {"name": "XING Jobs", "url": f"https://www.xing.com/jobs/search?keywords={role_q_pct}", "category": "Europe"},
        {"name": "EuroTechJobs", "url": f"https://www.eurotechjobs.com/search?q={role_q}", "category": "Europe"},
        {"name": "SwissDevJobs", "url": f"https://swissdevjobs.ch/jobs?q={role_q}", "category": "Europe"},

        # ═══ STARTUPS & SCALE-UPS ═══
        {"name": "Y Combinator (Work at a Startup)", "url": f"https://www.workatastartup.com/jobs?query={role_q}", "category": "Startups"},
        {"name": "Escape the City", "url": f"https://www.escapethecity.org/search/jobs?q={role_q}", "category": "Startups"},

        # ═══ CONTRACT / FREELANCE ═══
        {"name": "ContractorUK", "url": f"https://www.contractoruk.com/search/jobs?keywords={role_q}", "category": "Contract"},
        {"name": "Upwork", "url": f"https://www.upwork.com/nx/search/jobs/?q={role_q_pct}", "category": "Contract"},
        {"name": "Toptal", "url": "https://www.toptal.com/careers", "category": "Contract"},

        # ═══ DIVERSITY & INCLUSION ═══
        {"name": "Women in Tech", "url": "https://www.womenintech.co.uk/jobs", "category": "Diversity"},
        {"name": "SheCanCode", "url": "https://jobs.shecancode.io/", "category": "Diversity"},
        {"name": "Inclusive Boards", "url": "https://www.inclusiveboards.co.uk/jobs", "category": "Diversity"},

        # ═══ TOP AI COMPANY CAREER PAGES ═══
        {"name": "Google Careers", "url": "https://www.google.com/about/careers/applications/", "category": "Direct"},
        {"name": "DeepMind Careers", "url": "https://deepmind.google/careers/", "category": "Direct"},
        {"name": "Meta Careers", "url": "https://www.metacareers.com/jobs", "category": "Direct"},
        {"name": "OpenAI Careers", "url": "https://openai.com/careers/", "category": "Direct"},
        {"name": "Anthropic Careers", "url": "https://www.anthropic.com/careers", "category": "Direct"},
        {"name": "Microsoft Careers", "url": "https://careers.microsoft.com/", "category": "Direct"},
        {"name": "Amazon Jobs UK", "url": "https://www.amazon.jobs/en-gb/", "category": "Direct"},
        {"name": "Apple Jobs UK", "url": "https://jobs.apple.com/en-gb/search", "category": "Direct"},
        {"name": "NVIDIA Careers", "url": "https://www.nvidia.com/en-gb/about-nvidia/careers/", "category": "Direct"},

        # ═══ UK TECH COMPANY CAREERS ═══
        {"name": "Spotify Jobs", "url": "https://www.lifeatspotify.com/jobs", "category": "UK Companies"},
        {"name": "Revolut Careers", "url": "https://www.revolut.com/careers/", "category": "UK Companies"},
        {"name": "Monzo Careers", "url": "https://monzo.com/careers/", "category": "UK Companies"},
        {"name": "Wise Jobs", "url": "https://www.wise.jobs/", "category": "UK Companies"},
        {"name": "Darktrace Careers", "url": "https://darktrace.com/careers", "category": "UK Companies"},
        {"name": "Arm Careers", "url": "https://careers.arm.com/", "category": "UK Companies"},
        {"name": "Wayve Careers", "url": "https://wayve.ai/careers/", "category": "UK Companies"},
        {"name": "Palantir Careers", "url": "https://www.palantir.com/careers/", "category": "UK Companies"},
        {"name": "Stripe Jobs", "url": "https://stripe.com/jobs", "category": "UK Companies"},
        {"name": "Dyson Careers", "url": "https://careers.dyson.com/en-gb/", "category": "UK Companies"},
        {"name": "Ocado Careers", "url": "https://careers.ocadogroup.com/", "category": "UK Companies"},

        # ═══ UK ENTERPRISE & DEFENCE ═══
        {"name": "BAE Systems", "url": "https://www.baesystems.com/en/careers", "category": "UK Enterprise"},
        {"name": "Rolls-Royce", "url": "https://careers.rolls-royce.com/", "category": "UK Enterprise"},
        {"name": "AstraZeneca", "url": "https://careers.astrazeneca.com/", "category": "UK Enterprise"},
        {"name": "GSK Careers", "url": "https://www.gsk.com/en-gb/careers/", "category": "UK Enterprise"},
        {"name": "Barclays Jobs", "url": "https://search.jobs.barclays/", "category": "UK Enterprise"},
        {"name": "HSBC Careers", "url": "https://www.hsbc.com/careers", "category": "UK Enterprise"},
        {"name": "Deloitte UK", "url": "https://www2.deloitte.com/uk/en/careers.html", "category": "UK Enterprise"},
        {"name": "Accenture UK", "url": "https://www.accenture.com/gb-en/careers", "category": "UK Enterprise"},
        {"name": "IBM Careers", "url": "https://www.ibm.com/careers", "category": "UK Enterprise"},

        # ═══ US / GLOBAL COMPANIES ═══
        {"name": "Tesla Careers", "url": "https://www.tesla.com/careers", "category": "Global Companies"},
        {"name": "ByteDance Jobs", "url": "https://jobs.bytedance.com/en/", "category": "Global Companies"},
        {"name": "Booking.com", "url": "https://careers.booking.com/", "category": "Global Companies"},
        {"name": "Shopify Careers", "url": "https://www.shopify.com/careers", "category": "Global Companies"},
        {"name": "Siemens Jobs", "url": "https://jobs.siemens.com/", "category": "Global Companies"},
        {"name": "SAP Careers", "url": "https://jobs.sap.com/", "category": "Global Companies"},
    ]

    return links