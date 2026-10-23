# usage: python3 episodes/<slug>/sfx.py episodes/<slug>
import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','framework','sfxlib.py')).read())
for s in S[1:]: add(whoosh(),s-0.12,0.5)
# 1 hook
add(pop(),0.05,0.6); add(pop(),1.0,0.5)
for k in range(3): add(boop(1800),0.4+k*0.8,0.3)
# 2 twist / open
add(whoosh(0.6),T('twist')-0.1,0.6)
for k in range(5): add(tick(),T('twist')+k*0.22,0.6)
add(clac(),T('open')-0.05,0.8)
add(pop(),T('maze')-0.1,0.6); add(ding(1568,0.6),T('chamber'),0.5)
# 3 sensor
add(pop(),T('infrared')-0.1,0.6); add(pop(),T('sensor')-0.1,0.6)
add(thud(),T('trick')-0.05,0.5); add(rise(0.5,400,1000),T('face')-0.2,0.5); add(pop(),T('other')-0.1,0.6)
# 4 clean air
add(hum(T('reaches',1)+1.0-T('clean')),T('clean'),0.35); add(boop(500),T('never')+0.1,0.5); add(boop(400),T('never')+0.35,0.5)
# 5 smoke
add(whoosh(0.9),T('drifts')-0.2,0.7)
for k in range(6): add(tick(),T('scatter')+k*0.09,0.6)
add(chime(),T('sensor',3)-0.1,0.5)
# 6 alarm
add(zzzt(0.3),T('chip')-0.05,0.4)
for k in range(3): add(beep(),T('alarm')+k*0.35,1.0)
add(hum(1.4),T('buzzing'),0.3)
for k in range(3): add(beep(0.15),T('85')+0.1+k*0.25,0.8)
add(thud(),T('85')-0.05,0.6)
# 7 catch
add(thud(),T('catch')-0.05,0.7)
add(whoosh(1.0),T('maze',2),0.5); add(pop(),T('in',4)-0.1,0.6)
add(ding(1046,0.6),T('daylight')-0.2,0.4); add(clac(),T('out')-0.05,0.6)
# 8 battery
add(pop(),T('battery')-0.1,0.6)
st=T('flashes')-0.3; x=st
while x<S[8]-0.2: add(boop(1500),x,0.4); x+=1.1
# 9 americium
add(sizzle(1.0),T('radioactive')-0.2,0.5); add(pop(),T('americium')-0.1,0.6); add(thud(),T('never',2)-0.05,0.7)
# 10 half
add(pop(),S[9],0.6); add(rise(0.5,300,700),T('dying')-0.1,0.5); add(rise(0.4,700,350),T('half')-0.5,0.5); add(chime(),T('half')-0.1,0.5)
# 11 teaser
add(pop(),S[10],0.6); add(pop(),T("what's",2),0.5); add(pop(),T('remote')-0.4,0.5)
for k in range(3): add(boop(1800),S[10]+0.5+k*0.5,0.3)
finish()
