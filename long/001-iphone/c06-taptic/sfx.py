import sys, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())
_wh=whoosh
def whoosh(d=0.38): return lp(_wh(d),0.35)*0.35
for s in S[1:]: add(whoosh(),s-0.12,0.45)
add(pop(),0.1,0.5); add(ding(1320,0.5),T('home'),0.3); add(pop(),T('iphone')+0.1,0.4)
add(boop(400),S[1]+0.5,0.3); add(boop(400),S[1]+2.4,0.3); add(thud(),T('fake')-0.05,0.8)
x=T('weight')-0.2
while x<T('precise')+1.5: add(boop(140),x,0.25); x+=0.35
add(pop(),T('coil')-0.1,0.4); add(tick(),T('finger'),0.6)
x=T('spinning')-0.2
add(hum(T('bee')+0.6-x),x,0.5); add(zzzt(1.0),T('buzzes')-0.1,0.35)
add(beep(0.03,180),T('taps'),0.8); add(beep(0.03,180),T('short'),0.8); add(beep(0.03,180),T('sharp'),0.8); add(beep(0.03,180),T('controlled'),0.8)
x=T('keyboard')
while x<S[6]-0.2: add(tick(),x,0.45); x+=1/6
add(rise(1.5,200,500),T('lying'),0.25); add(thud(),T('finger',2),0.7)
finish()
