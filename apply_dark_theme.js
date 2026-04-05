const fs = require('fs');

try {
    let content = fs.readFileSync('index.html', 'utf-8');

    // Swap light colors for dark RO-style colors
    content = content.replace(/#f0f6ff/g, '#090f1d'); // Main app background
    content = content.replace(/bg-\[#f0f6ff\]/g, 'bg-[#090f1d]');

    content = content.replace(/background:\s*#ffffff/g, 'background:#131c31');
    content = content.replace(/background:\s*#f8fafc/g, 'background:#1b2742');
    content = content.replace(/background:\s*#f1f5f9/g, 'background:#223254');

    // Borders
    content = content.replace(/border(-.*?color)?:\s*1px solid #e2e8f0/g, 'border$1:1px solid #2a3f66');
    content = content.replace(/border(-.*?color)?:\s*1px solid #cbd5e1/g, 'border$1:1px solid #3b5380');

    // Text colors
    content = content.replace(/color:\s*#0f172a/g, 'color:#f8fafc');
    content = content.replace(/color:\s*#334155/g, 'color:#e2e8f0');
    content = content.replace(/color:\s*#475569/g, 'color:#cbd5e1');
    content = content.replace(/color:\s*#64748b/g, 'color:#94a3b8');

    // Box shadows
    content = content.replace(/rgba\(0,0,0,0\.05\)/g, 'rgba(0,0,0,0.3)');
    content = content.replace(/rgba\(0,0,0,0\.06\)/g, 'rgba(0,0,0,0.4)');
    content = content.replace(/rgba\(0,0,0,0\.08\)/g, 'rgba(0,0,0,0.5)');
    content = content.replace(/rgba\(0,0,0,0\.1\)/g, 'rgba(0,0,0,0.6)');

    // Specific RGBA replacements for hover/active states
    content = content.replace(/rgba\(0,0,0,0\.04\)/g, 'rgba(255,255,255,0.05)');
    content = content.replace(/rgba\(255,255,255,0\.8\)/g, 'rgba(255,255,255,0.15)');
    content = content.replace(/background:rgba\(255,255,255,0\.6\)/g, 'background:rgba(9,15,29,0.85)'); // Modal backdrops

    // CSS classes updates
    content = content.replace('.prog-track { background: #f1f5f9;', '.prog-track { background: #1b2742;');
    content = content.replace('background:#f1f5f9; margin-bottom:3px', 'background:#223254; margin-bottom:3px');
    content = content.replace(/@mouseenter="\$event\.currentTarget\.style\.background='#f1f5f9'"/g, '@mouseenter="$event.currentTarget.style.background=\'#223254\'"');
    content = content.replace(/@mouseleave="\$event\.currentTarget\.style\.background='#f8fafc'"/g, '@mouseleave="$event.currentTarget.style.background=\'#1b2742\'"');
    content = content.replace(/@mouseenter="\$event\.currentTarget\.style\.background='#ffffff'"/g, '@mouseenter="$event.currentTarget.style.background=\'#2a3f66\'"');
    content = content.replace(/@mouseleave="\$event\.currentTarget\.style\.background='#f8fafc'"/g, '@mouseleave="$event.currentTarget.style.background=\'#1b2742\'"');

    content = content.replace(/@mouseenter="\$event\.currentTarget\.style\.borderColor='#64748b'"/g, '@mouseenter="$event.currentTarget.style.borderColor=\'#60a5fa\'"');
    content = content.replace(/@mouseleave="\$event\.currentTarget\.style\.borderColor='#e2e8f0'"/g, '@mouseleave="$event.currentTarget.style.borderColor=\'#2a3f66\'"');
    content = content.replace(/@mouseleave="\$event\.currentTarget\.style\.borderColor='transparent'"/g, '@mouseleave="$event.currentTarget.style.borderColor=\'transparent\'"');

    fs.writeFileSync('index.html', content, 'utf-8');
    console.log("Applied dark RO theme");
} catch (e) {
    console.error(e);
}
