import sys
import traceback

try:
    with open('d:/website/loseWeight/roGroup/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replaces = {
        '#0e1a2b': '#f0f6ff',
        '#0a1520': '#ffffff',
        '#0a1420': '#f1f5f9',
        '#1b2d42': '#ffffff',
        '#142030': '#f8fafc',
        '#1a2d40': '#e2e8f0',
        '#1e3248': '#e2e8f0',
        '#28405a': '#cbd5e1',
        '#2a3f58': '#cbd5e1',
        '#c8d8ec': '#334155',
        '#e8f0fb': '#0f172a',
        '#6a8aaa': '#64748b',
        '#2a4060': '#94a3b8',
        '#3a5570': '#64748b',
        '#4a6a8a': '#475569',
        'rgba(255,255,255,0.06)': 'rgba(0,0,0,0.04)',
        'rgba(255,255,255,0.07)': 'rgba(0,0,0,0.05)',
        'rgba(255,255,255,0.05)': 'rgba(0,0,0,0.04)',
        'rgba(255,255,255,0.04)': 'rgba(0,0,0,0.03)',
        'rgba(255,255,255,0.03)': 'rgba(0,0,0,0.02)',
        'rgba(255,255,255,0.25)': 'rgba(255,255,255,0.8)',
        'rgba(0,0,0,0.15)': 'rgba(0,0,0,0.03)',
        'rgba(0,0,0,0.2)': 'rgba(0,0,0,0.04)',
        'rgba(0,0,0,0.5)': 'rgba(0,0,0,0.08)',
        'rgba(0,0,0,0.6)': 'rgba(0,0,0,0.1)',
        'rgba(0,0,0,0.3)': 'rgba(0,0,0,0.05)',
        'rgba(0,0,0,0.35)': 'rgba(0,0,0,0.06)',
        'rgba(0,0,0,0.75)': 'rgba(255,255,255,0.6)',
    }

    old_content = content
    for k, v in replaces.items():
        content = content.replace(k, v)

    content = content.replace('.nav-item:hover { background:#ffffff; color:#334155; }', '.nav-item:hover { background:#f1f5f9; color:#0f172a; }')
    content = content.replace("@mouseenter=\"$event.currentTarget.style.background='#ffffff'", "@mouseenter=\"$event.currentTarget.style.background='#f1f5f9'")

    if old_content == content:
        print('No changes were made to the content.')
    else:
        with open('d:/website/loseWeight/roGroup/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Theme successfully updated.')

except Exception as e:
    print('Error occurred:')
    traceback.print_exc()
    sys.exit(1)
