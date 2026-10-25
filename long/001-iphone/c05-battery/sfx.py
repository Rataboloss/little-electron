import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())
_wh=whoosh
def whoosh(d=0.38): return lp(_wh(d),0.35)*0.35
for s in S[1:]: add(whoosh(),s-0.12,0.45)
add(pop(),0.1,0.5); add(rise(0.5,300,700),T('big')-0.2,0.35); add(poof(),T('not')-0.05,0.5)
add(pop(),S[1]+0.05,0.5); add(rise(1.2,300,700),T('4,288')-0.4,0.3); add(pop(),T('oneplus')-0.3,0.5); add(rise(1.2,300,1100),T('7,300')-0.4,0.3); add(thud(),T('ouch')-0.05,0.8)
add(whoosh(0.4),T('sim'),0.5); add(clac(),T('anymore')-0.2,0.5); add(rise(0.8,400,1000),T('space'),0.3); add(ding(1568,0.5),T('battery',2),0.4)
add(pop(),S[3]+0.1,0.4); add(clac(),S[3]+0.3,0.3); add(rise(1.4,300,800),T('lasted')-0.2,0.25); add(rise(1.4,300,700),T('galaxy')-0.2,0.25); add(ding(1320,0.5),T('same'),0.4)
add(pop(),T('chip')-0.2,0.5); add(clac(),T('software')+0.4,0.5); add(chime(),T('software')+0.5,0.35)
add(rise(1.2,300,1200),T('wins')-0.6,0.3); add(chime(),T('twenty-five')+0.5,0.45); add(boop(330),T('fair'),0.4)
add(pop(),T('glue')-0.15,0.5); add(zzzt(0.6),T('electricity')-0.3,0.35)
add(zzzt(1.2),T('twelve')-0.2,0.25); [add(tick(),T('ninety')-0.3+i*0.12,0.35) for i in range(int((T('releases')-T('ninety')+0.3)/0.12))]
add(whoosh(0.5),T('releases'),0.5); add(ding(1568,0.6),T('releases')+0.2,0.45); add(clac(),T('switch')-0.1,0.6)
finish()
