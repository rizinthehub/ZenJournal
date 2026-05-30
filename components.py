def animated_logo(size=120, accent="#A8C5A0", text_color="#EDEDED", show_wordmark=True):
    wordmark = f"""
    <text x="155" y="78" font-family="Instrument Serif, serif"
          font-size="42" fill="{text_color}" class="zen-wordmark">
      Zen<tspan fill="{accent}">Journal</tspan>
    </text>
    """ if show_wordmark else ""

    return f"""
    <div style="display:flex; justify-content:center; padding:2rem 0;">
    <svg width="{size*3 if show_wordmark else size}" height="{size}"
         viewBox="0 0 450 120" xmlns="http://www.w3.org/2000/svg">

      <path d="M 30 30 L 110 30 L 35 95 L 115 95"
            stroke="{accent}" stroke-width="6"
            stroke-linecap="round" stroke-linejoin="round"
            fill="none" class="zen-stroke" />

      <path d="M 110 90 Q 130 75 125 60 Q 115 78 110 90 Z"
            fill="{accent}" class="zen-leaf" opacity="0" />

      {wordmark}

      <style>
        .zen-stroke {{
          stroke-dasharray: 320;
          stroke-dashoffset: 320;
          animation: drawZ 1.4s ease-out forwards;
        }}
        .zen-leaf {{
          transform-origin: 117px 80px;
          animation: bloomLeaf 0.6s ease-out 1.3s forwards;
        }}
        .zen-wordmark {{
          opacity: 0;
          animation: fadeWord 0.8s ease-out 1.5s forwards;
        }}
        @keyframes drawZ {{
          to {{ stroke-dashoffset: 0; }}
        }}
        @keyframes bloomLeaf {{
          0%   {{ opacity: 0; transform: scale(0) rotate(-30deg); }}
          60%  {{ opacity: 1; transform: scale(1.1) rotate(5deg); }}
          100% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
        }}
        @keyframes fadeWord {{
          from {{ opacity: 0; transform: translateX(-4px); }}
          to   {{ opacity: 1; transform: translateX(0); }}
        }}
      </style>
    </svg>
    </div>
    """