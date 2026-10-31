#!/usr/bin/env python3
"""Adds a day/night toggle (with remembered choice) to every page, idempotently."""
import re, glob, pathlib

EARLY = '<script>try{var t=localStorage.getItem("ayadati-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>'
MOON = '<svg class="ic m" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4 8.5 8.5 0 1 0 20 14.5z"/></svg>'
SUN = '<svg class="ic s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/></svg>'
CSS = """
/* theme toggle */
.theme-btn{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:12px;border:1px solid rgba(127,127,127,.4);background:rgba(127,127,127,.14);color:inherit;cursor:pointer;padding:0;font:inherit}
.theme-btn:hover{border-color:currentColor}.theme-btn:focus-visible{outline:3px solid #1287A0;outline-offset:2px}
.theme-btn .ic{width:20px;height:20px}.theme-btn .s{display:none}
:root[data-theme="dark"] .theme-btn .m{display:none}:root[data-theme="dark"] .theme-btn .s{display:block}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .theme-btn .m{display:none}:root:not([data-theme="light"]) .theme-btn .s{display:block}}
.theme-float{position:fixed;top:14px;left:14px;z-index:100;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
"""
JS = """<script>(function(){var R=document.documentElement,bs=document.querySelectorAll('[data-theme-toggle]');function cur(){return R.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}function go(){var n=cur()==='dark'?'light':'dark';R.setAttribute('data-theme',n);try{localStorage.setItem('ayadati-theme',n)}catch(e){}window.dispatchEvent(new Event('themechange'))}for(var i=0;i<bs.length;i++)bs[i].addEventListener('click',go)})();</script>"""
BTN = lambda cls: f'<button type="button" class="theme-btn {cls}" data-theme-toggle aria-label="تبديل الوضع الليلي والنهاري">{MOON}{SUN}</button>'

def guard_dark(s):
    """Make a plain `@media dark {:root{...}}` block respect an explicit data-theme."""
    if 'data-theme' in s: return s
    m = re.search(r'@media \(prefers-color-scheme: dark\)\s*\{\s*:root\s*\{(.*?)\}\s*\}', s, re.S)
    if not m: return s
    tokens = m.group(1)
    new = ('@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){' + tokens + '} }\n'
           '  :root[data-theme="dark"]{' + tokens + ' color-scheme: dark; }\n'
           '  :root[data-theme="light"]{ color-scheme: light; }')
    return s[:m.start()] + new + s[m.end():]

for path in glob.glob('*.html') + glob.glob('guides/*.html'):
    if 'googleeed' in path: continue
    s = pathlib.Path(path).read_text(encoding='utf-8'); o = s
    if 'ayadati-theme' not in s:
        s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + EARLY, 1)
    if path == '404.html':
        s = s.replace('@media(prefers-color-scheme:dark){body{background:#07131C;color:#E8F3F8}}', '@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) body{background:#07131C;color:#E8F3F8}}:root[data-theme="dark"] body{background:#07131C;color:#E8F3F8}:root[data-theme="light"] body{background:#F4FAFC;color:#0A2540}')
    s = guard_dark(s)
    if '/* theme toggle */' not in s:
        s = s.replace('</style>', CSS + '</style>', 1)
    if 'data-theme-toggle' not in s:
        if path == 'index.html':
            s = s.replace('<button type="button" class="lang-btn" id="lang-toggle">', BTN('') + '\n      <button type="button" class="lang-btn" id="lang-toggle">', 1)
            s = s.replace('</body>', JS + '\n</body>', 1)
        else:
            s = s.replace('<body>', '<body>\n' + BTN('theme-float'), 1) if '<body>' in s else re.sub(r'(<body[^>]*>)', r'\1\n' + BTN('theme-float').replace('\\','\\\\'), s, 1)
            s = s.replace('</body>', JS + '\n</body>', 1)
    if s != o:
        pathlib.Path(path).write_text(s, encoding='utf-8'); print('patched', path)
