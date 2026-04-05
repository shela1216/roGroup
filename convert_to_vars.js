const fs = require('fs');

try {
    let content = fs.readFileSync('index.html', 'utf-8');

    // Systemic replacements to use CSS variables
    content = content.replace(/#090f1d/g, 'var(--app-bg)');
    content = content.replace(/#0f172a/g, 'var(--sidebar-bg)');
    content = content.replace(/#1e293b/g, 'var(--sidebar-border)');
    content = content.replace(/#131c31/g, 'var(--card-bg)');
    content = content.replace(/#3b5380/g, 'var(--card-border)');
    content = content.replace(/#f8fafc/g, 'var(--text-primary)');
    content = content.replace(/#e2e8f0/g, 'var(--text-secondary)');
    content = content.replace(/#94a3b8/g, 'var(--text-muted)');
    content = content.replace(/#1b2742/g, 'var(--item-bg)');
    content = content.replace(/#223254/g, 'var(--item-hover-bg)');
    
    // Some specific border/background replacements that might have missed
    content = content.replace(/border:1px solid #e2e8f0/g, 'border:1px solid var(--sidebar-border)');
    content = content.replace(/border-bottom:1px solid #e2e8f0/g, 'border-bottom:1px solid var(--sidebar-border)');
    content = content.replace(/border-top:1px solid #e2e8f0/g, 'border-top:1px solid var(--sidebar-border)');
    content = content.replace(/border-right:1px solid #1e293b/g, 'border-right:1px solid var(--sidebar-border)');

    fs.writeFileSync('index.html', content, 'utf-8');
    console.log("Converted hardcoded colors to CSS variables");
} catch (e) {
    console.error(e);
}
