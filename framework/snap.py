"""Render check frames. usage: python3 framework/snap.py episodes/<slug> 1.5 4.0 ...  -> episodes/<slug>/sheet.png"""
import sys, os
from playwright.sync_api import sync_playwright
ep = os.path.abspath(sys.argv[1]); times = [float(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + ep + '/full.html'); pg.wait_for_timeout(400)
    if errs: print('PAGE ERRORS:', errs); sys.exit(1)
    for i, t in enumerate(times):
        pg.evaluate(f'render({t})'); pg.screenshot(path=f'{ep}/snap{i:02d}.png')
    b.close()
n = len(times); cols = min(8, n); rows = (n + cols - 1) // cols
os.system(f'ffmpeg -y -loglevel error -i "{ep}/snap%02d.png" -vf "scale=216:-1,tile={cols}x{rows}" "{ep}/sheet.png" && rm -f "{ep}"/snap*.png')
print('errors:', errs, '->', ep + '/sheet.png')
