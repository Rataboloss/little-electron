"""Assemble episodes/<slug>/scenes.html into a renderable page.
usage: python3 framework/build.py episodes/<slug>
scenes.html holds blocks <!--@title-->..<!--@end-->, @defs, @svg, @ov, @js, @f (see the example episodes).
The page must contain elements with ids t1 (hook title), t10 (teaser title) and big7 (catch title, may be hidden)."""
import sys, os, re
here = os.path.dirname(os.path.abspath(__file__)); ep = os.path.abspath(sys.argv[1])
base = open(os.path.join(here, 'base.html')).read()
body = open(os.path.join(ep, 'scenes.html')).read()
P = dict(re.findall(r'<!--@(\w+)-->(.*?)<!--@end-->', body, re.S))
out = re.sub(r'<title>.*?</title>', '<title>' + P['title'].strip() + '</title>', base)
for k, tag in [('defs', 'DEFS'), ('svg', 'SVG'), ('ov', 'OV'), ('js', 'JS'), ('f', 'F')]:
    out = out.replace('<!--' + tag + '-->', P[k])
out = out.replace('__FONT__', 'file://' + os.path.join(here, '..', 'fonts', 'Fredoka.ttf'))
out = out.replace('__TIMING__', open(os.path.join(ep, 'timing.json')).read())
open(os.path.join(ep, 'full.html'), 'w').write(out); print('built', os.path.join(ep, 'full.html'))
