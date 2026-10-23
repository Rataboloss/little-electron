"""Render every frame (30 fps) then mux with mixn.wav. usage: python3 framework/render.py episodes/<slug>"""
import os, json, sys
from playwright.sync_api import sync_playwright
ep = os.path.abspath(sys.argv[1]); fps = 30
END = json.load(open(os.path.join(ep, 'timing.json')))['end']; n = int(END * fps)
os.makedirs(os.path.join(ep, 'frames'), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + ep + '/full.html'); pg.wait_for_timeout(500)
    for i in range(n):
        pg.evaluate(f'render({i / fps})'); pg.screenshot(path=f'{ep}/frames/f{i:05d}.png')
    b.close()
print('frames', n)
