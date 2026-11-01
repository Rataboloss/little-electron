# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5); add(chime(),0.55,0.35)
add(pop(),T('electrons')-0.1,0.4); add(ding(1320,0.6),T('cages')-0.05,0.4)
# 2 case off
add(clac(),T('pull')-0.05,0.8); add(whoosh(0.5),T('case')-0.1,0.5)
add(pop(),T('controller')-0.1,0.6); add(pop(),T('memory')-0.1,0.6); add(pop(),T('crystal')-0.1,0.6)
for k in range(6): add(tick(),T('crystal')+0.2+k*0.12,0.35)
# 3 billions of cells
for k in range(14): add(tick(),S[2]+0.1+k*0.05,0.3)
add(ding(880,0.7),T('billions')-0.1,0.5)
# 4 floating gate in glass
add(pop(),T('floating')-0.15,0.6); add(rise(0.5,400,1000),T('wrapped')-0.1,0.4)
add(pop(),T('silicon')-0.1,0.5); add(chime(),T('glass',2),0.45)
# 5 high voltage
add(zzzt(0.6),T('voltage')-0.15,0.4)
for i in range(7): add(pop(),T('pushes')-0.3+i*0.12+0.6,0.35)
add(thud(),T('glass',3)+0.1,0.5)
# 6 zero / one / years
add(ding(660,0.6),T('zero')-0.1,0.5); add(ding(990,0.6),T('one')-0.1,0.5)
for k in range(10): add(tick(),T('years')+k*0.083,0.35)
add(boop(300),T('unplugged'),0.5); add(thud(),T('unplugged')+0.15,0.5)
# 7 wear
add(thud(),T('trick')-0.05,0.6)
add(sizzle(0.8),T('wears')-0.1,0.35); add(clac(),T('wears')+0.2,0.4); add(clac(),T('down')-0.1,0.45)
add(boop(220),T('down')-0.2,0.45)
# 8 wear levelling
x=T('spreads')
while x<T('none')-0.1: add(tick(),x,0.3); x+=0.1
add(chime(),T('first'),0.5)
# 9 flash
add(pop(),T('flash')-0.1,0.6); add(poof(),T('block')-0.05,0.5)
add(pop(),T('camera')-0.3,0.5); add(clac(),T('flash',2)-0.05,0.6); add(ding(1568,0.5),T('flash',2),0.4)
# 10 teaser
add(pop(),S[9],0.6); add(pop(),T("what's")+0.1,0.5); add(hum(0.9),T('toothbrush')-0.5,0.35)
finish()
