# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5); add(chime(),0.55,0.35)
# 2 crack open
add(clac(),T('crack')-0.05,0.9); add(whoosh(0.5),T('open'),0.6)
add(pop(),T('battery')-0.1,0.6); add(pop(),T('radio')-0.1,0.6); add(pop(),T('speaker')-0.1,0.6); add(pop(),T('microphones')-0.1,0.6)
# 3 safety
add(thud(),T("don't")-0.05,0.7); add(boop(400),T('home')-0.1,0.5); add(pop(),T('lithium')-0.1,0.5)
add(sizzle(1.0),T('fire')-0.3,0.45)
# 4 speaker parts
add(pop(),T('coil')-0.15,0.6); add(pop(),T('membrane')-0.1,0.5); add(pop(),T('magnet')-0.1,0.5); add(ding(1320,0.6),T('magnet')+0.1,0.4)
# 5 push pull
add(zzzt(0.3),T('current')-0.1,0.35)
add(boop(220),T('pushes')-0.1,0.45); add(boop(180),T('pulls')-0.1,0.45)
add(hum(1.2),T('sound')-0.3,0.35); add(chime(),T('sound'),0.45)
# 6 radio
add(pop(),T('bluetooth')-0.3,0.5)
x=T('hops')
while x<S[6]-0.25: add(tick(),x,0.45); x+= (1/24 if x>T('1,600') else 1/8)*3
add(ding(880,0.7),T('1,600')+0.3,0.5)
# 7 noise
add(thud(),T('trick')-0.05,0.6); add(pop(),T('noise')-0.1,0.5)
add(zzzt(0.9),T('microphone')-0.4,0.25); add(beep(0.15,2400),T('listens'),0.25)
# 8 waves
add(rise(0.5,300,900),T('opposite')-0.2,0.45); add(pop(),T('peaks')-0.1,0.4); add(pop(),T('valleys')-0.1,0.4)
add(poof(),T('cancels')-0.1,0.5); add(chime(),T('out'),0.5)
# 9 battery
add(thud(),T('catch')-0.05,0.7); add(pop(),T('tiny',2)-0.2,0.6); add(ding(880,0.7),T('fifty')-0.15,0.5)
for k in range(10): add(tick(),T('hundred')-0.2+k*0.12,0.4)
add(pop(),T('phone')-0.2,0.6)
# 10 Harald
add(pop(),S[9]+0.05,0.5); add(pop(),T('viking')-0.1,0.5); add(ding(1320,0.6),T('harald')-0.15,0.5); add(ding(1568,0.5),T('harald')+0.3,0.35)
add(whoosh(0.5),T('initials')-0.3,0.5); add(chime(),T('runes'),0.45)
# 11 teaser
add(pop(),S[10],0.6); add(pop(),T("what's",2),0.5); add(pop(),T('usb')-0.4,0.5)
finish()
