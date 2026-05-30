import streamlit as st
from styles import load_css
from theme import get_theme

st.set_page_config(page_title="ZenJournal — Write. Reflect. Grow.",
                   layout="wide", initial_sidebar_state="collapsed")
st.markdown(load_css(), unsafe_allow_html=True)
t = get_theme()

st.markdown(f"""
<style>
.block-container {{ max-width: 1100px; padding-top: 2rem; }}
.landing-hero {{ text-align: center; padding: 6rem 0 4rem 0; }}
.landing-eyebrow {{
    display: inline-block; padding: 0.4rem 0.9rem; border-radius: 999px;
    background: {t['bg_surface']}; border: 1px solid {t['border']};
    color: {t['text_secondary']}; font-size: 13px; margin-bottom: 2rem;
}}
.landing-headline {{
    font-family: 'Instrument Serif', serif; font-size: 84px;
    line-height: 1.0; letter-spacing: -0.03em;
    color: {t['text_primary']}; margin-bottom: 1.5rem;
}}
.landing-headline em {{ color: {t['accent']}; font-style: italic; }}
.landing-sub {{
    font-size: 19px; color: {t['text_secondary']};
    max-width: 560px; margin: 0 auto 2.5rem auto; line-height: 1.5;
}}
.landing-cta-row {{ display: flex; justify-content: center; gap: 1rem; }}
.btn-primary {{
    background: {t['accent']}; color: {t['accent_text']};
    padding: 0.85rem 1.6rem; border-radius: 8px;
    font-weight: 500; text-decoration: none; font-size: 15px;
    display: inline-block; transition: all 0.15s ease;
}}
.btn-primary:hover {{ background: {t['accent_hover']}; transform: translateY(-1px); }}
.btn-ghost {{
    background: transparent; color: {t['text_primary']};
    padding: 0.85rem 1.6rem; border-radius: 8px;
    border: 1px solid {t['border']};
    font-weight: 500; text-decoration: none; font-size: 15px;
}}
.social-proof {{
    text-align: center; color: {t['text_muted']}; font-size: 13px;
    text-transform: uppercase; letter-spacing: 0.08em;
    padding: 3rem 0; border-top: 1px solid {t['border']};
    border-bottom: 1px solid {t['border']}; margin: 3rem 0 6rem 0;
}}
.feature-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }}
.feature-card {{
    padding: 2rem; background: {t['bg_surface']};
    border: 1px solid {t['border']}; border-radius: 16px;
    transition: transform 0.2s ease;
}}
.feature-card:hover {{ transform: translateY(-4px); }}
.feature-icon {{
    width: 40px; height: 40px; background: {t['accent']}20;
    color: {t['accent']}; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 1.25rem; font-size: 20px;
}}
.feature-title {{
    font-family: 'Instrument Serif', serif;
    font-size: 24px; color: {t['text_primary']}; margin-bottom: 0.5rem;
}}
.feature-desc {{ color: {t['text_secondary']}; font-size: 14px; line-height: 1.6; }}
.quote {{ text-align: center; padding: 6rem 0; max-width: 700px; margin: 0 auto; }}
.quote-text {{
    font-family: 'Instrument Serif', serif; font-size: 32px;
    line-height: 1.4; color: {t['text_primary']}; margin-bottom: 1.5rem;
}}
.quote-author {{ color: {t['text_muted']}; font-size: 14px; }}
.footer-cta {{ text-align: center; padding: 8rem 0; border-top: 1px solid {t['border']}; }}
.footer-cta h2 {{
    font-family: 'Instrument Serif', serif; font-size: 64px;
    line-height: 1.05; letter-spacing: -0.02em; margin-bottom: 2rem;
}}
.footer-bar {{
    border-top: 1px solid {t['border']}; padding: 2rem 0;
    display: flex; justify-content: space-between;
    color: {t['text_muted']}; font-size: 13px;
}}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="zen-nav">
  <div class="zen-logo">Zen<span>Journal</span></div>
  <div class="zen-nav-links">
    <span>Features</span><span>Pricing</span><span>Sign in</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="landing-hero">
  <div class="landing-eyebrow">✦ Now with sentiment timeline</div>
  <div class="landing-headline">A journal that<br><em>listens back.</em></div>
  <div class="landing-sub">
    ZenJournal turns your daily writing into gentle insights —
    so you understand your patterns, not just record them.
  </div>
  <div class="landing-cta-row">
    <a href="#" class="btn-primary">Start writing — free</a>
    <a href="#" class="btn-ghost">Watch demo</a>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="social-proof">Trusted by 4,200+ writers, students, and quiet thinkers</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">✎</div>
    <div class="feature-title">Write</div>
    <div class="feature-desc">A distraction-free space designed like paper. No formatting toolbars. Just you and the page.</div>
  </div>
  <div class="feature-card">
    <div class="feature-icon">◐</div>
    <div class="feature-title">Reflect</div>
    <div class="feature-desc">Watch your mood evolve over weeks. Discover themes you didn't know were on your mind.</div>
  </div>
  <div class="feature-card">
    <div class="feature-icon">↗</div>
    <div class="feature-title">Grow</div>
    <div class="feature-desc">Weekly AI summaries surface patterns gently — never prescriptive, always private.</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote">
  <div class="quote-text">
    "I've tried five journaling apps. This is the first one that
    actually made me want to come back the next day."
  </div>
  <div class="quote-author">— Maya R., writer</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-cta">
  <h2>Start your<br>practice today.</h2>
  <a href="#" class="btn-primary">Open ZenJournal</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-bar">
  <span>© 2025 ZenJournal</span>
  <span>Privacy · Terms · Contact</span>
</div>
""", unsafe_allow_html=True)