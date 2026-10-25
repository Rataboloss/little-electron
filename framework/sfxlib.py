import numpy as np, wave, json, re
sr=48000; rng=np.random.default_rng(7)
import sys, os; EPDIR=os.path.abspath(sys.argv[1]); D=json.load(open(os.path.join(EPDIR,'timing.json')))
W=[(re.sub(r"^[^\w]+|[.,:?!]+$","",w["w"].lower()),w["t"]) for c in D["chunks"] for w in c["words"]]
def T(k,n=1):
    c=0
    for w,t in W:
        if w==k:
            c+=1
            if c==n: return t
    raise KeyError(k)
def rd(p):
    w=wave.open(p); return np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
def wr(p,a):
    a=np.clip(a,-1,1); w=wave.open(p,'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype(np.int16).tobytes()); w.close()
def t(d): return np.arange(int(d*sr))/sr
def lp(x,a):
    y=np.zeros_like(x); s=0.0; a=np.broadcast_to(a,x.shape)
    for i in range(len(x)): s+=a[i]*(x[i]-s); y[i]=s
    return y
def whoosh(d=0.38):
    # softened on 25/10/2026 (user found transitions too loud): darker filter, ~4x quieter
    tt=t(d); n=rng.standard_normal(len(tt)); env=np.sin(np.pi*tt/d)**2
    return lp(lp(n,0.02+0.25*np.sin(np.pi*tt/d))*env*1.2,0.35)*0.35
def pop():
    tt=t(0.09); f=300+700*tt/0.09; ph=2*np.pi*np.cumsum(f)/sr; return np.sin(ph)*np.exp(-tt*40)*0.8
def tick():
    tt=t(0.03); return np.sin(2*np.pi*2400*tt)*np.exp(-tt*150)*0.6
def clac():
    tt=t(0.15); n=rng.standard_normal(len(tt))*np.exp(-tt*120); th=np.sin(2*np.pi*120*tt)*np.exp(-tt*25); return n*0.6+th*0.8
def zzzt(d=0.25):
    tt=t(d); sq=np.sign(np.sin(2*np.pi*110*tt)); n=rng.standard_normal(len(tt))*0.4; trem=0.6+0.4*np.sign(np.sin(2*np.pi*30*tt))
    env=np.minimum(1,tt/0.01)*np.minimum(1,(d-tt)/0.04); return lp((sq+n)*trem,0.25)*env*0.7
def ding(f=1320,d=0.9):
    tt=t(d); return (np.sin(2*np.pi*f*tt)+0.4*np.sin(2*np.pi*f*1.5*tt))*np.exp(-tt*5)*0.5
def chime():
    out=np.zeros(int(1.2*sr))
    for i,f in enumerate([880,1108.7,1318.5,1760]):
        s=ding(f,0.8); o=int(i*0.07*sr); out[o:o+len(s)]+=s*0.6
    return out
def thud():
    tt=t(0.4); return np.sin(2*np.pi*70*tt*(1-0.3*tt))*np.exp(-tt*9)*1.1+rng.standard_normal(len(tt))*np.exp(-tt*80)*0.4
def sizzle(d=1.2):
    tt=t(d); n=rng.standard_normal(len(tt)); h=np.diff(np.concatenate([[0],n])); crack=(rng.random(len(tt))>0.9993)*rng.standard_normal(len(tt))*3
    return (h*0.25+lp(crack,0.5))*np.sin(np.pi*tt/d)
def boop(f):
    tt=t(0.14); return np.sin(2*np.pi*f*tt)*np.exp(-tt*18)*0.7
def hum(d):
    tt=t(d); env=np.minimum(1,tt/0.4)*np.minimum(1,(d-tt)/0.4)
    return (np.sin(2*np.pi*110*tt)+0.3*np.sin(2*np.pi*220*tt))*(0.7+0.3*np.sin(2*np.pi*1.1*tt))*env*0.35
def rise(d=0.6,f0=300,f1=1500):
    tt=t(d); f=f0+(f1-f0)*tt/d; ph=2*np.pi*np.cumsum(f)/sr; return np.sin(ph)*np.sin(np.pi*tt/d)*0.35
def poof():
    tt=t(0.6); n=rng.standard_normal(len(tt)); return lp(n,0.08)*np.exp(-tt*6)*2.0
def beep(d=0.22,f=3100):
    tt=t(d); env=np.minimum(1,tt/0.005)*np.minimum(1,(d-tt)/0.01); return lp(np.sign(np.sin(2*np.pi*f*tt)),0.3)*env*0.25
S=D["scenes"]
vo=rd(os.path.join(EPDIR,'vo.wav')); L=int(D["end"]*sr); mix=np.zeros(L); mix[:min(L,len(vo))]+=vo[:L]
fx=np.zeros(L)
def add(sig,at,g=1.0):
    o=max(0,int(at*sr)); e=min(L,o+len(sig)); fx[o:e]+=sig[:e-o]*g
def finish():
    global mix
    m=mix+fx*0.55
    m*=0.89/np.max(np.abs(m))
    wr(os.path.join(EPDIR,'mix.wav'),m); print('mix ok')
