from theme import get_theme

def load_css():
    t = get_theme()
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

    #MainMenu, footer, header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}
    .block-container {{
        padding-top: 3rem;
        padding-bottom: 6rem;
        max-width: 720px;
    }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background-color: {t['bg_primary']};
        color: {t['text_primary']};
    }}
    .stApp {{ background-color: {t['bg_primary']}; }}

    /* ---------- LOGO ---------- */
    .zen-logo {{
        font-family: 'Instrument Serif', serif;
        font-size: 32px;
        letter-spacing: -0.01em;
        color: {t['text_primary']};
        line-height: 1;
    }}
    .zen-logo span {{ color: {t['accent']}; }}

    /* ---------- NAV LINKS ---------- */
  .zen-nav-links {{
    display: flex;
    gap: 1.5rem;
    font-size: 14px;
    color: {t['text_secondary']};
    align-items: center;
    justify-content: flex-end;
    height: 40px;
    padding-bottom: 4px;
}}

    /* ---------- HERO ---------- */
    .zen-eyebrow {{
        font-size: 13px; color: {t['text_muted']};
        text-transform: uppercase; letter-spacing: 0.08em;
        margin-bottom: 0.75rem;
    }}
    .zen-hero {{
        font-family: 'Instrument Serif', serif;
        font-size: 44px; font-weight: 400; line-height: 1.1;
        color: {t['text_primary']};
        margin-bottom: 2.5rem;
        letter-spacing: -0.02em;
    }}

    /* ---------- TEXTAREA ---------- */
    .stTextArea textarea {{
        background-color: {t['bg_surface']} !important;
        border: 1px solid {t['border']} !important;
        border-radius: 12px !important;
        color: {t['text_primary']} !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important; line-height: 1.7 !important;
        padding: 1.25rem !important;
        min-height: 200px;
        transition: border-color 0.2s ease;
    }}
    .stTextArea textarea:focus {{
        border-color: {t['accent']} !important;
        box-shadow: 0 0 0 3px {t['accent']}20 !important;
    }}
    .stTextArea label {{ display: none; }}

    /* ---------- DEFAULT BUTTON (Save Entry) ---------- */
    .stButton > button {{
        background-color: {t['accent']} !important;
        color: {t['accent_text']} !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.65rem 1.5rem !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        transition: all 0.15s ease !important;
    }}
    .stButton > button:hover {{
        background-color: {t['accent_hover']} !important;
        transform: translateY(-1px);
    }}

    /* ---------- THEME TOGGLE BUTTON (overrides default) ---------- */
    .st-key-theme_btn button {{
        background-color: transparent !important;
        color: {t['text_primary']} !important;
        border: 1px solid {t['border']} !important;
        border-radius: 999px !important;
        width: 40px !important;
        height: 40px !important;
        min-height: 40px !important;
        padding: 0 !important;
        font-size: 16px !important;
        line-height: 1 !important;
        box-shadow: none !important;
        margin-top: 10px !important;
    }}
    .st-key-theme_btn button:hover {{
        background-color: {t['bg_elevated']} !important;
        border-color: {t['accent']} !important;
        color: {t['accent']} !important;
        transform: none !important;
    }}
    .st-key-theme_btn button:focus,
    .st-key-theme_btn button:active,
    .st-key-theme_btn button:focus-visible {{
        box-shadow: none !important;
        outline: none !important;
    }}

    /* ---------- SECTIONS ---------- */
    .zen-section {{
        margin-top: 5rem; padding-top: 2.5rem;
        border-top: 1px solid {t['border']};
    }}
    .zen-section-label {{
        font-size: 13px; color: {t['text_muted']};
        text-transform: uppercase; letter-spacing: 0.08em;
        margin-bottom: 1.5rem;
        display: flex; justify-content: space-between;
    }}

    /* ---------- ENTRY LIST ---------- */
    .entry-item {{
        padding: 1.25rem 0;
        border-bottom: 1px solid {t['border']};
    }}
    .entry-meta {{
        display: flex; align-items: center; gap: 0.75rem;
        font-size: 13px; color: {t['text_muted']};
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 0.5rem;
    }}
    .entry-dot {{
        width: 6px; height: 6px; border-radius: 50%;
        display: inline-block;
    }}
    .dot-positive {{ background: {t['mood_pos']}; }}
    .dot-neutral  {{ background: {t['mood_neu']}; }}
    .dot-negative {{ background: {t['mood_neg']}; }}
    .entry-text {{
        font-size: 15px; color: {t['text_secondary']}; line-height: 1.6;
    }}

    /* ---------- PILLS ---------- */
    .pill-cloud {{ display: flex; flex-wrap: wrap; gap: 0.5rem; }}
    .pill {{
        padding: 0.4rem 0.9rem; border-radius: 999px;
        background: {t['bg_surface']};
        border: 1px solid {t['border']};
        color: {t['text_secondary']};
        font-size: 13px;
    }}
    .pill-lg {{ font-size: 16px; color: {t['text_primary']}; padding: 0.55rem 1.1rem; }}
    .pill-md {{ font-size: 14px; }}

    /* ---------- ANIMATIONS ---------- */
    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(8px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .zen-hero, .zen-eyebrow, .stTextArea, .zen-section {{
        animation: fadeUp 0.6s ease-out backwards;
    }}
    .zen-eyebrow {{ animation-delay: 0.05s; }}
    .zen-hero    {{ animation-delay: 0.15s; }}
    .stTextArea  {{ animation-delay: 0.25s; }}
    </style>
    """