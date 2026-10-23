"""Generate the voiceover and the word/caption/scene timings for one episode.

usage: python3 framework/voice.py episodes/<slug>

Reads episodes/<slug>/episode.json and writes vo.wav + timing.json next to it.

episode.json:
{
  "voice": "am_puck", "speed": 1.0,
  "segments": [
    {"text": "What's inside a computer mouse?", "scene": true},
    {"text": "Let me explain."},
    {"text": "Flip it over:", "scene": true, "pause": 0.2},
    {"text": "38,000 times a second,", "say": "thirty-eight thousand times a second,", "split": [3]}
  ]
}
- text   : caption text (what is shown on screen)
- say    : optional spoken form (numbers, acronyms) when it differs from the caption
- scene  : true -> a new scene starts at this segment (the first segment always starts scene 1)
- pause  : silence after the segment (default 0.22 s after , : and 0.42 s after . ? !)
- split  : optional caption line breaks (word indices); default = auto, max ~5 words per line
"""
import json, os, re, sys
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.environ.get('KOKORO_DIR', os.path.join(HERE, '..', 'models'))
SR = 24000


def trim(x, thr=0.006, pad=0.03):
    idx = np.where(np.abs(x) > thr)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(pad * SR)); b = min(len(x), idx[-1] + int(pad * SR))
    return x[a:b]


def weight(w, spoken=None):
    s = spoken if spoken else w
    return len(re.sub(r"[^\w]", "", s)) + 2


def word_times(text, say, a, b):
    ws = text.split()
    # weight caption words by the spoken length of the matching part, when possible
    if say and len(say.split()) != len(ws):
        sp = say.split(); tot_sp = sum(weight(x) for x in sp)
        # spread the spoken weight proportionally over caption words by their own length
        k = [weight(w) for w in ws]; scale = tot_sp / sum(k); k = [x * scale for x in k]
        # give digits their spoken length
        for i, w in enumerate(ws):
            if re.search(r"\d", w):
                k[i] = weight(w) * 2.4
    else:
        sp = say.split() if say else ws
        k = [weight(w, s) for w, s in zip(ws, sp)]
    tot = sum(k); out = []; acc = 0
    for w, kk in zip(ws, k):
        out.append({"w": w, "t": round(a + (b - a) * acc / tot, 3)}); acc += kk
    return out


def auto_split(ws):
    if len(ws) <= 5:
        return [ws]
    cands = [i + 1 for i, w in enumerate(ws[:-1]) if w["w"][-1] in ",:"]
    mid = len(ws) / 2
    cut = min(cands, key=lambda c: abs(c - mid)) if cands else int(round(mid))
    if cut < 2 or cut > len(ws) - 2:
        cut = int(round(mid))
    return auto_split(ws[:cut]) + auto_split(ws[cut:])


def main(epdir):
    from kokoro_onnx import Kokoro
    ep = json.load(open(os.path.join(epdir, 'episode.json')))
    k = Kokoro(os.path.join(MODEL, 'kokoro-v1.0.onnx'), os.path.join(MODEL, 'voices-v1.0.bin'))
    voice, speed = ep.get('voice', 'am_puck'), ep.get('speed', 1.0)
    audio = [np.zeros(int(0.15 * SR), dtype=np.float32)]; t = 0.15
    segs = []
    for s in ep['segments']:
        x, sr = k.create(s.get('say', s['text']), voice=voice, speed=speed, lang='en-us')
        assert sr == SR
        x = trim(x.astype(np.float32))
        a = t; b = t + len(x) / SR
        audio.append(x); t = b
        p = s.get('pause', 0.42 if s['text'].rstrip()[-1] in '.?!' else 0.22)
        audio.append(np.zeros(int(p * SR), dtype=np.float32)); t += p
        segs.append((a, b, s))
    vo = np.concatenate(audio)
    sf.write(os.path.join(epdir, 'vo24.wav'), vo, SR)
    os.system(f'ffmpeg -y -loglevel error -i "{epdir}/vo24.wav" -ac 1 -ar 48000 "{epdir}/vo.wav"')
    chunks = []; scenes = []
    for i, (a, b, s) in enumerate(segs):
        if i == 0 or s.get('scene'):
            scenes.append(0.0 if i == 0 else round(a, 3))
        ws = word_times(s['text'], s.get('say'), a, b)
        if 'split' in s:
            c = [0] + s['split'] + [len(ws)]; parts = [ws[c[j]:c[j + 1]] for j in range(len(c) - 1)]
        else:
            parts = auto_split(ws)
        for part in parts:
            chunks.append({"start": part[0]["t"], "words": part})
    end = round(segs[-1][1] + 0.85, 2)
    json.dump({"chunks": chunks, "scenes": scenes, "end": end}, open(os.path.join(epdir, 'timing.json'), 'w'))
    print(f'duration {end:.2f}s  scenes {len(scenes)}')
    for c in chunks:
        print(f"{c['start']:6.2f}  " + ' '.join(w['w'] for w in c['words']))
    if end > 59.0:
        print('WARNING: longer than 59 s -> raise "speed" (e.g. 1.05) or shorten the script')


if __name__ == '__main__':
    main(os.path.abspath(sys.argv[1]))
