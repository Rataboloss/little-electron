# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5); add(chime(),0.55,0.35)
add(rise(0.5,400,1000),T('plastic')-0.3,0.35); add(boop(260),T('contacts')-0.3,0.5)
# 2 opened
add(clac(),T('open')-0.05,0.8); add(whoosh(0.5),T('open')+0.1,0.5)
add(pop(),T('battery')-0.1,0.6); add(pop(),T('circuit')-0.1,0.6); add(pop(),T('two')-0.05,0.6); add(pop(),T('coils')-0.05,0.6)
add(beep(0.15,2400),T('puncture')-0.25,0.3); add(beep(0.15,2400),T('puncture')+0.05,0.3)
# 3 base coil
add(poof(),T('hides')-0.1,0.4)
for k in range(6): add(tick(),T('hides')+0.1+k*0.07,0.35)
add(ding(880,0.7),T('coil')-0.1,0.45)
# 4 alternating current, field
add(hum(2.6),T('flips')-0.2,0.25)
for k in range(6): add(tick(),S[3]+0.5*k,0.3)
add(chime(),T('magnetic')-0.1,0.45)
# 5 through plastic
add(zzzt(0.35),T('electricity')-0.2,0.4); add(thud(),T("can't"),0.5)
add(rise(0.6,300,1200),T('magnetism')-0.2,0.4)
add(ding(1320,0.6),T('flow'),0.4)
for k in range(5): add(pop(),T('holes')-0.2+k*0.22+0.3,0.3)
add(chime(),T('gets'),0.4)
# 6 trick
add(thud(),T('trick')-0.05,0.6); add(clac(),T('spinning')-0.1,0.5); add(boop(220),T('motor')-0.1,0.45)
# 7 vibration
add(hum(2.2),T('pushes')-0.2,0.35); add(ding(1568,0.6),T('31,000')+0.6,0.4)
x=T('31,000')-0.3
while x<T('31,000')+0.6: add(tick(),x,0.3); x+=0.06
# 8 timer
x=T('chip')
while x<S[8]-0.2: add(tick(),x,0.3); x+=0.15
add(ding(990,0.6),T('minutes'),0.45)
# 9 history
add(pop(),T('1954')-0.3,0.6); add(clac(),T('wall')-0.05,0.6); add(zzzt(0.3),T('wall'),0.35)
# 10 teaser
add(pop(),S[9],0.6); add(pop(),T("what's")+0.1,0.5); add(beep(0.1,1800),T('scale')-0.4,0.3)
finish()
