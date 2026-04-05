import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Swap light colors for dark RO-style colors

# Backgrounds
content = content.replace('#f0f6ff', '#090f1d') # Main app background
content = content.replace('bg-[#f0f6ff]', 'bg-[#090f1d]')

# Let's target specific inline styles to avoid messing up the sidebar we just fixed
# Actually, the sidebar uses #0f172a and #1e293b.
# Cards and white backgrounds
content = re.sub(r'background:\s*#ffffff', r'background:#131c31', content)
content = re.sub(r'background:\s*#f8fafc', r'background:#1b2742', content)
content = re.sub(r'background:\s*#f1f5f9', r'background:#223254', content)

# Borders
content = re.sub(r'border(-.*?color)?:\s*1px solid #e2e8f0', r'\g<1>:1px solid #2a3f66', content)
content = re.sub(r'border(-.*?color)?:\s*1px solid #cbd5e1', r'\g<1>:1px solid #3b5380', content)

# Text colors
content = re.sub(r'color:\s*#0f172a', r'color:#f8fafc', content)
content = re.sub(r'color:\s*#334155', r'color:#e2e8f0', content)
content = re.sub(r'color:\s*#475569', r'color:#cbd5e1', content)
content = re.sub(r'color:\s*#64748b', r'color:#94a3b8', content)

# Box shadows
content = content.replace('rgba(0,0,0,0.05)', 'rgba(0,0,0,0.3)')
content = content.replace('rgba(0,0,0,0.06)', 'rgba(0,0,0,0.4)')
content = content.replace('rgba(0,0,0,0.08)', 'rgba(0,0,0,0.5)')
content = content.replace('rgba(0,0,0,0.1)', 'rgba(0,0,0,0.6)')

# Specific RGBA replacements for hover/active states
content = content.replace('rgba(0,0,0,0.04)', 'rgba(255,255,255,0.05)')
content = content.replace('rgba(255,255,255,0.8)', 'rgba(255,255,255,0.15)')
content = content.replace('background:rgba(255,255,255,0.6)', 'background:rgba(9,15,29,0.85)') # Modal backdrops

# CSS classes updates
content = content.replace('.prog-track { background: #f1f5f9;', '.prog-track { background: #1b2742;')
content = content.replace('background:#f1f5f9; margin-bottom:3px', 'background:#223254; margin-bottom:3px')
content = content.replace('@mouseenter="$event.currentTarget.style.background=\'#f1f5f9\'"', '@mouseenter="$event.currentTarget.style.background=\'#223254\'"')
content = content.replace('@mouseleave="$event.currentTarget.style.background=\'#f8fafc\'"', '@mouseleave="$event.currentTarget.style.background=\'#1b2742\'"')
content = content.replace('@mouseenter="$event.currentTarget.style.background=\'#ffffff\'"', '@mouseenter="$event.currentTarget.style.background=\'#2a3f66\'"')
content = content.replace('@mouseleave="$event.currentTarget.style.background=\'#f8fafc\'"', '@mouseleave="$event.currentTarget.style.background=\'#1b2742\'"')

content = content.replace('@mouseenter="$event.currentTarget.style.borderColor=\'#64748b\'"', '@mouseenter="$event.currentTarget.style.borderColor=\'#60a5fa\'"')
content = content.replace('@mouseleave="$event.currentTarget.style.borderColor=\'#e2e8f0\'"', '@mouseleave="$event.currentTarget.style.borderColor=\'#2a3f66\'"')
content = content.replace('@mouseleave="$event.currentTarget.style.borderColor=\'transparent\'"', '@mouseleave="$event.currentTarget.style.borderColor=\'transparent\'"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied dark RO theme")
