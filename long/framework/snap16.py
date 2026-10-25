"""Check frames. usage: python3 snap16.py <chapter> t1 t2 ...
-> sheet.png (16:9 thumbnails with the Short crop outlined) and sheet_short.png (what the Short shows)."""
import sys, os
from playwright.sync_api import sync_playwright
ep = os.path.abspath(sys.argv[1]); times = [float(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + ep + '/full.html#guide'); pg.wait_for_timeout(400)
    if errs: print('PAGE ERRORS:', errs); sys.exit(1)
    for i, t in enumerate(times):
        pg.evaluate(f'render({t})'); pg.screenshot(path=f'{ep}/snap{i:02d}.png')
    b.close()
n = len(times); cols = min(4, n); rows = (n + cols - 1) // cols
os.system(f'ffmpeg -y -loglevel error -i "{ep}/snap%02d.png" -vf "scale=480:-1,tile={cols}x{rows}:padding=6:color=white" "{ep}/sheet.png"')
cols2 = min(8, n); rows2 = (n + cols2 - 1) // cols2
os.system(f'ffmpeg -y -loglevel error -i "{ep}/snap%02d.png" -vf "crop=608:1080:656:0,scale=243:432,tile={cols2}x{rows2}:padding=4:color=white" "{ep}/sheet_short.png" && rm -f "{ep}"/snap*.png')
print('errors:', errs, '->', ep + '/sheet.png')
