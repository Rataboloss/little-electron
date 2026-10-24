# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5)
for k in range(3): add(clac(),0.6+k*0.8,0.35)
# 2 open
add(whoosh(0.5),T('open'),0.6); add(clac(),T('shell')-0.05,0.6)
add(pop(),T('circuit')-0.1,0.6); add(pop(),T('switches')-0.1,0.6); add(pop(),T('wheel')-0.1,0.6)
# 3 switch
add(pop(),S[2]+0.05,0.5); add(pop(),T('metal')-0.1,0.5)
add(clac(),T('snaps')-0.05,1.0); add(zzzt(0.3),T('snaps')+0.05,0.35); add(ding(1568,0.6),T('contact'),0.45)
# 4 wheel: one tick per notch
st=T('turns')-0.1; x=st
while x<S[4]-0.25: add(tick(),x,0.7); x+=1/2.6
add(pop(),T('encoder')-0.1,0.5); add(pop(),T('chip')-0.15,0.5); add(chime(),T('pulse')-0.1,0.45)
# 5 flip + light
add(thud(),T('trick')-0.05,0.6); add(whoosh(0.5),T('flip')-0.05,0.6); add(pop(),T('over'),0.5)
add(rise(0.5,300,900),T('red')-0.1,0.45); add(pop(),T('low')-0.1,0.5)
for i in range(4): add(pop(),T('bump')-0.2+i*0.05,0.35)
add(ding(1320,0.6),T('shadow')-0.1,0.5)
# 6 camera
add(pop(),T('camera')-0.15,0.6)
x=T('snaps',2)
while x<S[6]-0.2: add(tick(),x,0.6); x+=0.2
add(chime(),T('thousand'),0.5)
# 7 compare
add(pop(),T('picture')-0.2,0.5); add(ding(1320,0.6),T('last')-0.1,0.45); add(whoosh(0.5),T('slide')-0.3,0.5); add(chime(),T('movement')-0.1,0.5)
# 8 glass
add(thud(),T('catch')-0.05,0.7); add(pop(),T('glass')-0.15,0.6); add(boop(500),T('nothing')+0.1,0.5); add(boop(400),T('nothing')+0.35,0.5)
for k in range(3): add(pop(),T('lost')-0.2+k*0.1,0.4)
# 9 pixels
for k in range(8): add(tick(),T('photos')-0.4+k*0.12,0.45)
add(pop(),T('tiny',3)-0.2,0.5); add(ding(880,0.7),T('18')-0.15,0.5); add(pop(),T('pixels')-0.15,0.6)
# 10 1964
add(pop(),T('first')-0.2,0.5); add(ding(880,0.7),T('1964')-0.15,0.5); add(pop(),T('wooden')-0.1,0.5); add(pop(),T('metal',2)-0.1,0.5)
add(whoosh(0.5),T('cord')-0.25,0.5); add(rise(0.4,500,1200),T('tail')-0.15,0.5); add(pop(),T('tail'),0.6)
# 11 teaser
add(pop(),S[10],0.6); add(pop(),T("what's",2),0.5); add(pop(),T('earbuds')-0.4,0.5)
finish()
