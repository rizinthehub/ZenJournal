import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
from collections import Counter
import re

from styles import load_css
from theme import get_theme, toggle_theme
from backend import MoodAI

# ---------- CONFIG ----------
st.set_page_config(page_title="ZenJournal", layout="centered", initial_sidebar_state="collapsed")
st.markdown(load_css(), unsafe_allow_html=True)

t = get_theme()
app_logic = MoodAI()

# ---------- HEADER ----------
icon = "☾" if st.session_state.get("theme", "dark") == "dark" else "☀"

col_logo, col_nav, col_btn = st.columns([3, 3, 1], vertical_alignment="center")

with col_logo:
    st.markdown('<div class="zen-logo">Zen<span>Journal</span></div>', unsafe_allow_html=True)

with col_nav:
    st.markdown(
        '<div class="zen-nav-links" style="justify-content:flex-end;">'
        '<span>Today</span><span>Insights</span><span>Archive</span></div>',
        unsafe_allow_html=True
    )

with col_btn:
    if st.button(icon, key="theme_btn"):
        toggle_theme()
        st.rerun()

st.markdown(f'<div style="border-bottom:1px solid {t["border"]}; margin: 1rem 0 3rem 0;"></div>',
            unsafe_allow_html=True)

# ---------- HERO ----------
now = datetime.now()
greeting = "Good morning" if now.hour < 12 else "Good afternoon" if now.hour < 18 else "Good evening"
st.markdown(f"""
<div class="zen-eyebrow">{now.strftime('%A, %d %B')}</div>
<div class="zen-hero">{greeting}. What's on your mind?</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
entry = st.text_area("entry", placeholder="Start writing...", label_visibility="collapsed")
col1, col2 = st.columns([3, 1])
with col2:
    save = st.button("Save entry  →", key="save_btn")

if save and entry:
    score, label = app_logic.analyze_entry(entry)
    app_logic.save_entry(entry, score, label)
    st.toast("Entry saved", icon="✓")
    st.rerun()

# ---------- LOAD DATA ----------
try:
    data = app_logic.load_data()
    if not data.empty:
        data['Date'] = pd.to_datetime(data['Date'])
        has_data = True
    else:
        has_data = False
except Exception:
    has_data = False

# ---------- MOOD CHART ----------
if has_data:
    st.markdown('<div class="zen-section"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="zen-section-label">
      <span>Mood over time</span><span>Last 30 days</span>
    </div>
    """, unsafe_allow_html=True)

    chart_data = data[['Date', 'Mood_Score']].tail(30).rename(columns={'Mood_Score': 'Mood'})

    chart = (
        alt.Chart(chart_data)
        .mark_area(
            line={"color": t['accent'], "strokeWidth": 2},
            color=alt.Gradient(
                gradient="linear",
                stops=[alt.GradientStop(color=t['accent'], offset=0),
                       alt.GradientStop(color=t['chart_gradient_end'], offset=1)],
                x1=1, x2=1, y1=1, y2=0
            ),
            interpolate="monotone"
        )
        .encode(
            x=alt.X("Date:T", axis=alt.Axis(labelColor=t['text_muted'], domain=False,
                                            ticks=False, title=None, grid=False)),
            y=alt.Y("Mood:Q", axis=alt.Axis(labelColor=t['text_muted'], domain=False,
                                            ticks=False, title=None, grid=False)),
        )
        .properties(height=200, background="transparent")
        .configure_view(strokeWidth=0)
    )
    st.altair_chart(chart, width='stretch')

# ---------- THEMES (Pills from real data) ----------
if has_data:
    st.markdown('<div class="zen-section"></div>', unsafe_allow_html=True)
    st.markdown('<div class="zen-section-label"><span>Themes this month</span></div>',
                unsafe_allow_html=True)

    stopwords = {"the", "is", "a", "and", "to", "of", "in", "it", "i", "im", "i'm",
                 "for", "on", "with", "this", "that", "was", "but", "my", "me",
                 "you", "have", "had", "be", "are", "as", "at", "an", "so", "if",
                 "do", "did", "not", "no", "yes", "we", "or", "from", "by", "all"}

    all_text = " ".join(data['Entry'].astype(str)).lower()
    words = re.findall(r'\b[a-z]{3,}\b', all_text)
    filtered = [w for w in words if w not in stopwords]

    if filtered:
        top_words = Counter(filtered).most_common(10)
        max_count = top_words[0][1]

        pills_html = '<div class="pill-cloud">'
        for word, count in top_words:
            ratio = count / max_count
            if ratio > 0.7:
                size = "lg"
            elif ratio > 0.4:
                size = "md"
            else:
                size = ""
            cls = f"pill pill-{size}" if size else "pill"
            pills_html += f'<span class="{cls}">{word}</span>'
        pills_html += '</div>'
        st.markdown(pills_html, unsafe_allow_html=True)

# ---------- RECENT ENTRIES ----------
if has_data:
    st.markdown('<div class="zen-section"></div>', unsafe_allow_html=True)
    st.markdown('<div class="zen-section-label"><span>Recent entries</span></div>',
                unsafe_allow_html=True)

    recent = data.sort_values(by='Date', ascending=False).head(5)
    for _, row in recent.iterrows():
        date_str = row['Date'].strftime("%b %d · %I:%M %p")
        mood = row['Sentiment']
        text_preview = row['Entry'][:120] + ("..." if len(row['Entry']) > 120 else "")
        st.markdown(f"""
        <div class="entry-item">
          <div class="entry-meta">
            <span class="entry-dot dot-{mood}"></span>{date_str} · <span style="color:{t['text_muted']}">{mood}</span>
          </div>
          <div class="entry-text">{text_preview}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown(f'<div style="color:{t["text_muted"]}; text-align:center; padding:3rem 0; font-size:14px;">Write your first entry above to see insights.</div>',
                unsafe_allow_html=True)