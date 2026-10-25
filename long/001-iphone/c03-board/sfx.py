import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())
_wh=whoosh
def whoosh(d=0.38): return lp(_wh(d),0.35)*0.35
for s in S[1:]: add(whoosh(),s-0.12,0.45)
add(pop(),0.1,0.5); add(whoosh(0.6),T('computer'),0.4); add(pop(),T('pocket')+0.2,0.6)
add(pop(),S[1]+0.05,0.5); add(boop(300),T('one'),0.5); add(whoosh(0.4),T('two')-0.1,0.5); add(pop(),T('lasagna')-0.2,0.6); add(ding(1320,0.5),T('lasagna'),0.35)
add(thud(),T('soldered')+0.6,0.6); add(pop(),T('frame')-0.2,0.5); [add(tick(),T('soldered')+0.7+i*0.08,0.4) for i in range(8)]; add(pop(),T('started'),0.5)
add(rise(0.8,900,400),T('thirty')-0.4,0.35); add(ding(1568,0.5),T('battery'),0.45)
add(pop(),T('storage')-0.2,0.5); add(pop(),T('main')-0.2,0.5); add(pop(),T('cooling')-0.3,0.5); add(hum(1.5),T('cooling'),0.25)
add(boop(220),T('catch')-0.1,0.5); add(thud(),T('messy'),0.7); add(clac(),T('split'),0.6); add(sizzle(0.8),T('split')+0.1,0.25)
finish()
