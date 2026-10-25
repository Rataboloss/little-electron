import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())
_wh=whoosh
def whoosh(d=0.38): return lp(_wh(d),0.35)*0.35
for s in S[1:]: add(whoosh(),s-0.12,0.45)
add(pop(),0.1,0.5); [add(pop(),0.3+i*0.2,0.35) for i in range(3)]; add(clac(),T('spare'),0.4)
add(pop(),S[1]+0.05,0.5); add(boop(260),T('notice'),0.5)
for w in ['battery','screen','cameras','logic']: add(pop(),T(w)-0.2,0.45)
[add(beep(0.06,2200),T('tracked')+i*0.12,0.25) for i in range(4)]
add(whoosh(0.4),T('part',2)-0.2,0.5); add(clac(),T('part',2)+0.3,0.4); add(pop(),T('settings')-0.2,0.4); add(boop(200),T('unknown'),0.6)
add(ding(1568,0.4),T('unlock')-0.2,0.5); [add(tick(),T('five')-0.6+i*0.2,0.35) for i in range(5)]; add(ding(1568,0.4),T('later')-0.1,0.5); add(thud(),T('forgot'),0.5)
add(pop(),T('servers')-0.4,0.5); [add(beep(0.04,1800),T('data')+i*0.3,0.18) for i in range(6)]
add(pop(),T('quality')-0.4,0.5); add(pop(),T('critics')-0.2,0.5)
add(pop(),T('battery',2)-0.3,0.5); add(pop(),T('passport')-0.4,0.5); add(thud(),T('passport')+0.45,0.7)
finish()
