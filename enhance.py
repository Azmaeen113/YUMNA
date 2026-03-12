import re

with open(r'f:\E\Downloads\YUMNA\oshudh-ki-boss.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════════════════════════
# 1. ADD FLATICON CDN LINKS IN HEAD
# ══════════════════════════════════════════════════════════════════════
flaticon_css = """<link rel='stylesheet' href='https://cdn-uicons.flaticon.com/2.6.0/uicons-regular-rounded/css/uicons-regular-rounded.css'>
<link rel='stylesheet' href='https://cdn-uicons.flaticon.com/2.6.0/uicons-solid-rounded/css/uicons-solid-rounded.css'>
<link rel='stylesheet' href='https://cdn-uicons.flaticon.com/2.6.0/uicons-bold-rounded/css/uicons-bold-rounded.css'>"""

content = content.replace(
    """<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,300&display=swap" rel="stylesheet">""",
    """<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,300&display=swap" rel="stylesheet">
""" + flaticon_css
)

# ══════════════════════════════════════════════════════════════════════
# 2. ADD NEW CSS - lang-flag, both-subtitle, icon styling  
# ══════════════════════════════════════════════════════════════════════
new_css = """
/* ── LANGUAGE FLAGS ── */
.lang-flag {
  width: 20px;
  height: 14px;
  border-radius: 3px;
  object-fit: cover;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

/* ── BILINGUAL (BOTH) MODE ── */
.both-subtitle {
  display: block;
  font-size: 0.75em;
  color: rgba(0,0,0,0.45);
  font-weight: 400;
  font-family: var(--font-body);
  margin-top: 2px;
  line-height: 1.4;
}
.warning-banner .both-subtitle,
.med-card-stat .both-subtitle,
.mission-card .both-subtitle,
footer .both-subtitle {
  color: rgba(255,255,255,0.4);
}

/* ── FLATICON ICON STYLING ── */
.nav-links a i.fi,
.mobile-menu a i.fi {
  font-size: 15px;
  vertical-align: middle;
  margin-right: 2px;
}
.section-tag i.fi {
  font-size: 14px;
  vertical-align: middle;
}
.hero-card-icon i.fi {
  font-size: 36px;
}
.med-icon-wrap i.fi {
  font-size: 28px;
}
.tip-icon i.fi {
  font-size: 40px;
}
.storage-icon i.fi {
  font-size: 28px;
}
.med-card-stat-icon i.fi {
  font-size: 20px;
  color: var(--yellow);
}
.btn-primary i.fi,
.btn-secondary i.fi {
  font-size: 16px;
  vertical-align: middle;
}
.strip-item i.fi {
  font-size: 14px;
  color: var(--yellow);
}
.risk-chip i.fi {
  font-size: 12px;
}
.med-tips-title i.fi {
  font-size: 14px;
  color: var(--green);
}
.faq-badge i.fi {
  font-size: 11px;
}
.dos-donts-title i.fi {
  font-size: 22px;
}
.contact-icon i.fi {
  font-size: 18px;
}
.badge-icon i.fi {
  font-size: 48px;
  color: var(--black);
}
.founder-avatar i.fi {
  font-size: 28px;
}
.warning-banner .icon i.fi {
  font-size: 24px;
  color: var(--yellow);
}
.pill-float i.fi {
  font-size: inherit;
  opacity: inherit;
}
.hero-card-badge i.fi {
  font-size: 11px;
}
"""

content = content.replace(
    "/* ── PAGE TRANSITION ── */",
    new_css + "\n/* ── PAGE TRANSITION ── */"
)

# ══════════════════════════════════════════════════════════════════════
# 3. FIX BANGLA FONT INCONSISTENCY
# ══════════════════════════════════════════════════════════════════════

# .stat-num
content = content.replace(
    """  font-size: 26px; font-weight: 800; color: var(--black);
  font-family: var(--font-display); line-height: 1;""",
    """  font-size: 26px; font-weight: 800; color: var(--black);
  font-family: var(--font-bn); line-height: 1;"""
)

# .section-tag
content = content.replace(
    """  font-size: 12px; font-weight: 700; margin-bottom: 16px;
  border: 1px solid var(--yellow); text-transform: uppercase; letter-spacing: 0.5px;
  font-family: var(--font-display);""",
    """  font-size: 12px; font-weight: 700; margin-bottom: 16px;
  border: 1px solid var(--yellow); text-transform: uppercase; letter-spacing: 0.5px;
  font-family: var(--font-bn);"""
)

# .rule-num
content = content.replace(
    """  justify-content: center; font-weight: 800; font-size: 20px;
  color: var(--black); flex-shrink: 0;
  font-family: var(--font-display);""",
    """  justify-content: center; font-weight: 800; font-size: 20px;
  color: var(--black); flex-shrink: 0;
  font-family: var(--font-bn);"""
)

# .med-tips-title
content = content.replace(
    """  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.5px; color: var(--black); margin-bottom: 8px;
  font-family: var(--font-display);""",
    """  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.5px; color: var(--black); margin-bottom: 8px;
  font-family: var(--font-bn);"""
)

# .med-card-category  
content = content.replace(
    """  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.5px; margin-bottom: 4px; font-family: var(--font-display);""",
    """  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.5px; margin-bottom: 4px; font-family: var(--font-bn);"""
)

# ══════════════════════════════════════════════════════════════════════
# 4. REPLACE FLAG IMAGES
# ══════════════════════════════════════════════════════════════════════
content = content.replace(
    '<img src="https://flagcdn.com/w20/bd.png" alt="BD">',
    '<img src="bangladesh.png" alt="Bangla" class="lang-flag">'
)
content = content.replace(
    '<img src="https://flagcdn.com/w20/gb.png" alt="EN">',
    '<img src="united-kingdom.png" alt="English" class="lang-flag">'
)

# ══════════════════════════════════════════════════════════════════════
# 5. REPLACE ALL EMOJIS WITH FLATICON ICONS
# ══════════════════════════════════════════════════════════════════════

# --- NAVBAR ---
content = content.replace(
    '''<li><a onclick="showPage('home')" id="nav-home" class="active">🏠 <span id="n-home">হোম</span></a></li>''',
    '''<li><a onclick="showPage('home')" id="nav-home" class="active"><i class="fi fi-rr-home"></i> <span id="n-home">হোম</span></a></li>'''
)

# --- MOBILE MENU ---
content = content.replace(
    '''<a onclick="showPage('home');toggleMenu()">🏠 <span id="mn-home">হোম</span></a>''',
    '''<a onclick="showPage('home');toggleMenu()"><i class="fi fi-rr-home"></i> <span id="mn-home">হোম</span></a>'''
)
content = content.replace(
    '''<a onclick="showPage('medicines');toggleMenu()"><span id="mn-med">💊 ওষুধ সমূহ</span></a>''',
    '''<a onclick="showPage('medicines');toggleMenu()"><i class="fi fi-rr-capsule"></i> <span id="mn-med">ওষুধ সমূহ</span></a>'''
)
content = content.replace(
    '''<a onclick="showPage('expiry');toggleMenu()"><span id="mn-exp">📅 মেয়াদ ও সংরক্ষণ</span></a>''',
    '''<a onclick="showPage('expiry');toggleMenu()"><i class="fi fi-rr-calendar"></i> <span id="mn-exp">মেয়াদ ও সংরক্ষণ</span></a>'''
)
content = content.replace(
    '''<a onclick="showPage('safety');toggleMenu()"><span id="mn-safe">🛡️ নিরাপত্তা টিপস</span></a>''',
    '''<a onclick="showPage('safety');toggleMenu()"><i class="fi fi-rr-shield-check"></i> <span id="mn-safe">নিরাপত্তা টিপস</span></a>'''
)
content = content.replace(
    '''<a onclick="showPage('faq');toggleMenu()">❓ FAQ</a>''',
    '''<a onclick="showPage('faq');toggleMenu()"><i class="fi fi-rr-interrogation"></i> FAQ</a>'''
)
content = content.replace(
    '''<a onclick="showPage('about');toggleMenu()"><span id="mn-about">ℹ️ আমাদের সম্পর্কে</span></a>''',
    '''<a onclick="showPage('about');toggleMenu()"><i class="fi fi-rr-info"></i> <span id="mn-about">আমাদের সম্পর্কে</span></a>'''
)

# Nav FAQ link (desktop)
content = content.replace(
    '''<li><a onclick="showPage('faq')" id="nav-faq">FAQ</a></li>''',
    '''<li><a onclick="showPage('faq')" id="nav-faq"><i class="fi fi-rr-interrogation"></i> FAQ</a></li>'''
)

# Both mode button globe
content = content.replace(
    '''<span>🌐</span> <span>Both</span>''',
    '''<i class="fi fi-rr-globe" style="font-size:14px;"></i> <span>Both</span>'''
)

# --- HERO FLOATING PILLS ---
content = content.replace(
    '''<span class="pill-float" style="top:15%;left:8%;animation-duration:7s;">💊</span>''',
    '''<span class="pill-float" style="top:15%;left:8%;animation-duration:7s;"><i class="fi fi-rr-capsule"></i></span>'''
)
content = content.replace(
    '''<span class="pill-float" style="top:60%;left:5%;animation-duration:9s;">🩺</span>''',
    '''<span class="pill-float" style="top:60%;left:5%;animation-duration:9s;"><i class="fi fi-rr-stethoscope"></i></span>'''
)
content = content.replace(
    '''<span class="pill-float" style="top:25%;right:8%;animation-duration:6s;">⚕️</span>''',
    '''<span class="pill-float" style="top:25%;right:8%;animation-duration:6s;"><i class="fi fi-rr-cross"></i></span>'''
)
content = content.replace(
    '''<span class="pill-float" style="top:70%;right:12%;animation-duration:8s;">🏥</span>''',
    '''<span class="pill-float" style="top:70%;right:12%;animation-duration:8s;"><i class="fi fi-rr-hospital"></i></span>'''
)
content = content.replace(
    '''<span class="pill-float" style="top:45%;left:15%;animation-duration:11s;">💉</span>''',
    '''<span class="pill-float" style="top:45%;left:15%;animation-duration:11s;"><i class="fi fi-rr-syringe"></i></span>'''
)

# --- HERO CTA BUTTONS ---
content = content.replace(
    '''<button class="btn-primary" onclick="showPage('medicines')" id="cta-learn">💊 ওষুধ সম্পর্কে জানুন</button>''',
    '''<button class="btn-primary" onclick="showPage('medicines')" id="cta-learn"><i class="fi fi-rr-capsule"></i> <span>ওষুধ সম্পর্কে জানুন</span></button>'''
)
content = content.replace(
    '''<button class="btn-secondary" onclick="showPage('safety')" id="cta-tips">🛡️ নিরাপত্তা টিপস</button>''',
    '''<button class="btn-secondary" onclick="showPage('safety')" id="cta-tips"><i class="fi fi-rr-shield-check"></i> <span>নিরাপত্তা টিপস</span></button>'''
)

# --- HERO CARDS ---
content = content.replace(
    '''<div class="hero-card-icon">🦠</div>''',
    '''<div class="hero-card-icon"><i class="fi fi-rr-bacteria"></i></div>'''
)
content = content.replace(
    '''<div class="hero-card-icon">📋</div>''',
    '''<div class="hero-card-icon"><i class="fi fi-rr-document"></i></div>'''
)
content = content.replace(
    '''<span class="hero-card-badge">⚠️ Antibiotic Resistance</span>''',
    '''<span class="hero-card-badge"><i class="fi fi-sr-triangle-warning"></i> Antibiotic Resistance</span>'''
)
content = content.replace(
    '''<span class="hero-card-badge">📌 WHO Data</span>''',
    '''<span class="hero-card-badge"><i class="fi fi-rr-marker"></i> WHO Data</span>'''
)

# Warning banner
content = content.replace(
    '''<span class="icon">⚡</span>''',
    '''<span class="icon"><i class="fi fi-sr-bolt"></i></span>'''
)

# --- AWARENESS STRIP ---
# Replace strip dots (● → icon)
content = content.replace(
    '<span class="strip-dot">●</span>',
    '<i class="fi fi-sr-bullet" style="color:var(--yellow);font-size:8px;"></i>'
)

# --- SECTION TAGS ---
content = content.replace(
    '''<div class="section-tag">💊 <span id="mt-tag">ওষুধ তথ্য</span></div>''',
    '''<div class="section-tag"><i class="fi fi-rr-capsule"></i> <span id="mt-tag">ওষুধ তথ্য</span></div>'''
)
content = content.replace(
    '''<div class="section-tag">📅 <span id="et-tag">মেয়াদ ও সংরক্ষণ</span></div>''',
    '''<div class="section-tag"><i class="fi fi-rr-calendar"></i> <span id="et-tag">মেয়াদ ও সংরক্ষণ</span></div>'''
)
content = content.replace(
    '''<div class="section-tag">🛡️ <span id="st-tag">নিরাপত্তা</span></div>''',
    '''<div class="section-tag"><i class="fi fi-rr-shield-check"></i> <span id="st-tag">নিরাপত্তা</span></div>'''
)
content = content.replace(
    '''<div class="section-tag">❓ FAQ</div>''',
    '''<div class="section-tag"><i class="fi fi-rr-interrogation"></i> FAQ</div>'''
)
content = content.replace(
    '''<div class="section-tag">ℹ️ <span id="ab-tag">আমাদের সম্পর্কে</span></div>''',
    '''<div class="section-tag"><i class="fi fi-rr-info"></i> <span id="ab-tag">আমাদের সম্পর্কে</span></div>'''
)
content = content.replace(
    '''<div class="section-tag">📱 QR Code</div>''',
    '''<div class="section-tag"><i class="fi fi-rr-smartphone"></i> QR Code</div>'''
)

# --- MEDICINE CARD ICONS ---
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#FEE2E2;">🦠</div>''',
    '''<div class="med-icon-wrap" style="background:#FEE2E2;"><i class="fi fi-rr-bacteria" style="color:#991B1B;"></i></div>'''
)
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#EDE9FE;">😴</div>''',
    '''<div class="med-icon-wrap" style="background:#EDE9FE;"><i class="fi fi-rr-moon" style="color:#5B21B6;"></i></div>'''
)
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#D1FAE5;">🫃</div>''',
    '''<div class="med-icon-wrap" style="background:#D1FAE5;"><i class="fi fi-rr-heart-rate" style="color:#065F46;"></i></div>'''
)
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#FEF3C7;">🩹</div>''',
    '''<div class="med-icon-wrap" style="background:#FEF3C7;"><i class="fi fi-rr-band-aid" style="color:#92400E;"></i></div>'''
)
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#FCE7F3;">🌸</div>''',
    '''<div class="med-icon-wrap" style="background:#FCE7F3;"><i class="fi fi-rr-flower" style="color:#9D174D;"></i></div>'''
)
content = content.replace(
    '''<div class="med-icon-wrap" style="background:#DBEAFE;">🤧</div>''',
    '''<div class="med-icon-wrap" style="background:#DBEAFE;"><i class="fi fi-rr-head-side-cough" style="color:#1E40AF;"></i></div>'''
)

