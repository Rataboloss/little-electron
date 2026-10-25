"""Render all frames of a chapter (30 fps, JPEG) with N parallel browsers.
usage: python3 render16.py <chapter> [workers]"""
import os, json, sys
from multiprocessing import Process
ep = os.path.abspath(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 2; fps = 30
END = json.load(open(os.path.join(ep, 'timing.json')))['end']; n = int(round(END * fps))
os.makedirs(os.path.join(ep, 'frames'), exist_ok=True)
def work(k):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        pg.goto('file://' + ep + '/full.html'); pg.wait_for_timeout(500)
        for i in range(k, n, W):
            pg.evaluate(f'render({i / fps})'); pg.screenshot(path=f'{ep}/frames/f{i:05d}.jpg', type='jpeg', quality=94)
        b.close()
ps = [Process(target=work, args=(k,)) for k in range(W)]
[p.start() for p in ps]; [p.join() for p in ps]
print('frames', n)
