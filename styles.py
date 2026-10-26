CSS = """
<style>
    .stApp { background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%); }
    .hero { background: linear-gradient(135deg, #1e3a8a 0%, #2b6cb0 100%); color: #fff; padding: 2.2rem 2.4rem; border-radius: 18px; margin-bottom: 1.4rem; }
    .hero h1 { margin: 0 0 .35rem 0; font-size: 2.1rem; font-weight: 800; }
    .hero p { margin: 0; opacity: .92; font-size: 1.02rem; }
    .banner { background: #fff7ed; border-left: 6px solid #c05621; color: #7c2d12; padding: .9rem 1.1rem; border-radius: 10px; font-size: .95rem; margin: .4rem 0 1.2rem 0; }
    .metric-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 1rem 1.2rem; box-shadow: 0 1px 3px rgba(15,23,42,.05); }
    .section-title { font-weight: 700; color: #1e293b; margin-top: 1.2rem; margin-bottom: .4rem; font-size: 1.15rem; }
    .footer { text-align: center; color: #64748b; font-size: .85rem; margin-top: 2.5rem; }
</style>
"""

HERO = """<div class="hero"><h1>🌍 Hosting the Displaced</h1><p>Absolute numbers versus capacity · 1951-2025 · UNHCR · World Bank · UCDP/PRIO · DHS</p></div>"""

BANNER = """<div class="banner"> <b>Policy brief, not a live indicator.</b> Static snapshot (2026-07-31). UNHCR registered counts and DHS modelled estimates are never combined here.</div>"""

def section_title(text):
    return '<div class="section-title">' + text + '</div>'

def metric_card_html(title, value, note):
    return (
        '<div class="metric-card">'
        '<div style="font-size:.75rem;color:#64748b;letter-spacing:.04em;text-transform:uppercase;">' + title + '</div>'
        '<div style="font-size:1.7rem;font-weight:800;color:#1e3a8a;margin:.2rem 0;">' + str(value) + '</div>'
        '<div style="font-size:.78rem;color:#64748b;">' + note + '</div>'
        '</div>'
    )

def so_what_html(year, overlap):
    return (
        '<div class="metric-card" style="margin-top:1rem;">'
        '<b>So what for UNHCR.</b> In ' + str(year) + ', the top-10 absolute hosts and the top-10 '
        'per-capita hosts overlapped in <b>' + str(overlap) + '</b> countries. Absolute hosting '
        'rewards large economies and geographic proximity to crises. Per-capita hosting reveals '
        'small states carrying a load many multiples of the global median per resident. '
        'Drag the year or threshold slider - the asymmetry persists across both.'
        '</div>'
    )

def footer_html(author, snapshot):
    return '<div class="footer">Hosting the Displaced · ' + author + ' · Data: UNHCR · World Bank · UCDP/PRIO · DHS · snapshot ' + snapshot + '</div>'