# --- RISK CHIPS ---
content = content.replace('<span class="risk-chip danger">⚠️ Resistant Bacteria</span>',
    '<span class="risk-chip danger"><i class="fi fi-sr-triangle-warning"></i> Resistant Bacteria</span>')
content = content.replace('<span class="risk-chip warn">🤢 পেট সমস্যা</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-face-unamused"></i> পেট সমস্যা</span>')
content = content.replace('<span class="risk-chip danger">🫘 Liver/Kidney ক্ষতি</span>',
    '<span class="risk-chip danger"><i class="fi fi-sr-triangle-warning"></i> Liver/Kidney ক্ষতি</span>')
content = content.replace('<span class="risk-chip danger">🔗 Addiction তৈরি</span>',
    '<span class="risk-chip danger"><i class="fi fi-rr-link-alt"></i> Addiction তৈরি</span>')
content = content.replace('<span class="risk-chip warn">💫 মাথা ঘোরা</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-dizzy"></i> মাথা ঘোরা</span>')
content = content.replace('<span class="risk-chip danger">🧠 স্মৃতিশক্তি হ্রাস</span>',
    '<span class="risk-chip danger"><i class="fi fi-rr-brain"></i> স্মৃতিশক্তি হ্রাস</span>')
content = content.replace('<span class="risk-chip warn">🦴 হাড় দুর্বল</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-bone"></i> হাড় দুর্বল</span>')
content = content.replace('<span class="risk-chip warn">🫘 Kidney সমস্যা</span>',
    '<span class="risk-chip warn"><i class="fi fi-sr-triangle-warning"></i> Kidney সমস্যা</span>')
content = content.replace('<span class="risk-chip info">💊 Vitamin শোষণে সমস্যা</span>',
    '<span class="risk-chip info"><i class="fi fi-rr-capsule"></i> Vitamin শোষণে সমস্যা</span>')
content = content.replace('<span class="risk-chip danger">🫀 Liver ক্ষতি (অতিরিক্তে)</span>',
    '<span class="risk-chip danger"><i class="fi fi-rr-heart"></i> Liver ক্ষতি (অতিরিক্তে)</span>')
content = content.replace('<span class="risk-chip warn">🤢 পেটের আলসার</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-face-unamused"></i> পেটের আলসার</span>')
content = content.replace('<span class="risk-chip info">🩸 Blood পাতলা হওয়া</span>',
    '<span class="risk-chip info"><i class="fi fi-rr-tint"></i> Blood পাতলা হওয়া</span>')
content = content.replace('<span class="risk-chip warn">🤢 বমি বমি ভাব (শুরুতে)</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-face-unamused"></i> বমি বমি ভাব (শুরুতে)</span>')
content = content.replace('<span class="risk-chip info">📅 Period পরিবর্তন</span>',
    '<span class="risk-chip info"><i class="fi fi-rr-calendar"></i> Period পরিবর্তন</span>')
content = content.replace('<span class="risk-chip warn">🩸 Blood clot (কদাচিৎ)</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-tint"></i> Blood clot (কদাচিৎ)</span>')
content = content.replace('<span class="risk-chip warn">😴 ঘুম ঘুম ভাব</span>',
    '<span class="risk-chip warn"><i class="fi fi-rr-moon"></i> ঘুম ঘুম ভাব</span>')
content = content.replace('<span class="risk-chip info">🫦 মুখ শুকিয়ে যাওয়া</span>',
    '<span class="risk-chip info"><i class="fi fi-rr-face-unamused"></i> মুখ শুকিয়ে যাওয়া</span>')
content = content.replace('<span class="risk-chip info">🚗 গাড়ি চালানো বিপদ</span>',
    '<span class="risk-chip info"><i class="fi fi-rr-car-side"></i> গাড়ি চালানো বিপদ</span>')

# --- MED TIPS TITLES ---
content = content.replace(
    '<div class="med-tips-title">✅ সঠিক ব্যবহার</div>',
    '<div class="med-tips-title"><i class="fi fi-sr-check-circle"></i> সঠিক ব্যবহার</div>'
)
content = content.replace(
    '<div class="med-tips-title">✅ সতর্কতা</div>',
    '<div class="med-tips-title"><i class="fi fi-sr-check-circle"></i> সতর্কতা</div>'
)
content = content.replace(
    '<div class="med-tips-title">✅ নিরাপদ ব্যবহার</div>',
    '<div class="med-tips-title"><i class="fi fi-sr-check-circle"></i> নিরাপদ ব্যবহার</div>'
)
content = content.replace(
    '<div class="med-tips-title">✅ সঠিক নিয়ম</div>',
    '<div class="med-tips-title"><i class="fi fi-sr-check-circle"></i> সঠিক নিয়ম</div>'
)
content = content.replace(
    '<div class="med-tips-title">✅ জানুন ও সতর্ক থাকুন</div>',
    '<div class="med-tips-title"><i class="fi fi-sr-check-circle"></i> জানুন ও সতর্ক থাকুন</div>'
)

