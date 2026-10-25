"""Write sfx.py into every chapter folder, then run them all. usage: python3 sfx_all.py"""
import os, subprocess
here = os.path.dirname(os.path.abspath(__file__))
HEAD = "import sys, os\nexec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','framework','sfxlib.py')).read())\nfor s in S[1:]: add(whoosh(),s-0.12,0.45)\n"
FX = {
'c00-intro': """add(pop(),0.1,0.6); add(chime(),0.5,0.3); add(pop(),T('twelve')-0.2,0.6); add(ding(1320,0.6),T('dollars'),0.4)
add(boop(300),T('today')-0.1,0.5); add(clac(),T('open')-0.05,0.8)
add(boop(500),T('relax')-0.1,0.5); add(rise(0.8,500,900),T('relax')+0.2,0.25); add(ding(1568,0.5),T('drawing'),0.45)
add(pop(),T("i'm")-0.1,0.6); add(chime(),T('electron'),0.35); add(pop(),T('different')-0.15,0.55); add(pop(),T('android')-0.15,0.55); add(thud(),T('android')+0.05,0.4)
for w in ['lasagna','drop','fake','passport']: add(pop(),T(w)-0.3,0.6)
add(boop(220),T('passport'),0.4); add(rise(0.5,400,1400),T('crack')-0.4,0.35); add(clac(),T('crack'),0.9)""",
'c01-open': """add(pop(),0.1,0.5); [add(pop(),0.5+i*0.25,0.4) for i in range(3)]
add(pop(),T('pentalobe')-0.4,0.6); [add(tick(),T('five')+i*0.16,0.6) for i in range(5)]
add(boop(260),T('useless')-0.2,0.5); add(thud(),T('useless'),0.7); add(pop(),T('since')-0.1,0.5)
add(hum(2.5),T('heat')-0.1,0.3); add(pop(),T('croissant')-0.3,0.6); add(rise(1.0,300,1200),T('seventy')-0.6,0.3)
add(whoosh(0.5),T('screen',2)-0.4,0.6); add(thud(),T('expensive'),0.7); [add(ding(1760,0.3),T('expensive')+i*0.15,0.25) for i in range(3)]
add(whoosh(0.5),T('opens')-0.2,0.5); add(pop(),T('coil')-0.2,0.5); add(boop(180),T('coil')+0.3,0.45)
[add(pop(),T('ifixit')+i*0.15,0.4) for i in range(4)]
[add(clac(),T('cracked')-0.1+i*0.22,0.6) for i in range(3)]
add(thud(),T('maybe'),0.7)""",
'c02-brain': """add(pop(),0.15,0.5); add(pop(),T('brain')-0.2,0.6); add(ding(1320,0.6),T('apple')-0.1,0.5); add(boop(200),T('kind')-0.1,0.5)
add(pop(),0.05,0.5); add(pop(),T('designed')-0.2,0.5); add(pop(),T('built')-0.2,0.5); add(rise(0.5,500,1500),T('two-nanometer')-0.3,0.35)
[add(tick(),S[2]+0.4+i*0.16,0.4) for i in range(15)]; add(ding(1568,0.5),S[2]+2.8,0.4)
add(pop(),S[3]+0.2,0.4); add(pop(),S[3]+0.35,0.4); add(pop(),S[3]+0.5,0.4); add(whoosh(0.4),T('buy'),0.4)
[add(pop(),T('mediatek')+i*0.25,0.45) for i in range(4)]
add(ding(1320,0.5),T('going'),0.4); add(ding(1568,0.5),T('modem'),0.4); add(ding(1760,0.5),T('wireless'),0.4)
add(boop(200),T('well'),0.5); add(whoosh(0.5),T('us')-0.2,0.5); add(clac(),T('qualcomm',2),0.5)
add(pop(),T('breakups')-0.3,0.5); add(clac(),T('time')-0.1,0.8)""",
'c03-board': """add(pop(),0.1,0.5); add(whoosh(0.6),T('computer'),0.4); add(pop(),T('pocket')+0.2,0.6)
add(pop(),S[1]+0.05,0.5); add(boop(300),T('one'),0.5); add(whoosh(0.4),T('two')-0.1,0.5); add(pop(),T('lasagna')-0.2,0.6); add(ding(1320,0.5),T('lasagna'),0.35)
add(thud(),T('soldered')+0.6,0.6); add(pop(),T('frame')-0.2,0.5); [add(tick(),T('soldered')+0.7+i*0.08,0.4) for i in range(8)]; add(pop(),T('started'),0.5)
add(rise(0.8,900,400),T('thirty')-0.4,0.35); add(ding(1568,0.5),T('battery'),0.45)
add(pop(),T('storage')-0.2,0.5); add(pop(),T('main')-0.2,0.5); add(pop(),T('cooling')-0.3,0.5); add(hum(1.5),T('cooling'),0.25)
add(boop(220),T('catch')-0.1,0.5); add(thud(),T('messy'),0.7); add(clac(),T('split'),0.6); add(sizzle(0.8),T('split')+0.1,0.25)""",
'c04-faceid': """add(pop(),0.1,0.5); add(hum(1.5),T('dark')-0.3,0.3)
add(pop(),T('projector')-0.3,0.5)
x=T('throws')
while x<T('throws')+1.9: add(tick(),x,0.35); x+=0.06
add(ding(1568,0.6),T('dots')+0.1,0.45); add(rise(0.6,1200,2400),T('infrared')-0.2,0.25)
add(pop(),S[2]+0.1,0.5); add(rise(1.0,300,900),T('builds')-0.2,0.3); add(chime(),T('map'),0.4)
add(pop(),S[3]+0.1,0.3); add(ding(1760,0.6),T('million'),0.5)
add(pop(),S[4]+0.1,0.5); add(boop(160),T('evil')-0.1,0.6); add(pop(),T('twins'),0.5); add(thud(),T('fool'),0.7)
add(pop(),S[5]+0.1,0.4); [add(tick(),T('screen')-0.4+i*0.05,0.4) for i in range(8)]
add(pop(),S[6]+0.1,0.5); add(clac(),T('photo')-0.3,0.4)
[add(tick(),T('133')+i*0.08,0.35) for i in range(20)]; add(boop(240),T('unlocked'),0.5); add(pop(),T('printed')-0.3,0.6); add(ding(1320,0.6),T('fingerprint'),0.45)""",
'c05-battery': """add(pop(),0.1,0.5); add(rise(0.5,300,700),T('big')-0.2,0.35); add(poof(),T('not')-0.05,0.5)
add(pop(),S[1]+0.05,0.5); add(rise(1.2,300,700),T('4,288')-0.4,0.3); add(pop(),T('oneplus')-0.3,0.5); add(rise(1.2,300,1100),T('7,300')-0.4,0.3); add(thud(),T('ouch')-0.05,0.8)
add(whoosh(0.4),T('sim'),0.5); add(clac(),T('anymore')-0.2,0.5); add(rise(0.8,400,1000),T('space'),0.3); add(ding(1568,0.5),T('battery',2),0.4)
add(pop(),S[3]+0.1,0.4); add(clac(),S[3]+0.3,0.3); add(rise(1.4,300,800),T('lasted')-0.2,0.25); add(rise(1.4,300,700),T('galaxy')-0.2,0.25); add(ding(1320,0.5),T('same'),0.4)
add(pop(),T('chip')-0.2,0.5); add(clac(),T('software')+0.4,0.5); add(chime(),T('software')+0.5,0.35)
add(rise(1.2,300,1200),T('wins')-0.6,0.3); add(chime(),T('twenty-five')+0.5,0.45); add(boop(330),T('fair'),0.4)
add(pop(),T('glue')-0.15,0.5); add(zzzt(0.6),T('electricity')-0.3,0.35)
add(zzzt(1.2),T('twelve')-0.2,0.25); [add(tick(),T('ninety')-0.3+i*0.12,0.35) for i in range(int((T('releases')-T('ninety')+0.3)/0.12))]
add(whoosh(0.5),T('releases'),0.5); add(ding(1568,0.6),T('releases')+0.2,0.45); add(clac(),T('switch')-0.1,0.6)""",
'c06-taptic': """add(pop(),0.1,0.5); add(ding(1320,0.5),T('home'),0.3); add(pop(),T('iphone')+0.1,0.4)
add(boop(400),S[1]+0.5,0.3); add(boop(400),S[1]+2.4,0.3); add(thud(),T('fake')-0.05,0.8)
x=T('weight')-0.2
while x<T('precise')+1.5: add(boop(140),x,0.25); x+=0.35
add(pop(),T('coil')-0.1,0.4); add(tick(),T('finger'),0.6)
x=T('spinning')-0.2
add(hum(T('bee')+0.6-x),x,0.5); add(zzzt(1.0),T('buzzes')-0.1,0.35)
add(beep(0.03,180),T('taps'),0.8); add(beep(0.03,180),T('short'),0.8); add(beep(0.03,180),T('sharp'),0.8); add(beep(0.03,180),T('controlled'),0.8)
x=T('keyboard')
while x<S[6]-0.2: add(tick(),x,0.45); x+=1/6
add(rise(1.5,200,500),T('lying'),0.25); add(thud(),T('finger',2),0.7)""",
'c07-camera': """add(pop(),0.1,0.5); add(clac(),T('blades')-0.1,0.5); add(sizzle(0.4),T('blades'),0.3)
add(pop(),S[1]+0.1,0.4)
x=S[1]+0.2
while x<S[2]-0.3: add(tick(),x,0.25); x+=0.45
add(ding(1320,0.5),T('pupil'),0.35); add(pop(),T('six')-0.1,0.5)
add(pop(),T('tip')-0.2,0.5); add(zzzt(0.6),T('electromagnets')-0.3,0.3)
add(rise(0.8,400,1500),T('seven')-0.3,0.35); add(chime(),T('light'),0.3); add(whoosh(0.4),T('closed')-0.2,0.4); add(ding(1568,0.5),T('sharp'),0.35)
add(pop(),T('android')-0.1,0.5); add(pop(),T('galaxy'),0.45); add(ding(1320,0.5),T('2018'),0.4)
add(boop(220),T('catch')-0.1,0.5); add(clac(),T('stuck'),0.6); add(thud(),T('whole'),0.6)
add(whoosh(0.8),T('flew')-0.2,0.6); add(chime(),T('free'),0.45)""",
'c08-cooling': """add(pop(),0.1,0.5); add(hum(1.5),0.3,0.3); add(clac(),T('fan'),0.5)
add(pop(),T('water')-0.2,0.7); add(ding(1568,0.5),T('water',2),0.4)
add(pop(),T('chamber')-0.2,0.5); [add(pop(),T('pure')+i*0.1,0.3) for i in range(7)]; add(zzzt(1.4),T('laser-welded')-0.3,0.25); add(sizzle(1.3),T('laser-welded')-0.2,0.3)
add(sizzle(1.0),T('heats')-0.2,0.25); add(whoosh(0.8),T('vapor',2),0.35); add(ding(880,0.6),T('cools'),0.3); add(boop(500),T('back'),0.35); add(chime(),T('starts'),0.3)
add(pop(),T('three')-0.2,0.5); add(rise(0.9,300,1000),T('forty')-0.3,0.35); add(ding(1568,0.5),T('hot'),0.35)
add(pop(),S[4]+0.05,0.5); add(beep(0.15,880),T('2018')-0.2,0.25); add(beep(0.15,1320),T('2018'),0.25)
add(pop(),T('party'),0.5); add(chime(),T('cake'),0.5); add(pop(),T('cake')-0.3,0.6)""",
'c09-frenemies': """add(pop(),0.15,0.4); add(pop(),0.3,0.4); add(pop(),0.45,0.4); add(pop(),0.6,0.4)
add(pop(),S[1]+0.05,0.5); add(rise(0.5,500,1200),T('tech'),0.25); add(boop(300),T('who')-0.1,0.5)
add(pop(),T('samsung')-0.2,0.5); add(pop(),T('lg')-0.2,0.5); add(thud(),T('samsung',2),0.6)
add(pop(),T('rival')-0.2,0.5); add(boop(160),T('awkward'),0.4); [add(tick(),T('dinner')+0.3+i*0.6,0.3) for i in range(3)]
add(pop(),T('lightning')-0.3,0.5); add(pop(),T('europe')-0.2,0.5); add(clac(),T('usb-c')-0.1,0.5); add(ding(1320,0.6),T('next'),0.4)
add(pop(),T('samsung',3)-0.3,0.5); add(pop(),T('brussels')-0.4,0.5); add(chime(),T('brussels'),0.4)""",
'c10-parts': """add(pop(),0.1,0.5); [add(pop(),0.3+i*0.2,0.35) for i in range(3)]; add(clac(),T('spare'),0.4)
add(pop(),S[1]+0.05,0.5); add(boop(260),T('notice'),0.5)
for w in ['battery','screen','cameras','logic']: add(pop(),T(w)-0.2,0.45)
[add(beep(0.06,2200),T('tracked')+i*0.12,0.25) for i in range(4)]
add(whoosh(0.4),T('part',2)-0.2,0.5); add(clac(),T('part',2)+0.3,0.4); add(pop(),T('settings')-0.2,0.4); add(boop(200),T('unknown'),0.6)
add(ding(1568,0.4),T('unlock')-0.2,0.5); [add(tick(),T('five')-0.6+i*0.2,0.35) for i in range(5)]; add(ding(1568,0.4),T('later')-0.1,0.5); add(thud(),T('forgot'),0.5)
add(pop(),T('servers')-0.4,0.5); [add(beep(0.04,1800),T('data')+i*0.3,0.18) for i in range(6)]
add(pop(),T('quality')-0.4,0.5); add(pop(),T('critics')-0.2,0.5)
add(pop(),T('battery',2)-0.3,0.5); add(pop(),T('passport')-0.4,0.5); add(thud(),T('passport')+0.45,0.7)""",
'c11-price': """add(pop(),0.1,0.5); add(pop(),T('worth')-0.2,0.5); [add(ding(2093,0.2),0.6+i*0.25,0.2) for i in range(5)]
x=T('counterpoint')
while x<T('410')-0.3: add(tick(),x,0.3); x+=0.09
add(ding(1320,0.6),T('410'),0.45); add(rise(1.0,300,1200),T('sold'),0.3); add(thud(),T('1,199'),0.6)
for w in ['design','software','shipping','marketing','tables','profit']: add(pop(),T(w)-0.25,0.45)
add(pop(),T('research',2)-0.25,0.45); add(ding(2093,0.3),T('profit'),0.35)
add(zzzt(0.5),T('exploded')-0.6,0.3); add(poof(),T('exploded'),0.9); add(thud(),T('exploded'),0.6)
add(rise(0.8,300,900),T('trendforce'),0.25); add(ding(1568,0.5),T('38'),0.4)
add(boop(260),T('price'),0.4); add(whoosh(0.3),T('hundred')-0.3,0.4); add(ding(2093,0.3),T('hundred'),0.4); add(boop(180),T('funny'),0.4)""",
'c12-outro': """add(pop(),0.1,0.5); add(pop(),T('android')-0.3,0.5); add(clac(),T('wrong'),0.6); add(chime(),T('different'),0.35)
for w in ['chip','modem','cooling','software']: add(pop(),T(w)-0.2,0.45)
add(hum(1.2),T('together'),0.25); add(chime(),T('together')+0.3,0.3)
[add(pop(),S[2]+0.1+i*0.08,0.35) for i in range(5)]; add(pop(),T('bigger'),0.4); add(pop(),T('brands'),0.4); add(pop(),T('freedom'),0.4)
add(pop(),S[3]+0.05,0.5); add(chime(),T('philosophies'),0.35)
add(pop(),T('subscribe')-0.2,0.6); add(ding(1568,0.4),T('subscribe')+0.1,0.5); add(ding(1568,0.4),T('subscribe')+0.35,0.4); add(rise(0.8,400,1200),T('grow')-0.4,0.3)
add(pop(),T('foldable')-0.4,0.6); add(chime(),T('see'),0.45)""",
'tail': """add(pop(),0.1,0.6); add(pop(),0.3,0.5); add(chime(),0.4,0.4)""",
}
for i in range(1, 13):
    FX[f'st{i:02d}'] = "add(whoosh(0.5),0.0,0.6); add(pop(),0.15,0.5); add(ding(1320,0.5),0.3,0.3); add(whoosh(0.4),1.35,0.4)"
FX['endscreen'] = "add(chime(),0.2,0.4); [add(pop(),0.5+i*0.15,0.35) for i in range(3)]"
for k, v in FX.items():
    d = os.path.join(here, k)
    open(os.path.join(d, 'sfx.py'), 'w').write(HEAD + v + "\nfinish()\n")
print('written', len(FX))
