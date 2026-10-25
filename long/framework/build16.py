"""Assemble <chapter>/scenes.html into <chapter>/full.html (16:9). usage: python3 build16.py <chapter dir>"""
import sys, os, re
here = os.path.dirname(os.path.abspath(__file__)); ep = os.path.abspath(sys.argv[1])
base = open(os.path.join(here, 'base16.html')).read()
body = open(os.path.join(ep, 'scenes.html')).read()
P = dict(re.findall(r'<!--@(\w+)-->(.*?)<!--@end-->', body, re.S))
out = re.sub(r'<title>.*?</title>', '<title>' + P.get('title', 'Little Electron').strip() + '</title>', base)
for k, tag in [('defs', 'DEFS'), ('svg', 'SVG'), ('ov', 'OV'), ('js', 'JS'), ('f', 'F')]:
    out = out.replace('<!--' + tag + '-->', P.get(k, ''))
out = out.replace('__FONT__', 'file://' + os.path.abspath(os.path.join(here, '..', '..', 'fonts', 'Fredoka.ttf')))
out = out.replace('__TIMING__', open(os.path.join(ep, 'timing.json')).read())
open(os.path.join(ep, 'full.html'), 'w').write(out); print('built', os.path.join(ep, 'full.html'))