# --- MED CARD STAT ICONS ---
content = content.replace(
    '<span class="med-card-stat-icon">📊</span>',
    '<span class="med-card-stat-icon"><i class="fi fi-rr-chart-histogram"></i></span>'
)

# --- EXPIRY SECTION ---
# Expiry tip card icons
content = content.replace(
    '<div class="tip-icon">🔍</div>',
    '<div class="tip-icon"><i class="fi fi-rr-search" style="color:var(--black);"></i></div>'
)
content = content.replace(
    '<div class="tip-icon">⚠️</div>',
    '<div class="tip-icon"><i class="fi fi-sr-triangle-warning" style="color:#991B1B;"></i></div>'
)
content = content.replace(
    '<div class="tip-icon">🗑️</div>',
    '<div class="tip-icon"><i class="fi fi-rr-trash" style="color:#065F46;"></i></div>'
)

# Expiry demo section icons
content = content.replace(
    '<div style="font-size:24px;">✅</div>',
    '<div style="font-size:24px;"><i class="fi fi-sr-check-circle" style="color:#22863A;"></i></div>'
)
content = content.replace(
    '<div style="font-size:24px;">❌</div>',
    '<div style="font-size:24px;"><i class="fi fi-sr-cross-circle" style="color:#E53E3E;"></i></div>'
)

# Storage icons  
content = content.replace(
    '<div class="storage-icon">🌡️</div>',
    '<div class="storage-icon"><i class="fi fi-rr-thermometer-half"></i></div>'
)
content = content.replace(
    '<div class="storage-icon">💧</div>',
    '<div class="storage-icon"><i class="fi fi-rr-raindrops"></i></div>'
)
content = content.replace(
    '<div class="storage-icon">👶</div>',
    '<div class="storage-icon"><i class="fi fi-rr-child-head"></i></div>'
)
content = content.replace(
    '<div class="storage-icon">❄️</div>',
    '<div class="storage-icon"><i class="fi fi-rr-snowflake"></i></div>'
)

# --- SAFETY SECTION ---
# Dos/donts titles
content = content.replace(
    '<div class="dos-donts-title">✅ <span id="dos-title">যা করবেন</span></div>',
    '<div class="dos-donts-title"><i class="fi fi-sr-check-circle" style="color:var(--green);"></i> <span id="dos-title">যা করবেন</span></div>'
)
content = content.replace(
    '<div class="dos-donts-title">❌ <span id="donts-title">যা করবেন না</span></div>',
    '<div class="dos-donts-title"><i class="fi fi-sr-cross-circle" style="color:var(--red);"></i> <span id="donts-title">যা করবেন না</span></div>'
)

# Do/Dont list icons
content = content.replace('<span class="do-icon">✓</span>', '<span class="do-icon"><i class="fi fi-sr-check"></i></span>')
content = content.replace('<span class="dont-icon">✗</span>', '<span class="dont-icon"><i class="fi fi-sr-cross"></i></span>')

# --- ABOUT SECTION ---
content = content.replace(
    '<div class="founder-avatar">👩‍⚕️</div>',
    '<div class="founder-avatar"><i class="fi fi-rr-stethoscope"></i></div>'
)
content = content.replace(
    '<span class="badge-icon">🏆</span>',
    '<span class="badge-icon"><i class="fi fi-rr-trophy"></i></span>'
)

# Contact icons
content = content.replace(
    '<span class="contact-icon">📧</span>',
    '<span class="contact-icon"><i class="fi fi-rr-envelope"></i></span>'
)
content = content.replace(
    '<span class="contact-icon">👩‍⚕️</span>',
    '<span class="contact-icon"><i class="fi fi-rr-user-md"></i></span>'
)
content = content.replace(
    '<span class="contact-icon">⚠️</span>',
    '<span class="contact-icon"><i class="fi fi-sr-triangle-warning"></i></span>'
)

# --- QR PAGE ---
content = content.replace(
    '''<h3 style="font-family:var(--font-bn);font-weight:700;font-size:20px;color:var(--yellow);margin-bottom:12px;" id="poster-head">📋 Poster Text</h3>''',
    '''<h3 style="font-family:var(--font-bn);font-weight:700;font-size:20px;color:var(--yellow);margin-bottom:12px;" id="poster-head"><i class="fi fi-rr-document" style="margin-right:6px;"></i> Poster Text</h3>'''
)
content = content.replace(
    '''<p style="font-family:var(--font-bn);font-size:18px;font-weight:700;color:var(--white);margin-bottom:8px;" id="poster-line1">💊 ওষুধ কিনছেন?</p>''',
    '''<p style="font-family:var(--font-bn);font-size:18px;font-weight:700;color:var(--white);margin-bottom:8px;" id="poster-line1"><i class="fi fi-rr-capsule" style="margin-right:4px;"></i> ওষুধ কিনছেন?</p>'''
)

# QR CTA button
content = content.replace(
    '''<button onclick="showPage('qr-page')" class="btn-primary" style="width:100%;justify-content:center;" id="qr-btn">📱 QR Code দেখুন</button>''',
    '''<button onclick="showPage('qr-page')" class="btn-primary" style="width:100%;justify-content:center;" id="qr-btn"><i class="fi fi-rr-smartphone"></i> QR Code দেখুন</button>'''
)

# Download and print buttons
content = content.replace(
    '''<button onclick="downloadQR()" class="btn-primary" id="dl-btn">⬇️ QR Download করুন</button>''',
    '''<button onclick="downloadQR()" class="btn-primary" id="dl-btn"><i class="fi fi-rr-download"></i> QR Download করুন</button>'''
)
content = content.replace(
    '''<button onclick="window.print()" class="btn-secondary" id="print-btn">🖨️ Print করুন</button>''',
    '''<button onclick="window.print()" class="btn-secondary" id="print-btn"><i class="fi fi-rr-print"></i> Print করুন</button>'''
)

# --- FOOTER ---
content = content.replace(
    '''<p class="footer-disclaimer" id="ft-disclaimer">⚠️ এই website শুধুমাত্র সচেতনতা বৃদ্ধির উদ্দেশ্যে তৈরি। চিকিৎসার জন্য সবসময় qualified doctor বা pharmacist-এর পরামর্শ নিন।</p>''',
    '''<p class="footer-disclaimer" id="ft-disclaimer"><i class="fi fi-sr-triangle-warning"></i> এই website শুধুমাত্র সচেতনতা বৃদ্ধির উদ্দেশ্যে তৈরি। চিকিৎসার জন্য সবসময় qualified doctor বা pharmacist-এর পরামর্শ নিন।</p>'''
)

# --- FAQ BADGES (in HTML) ---
content = content.replace(
    '<span class="faq-badge badge-danger">⚠️ Antibiotic</span>',
    '<span class="faq-badge badge-danger"><i class="fi fi-sr-triangle-warning"></i> Antibiotic</span>'
)
content = content.replace(
    '<span class="faq-badge badge-warn">💊 Painkiller</span>',
    '<span class="faq-badge badge-warn"><i class="fi fi-rr-capsule"></i> Painkiller</span>'
)
content = content.replace(
    '<span class="faq-badge badge-warn">🌸 Birth Pill</span>',
    '<span class="faq-badge badge-warn"><i class="fi fi-rr-flower"></i> Birth Pill</span>'
)
content = content.replace(
    '<span class="faq-badge badge-danger">⏰ Expiry</span>',
    '<span class="faq-badge badge-danger"><i class="fi fi-rr-alarm-clock"></i> Expiry</span>'
)
content = content.replace(
    '<span class="faq-badge badge-safe">💬 Generic</span>',
    '<span class="faq-badge badge-safe"><i class="fi fi-rr-comment-alt"></i> Generic</span>'
)
content = content.replace(
    '<span class="faq-badge badge-warn">😴 Sleeping Pill</span>',
    '<span class="faq-badge badge-warn"><i class="fi fi-rr-moon"></i> Sleeping Pill</span>'
)
content = content.replace(
    '<span class="faq-badge badge-safe">🫃 Gastric</span>',
    '<span class="faq-badge badge-safe"><i class="fi fi-rr-heart-rate"></i> Gastric</span>'
)
content = content.replace(
    '<span class="faq-badge badge-danger">🤧 Allergy</span>',
    '<span class="faq-badge badge-danger"><i class="fi fi-rr-head-side-cough"></i> Allergy</span>'
)

# ══════════════════════════════════════════════════════════════════════
# 6. REPLACE ENTIRE JS SECTION WITH ENHANCED VERSION
# ══════════════════════════════════════════════════════════════════════

old_js_start = "// ── Language toggle ───────────────────────────────────────────────────"
old_js_end = "</script>"

# Find the position of the language toggle section
js_start_idx = content.find(old_js_start)
js_end_idx = content.find(old_js_end, js_start_idx) + len(old_js_end)

