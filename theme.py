import streamlit as st

THEMES = {
    "dark": {
        "bg_primary": "#0F0F11",
        "bg_surface": "#17171A",
        "bg_elevated": "#1F1F23",
        "border": "#26262B",
        "text_primary": "#EDEDED",
        "text_secondary": "#A1A1A6",
        "text_muted": "#6E6E73",
        "accent": "#A8C5A0",
        "accent_hover": "#B9D2B1",
        "accent_text": "#0F0F11",
        "mood_pos": "#7FB069",
        "mood_neu": "#C9B380",
        "mood_neg": "#C77B7B",
        "chart_gradient_end": "#0F0F11",
    },
    "light": {
        "bg_primary": "#FAF9F6",
        "bg_surface": "#FFFFFF",
        "bg_elevated": "#F2F0EB",
        "border": "#E8E5DE",
        "text_primary": "#1A1A1A",
        "text_secondary": "#52525B",
        "text_muted": "#8A8A93",
        "accent": "#6B8E5A",
        "accent_hover": "#5A7A4B",
        "accent_text": "#FFFFFF",
        "mood_pos": "#5A8A47",
        "mood_neu": "#A88B4A",
        "mood_neg": "#A85A5A",
        "chart_gradient_end": "#FAF9F6",
    }
}

def get_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    return THEMES[st.session_state.theme]

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"