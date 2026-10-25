import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.45)
add(pop(),0.1,0.5); add(hum(1.5),T('dark')-0.3,0.3)
add(pop(),T('projector')-0.3,0.5)
x=T('throws')
while x<T('throws')+1.9: add(tick(),x,0.35); x+=0.06
add(ding(1568,0.6),T('dots')+0.1,0.45); add(rise(0.6,1200,2400),T('infrared')-0.2,0.25)
add(pop(),S[2]+0.1,0.5); add(rise(1.0,300,900),T('builds')-0.2,0.3); add(chime(),T('map'),0.4)
add(pop(),S[3]+0.1,0.3); add(ding(1760,0.6),T('million'),0.5)
add(pop(),S[4]+0.1,0.5); add(boop(160),T('evil')-0.1,0.6); add(pop(),T('twins'),0.5); add(thud(),T('fool'),0.7)
add(pop(),S[5]+0.1,0.4); [add(tick(),T('screen')-0.4+i*0.05,0.4) for i in range(8)]
add(pop(),S[6]+0.1,0.5); add(clac(),T('photo')-0.3,0.4)
[add(tick(),T('133')+i*0.08,0.35) for i in range(20)]; add(boop(240),T('unlocked'),0.5); add(pop(),T('printed')-0.3,0.6); add(ding(1320,0.6),T('fingerprint'),0.45)
finish()