new_js = r"""// ── Language toggle ───────────────────────────────────────────────────
const translations = {
  en: {
    'logo-text': 'Oshudh Ki Boss?',
    'logo-sub': 'Know Your Medicine, Gain Health',
    'n-home': 'Home', 'n-med': 'Medicines', 'n-exp': 'Expiry & Storage',
    'n-safe': 'Safety Tips', 'n-about': 'About Us',
    'mn-home': 'Home', 'mn-med': 'Medicines',
    'mn-exp': 'Expiry & Storage', 'mn-safe': 'Safety Tips',
    'mn-about': 'About Us',
    'hero-tag': 'For the working people of Bangladesh',
    'hero-title-main': 'Oshudh Ki Boss?',
    'hero-sub-bn': 'Know Your Medicine, Gain Health',
    'hero-sub-en': 'Empowering communities through medicine literacy',
    'stat1': 'Medicine without doctor', 'stat2': 'Deaths from AMR (2019)', 'stat3': 'Sleeping pill users',
    'cta-learn': '<i class="fi fi-rr-capsule"></i> <span>Learn About Medicines</span>',
    'cta-tips': '<i class="fi fi-rr-shield-check"></i> <span>Safety Tips</span>',
    'hc1-title': 'Antibiotic Resistance is Growing!',
    'hc1-text': 'Wrong use of antibiotics creates resistant bacteria. In the future, medicines stop working.',
    'hc2-title': 'No Medicine Without Prescription',
    'hc2-text': 'WHO says most medicine in Bangladesh is bought without a doctor\'s advice. This is extremely dangerous.',
    'warn-text': '<strong>Did you know?</strong> Taking medicine incorrectly can damage your liver, kidneys and other vital organs. Stay informed, stay healthy.',
    's1': 'Complete your full antibiotic course',
    's2': 'Check the expiry date before buying',
    's3': 'No sleeping pills without a doctor\'s prescription',
    's4': 'Never use someone else\'s medicine',
    's5': 'Keep medicines away from children',
    's1b': 'Complete your full antibiotic course',
    's2b': 'Check the expiry date before buying',
    's3b': 'No sleeping pills without a doctor\'s prescription',
    's4b': 'Never use someone else\'s medicine',
    's5b': 'Keep medicines away from children',
    'mt-tag': 'Medicine Info',
    'mt-title': 'Correct Use of Common Medicines',
    'mt-desc': 'Learn accurate information about each medicine \u2014 why to take it, how to take it, and when to be cautious.',
    'fa': 'All Medicines', 'fb': 'Antibiotics', 'fc': 'Sleeping Pills',
    'fd': 'Gastric', 'fe': 'Painkillers', 'ff': 'Birth Control',
    'm1-title': 'Antibiotics', 'm1-desc': 'Antibiotics are medicines that fight bacterial infections. But many people take antibiotics for colds or fever \u2014 this is wrong and dangerous. Antibiotics do not work on viruses.',
    'm1t1': 'Never take antibiotics without a doctor\'s prescription',
    'm1t2': 'Complete the full course \u2014 never stop halfway',
    'm1t3': 'Never use someone else\'s antibiotic',
    'm1t4': 'Taking with or after food reduces stomach upset',
    'm1-stat': 'In Bangladesh in 2019, <strong>26,200 people died due to AMR</strong> (Antibiotic Resistance). (WHO / The Business Standard)',
    'm2-title': 'Sleeping Pills',
    'm2-desc': 'Many people use sleeping pills for sleep problems. These are benzodiazepines \u2014 they should only be available with a doctor\'s prescription. They are addictive and affect memory long-term.',
    'm2t1': 'Never start on your own \u2014 Prescription is required',
    'm2t2': 'Do not drive or operate heavy machinery',
    'm2t3': 'Never with alcohol \u2014 extremely dangerous',
    'm2t4': 'Do not stop suddenly \u2014 reduce gradually with doctor\'s advice',
    'm2-stat': 'Approximately <strong>300,000 people in Bangladesh</strong> use sleeping pills or sedatives. (The Daily Star)',
    'm3-title': 'Gastric Medicine',
    'm3-desc': 'Gastric medicine is most commonly used in Bangladesh. These PPI medicines are better not taken long-term. See a doctor if needed.',
    'm3t1': 'Take 20-30 minutes before meals (on empty stomach)',
    'm3t2': 'Do not take without doctor for more than 8 weeks',
    'm3t3': 'Reduce spicy and fried foods',
    'm3t4': 'Do not eat just before sleeping',
    'm3-stat': 'Long-term use causes problems with <strong>Vitamin B12, Magnesium and Calcium</strong> absorption. (Banglajol Medical Journal)',
    'm4-title': 'Painkillers',
    'm4-desc': 'Painkillers are the most commonly used medicines. Paracetamol is generally safe, but in high doses damages the liver. Ibuprofen can cause stomach problems. Taking two painkillers together is dangerous.',
    'm4t1': 'For adults: maximum Paracetamol 500mg \u00d7 4 times daily',
    'm4t2': 'Take Ibuprofen with food \u2014 not on empty stomach',
    'm4t3': 'Do not take two painkillers together',
    'm4t4': 'Do not take for more than 3 days without doctor',
    'm4-stat': 'Paracetamol overdose is one of the leading causes of <strong>acute liver failure</strong> worldwide. Follow the correct dose.',
    'm5-title': 'Birth Control Pills',
    'm5-desc': 'Birth control pills must be taken correctly at the same time every day. Missing one pill reduces effectiveness. Emergency pills should not be used regularly.',
    'm5t1': 'Take at the same time every day \u2014 after breakfast is good',
    'm5t2': 'If one pill is missed, take two the next day and be extra cautious',
    'm5t3': 'Breastfeeding mothers should use a different type of pill',
    'm5t4': 'Consult a doctor or pharmacist before starting',
    'm5-stat': 'When used correctly, OCP is <strong>99%+ effective</strong>. But with incorrect use, effectiveness drops to 91%.',
    'm6-title': 'Antihistamine / Allergy Medicine',
    'm6-desc': 'Used for allergies, sneezing, itching and rashes. Older antihistamines (Chlorpheniramine, Phenergan) cause drowsiness. Many people drive without knowing this \u2014 dangerous!',
    'm6t1': 'Take older antihistamines (Phenergan, Avil) at night',
    'm6t2': 'Newer antihistamines (Cetirizine, Loratadine) cause less drowsiness',
    'm6t3': 'Do not drive after taking them',
    'm6t4': 'Children\'s dose is different from adults \u2014 be careful',
    'm6-stat': 'Many in Bangladesh take <strong>Phenergan or Avil</strong> as a cough medicine \u2014 but it is an antihistamine and sedative.',
    'et-tag': 'Expiry & Storage', 'et-title': 'Medicine Expiry & Proper Storage',
    'et-desc': 'Expired medicine has no benefit, it can even cause harm. If not stored properly, medicine can spoil even before expiry.',
    'eh-title': 'EXP: 07/2027 \u2014 What Does This Mean?',
    'eh-text': 'Every medicine packet has an EXP or Expiry Date. This means the medicine is usable until the last day of that month. After that, the chemical may change and effectiveness decreases.',
    'eh-text2': 'In Bangladesh\'s hot and humid climate, medicine deteriorates even faster. So proper storage is essential.',
    'exp-meaning': 'Do not use after July 2027',
    'before-exp': 'Within expiry', 'after-exp': 'Expired',
    'exp-cards-title': 'Important Expiry Information',
    'ec1-t': 'Where to look?', 'ec1-p': 'Usually on the back of the strip, bottom of the box, or bottle label. "MFG" means manufacturing date, "EXP" means expiry date.',
    'ec2-t': 'What happens if you take expired medicine?', 'ec2-p': 'Some medicines just become less effective, others become toxic. Especially eye drops, liquid antibiotics and insulin are dangerous after expiry. Don\'t take the risk.',
    'ec3-t': 'How to dispose of old medicines?', 'ec3-p': 'Don\'t pour down the drain \u2014 pollutes the environment. Don\'t flush down the toilet. Put in a sealed bag and in the dustbin, or return to a nearby pharmacy.',
    'store-title': 'How to Store Medicines',
    'sc1-t': 'Protect from heat', 'sc1-p': 'Keep most medicines at room temperature (15-25\u00b0C). In Bangladesh\'s heat, keep the medicine cabinet in a cool place. Keep away from direct sunlight.',
    'sc2-t': 'Avoid humidity', 'sc2-p': 'Don\'t keep medicines in the bathroom \u2014 steam damages medicines. Keep in original packaging and tightly closed.',
    'sc3-t': 'Out of children\'s reach', 'sc3-p': 'Children may eat colorful tablets thinking they are candy. Always keep in a locked cabinet or high place.',
    'sc4-t': 'Medicines that need refrigeration', 'sc4-p': 'Insulin, some eye drops and liquid antibiotics need to be refrigerated. Do not freeze. Medicines labeled "Store in Cool Place" can go in the fridge door.',
    'st-tag': 'Safety', 'st-title': 'Golden Rules of Medicine Use',
    'st-desc': 'Following these simple rules can prevent most medicine-related accidents.',
    'sr1-t': 'Don\'t take medicine without doctor\'s advice',
    'sr1-p': 'Everyone\'s body is different. What worked for your neighbour may be dangerous for you. Especially antibiotic, steroid and sleeping pill require a prescription.',
    'sr2-t': 'Don\'t use someone else\'s medicine',
    'sr2-p': 'Even with the same symptoms, the cause may be different. Using someone else\'s medicine can worsen your condition and delay correct diagnosis.',
    'sr3-t': 'Read the label completely',
    'sr3-p': 'Dose, frequency, before or after food \u2014 this information is on the label. If you can\'t read it, ask the pharmacist.',
    'sr4-t': 'Be careful with multiple medicines',
    'sr4-p': 'Taking two medicines together can cause drug interaction. For example, taking Paracetamol with Warfarin (blood thinner) is dangerous. Tell your doctor about all medicines you take.',
    'sr5-t': 'Complete the full antibiotic course',
    'sr5-p': 'Don\'t stop antibiotics just because you feel better. If the doctor gave a 7-day course, take all 7 days. Half a course doesn\'t kill bacteria, it makes them resistant.',
    'sr6-t': 'Ask your pharmacist',
    'sr6-p': 'Pharmacists don\'t just sell medicines \u2014 they are trained professionals. Ask any questions about side effects, dose, or interactions. They are ready to help.',
    'dos-title': 'What To Do', 'donts-title': 'What NOT To Do',
    'do1': 'Follow doctor\'s prescription', 'do2': 'Get pharmacist\'s advice',
    'do3': 'Complete the full medicine course', 'do4': 'Check expiry date before buying',
    'do5': 'Tell doctor if you have side effects', 'do6': 'Store medicines in cool dry place',
    'do7': 'Tell doctor about allergies in advance',
    'dont1': 'Don\'t start antibiotics without doctor', 'dont2': 'Don\'t stop medicine halfway',
    'dont3': 'Don\'t take someone else\'s medicine', 'dont4': 'Don\'t take expired medicine',
    'dont5': 'Don\'t store in bathroom or kitchen', 'dont6': 'Don\'t take too many different medicines',
    'dont7': 'Don\'t leave medicines within children\'s reach',
    'gen-title': 'Generic vs Brand \u2014 What\'s the Difference?',
    'gen-desc': 'The same medicine is sold under different names. The generic name is the name of the core chemical \u2014 it does the same job in all brands.',
    'gc1': 'Paracetamol (Generic)', 'gc1b': 'Napa, Ace, Renova, Tylenol, Panadol', 'gc1c': 'Same medicine, different brand name',
    'gc2': 'Omeprazole (Generic)', 'gc2b': 'Omez, Losec, Prilosec, Seclo', 'gc2c': 'Cheaper generic works just as well',
    'gc3': 'Cetirizine (Generic)', 'gc3b': 'Alatrol, Cetrizin, Zyrtec, Allegra', 'gc3c': 'You can ask pharmacist for generic',
    'fq-title': 'Frequently Asked Questions', 'fq-desc': 'The questions people ask most \u2014 simple answers.',
    'fq1-q': '<span class="faq-badge badge-danger"><i class="fi fi-sr-triangle-warning"></i> Antibiotic</span>Can I stop Antibiotics when I feel better?',
    'fq1-a': 'No, absolutely not. If the doctor gave a 5-day course, take all 5 days even if you feel better after 3. Because 90% of bacteria die in 3 days, but the remaining 10% are the strongest. If you don\'t kill them, antibiotics won\'t work later (Antibiotic Resistance).',
    'fq2-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-capsule"></i> Painkiller</span>Will taking two Painkillers together work better for severe pain?',
    'fq2-a': 'No! Taking two similar painkillers (like two paracetamols, or paracetamol + ibuprofen) together is dangerous. It can seriously damage the liver or stomach. For severe pain, talk to a doctor before increasing the dose.',
    'fq3-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-flower"></i> Birth Pill</span>What to do if I miss a birth control pill?',
    'fq3-a': 'If you remember within 24 hours, take one pill. If more than 24 hours have passed, skip that pill and take the next one at the normal time. But be extra cautious during this time. If two pills are missed, get a doctor\'s advice immediately.',
    'fq4-q': '<span class="faq-badge badge-danger"><i class="fi fi-rr-alarm-clock"></i> Expiry</span>Is it safe to take expired medicine in an emergency?',
    'fq4-a': 'Most solid tablets just become less effective \u2014 they don\'t immediately become toxic. But liquid antibiotics, eye drops, insulin and injections can be dangerous when expired. Use fresh medicine wherever possible and don\'t keep expired medicines at home.',
    'fq5-q': '<span class="faq-badge badge-safe"><i class="fi fi-rr-comment-alt"></i> Generic</span>If pharmacist gives a different brand, will it work the same?',
    'fq5-a': 'Yes, usually. If the doctor writes Napa but the pharmacist gives Ace or Renova, it does the same job \u2014 because the core chemical is Paracetamol in all of them. These are called Generics. However, for some special medicines (like thyroid, seizure) you should not change brands. Ask the pharmacist if in doubt.',
    'fq6-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-moon"></i> Sleeping Pill</span>Are sleeping pills safe?',
    'fq6-a': 'Sleeping pills are safe short-term with a doctor\'s prescription. But they become addictive long-term (more than 2 weeks). Stopping suddenly causes withdrawal. For a permanent solution to sleep problems, change your lifestyle and get a doctor\'s advice.',
    'fq7-q': '<span class="faq-badge badge-safe"><i class="fi fi-rr-heart-rate"></i> Gastric</span>Is it okay to take gastric medicine every day?',
    'fq7-a': 'No, it is not okay to take every day. At most 4-8 weeks when needed. More than that can cause weak bones, reduced Vitamin B12 and kidney problems. Change your lifestyle \u2014 reduce spicy food, eat on time.',
    'fq8-q': '<span class="faq-badge badge-danger"><i class="fi fi-rr-head-side-cough"></i> Allergy</span>Can I drive after taking allergy medicine?',
    'fq8-a': 'Older antihistamines (Phenergan, Avil, Chlorpheniramine) cause drowsiness \u2014 driving is dangerous. Newer antihistamines (Cetirizine, Loratadine, Fexofenadine) cause comparatively less drowsiness. But after taking any allergy medicine, assess your own condition before driving.',
    'ab-tag': 'About', 'ab-title': 'The Story Behind This Initiative',
    'founder-name': 'Habeba Hussain', 'founder-role': 'Pharmacy Student & Fellow',
    'ab-p1': 'Most working people in Bangladesh \u2014 garment workers, rickshaw pullers, shopkeepers, domestic workers \u2014 do not know correct information about medicines. They often buy medicine from nearby shops, lacking both time and money to visit a doctor.',
    'ab-p2': 'Studying pharmacy, I saw that these people could avoid many dangers if they just had the right information. Antibiotic resistance, overdose, expired medicine \u2014 these problems are happening simply due to lack of knowledge.',
    'ab-p3': 'This website was created for those people. In simple Bangla, in plain language \u2014 so anyone can understand. There will be QR code posters in local pharmacies \u2014 people can scan and learn while buying medicine.',
    'fel-title': 'Fellowship Program \u2014 Round 2',
    'fel-desc': 'This project was created as part of a Fellowship Program. Goal: Increase medicine awareness among working-class people.',
    'mis-title': 'Our Mission',
    'mp1': 'Providing correct medicine information in simple language',
    'mp2': 'Awareness about antibiotic misuse and resistance',
    'mp3': 'Delivering information directly to pharmacies via QR code',
    'mp4': 'Protecting people from the dangers of expired medicines',
    'mp5': 'Health protection for working and less-educated people',
    'cont-title': 'Contact Us',
    'cont-role': 'Pharmacy Student, Bangladesh',
    'disclaimer-text': 'This website is for awareness only. Always consult a qualified doctor for medical treatment.',
    'qr-cta-title': 'QR Code Poster',
    'qr-cta-desc': 'This poster will be in local pharmacies. Scanning it takes you directly to this website.',
    'qr-btn': '<i class="fi fi-rr-smartphone"></i> View QR Code',
    'qr-title': 'Pharmacy Poster QR Code',
    'qr-desc': 'Scan the QR code below or print it and put it in your pharmacy.',
    'poster-head': '<i class="fi fi-rr-document" style="margin-right:6px;"></i> Poster Text',
    'poster-line1': '<i class="fi fi-rr-capsule" style="margin-right:4px;"></i> Buying medicine?',
    'poster-line2': 'Use it correctly.<br>Scan this QR code and learn for free.',
    'poster-cta': 'Oshudh Ki Boss? | Know Your Medicine, Gain Health',
    'qr-caption': 'Scanning this QR Code takes you directly to this website.',
    'dl-btn': '<i class="fi fi-rr-download"></i> Download QR',
    'print-btn': '<i class="fi fi-rr-print"></i> Print',
    'ft-desc': 'A medicine awareness initiative for the working people of Bangladesh. In simple language, free of charge.',
    'fl1': 'Home', 'fl2': 'Medicines', 'fl3': 'Expiry', 'fl4': 'Safety', 'fl5': 'FAQ',
    'fl6': 'About Us', 'fl7': 'QR Code',
    'ft-disclaimer': '<i class="fi fi-sr-triangle-warning"></i> This website is for awareness purposes only. Always consult a qualified doctor or pharmacist for treatment.',
  },
  bn: {
    'logo-text': 'ওষুধটা কী বস?',
    'logo-sub': 'Know Your Medicine',
    'n-home': 'হোম', 'n-med': 'ওষুধ সমূহ', 'n-exp': 'মেয়াদ ও সংরক্ষণ',
    'n-safe': 'নিরাপত্তা টিপস', 'n-about': 'আমাদের সম্পর্কে',
    'mn-home': 'হোম', 'mn-med': 'ওষুধ সমূহ',
    'mn-exp': 'মেয়াদ ও সংরক্ষণ', 'mn-safe': 'নিরাপত্তা টিপস',
    'mn-about': 'আমাদের সম্পর্কে',
    'hero-tag': 'বাংলাদেশের কর্মজীবী মানুষের জন্য',
    'hero-title-main': 'ওষুধটা কী বস?',
    'hero-sub-bn': 'ওষুধ জানি, স্বাস্থ্য পাই',
    'hero-sub-en': 'Know Your Medicine, Gain Health',
    'stat1': 'ডাক্তার ছাড়া ওষুধ', 'stat2': 'AMR-এ মৃত্যু (২০১৯)', 'stat3': 'ঘুমের ওষুধ ব্যবহারকারী',
    'cta-learn': '<i class="fi fi-rr-capsule"></i> <span>ওষুধ সম্পর্কে জানুন</span>',
    'cta-tips': '<i class="fi fi-rr-shield-check"></i> <span>নিরাপত্তা টিপস</span>',
    'hc1-title': 'Antibiotic Resistance বাড়ছে!',
    'hc1-text': 'ভুলভাবে antibiotic ব্যবহারে শরীরে resistant bacteria তৈরি হয়। ফলে ভবিষ্যতে ওষুধ কাজ করে না।',
    'hc2-title': 'Prescription ছাড়া ওষুধ নয়',
    'hc2-text': 'WHO বলছে, বাংলাদেশে অধিকাংশ ওষুধ doctor এর পরামর্শ ছাড়াই কেনা হয়। এটি অত্যন্ত বিপজ্জনক।',
    'warn-text': '<strong>জানেন কি?</strong> ভুলভাবে ওষুধ খেলে liver, kidney ও শরীরের গুরুত্বপূর্ণ অঙ্গের ক্ষতি হতে পারে। সচেতন হন, সুস্থ থাকুন।',
    's1': 'Antibiotic সম্পূর্ণ course শেষ করুন',
    's2': 'Expiry date দেখে ওষুধ কিনুন',
    's3': 'Doctor এর prescription ছাড়া ঘুমের ওষুধ নয়',
    's4': 'অন্যের ওষুধ নিজে খাবেন না',
    's5': 'শিশুদের নাগালের বাইরে ওষুধ রাখুন',
    's1b': 'Antibiotic সম্পূর্ণ course শেষ করুন',
    's2b': 'Expiry date দেখে ওষুধ কিনুন',
    's3b': 'Doctor এর prescription ছাড়া ঘুমের ওষুধ নয়',
    's4b': 'অন্যের ওষুধ নিজে খাবেন না',
    's5b': 'শিশুদের নাগালের বাইরে ওষুধ রাখুন',
    'mt-tag': 'ওষুধ তথ্য',
    'mt-title': 'সাধারণ ওষুধের সঠিক ব্যবহার',
    'mt-desc': 'প্রতিটি ওষুধ সম্পর্কে সঠিক তথ্য জানুন — কী কারণে খাবেন, কীভাবে খাবেন, এবং কখন সতর্ক হবেন।',
    'fa': 'সব ওষুধ', 'fb': 'Antibiotics', 'fc': 'ঘুমের ওষুধ',
    'fd': 'গ্যাস্ট্রিক', 'fe': 'Painkillers', 'ff': 'Birth Control',
    'm1-title': 'অ্যান্টিবায়োটিক',
    'm1-desc': 'Antibiotic হলো এমন ওষুধ যা ব্যাকটেরিয়ার সংক্রমণ দূর করে। কিন্তু অনেকে সর্দি-জ্বরেও antibiotic খান — এটি ভুল এবং বিপজ্জনক। Virus-এ antibiotic কাজ করে না।',
    'm1t1': 'Doctor এর পরামর্শ ছাড়া antibiotic খাবেন না',
    'm1t2': 'সম্পূর্ণ course শেষ করুন — মাঝপথে বন্ধ করবেন না',
    'm1t3': 'অন্যের antibiotic নিজে ব্যবহার করবেন না',
    'm1t4': 'খাবারের সাথে বা পরে খেলে পেটের সমস্যা কমে',
    'm1-stat': 'বাংলাদেশে ২০১৯ সালে <strong>AMR-এর কারণে ২৬,২০০ জন</strong> মারা গেছেন। (WHO / The Business Standard)',
    'm2-title': 'ঘুমের ওষুধ',
    'm2-desc': 'ঘুমের সমস্যায় অনেকে এই ওষুধ ব্যবহার করেন। এগুলো benzodiazepine শ্রেণির — শুধুমাত্র doctor-এর prescription এ পাওয়া উচিত। এরা addictive এবং দীর্ঘমেয়াদে স্মৃতিশক্তিতে প্রভাব ফেলে।',
    'm2t1': 'কখনো নিজে থেকে শুরু করবেন না — Prescription আবশ্যক',
    'm2t2': 'গাড়ি চালাবেন না বা ভারী কাজ করবেন না',
    'm2t3': 'Alcohol-এর সাথে একদম নয় — মারাত্মক বিপদ',
    'm2t4': 'হঠাৎ বন্ধ না করে doctor-এর পরামর্শে ধীরে ধীরে কমান',
    'm2-stat': 'বাংলাদেশে প্রায় <strong>৩ লাখ মানুষ</strong> ঘুমের ওষুধ বা sedative ব্যবহার করেন। (The Daily Star)',
    'm3-title': 'গ্যাস্ট্রিকের ওষুধ',
    'm3-desc': 'বাংলাদেশে গ্যাস্ট্রিকের ওষুধ সবচেয়ে বেশি খাওয়া হয়। এই PPI (Proton Pump Inhibitor) ওষুধ দীর্ঘমেয়াদে না খাওয়াই ভালো। প্রয়োজনে doctor দেখান।',
    'm3t1': 'খাবার আগে (খালি পেটে) ২০-৩০ মিনিট আগে খান',
    'm3t2': 'দীর্ঘমেয়াদে (৮ সপ্তাহের বেশি) doctor ছাড়া নয়',
    'm3t3': 'মশলাদার ও ভাজা খাবার কমান',
    'm3t4': 'রাতে শোওয়ার আগে খাবেন না',
    'm3-stat': 'দীর্ঘমেয়াদী ব্যবহারে <strong>Vitamin B12, Magnesium ও Calcium</strong> শোষণে সমস্যা হয়। (Banglajol Medical Journal)',
    'm4-title': 'ব্যথার ওষুধ',
    'm4-desc': 'Painkiller সবচেয়ে বেশি ব্যবহৃত ওষুধ। Paracetamol সাধারণত নিরাপদ, কিন্তু বেশি dose-এ liver ক্ষতি করে। Ibuprofen পেট খারাপ করতে পারে। দুটো painkiller একসাথে খাওয়া বিপজ্জনক।',
    'm4t1': 'প্রাপ্তবয়স্কের জন্য Paracetamol সর্বোচ্চ 500mg × ৪ বার দিনে',
    'm4t2': 'Ibuprofen খাবারের সাথে খান — খালি পেটে নয়',
    'm4t3': 'দুটো painkiller একসাথে খাবেন না',
    'm4t4': '৩ দিনের বেশি doctor ছাড়া নয়',
    'm4-stat': 'Paracetamol overdose বিশ্বের অন্যতম প্রধান <strong>acute liver failure-এর কারণ</strong>। সঠিক dose মেনে চলুন।',
    'm5-title': 'জন্মনিয়ন্ত্রণ বড়ি',
    'm5-desc': 'জন্মনিয়ন্ত্রণ বড়ি সঠিকভাবে প্রতিদিন একই সময়ে খেতে হয়। একটি pill miss হলে effectiveness কমে যায়। Emergency pill নিয়মিত ব্যবহার করা উচিত নয়।',
    'm5t1': 'প্রতিদিন একই সময়ে খান — সকালের নাস্তার পরে ভালো',
    'm5t2': 'একটি pill বাদ পড়লে পরের দিন দুটো খান এবং অতিরিক্ত সতর্ক থাকুন',
    'm5t3': 'বুকের দুধ খাওয়ানো মায়েরা ভিন্ন ধরনের pill ব্যবহার করুন',
    'm5t4': 'শুরু করার আগে doctor বা pharmacist-এর পরামর্শ নিন',
    'm5-stat': 'সঠিকভাবে ব্যবহার করলে OCP <strong>৯৯%+ কার্যকর</strong>। কিন্তু ভুল ব্যবহারে কার্যকারিতা ৯১%-এ নেমে আসে।',
    'm6-title': 'Antihistamine / Allergy ওষুধ',
    'm6-desc': 'Allergy, হাঁচি, চুলকানি, রাশের জন্য এই ওষুধ ব্যবহার হয়। পুরনো antihistamine (Chlorpheniramine, Phenergan) ঘুমভাব সৃষ্টি করে। অনেকে এটা না জেনে গাড়ি চালান — বিপজ্জনক!',
    'm6t1': 'পুরনো antihistamine (Phenergan, Avil) রাতে নিন',
    'm6t2': 'নতুন antihistamine (Cetirizine, Loratadine) কম ঘুমভাব দেয়',
    'm6t3': 'খাওয়ার পর গাড়ি চালাবেন না',
    'm6t4': 'শিশুদের dose প্রাপ্তবয়স্কদের চেয়ে আলাদা — সাবধান',
    'm6-stat': 'বাংলাদেশে অনেকে <strong>Phenergan বা Avil</strong> কাশির ওষুধ হিসেবে খান — কিন্তু এটি antihistamine এবং sedative।',
    'et-tag': 'মেয়াদ ও সংরক্ষণ', 'et-title': 'ওষুধের মেয়াদ ও সঠিক সংরক্ষণ',
    'et-desc': 'মেয়াদ উত্তীর্ণ ওষুধ খেলে কোনো উপকার নেই, বরং ক্ষতি হতে পারে। সঠিকভাবে সংরক্ষণ না করলে ওষুধ আগেই নষ্ট হয়।',
    'eh-title': 'EXP: 07/2027 — এর মানে কী?',
    'eh-text': 'প্রতিটি ওষুধের প্যাকেটে EXP বা Expiry Date লেখা থাকে। এই তারিখ মানে হলো — এই মাসের শেষ দিন পর্যন্ত ওষুধটি ব্যবহারযোগ্য। তারপর থেকে ওষুধের chemical বদলে যেতে পারে এবং effectiveness কমে যায়।',
    'eh-text2': 'বাংলাদেশের গরম ও আর্দ্র আবহাওয়ায় ওষুধ আরও দ্রুত নষ্ট হয়। তাই সঠিক জায়গায় রাখা জরুরি।',
    'exp-meaning': 'জুলাই ২০২৭ এর পর ব্যবহার করবেন না',
    'before-exp': 'মেয়াদের মধ্যে', 'after-exp': 'মেয়াদ শেষ',
    'exp-cards-title': 'মেয়াদ সংক্রান্ত গুরুত্বপূর্ণ তথ্য',
    'ec1-t': 'কোথায় দেখবেন?', 'ec1-p': 'ওষুধের strip-এর পেছনে, box-এর নিচে বা bottle-এর label-এ সাধারণত EXP বা Exp. Date লেখা থাকে। "MFG" মানে তৈরির তারিখ, "EXP" মানে মেয়াদ শেষের তারিখ।',
    'ec2-t': 'মেয়াদ শেষ ওষুধ খেলে কী হয়?', 'ec2-p': 'কিছু ওষুধ শুধু কম কার্যকর হয়, আবার কিছু toxic হয়ে যায়। বিশেষত Eye drops, liquid antibiotics ও insulin মেয়াদের পরে বিপজ্জনক। Risk নেওয়া উচিত নয়।',
    'ec3-t': 'পুরনো ওষুধ ফেলবেন কীভাবে?', 'ec3-p': 'পানিতে ফেলবেন না — পরিবেশ দূষিত হয়। Toilet-এ flush করবেন না। একটি sealed bag-এ ভরে dustbin-এ ফেলুন, অথবা কাছের pharmacy-তে জমা দিন।',
    'store-title': 'ওষুধ কীভাবে সংরক্ষণ করবেন',
    'sc1-t': 'তাপমাত্রা থেকে বাঁচান', 'sc1-p': 'বেশিরভাগ ওষুধ Room temperature (১৫-২৫°C)-এ রাখুন। বাংলাদেশের গরমে ওষুধের cabinet ঠান্ডা জায়গায় রাখুন। সরাসরি রোদ থেকে দূরে রাখুন।',
    'sc2-t': 'আর্দ্রতা এড়িয়ে চলুন', 'sc2-p': 'Bathroom-এ ওষুধ রাখবেন না — ভাপ ওষুধ নষ্ট করে। Original packaging-এ রাখুন এবং tight করে বন্ধ রাখুন।',
    'sc3-t': 'শিশুদের নাগালের বাইরে', 'sc3-p': 'শিশুরা রঙিন tablet দেখলে candy মনে করে খেয়ে ফেলতে পারে। সবসময় lock করা cabinet-এ বা উঁচু জায়গায় রাখুন।',
    'sc4-t': 'Refrigerator-এ রাখার ওষুধ', 'sc4-p': 'Insulin, কিছু eye drops ও liquid antibiotic ফ্রিজে রাখতে হয়। Freeze করবেন না। যে সব ওষুধে "Store in Cool Place" লেখা সেগুলো ফ্রিজের দরজায় রাখুন।',
    'st-tag': 'নিরাপত্তা', 'st-title': 'ওষুধ ব্যবহারের সোনালি নিয়ম',
    'st-desc': 'এই সাধারণ নিয়মগুলো মেনে চললে অধিকাংশ ওষুধজনিত দুর্ঘটনা এড়ানো সম্ভব।',
    'sr1-t': 'Doctor-এর পরামর্শ ছাড়া ওষুধ খাবেন না',
    'sr1-p': 'প্রতিটি মানুষের শরীর আলাদা। আপনার প্রতিবেশীর যে ওষুধ কাজ করেছে, সেটা আপনার জন্য বিপজ্জনক হতে পারে। বিশেষত antibiotic, steroid ও sleeping pill-এর ক্ষেত্রে prescription আবশ্যক।',
    'sr2-t': 'অন্যের ওষুধ ব্যবহার করবেন না',
    'sr2-p': 'একই রোগের উপসর্গ থাকলেও কারণ ভিন্ন হতে পারে। অন্যের ওষুধ নিলে আপনার রোগ বাড়তে পারে এবং সঠিক রোগ নির্ণয় দেরি হবে।',
    'sr3-t': 'Label সম্পূর্ণ পড়ুন',
    'sr3-p': 'Dose, কতবার খাবেন, খাবারের আগে না পরে — এই তথ্যগুলো label-এ থাকে। পড়তে না পারলে pharmacist-কে জিজ্ঞেস করুন।',
    'sr4-t': 'একসাথে অনেক ওষুধ সতর্কতার সাথে খান',
    'sr4-p': 'দুটো ওষুধ একসাথে খেলে drug interaction হতে পারে। যেমন Paracetamol-এর সাথে Warfarin (blood thinner) একসাথে নিলে বিপদ। সব ওষুধের তথ্য doctor-কে জানান।',
    'sr5-t': 'Antibiotic সম্পূর্ণ course শেষ করুন',
    'sr5-p': 'ভালো লাগলেই antibiotic বন্ধ করবেন না। Doctor যদি ৭ দিনের course দিয়েছেন, সম্পূর্ণ ৭ দিন খান। অর্ধেক কোর্সে bacteria মরে না, বরং resistant হয়ে যায়।',
    'sr6-t': 'Pharmacist-কে প্রশ্ন করুন',
    'sr6-p': 'Pharmacist শুধু ওষুধ বিক্রি করেন না — তারা trained professional। ওষুধের side effect, dose, বা interaction নিয়ে যেকোনো প্রশ্ন করুন। তারা সাহায্য করতে প্রস্তুত।',
    'dos-title': 'যা করবেন', 'donts-title': 'যা করবেন না',
    'do1': 'Doctor-এর prescription মেনে চলুন', 'do2': 'Pharmacist-এর পরামর্শ নিন',
    'do3': 'ওষুধের পুরো course শেষ করুন', 'do4': 'Expiry date দেখে ওষুধ কিনুন',
    'do5': 'Side effect হলে doctor-কে জানান', 'do6': 'ওষুধ ঠান্ডা ও শুষ্ক জায়গায় রাখুন',
    'do7': 'Allergy থাকলে doctor-কে আগে বলুন',
    'dont1': 'Doctor ছাড়া antibiotic শুরু করবেন না', 'dont2': 'মাঝপথে ওষুধ বন্ধ করবেন না',
    'dont3': 'অন্যের ওষুধ নিজে নেবেন না', 'dont4': 'Expired ওষুধ খাবেন না',
    'dont5': 'Bathroom বা রান্নাঘরে ওষুধ রাখবেন না', 'dont6': 'একসাথে অনেক ধরনের ওষুধ নেবেন না',
    'dont7': 'শিশুদের নাগালে ওষুধ রাখবেন না',
    'gen-title': 'Generic vs Brand — কী পার্থক্য?',
    'gen-desc': 'একই ওষুধ ভিন্ন নামে বিক্রি হয়। Generic নামটি মূল chemical-এর নাম — এটি সব brand-এ একই কাজ করে।',
    'gc1': 'Paracetamol (Generic)', 'gc1b': 'Napa, Ace, Renova, Tylenol, Panadol', 'gc1c': 'একই ওষুধ, আলাদা brand নাম',
    'gc2': 'Omeprazole (Generic)', 'gc2b': 'Omez, Losec, Prilosec, Seclo', 'gc2c': 'সস্তা generic নিলেও একই কাজ হয়',
    'gc3': 'Cetirizine (Generic)', 'gc3b': 'Alatrol, Cetrizin, Zyrtec, Allergra', 'gc3c': 'Pharmacist-কে generic চাইতে পারেন',
    'fq-title': 'সচরাচর জিজ্ঞাসা', 'fq-desc': 'মানুষ যেসব প্রশ্ন সবচেয়ে বেশি করেন — সহজ ভাষায় উত্তর।',
    'fq1-q': '<span class="faq-badge badge-danger"><i class="fi fi-sr-triangle-warning"></i> Antibiotic</span>ভালো লাগলেই কি Antibiotic বন্ধ করা যাবে?',
    'fq1-a': 'না, একদমই না। Doctor যদি ৫ দিনের course দিয়েছেন, ৩ দিনেই ভালো লাগলেও বাকি ২ দিন খান। কারণ — ৩ দিনে ৯০% bacteria মরে যায়, কিন্তু বাকি ১০% সবচেয়ে শক্তিশালী। এদের মেরে না ফেললে পরে antibiotic কাজ করবে না (Antibiotic Resistance)।',
    'fq2-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-capsule"></i> Painkiller</span>ব্যথা বেশি হলে কি দুটো Painkiller একসাথে খেলে বেশি কাজ হবে?',
    'fq2-a': 'না! একই ধরনের দুটো painkiller (যেমন দুটো paracetamol বা paracetamol + ibuprofen) একসাথে খাওয়া বিপজ্জনক। এতে liver বা stomach-এর মারাত্মক ক্ষতি হতে পারে। বেশি ব্যথায় dose বাড়ানোর আগে doctor-এর সাথে কথা বলুন।',
    'fq3-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-flower"></i> Birth Pill</span>জন্মনিয়ন্ত্রণ বড়ি একটি মিস হলে কী করব?',
    'fq3-a': 'যদি মনে পড়লে ২৪ ঘণ্টার মধ্যে একটি pill খান। যদি ২৪ ঘণ্টার বেশি হয়ে যায়, তাহলে সেই pill বাদ দিন এবং পরের দিন থেকে স্বাভাবিক সময়ে খান। কিন্তু এই সময় অতিরিক্ত সতর্ক থাকুন। দুটো pill মিস হলে তাৎক্ষণিক doctor-এর পরামর্শ নিন।',
    'fq4-q': '<span class="faq-badge badge-danger"><i class="fi fi-rr-alarm-clock"></i> Expiry</span>Emergency-তে মেয়াদ শেষ ওষুধ খাওয়া কি নিরাপদ?',
    'fq4-a': 'বেশিরভাগ solid tablet কিছুটা কম কার্যকর হয় — সাথে সাথে বিষাক্ত হয় না। কিন্তু liquid antibiotic, eye drop, insulin ও injection expired হলে বিপজ্জনক হতে পারে। যতটা সম্ভব fresh ওষুধ ব্যবহার করুন এবং expired ওষুধ ঘরে না রেখে ফেলে দিন।',
    'fq5-q': '<span class="faq-badge badge-safe"><i class="fi fi-rr-comment-alt"></i> Generic</span>Pharmacist ভিন্ন brand দিলে কি একই কাজ হবে?',
    'fq5-a': 'হ্যাঁ, সাধারণত। Doctor Napa লিখলেও Pharmacist Ace বা Renova দিলে একই কাজ হয় — কারণ সবের মূল chemical Paracetamol। এই ওষুধগুলোকে Generic বলে। তবে কিছু বিশেষ ওষুধের ক্ষেত্রে (যেমন thyroid, seizure) brand বদলানো উচিত নয়। সন্দেহ হলে pharmacist-কে জিজ্ঞেস করুন।',
    'fq6-q': '<span class="faq-badge badge-warn"><i class="fi fi-rr-moon"></i> Sleeping Pill</span>ঘুমের ওষুধ কি নিরাপদ?',
    'fq6-a': 'Sleeping pill স্বল্পমেয়াদে doctor-এর prescription-এ নিরাপদ। কিন্তু দীর্ঘমেয়াদে (২ সপ্তাহের বেশি) addictive হয়ে যায়। হঠাৎ বন্ধ করলে withdrawal হয়। ঘুমের সমস্যার স্থায়ী সমাধানের জন্য lifestyle পরিবর্তন ও doctor-এর পরামর্শ নিন।',
    'fq7-q': '<span class="faq-badge badge-safe"><i class="fi fi-rr-heart-rate"></i> Gastric</span>গ্যাস্ট্রিকের ওষুধ কি প্রতিদিন খাওয়া ঠিক?',
    'fq7-a': 'না, প্রতিদিন খাওয়া ঠিক নয়। প্রয়োজনে সর্বোচ্চ ৪-৮ সপ্তাহ খাওয়া যায়। এর বেশি খেলে হাড় দুর্বল হওয়া, Vitamin B12 কমে যাওয়া এবং kidney সমস্যা হতে পারে। Lifestyle পরিবর্তন করুন — মশলাদার খাবার কমান, সময়মতো খান।',
    'fq8-q': '<span class="faq-badge badge-danger"><i class="fi fi-rr-head-side-cough"></i> Allergy</span>Allergy-র ওষুধ খেলে কি গাড়ি চালানো যাবে?',
    'fq8-a': 'পুরনো antihistamine (যেমন Phenergan, Avil, Chlorpheniramine) খেলে ঘুম আসে — গাড়ি চালানো বিপজ্জনক। নতুন antihistamine (Cetirizine, Loratadine, Fexofenadine) তুলনামূলক কম ঘুমভাব দেয়। তবে যেকোনো allergy ওষুধ খাওয়ার পরে নিজের অবস্থা বুঝে গাড়ি চালান।',
    'ab-tag': 'আমাদের সম্পর্কে', 'ab-title': 'এই উদ্যোগের পেছনের গল্প',
    'founder-name': 'Habeba Hussain', 'founder-role': 'Pharmacy Student & Fellow',
    'ab-p1': 'বাংলাদেশের অধিকাংশ কর্মজীবী মানুষ — গার্মেন্টস শ্রমিক, রিকশাচালক, দোকানদার, গৃহকর্মী — ওষুধ সম্পর্কে সঠিক তথ্য জানেন না। তারা প্রায়ই পাশের দোকান থেকে নিজেই ওষুধ কিনে খান, doctor-এর কাছে যাওয়ার সময় ও টাকা দুটোই নেই।',
    'ab-p2': 'Pharmacy-তে পড়তে গিয়ে দেখলাম, এই মানুষগুলো শুধু একটু সঠিক তথ্য পেলেই অনেক বিপদ এড়াতে পারতেন। Antibiotic resistance, overdose, expired medicine — এই সমস্যাগুলো শুধু জ্ঞানের অভাবেই হচ্ছে।',
    'ab-p3': 'এই website-টি তৈরি হয়েছে সেই মানুষগুলোর জন্য। সহজ বাংলায়, সরল ভাষায় — যাতে যে কেউ বুঝতে পারেন। Local pharmacy-তে QR code poster থাকবে — ওষুধ কিনতে গিয়েই scan করে জানতে পারবেন।',
    'fel-title': 'Fellowship Program — Round 2',
    'fel-desc': 'এই প্রকল্পটি একটি Fellowship Program-এর অংশ হিসেবে তৈরি করা হয়েছে। লক্ষ্য: কর্মজীবী মানুষের মধ্যে ওষুধ সংক্রান্ত সচেতনতা বাড়ানো।',
    'mis-title': 'আমাদের লক্ষ্য',
    'mp1': 'সহজ ভাষায় ওষুধের সঠিক তথ্য প্রদান',
    'mp2': 'Antibiotic misuse ও resistance সম্পর্কে সচেতনতা',
    'mp3': 'QR code-এর মাধ্যমে pharmacy-তে সরাসরি তথ্য পৌঁছে দেওয়া',
    'mp4': 'Expired medicine-এর বিপদ থেকে মানুষকে রক্ষা করা',
    'mp5': 'কর্মজীবী ও স্বল্পশিক্ষিত মানুষের স্বাস্থ্য সুরক্ষা',
    'cont-title': 'যোগাযোগ করুন',
    'cont-role': 'Pharmacy Student, Bangladesh',
    'disclaimer-text': 'এই website শুধু সচেতনতার জন্য। চিকিৎসার জন্য সবসময় qualified doctor-এর পরামর্শ নিন।',
    'qr-cta-title': 'QR Code Poster',
    'qr-cta-desc': 'Local pharmacy-তে এই poster থাকবে। Scan করলে সরাসরি এই website-এ আসা যাবে।',
    'qr-btn': '<i class="fi fi-rr-smartphone"></i> QR Code দেখুন',
    'qr-title': 'Pharmacy Poster QR Code',
    'qr-desc': 'নিচের QR Code টি scan করুন বা print করে pharmacy-তে লাগান।',
    'poster-head': '<i class="fi fi-rr-document" style="margin-right:6px;"></i> Poster Text',
    'poster-line1': '<i class="fi fi-rr-capsule" style="margin-right:4px;"></i> ওষুধ কিনছেন?',
    'poster-line2': 'সঠিকভাবে ব্যবহার করুন।<br>এই QR code scan করুন এবং বিনামূল্যে জানুন।',
    'poster-cta': 'ওষুধটা কী বস? | ওষুধ জানি, স্বাস্থ্য পাই',
    'qr-caption': 'এই QR Code scan করলে সরাসরি এই website-এ আসা যাবে।',
    'dl-btn': '<i class="fi fi-rr-download"></i> QR Download করুন',
    'print-btn': '<i class="fi fi-rr-print"></i> Print করুন',
    'ft-desc': 'বাংলাদেশের কর্মজীবী মানুষের জন্য ওষুধ সচেতনতার একটি উদ্যোগ। সহজ ভাষায়, বিনামূল্যে।',
    'fl1': 'হোম', 'fl2': 'ওষুধ সমূহ', 'fl3': 'মেয়াদ', 'fl4': 'নিরাপত্তা', 'fl5': 'FAQ',
    'fl6': 'আমাদের সম্পর্কে', 'fl7': 'QR Code',
    'ft-disclaimer': '<i class="fi fi-sr-triangle-warning"></i> এই website শুধুমাত্র সচেতনতা বৃদ্ধির উদ্দেশ্যে তৈরি। চিকিৎসার জন্য সবসময় qualified doctor বা pharmacist-এর পরামর্শ নিন।',
  }
};

let currentLang = localStorage.getItem('oshudh-lang') || 'bn';

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('oshudh-lang', lang);
  
  document.getElementById('btn-bn').classList.toggle('active', lang === 'bn');
  document.getElementById('btn-en').classList.toggle('active', lang === 'en');
  document.getElementById('btn-both').classList.toggle('active', lang === 'both');

  if (lang === 'en') {
    document.body.classList.remove('lang-bn');
    applyTranslations('en');
  } else if (lang === 'bn') {
    document.body.classList.add('lang-bn');
    applyTranslations('bn');
  } else {
    // Both mode: show Bangla first + English subtitle
    document.body.classList.add('lang-bn');
    applyBothMode();
  }

  // Preserve active nav highlighting
  preserveNavHighlight();
}

function applyTranslations(lang) {
  const t = translations[lang];
  if (!t) return;
  for (const [id, text] of Object.entries(t)) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = text;
  }
}

function applyBothMode() {
  const bn = translations['bn'];
  const en = translations['en'];
  if (!bn || !en) return;

  // IDs that contain HTML structure (FAQ badges etc.) - just apply bn
  const htmlContentIds = ['warn-text', 'cta-learn', 'cta-tips', 'qr-btn', 'dl-btn', 'print-btn',
    'poster-head', 'poster-line1', 'poster-line2', 'ft-disclaimer',
    'fq1-q','fq2-q','fq3-q','fq4-q','fq5-q','fq6-q','fq7-q','fq8-q',
    'm1-stat','m2-stat','m3-stat','m4-stat','m5-stat','m6-stat'];

  for (const [id, bnText] of Object.entries(bn)) {
    const el = document.getElementById(id);
    if (!el) continue;
    const enText = en[id];
    if (!enText || bnText === enText) {
      el.innerHTML = bnText;
      continue;
    }

    if (htmlContentIds.includes(id)) {
      // For complex HTML content, show bn version only
      el.innerHTML = bnText;
      continue;
    }

    // For FAQ answers, show both
    if (id.startsWith('fq') && id.endsWith('-a')) {
      el.innerHTML = bnText + '<span class="both-subtitle">' + enText + '</span>';
      continue;
    }

    // Strip any HTML tags for subtitle comparison
    const bnPlain = bnText.replace(/<[^>]*>/g, '').trim();
    const enPlain = enText.replace(/<[^>]*>/g, '').trim();
    
    if (bnPlain === enPlain) {
      el.innerHTML = bnText;
    } else {
      el.innerHTML = bnText + '<span class="both-subtitle">' + enPlain + '</span>';
    }
  }
}

function preserveNavHighlight() {
  // Find the currently active section and re-highlight
  const activeSection = document.querySelector('section.active');
  if (activeSection) {
    const id = activeSection.id;
    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
    const navMap = { home:'nav-home', medicines:'nav-medicines', expiry:'nav-expiry', safety:'nav-safety', faq:'nav-faq', about:'nav-about', 'qr-page':'nav-about' };
    const navEl = document.getElementById(navMap[id]);
    if (navEl) navEl.classList.add('active');
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  // Apply saved language
  const savedLang = localStorage.getItem('oshudh-lang');
  if (savedLang && savedLang !== 'bn') {
    setLang(savedLang);
  }

  // Close mobile menu on outside click
  document.addEventListener('click', (e) => {
    const menu = document.getElementById('mobileMenu');
    const ham = document.getElementById('hamburger');
    if (menu.classList.contains('open') && !menu.contains(e.target) && !ham.contains(e.target)) {
      menu.classList.remove('open');
    }
  });
});
</script>"""

content = content[0:js_start_idx] + new_js + content[js_end_idx:]

# ══════════════════════════════════════════════════════════════════════
# WRITE THE RESULT
# ══════════════════════════════════════════════════════════════════════
with open(r'f:\E\Downloads\YUMNA\oshudh-ki-boss.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! All enhancements applied.")
print(f"Final file size: {len(content)} characters")
