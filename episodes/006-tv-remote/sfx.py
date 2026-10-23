# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5)
for k in range(4): add(boop(1700),0.5+k*0.5,0.25)
# 2 open
add(clac(),T('pop')-0.05,0.8); add(whoosh(0.5),T('back'),0.5)
add(pop(),T('keypad')-0.1,0.6); add(pop(),T('circuit')-0.1,0.6)
# 3 flip
add(whoosh(0.5),T('flip')-0.05,0.6); add(pop(),T('over'),0.5); add(ding(1320,0.6),T('carbon')-0.1,0.5)
# 4 press
add(clac(),T('press')+0.1,0.9); add(zzzt(0.3),T('bridges'),0.35); add(ding(1568,0.6),T('gold'),0.45)
# 5 grid
add(pop(),T('chip')-0.1,0.5)
x=T('chip')
while x<T('pressed')-0.2: add(tick(),x,0.5); x+=1/6
add(clac(),T('tell')-0.2,0.6); add(chime(),T('pressed')-0.1,0.5)
# 6 LED
add(thud(),T('trick')-0.05,0.6); add(pop(),T('led')-0.1,0.5); add(thud(),T('see')-0.1,0.5); add(rise(0.5,300,900),T('infrared')-0.1,0.5)
# 7 code
add(pop(),T('38,000')-0.15,0.6); add(hum(1.2),T('38,000'),0.25)
for i,b in enumerate([1,0,1,1,0,1,0,0]): add(boop(1400 if b else 700),T('code')-0.3+i*0.06,0.35)
for k in range(8): add(tick(),T('every')+k*0.08,0.5)
# 8 TV
add(pop(),S[7],0.5); add(ding(1320,0.6),T('flicker')-0.1,0.45)
add(pop(),T('lamps')-0.15,0.5); add(pop(),T('sunlight')-0.15,0.5); add(thud(),T('confuse')-0.1,0.6)
# 9 phone
add(pop(),T('want')-0.1,0.6); add(whoosh(0.5),T('point')-0.3,0.5); add(clac(),T('press',2),0.6); add(chime(),T('flash')-0.1,0.55)
# 10 1955
add(pop(),T('first')-0.1,0.5); add(ding(880,0.7),T('1955')-0.1,0.5); add(rise(0.4,500,1200),T('basically')-0.1,0.5); add(pop(),T('flashlight')-0.1,0.6)
# 11 teaser
add(pop(),S[10],0.6); add(pop(),T("what's",2),0.5); add(pop(),T('mouse')-0.4,0.5)
finish()
