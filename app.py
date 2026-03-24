"""
AI Labour Market Aggregator Dashboard
Built by Collins Lemeke @ AI Nexus, University of Greater Manchester
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timezone
from data import get_all_roles, generate_jobs, get_skills_data, get_location_data, get_kpi_data, TREND_FIELDS, TREND_YEARS, TREND_DATA

# ═══════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="AI Labour Market Aggregator ALMA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "selected_job_idx" not in st.session_state:
    st.session_state.selected_job_idx = 0

is_dark = st.session_state.theme == "dark"

# ═══════════════════════════════════════════════════════════
# THEME COLORS
# ═══════════════════════════════════════════════════════════
if is_dark:
    BG = "#05070D"
    SURFACE = "#0B0F18"
    PANEL = "#10141F"
    ELEVATED = "#161B28"
    BORDER = "#1C2333"
    TEXT_PRIMARY = "#E8ECF4"
    TEXT_SECONDARY = "#8892A4"
    TEXT_MUTED = "#505A6E"
    ACCENT1 = "#00D4FF"
    ACCENT2 = "#00FF88"
    ACCENT3 = "#FFB800"
    ACCENT4 = "#FF6B6B"
    ACCENT5 = "#A78BFA"
    CHART_GRID = "#1C2333"
    COLORS = [ACCENT1, ACCENT2, ACCENT3, ACCENT4, ACCENT5, ACCENT1, ACCENT2, ACCENT3]
else:
    BG = "#F2F4F7"
    SURFACE = "#FFFFFF"
    PANEL = "#FFFFFF"
    ELEVATED = "#F7F8FA"
    BORDER = "#DFE3EA"
    TEXT_PRIMARY = "#111827"
    TEXT_SECONDARY = "#5A6478"
    TEXT_MUTED = "#8E96A6"
    ACCENT1 = "#0088B3"
    ACCENT2 = "#00875A"
    ACCENT3 = "#B07800"
    ACCENT4 = "#CF222E"
    ACCENT5 = "#7C3AED"
    CHART_GRID = "#DFE3EA"
    COLORS = [ACCENT1, ACCENT2, ACCENT3, ACCENT4, ACCENT5, ACCENT1, ACCENT2, ACCENT3]

ACCENTS = [ACCENT1, ACCENT2, ACCENT3, ACCENT4]

# ═══════════════════════════════════════════════════════════
# CSS - Styling only, not layout
# ═══════════════════════════════════════════════════════════
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

    #MainMenu, footer, header {{ display: none !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    [data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}

    [data-testid="stAppViewContainer"], [data-testid="stMain"],
    .stApp, section.main {{
        background: {BG} !important;
        color: {TEXT_PRIMARY} !important;
        font-family: 'Outfit', sans-serif !important;
    }}

    .block-container {{
        padding-top: 0.5rem !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
    }}

    [data-testid="stSelectbox"] label {{ color: {TEXT_SECONDARY} !important; font-size: 12px !important; }}
    [data-testid="stSelectbox"] > div > div {{
        background: {ELEVATED} !important;
        border-color: {BORDER} !important;
        color: {TEXT_PRIMARY} !important;
    }}
    [data-testid="stSelectbox"] > div > div > div {{ color: {TEXT_PRIMARY} !important; }}
    [data-testid="stSelectbox"] span {{ color: {TEXT_PRIMARY} !important; }}
    [data-testid="stSelectbox"] svg {{ fill: {TEXT_SECONDARY} !important; }}
    [data-baseweb="popover"] {{ background: {"#161B28" if is_dark else "#1a1a2e"} !important; border: 1px solid {BORDER} !important; }}
    [data-baseweb="popover"] li {{ color: #FFFFFF !important; }}
    [data-baseweb="popover"] li:hover {{ background: {"#1E2538" if is_dark else "#2a2a4a"} !important; }}
    ul[role="listbox"] {{ background: {"#161B28" if is_dark else "#1a1a2e"} !important; }}
    ul[role="listbox"] li {{ color: #FFFFFF !important; opacity: 1 !important; }}
    [data-baseweb="menu"] {{ background: {"#161B28" if is_dark else "#1a1a2e"} !important; }}
    [data-baseweb="select"] > div {{ color: {TEXT_PRIMARY} !important; }}
    [data-baseweb="select"] input {{ color: {TEXT_PRIMARY} !important; }}

    .stButton > button {{
        background: {ELEVATED} !important;
        color: {ACCENT1} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 6px !important;
        font-size: 11px !important;
        padding: 4px 12px !important;
    }}
    .stButton > button:hover {{ border-color: {ACCENT1} !important; }}

    .js-plotly-plot .plotly .modebar {{ display: none !important; }}
    ::-webkit-scrollbar {{ width: 5px; }}
    ::-webkit-scrollbar-track {{ background: {BG}; }}
    ::-webkit-scrollbar-thumb {{ background: {TEXT_MUTED}; border-radius: 3px; }}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════
now_uk = datetime.now(timezone.utc)
time_str = now_uk.strftime("%d %b %Y, %H:%M UTC")

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:space-between; padding:8px 4px 12px; border-bottom:1px solid {BORDER}; margin-bottom:12px;">
    <div style="display:flex; align-items:center; gap:12px;">
        <div style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg,{ACCENT1},{ACCENT2}); display:flex; align-items:center; justify-content:center; font-weight:800; font-size:12px; color:#05070D;">AI</div>
        <div>
            <div style="font-size:15px; font-weight:700; color:{TEXT_PRIMARY}; letter-spacing:-0.3px;">AI Labour Market Aggregator (ALMA)</div>
            <div style="font-size:9px; font-weight:500; color:{TEXT_MUTED}; letter-spacing:1px; text-transform:uppercase;">Central Hub for AI/Tech Jobs</div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:14px;">
        <div style="display:flex; align-items:center; gap:5px; font-size:10px; font-weight:600; color:{ACCENT2}; letter-spacing:0.8px; text-transform:uppercase;">
            <span style="width:6px; height:6px; border-radius:50%; background:{ACCENT2}; display:inline-block;"></span> LIVE
        </div>
        <span style="font-size:10px; color:{TEXT_MUTED}; font-family:'IBM Plex Mono',monospace;">{time_str}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# ROLE SELECTOR + THEME TOGGLE
# ═══════════════════════════════════════════════════════════
all_roles = get_all_roles()
role_options = [r['name'] for r in all_roles]

sel_col, spacer_col, theme_col = st.columns([3, 7, 1])
with sel_col:
    selected_display = st.selectbox("Select AI Role", role_options, index=0, label_visibility="collapsed")
with theme_col:
    if st.button("☀️ Light" if is_dark else "🌙 Dark", key="theme_toggle"):
        st.session_state.theme = "light" if is_dark else "dark"
        st.rerun()

selected_role = selected_display

# Generate data
df_jobs = generate_jobs(selected_role, num_jobs=20)
kpi_data = get_kpi_data(selected_role, df_jobs)
skills_data = get_skills_data(selected_role)
location_data = get_location_data(selected_role)

# ═══════════════════════════════════════════════════════════
# THREE COLUMN LAYOUT
# ═══════════════════════════════════════════════════════════
left_col, center_col, right_col = st.columns([1, 3, 1])

# ═══════════ LEFT: JOB LISTINGS ═══════════
with left_col:
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:space-between; padding-bottom:8px; border-bottom:1px solid {BORDER}; margin-bottom:8px;">
        <span style="font-size:13px; font-weight:700; color:{TEXT_PRIMARY};">{selected_role}</span>
        <span style="font-size:10px; font-family:'IBM Plex Mono',monospace; color:{ACCENT1}; background:rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.10); padding:2px 8px; border-radius:8px;">{kpi_data['total']}</span>
    </div>
    """, unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        type_filter = st.selectbox("Type", ["All", "Full-time", "Contract", "Remote"], label_visibility="collapsed", key="tf")
    with f2:
        mode_filter = st.selectbox("Mode", ["All Modes", "Onsite", "Hybrid", "Remote"], label_visibility="collapsed", key="mf")

    filtered_df = df_jobs.copy()
    if type_filter != "All":
        filtered_df = filtered_df[filtered_df["type"] == type_filter]
    if mode_filter != "All Modes":
        filtered_df = filtered_df[filtered_df["mode"] == mode_filter]
    filtered_df = filtered_df.reset_index(drop=True)

    if len(filtered_df) == 0:
        st.info("No jobs match these filters.")
    else:
        if st.session_state.selected_job_idx >= len(filtered_df):
            st.session_state.selected_job_idx = 0

        for idx in range(len(filtered_df)):
            row = filtered_df.iloc[idx]
            is_selected = (idx == st.session_state.selected_job_idx)

            if row["type"] == "Full-time":
                tc = ACCENT1
            elif row["type"] == "Contract":
                tc = ACCENT3
            else:
                tc = ACCENT5

            tc_bg = f"rgba({','.join(str(int(tc.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.10)"
            sal_bg = f"rgba({','.join(str(int(ACCENT2.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.10)"
            sel_style = f"border-left:3px solid {ACCENT1}; background:rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.06);" if is_selected else f"border-left:3px solid transparent;"

            st.markdown(f"""
            <div style="{sel_style} padding:8px 10px; border-bottom:1px solid {BORDER};">
                <div style="font-size:12px; font-weight:600; color:{TEXT_PRIMARY};">{row['company']}</div>
                <div style="font-size:10.5px; color:{TEXT_SECONDARY}; margin-bottom:4px;">{row['role']}</div>
                <div style="display:flex; flex-wrap:wrap; gap:4px;">
                    <span style="font-size:9px; padding:2px 6px; border-radius:4px; color:{ACCENT2}; background:{sal_bg}; font-family:'IBM Plex Mono',monospace;">{row['salary']}</span>
                    <span style="font-size:9px; padding:2px 6px; border-radius:4px; color:{TEXT_MUTED}; background:{ELEVATED};">{row['location'].split(',')[0]}</span>
                    <span style="font-size:9px; padding:2px 6px; border-radius:4px; color:{tc}; background:{tc_bg};">{row['type']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Select", key=f"job_{idx}"):
                st.session_state.selected_job_idx = idx
                st.rerun()

# ═══════════ CENTRE: ANALYTICS ═══════════
with center_col:
    k1, k2, k3, k4 = st.columns(4)
    kpi_items = [
        ("Total Listings", kpi_data["total"], "18% ↑ this month", ACCENT1),
        ("Avg. Salary (UK)", kpi_data["avg_salary"], "5.2% ↑ vs Q4", ACCENT2),
        ("Top Location", kpi_data["top_location"], "28% of roles", ACCENT3),
        ("Remote Available", kpi_data["remote_pct"], "6% ↓ vs Q4", ACCENT4),
    ]

    for col, (label, value, delta, color) in zip([k1, k2, k3, k4], kpi_items):
        with col:
            st.markdown(f"""
            <div style="background:{PANEL}; border:1px solid {BORDER}; border-radius:10px; padding:16px 18px; position:relative; overflow:hidden; margin-bottom:12px;">
                <div style="position:absolute; top:0; left:0; right:0; height:2px; background:{color};"></div>
                <div style="font-size:9.5px; font-weight:600; color:{TEXT_MUTED}; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:8px;">{label}</div>
                <div style="font-family:'IBM Plex Mono',monospace; font-size:24px; font-weight:700; color:{color}; line-height:1;">{value}</div>
                <div style="font-size:10px; font-weight:600; color:{TEXT_SECONDARY}; margin-top:6px; font-family:'IBM Plex Mono',monospace;">{delta}</div>
            </div>
            """, unsafe_allow_html=True)

    chart_l, chart_r = st.columns(2)

    with chart_l:
        st.markdown(f"<div style='font-size:11px; font-weight:600; color:{TEXT_SECONDARY}; letter-spacing:0.6px; text-transform:uppercase; margin-bottom:6px;'>Most Requested Skills</div>", unsafe_allow_html=True)
        sn = list(skills_data.keys())
        sv = list(skills_data.values())
        fig_s = go.Figure()
        fig_s.add_trace(go.Bar(y=sn[::-1], x=sv[::-1], orientation="h",
            marker=dict(color=COLORS[:len(sn)][::-1], cornerradius=4),
            text=[f"{v}%" for v in sv[::-1]], textposition="outside",
            textfont=dict(family="IBM Plex Mono", size=11, color=TEXT_SECONDARY)))
        fig_s.update_layout(height=340, margin=dict(l=0, r=50, t=5, b=5),
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(visible=False, range=[0, 115]),
            yaxis=dict(tickfont=dict(family="Outfit", size=12, color=TEXT_SECONDARY), showgrid=False),
            bargap=0.3)
        st.plotly_chart(fig_s, use_container_width=True, config={"displayModeBar": False})

    with chart_r:
        st.markdown(f"<div style='font-size:11px; font-weight:600; color:{TEXT_SECONDARY}; letter-spacing:0.6px; text-transform:uppercase; margin-bottom:6px;'>Location Distribution</div>", unsafe_allow_html=True)
        ln = list(location_data.keys())
        lv = list(location_data.values())
        fig_p = go.Figure()
        fig_p.add_trace(go.Pie(labels=ln, values=lv, hole=0.6,
            marker=dict(colors=COLORS[:len(ln)]),
            textinfo="label+percent",
            textfont=dict(family="Outfit", size=11, color="#111827")))
        fig_p.update_layout(height=340, margin=dict(l=10, r=10, t=10, b=10),
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            annotations=[dict(text=f"<b>{len(ln)}</b><br><span style='font-size:9px'>Countries</span>",
                x=0.5, y=0.5, font=dict(family="IBM Plex Mono", size=18, color=TEXT_PRIMARY), showarrow=False)])
        st.plotly_chart(fig_p, use_container_width=True, config={"displayModeBar": False})

    # ═══════ AI DEMAND TREND CHART ═══════
    st.markdown(f"<div style='font-size:11px; font-weight:600; color:{TEXT_SECONDARY}; letter-spacing:0.6px; text-transform:uppercase; margin:16px 0 8px; padding-top:12px; border-top:1px solid {BORDER};'>AI Field Demand Trends (Global)</div>", unsafe_allow_html=True)

    trend_fields = TREND_FIELDS
    trend_years = TREND_YEARS
    trend_data = TREND_DATA
    
    trend_colors = ["#1E3A8A", "#38BDF8", "#22C55E", "#8B5CF6", "#F97316", "#EF4444", "#92400E", "#EC4899", "#EAB308"]
    trend_dashes = ["dash", "dot", "dashdot", "longdash", "longdashdot", "dash", "dot", "dashdot", "longdash"]

    fig_trend = go.Figure()
    for i, field in enumerate(trend_fields):
        fig_trend.add_trace(go.Scatter(
            x=trend_years, y=trend_data[field],
            mode="lines+markers",
            name=field,
            line=dict(color=trend_colors[i], width=2.5, dash=trend_dashes[i]),
            marker=dict(size=5),
        ))

    fig_trend.update_layout(
        height=360,
        margin=dict(l=0, r=0, t=10, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            tickfont=dict(family="IBM Plex Mono", size=10, color=TEXT_SECONDARY),
            gridcolor=CHART_GRID, showgrid=True, title=None,
        ),
        yaxis=dict(
            tickfont=dict(family="IBM Plex Mono", size=10, color=TEXT_SECONDARY),
            gridcolor=CHART_GRID, showgrid=True,
            title=dict(text="Demand Index", font=dict(family="Outfit", size=10, color=TEXT_MUTED)),
        ),
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5,
            font=dict(family="Outfit", size=10, color=TEXT_SECONDARY),
            bgcolor="rgba(0,0,0,0)",
        ),
    )
    st.plotly_chart(fig_trend, use_container_width=True, config={"displayModeBar": False})

    # ═══════ JOB BOARD LINKS: Horizontal Bars ═══════
    from data import get_constellation_links
    c_links = get_constellation_links(selected_role)

    # Group by category with display order
    cat_order = ["AI Specific", "UK Job Board", "UK Tech Board", "USA", "Canada", "Europe", "Direct", "UK Companies", "UK Enterprise", "Global Companies", "Startups", "Diversity", "Contract"]
    cat_labels = {
        "AI Specific": "🤖 AI & ML Specific",
        "UK Job Board": "🇬🇧 UK Job Boards",
        "UK Tech Board": "💻 UK Tech Boards",
        "USA": "🇺🇸 United States",
        "Canada": "🇨🇦 Canada",
        "Europe": "🇪🇺 Germany & Europe",
        "Direct": "🏢 Top AI Companies",
        "UK Companies": "🇬🇧 UK Tech Careers",
        "UK Enterprise": "🏛️ UK Enterprise & Finance",
        "Global Companies": "🌍 Global Companies",
        "Startups": "🚀 Startups & Scale-ups",
        "Diversity": "🌈 Diversity & Inclusion",
        "Contract": "📝 Contract & Freelance",
    }
    cat_bar_colors = {
        "AI Specific": (ACCENT4, f"rgba({','.join(str(int(ACCENT4.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "UK Job Board": (ACCENT1, f"rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "UK Tech Board": (ACCENT2, f"rgba({','.join(str(int(ACCENT2.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "USA": (ACCENT1, f"rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Canada": (ACCENT4, f"rgba({','.join(str(int(ACCENT4.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Europe": (ACCENT5, f"rgba({','.join(str(int(ACCENT5.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Direct": (ACCENT3, f"rgba({','.join(str(int(ACCENT3.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "UK Companies": (ACCENT2, f"rgba({','.join(str(int(ACCENT2.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "UK Enterprise": (ACCENT3, f"rgba({','.join(str(int(ACCENT3.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Global Companies": (ACCENT1, f"rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Startups": (ACCENT2, f"rgba({','.join(str(int(ACCENT2.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Diversity": (ACCENT5, f"rgba({','.join(str(int(ACCENT5.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
        "Contract": (ACCENT3, f"rgba({','.join(str(int(ACCENT3.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.12)"),
    }

    # Build grouped links
    grouped = {}
    for lk in c_links:
        cat = lk["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(lk)

    st.markdown(f"""
    <div style="margin-top:20px; padding-top:14px; border-top:1px solid {BORDER};">
        <div style="font-size:12px; font-weight:700; color:{TEXT_PRIMARY}; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:6px; text-align:center;">
            Explore More Tech Jobs <span style="color:{ACCENT1}; font-weight:400; font-size:10px; text-transform:none;">— {selected_role}</span>
        </div>
        <div style="width:120px; height:2px; background:linear-gradient(90deg,{ACCENT1},{ACCENT2}); border-radius:2px; margin:0 auto 14px;"></div>
    </div>
    """, unsafe_allow_html=True)

    for cat in cat_order:
        if cat not in grouped:
            continue
        links_in_cat = grouped[cat]
        fg, bg = cat_bar_colors.get(cat, (ACCENT1, "rgba(0,212,255,0.12)"))
        label = cat_labels.get(cat, cat)

        bars_html = ""
        for lk in links_in_cat:
            bars_html += f"<a href='{lk['url']}' target='_blank' style='display:inline-block; padding:6px 16px; border-radius:8px; font-size:12px; font-weight:500; color:{fg}; background:{bg}; text-decoration:none; border:1px solid transparent; transition:all 0.2s; font-family:IBM Plex Mono,monospace; white-space:nowrap;' onmouseover=\"this.style.borderColor='{fg}';this.style.background='{bg.replace('0.12','0.25')}'\" onmouseout=\"this.style.borderColor='transparent';this.style.background='{bg}'\">{lk['name']}</a> "

        st.markdown(f"""
        <div style="margin-bottom:12px;">
            <div style="font-size:10px; font-weight:600; color:{TEXT_MUTED}; margin-bottom:6px; letter-spacing:0.5px;">{label}</div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">{bars_html}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════ RIGHT: JOB DETAILS ═══════════
with right_col:
    if len(filtered_df) > 0:
        si = min(st.session_state.selected_job_idx, len(filtered_df) - 1)
        job = filtered_df.iloc[si]
        a1_rgb = ','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))

        # Header
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1.2px; text-transform:uppercase; color:{TEXT_MUTED}; margin-bottom:10px; padding-bottom:6px; border-bottom:1px solid {BORDER};'>Job Details <span style=\"float:right; color:{ACCENT1};\">{si+1} of {len(filtered_df)}</span></div>", unsafe_allow_html=True)

        # Company & Role
        st.markdown(f"<div style='font-size:19px; font-weight:700; color:{TEXT_PRIMARY}; margin-bottom:2px; line-height:1.2;'>{job['company']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:13px; color:{ACCENT1}; font-weight:500; margin-bottom:14px;'>{job['role']}</div>", unsafe_allow_html=True)

        # Overview section title
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:{TEXT_MUTED}; margin-bottom:6px; padding-bottom:4px; border-bottom:1px solid {BORDER};'>Overview</div>", unsafe_allow_html=True)

        # Overview rows - each as separate call
        overview_items = [
            ("Salary", f"<span style='font-family:IBM Plex Mono,monospace; color:{ACCENT2}; font-weight:600;'>{job['salary']}</span>"),
            ("Location", f"<span style='font-weight:600; color:{TEXT_PRIMARY};'>{job['location']}</span>"),
            ("Work Mode", f"<span style='font-weight:600; color:{TEXT_PRIMARY};'>{job['mode']}</span>"),
            ("Type", f"<span style='font-weight:600; color:{TEXT_PRIMARY};'>{job['type']}</span>"),
            ("Experience", f"<span style='font-weight:600; color:{TEXT_PRIMARY};'>{job['experience']}</span>"),
            ("Posted", f"<span style='font-weight:600; color:{TEXT_PRIMARY};'>{job['posted']} 2026</span>"),
        ]
        for label, val in overview_items:
            st.markdown(f"<div style='display:flex; justify-content:space-between; padding:4px 0; font-size:12px;'><span style='color:{TEXT_SECONDARY};'>{label}</span>{val}</div>", unsafe_allow_html=True)

        # Skills section
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:{TEXT_MUTED}; margin:14px 0 6px; padding-bottom:4px; border-bottom:1px solid {BORDER};'>Required Skills</div>", unsafe_allow_html=True)
        sk_html = " ".join([f"<span style='display:inline-block; font-size:10px; padding:3px 9px; border-radius:6px; background:rgba({a1_rgb},0.10); color:{ACCENT1}; font-weight:500; margin:2px;'>{s}</span>" for s in job["skills"]])
        st.markdown(f"<div>{sk_html}</div>", unsafe_allow_html=True)

        # Description
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:{TEXT_MUTED}; margin:14px 0 6px; padding-bottom:4px; border-bottom:1px solid {BORDER};'>Description</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:12px; color:{TEXT_SECONDARY}; line-height:1.7;'>{job['description']}</div>", unsafe_allow_html=True)

        # Industry & Tips
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:{TEXT_MUTED}; margin:14px 0 6px; padding-bottom:4px; border-bottom:1px solid {BORDER};'>How to Apply</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:11px; color:{TEXT_SECONDARY}; line-height:1.6;'>Visit the company careers page below. Search for <b style=\"color:{ACCENT1};\">{selected_role}</b> in their job listings. Tailor your CV to match the skills listed above. Many roles accept applications via LinkedIn Easy Apply as well.</div>", unsafe_allow_html=True)

        # Search button
        st.markdown(f"<a href='{job['apply_url']}' target='_blank' style='display:block; width:100%; padding:12px; border-radius:8px; background:linear-gradient(135deg,{ACCENT1},{ACCENT2}); color:#05070D; font-size:13px; font-weight:700; text-align:center; text-decoration:none; margin-top:16px;'>Search Now →</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{job['website']}' target='_blank' style='display:block; text-align:center; margin-top:8px; font-size:11px; color:{ACCENT1}; text-decoration:none; font-weight:500;'>Visit {job['company']} Website ↗</a>", unsafe_allow_html=True)

        # Quick links to search this role on major boards
        role_q = selected_role.replace(" ", "+")
        st.markdown(f"<div style='font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:{TEXT_MUTED}; margin:16px 0 6px; padding-bottom:4px; border-bottom:1px solid {BORDER};'>Also Search On</div>", unsafe_allow_html=True)
        quick_links = [
            ("Indeed", f"https://uk.indeed.com/jobs?q={role_q}"),
            ("LinkedIn", f"https://www.linkedin.com/jobs/search/?keywords={role_q}"),
            ("Reed", f"https://www.reed.co.uk/jobs/{selected_role.replace(' ','-').lower()}-jobs"),
            ("Totaljobs", f"https://www.totaljobs.com/jobs/{selected_role.replace(' ','-').lower()}"),
        ]
        ql_html = " ".join([f"<a href='{url}' target='_blank' style='display:inline-block; font-size:9px; padding:3px 8px; border-radius:5px; background:rgba({','.join(str(int(ACCENT1.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.10); color:{ACCENT1}; text-decoration:none; font-weight:500; margin:2px;'>{name}</a>" for name, url in quick_links])
        st.markdown(f"<div>{ql_html}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align:center; padding:40px 0; color:{TEXT_MUTED};'>📭 No jobs match filters</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align:center; padding:20px 0 10px; font-size:10px; color:{TEXT_MUTED}; border-top:1px solid {BORDER}; margin-top:16px;">
    <span style="color:{ACCENT1}; font-weight:600;">ALMA</span> — Built by Collins Lemeke @ AI Nexus, UGM — Data: Adzuna · Jooble · JSearch · USAJobs
</div>
""", unsafe_allow_html=True)