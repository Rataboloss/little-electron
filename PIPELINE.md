# Little Electron — daily Short pipeline

Little Electron is an English-language YouTube/TikTok channel of ~55 s animated electronics
explainers ("What's inside…?" teardowns). Episodes 5 and 6 in `episodes/` are the reference
for quality, structure and art direction: read both `scenes.html` files before writing a new one.

## Daily run (scheduled task)

0. **Repo** — if `/home/claude/little-electron` doesn't exist, attach `Rataboloss/little-electron`
   (push access) and clone it there; work from the repo root. The voice is Kokoro `am_puck`.

1. **Setup** — from the repo root: `bash framework/setup.sh` (installs Kokoro, downloads the
   voice model and the Fredoka font from GitHub; ~1 min).
2. **Topic** — take the first unchecked item in `topics.md`. The previous episode's teaser
   ("Next time: what's inside a …?") already names it: always follow the teaser.
3. **Script** (English, 140–155 words, must stay under 59 s) — same arc as episodes 5–6:
   hook "What's inside a X? Let me explain." → open it up → part 1 → "But here's the trick:" →
   part 2 → "Here's the catch:" → one surprising number or comparison → one history fact →
   "Next time: what's inside a Y?" (Y = the next item in `topics.md`).
   Short sentences, one idea each, concrete numbers. Add a safety line when opening the object
   could be dangerous (mains voltage, capacitors, lithium cells, microwave ovens: say NOT to open).
4. **Fact-check** every number, date and name with web searches. Keep a `facts.md` in the episode
   folder: claim → source URL. If a claim can't be confirmed, rewrite it.
5. **Voice** — write `episodes/NNN-slug/episode.json` (format documented at the top of
   `framework/voice.py`; mark the first segment of each of ~10 scenes with `"scene": true`, use
   `"say"` for numbers/acronyms), then `python3 framework/voice.py episodes/NNN-slug`.
   If it warns > 59 s, raise `speed` (max 1.08) or cut words.
6. **Animation** — write `episodes/NNN-slug/scenes.html` (blocks @title @defs @svg @ov @js @f,
   one `<g id="sN">` + `<div class="ov" id="oN">` + `F[N-1]` per scene), then
   `python3 framework/build.py …` and `python3 framework/snap.py … <12-16 times>`; **look at
   `sheet.png`** and fix overlaps, empty frames and anything off-centre. Repeat until clean.
   Anchor animations on spoken words with `T('word', n)` (n = nth occurrence, lowercase, trailing
   punctuation stripped). A missing anchor throws `anchor xxx` on load.
7. **Sound** — copy an example `sfx.py`, re-place the effects on this episode's words,
   `python3 episodes/NNN-slug/sfx.py episodes/NNN-slug`.
8. **Render** — `python3 framework/render.py episodes/NNN-slug` (~4 min, run it in the
   background), then `bash framework/encode.sh episodes/NNN-slug little_electron_<slug>.mp4`.
   Check: duration < 60 s, 1080×1920, loudness ≈ −14/−15 LUFS; grab ~10 frames from the MP4 and look.
9. **Commit** — copy the MP4 to `videos/`, commit the episode folder (NOT `frames/`, `*.wav`,
   `full.html`) and push. Public URL of the video:
   `https://raw.githubusercontent.com/<owner>/<repo>/main/videos/little_electron_<slug>.mp4`
10. **Ask the owner** — send the MP4 (SendUserFile, status proactive) with the title,
    description and tags, and ask in one line: "OK to publish?" Then stop and wait.
    Do NOT publish without an explicit yes. If they ask for changes, apply them and resend.
11. **Publish** (only after yes) — Metricool brand id `7594471`, timezone Europe/Paris:
    - YouTube Short at the next 16:00 (`youtubeData`: type "short", title, tags,
      category "SCIENCE_TECHNOLOGY", madeForKids false), text = description;
    - TikTok at the next 18:00 (`tiktokData`: title, privacyOption "PUBLIC_TO_EVERYONE",
      isAigc true), text = one-line hook + 5 hashtags;
    - Instagram Reel at the next 10:00 (`instagramData`: type "REEL", showReelOnFeed true,
      isAiGenerated true), text = hook line + 1-2 sentences + a question + 3-5 hashtags.
    `media` = the raw.githubusercontent URL. Check `getScheduledPosts` first so you never post
    twice the same day; if a slot is taken, use the next free day.
12. **Close the loop** — tick the topic in `topics.md` (with the date), add a line to `log.md`,
    commit and push.

## Sound
- Transition whooshes must stay soft (user feedback 25/10/2026): use `whoosh()` from sfxlib as is, gain ≤ 0.5, never boost it.

## Art direction (do not drift)
- 1080×1920, background `#1B1F3B`, circuit traces in `#2A3060`; font Fredoka (600/700).
- Palette: yellow `#FFD23F` (titles, highlights), cyan `#3DDCFF` (labels, current, chips),
  pink `#FF8FA3` (warnings, "BEEP!"-style shouts), red `#FF5C5C` (LEDs/IR), gold `#F2C14E`
  (copper/gold), greys `#EEF0F7 #D5D9E6 #B9C0CF #8A90A6`, darks `#2B2F45 #3A4170 #14172C`,
  PCB green `#1F8A6A / #2FB088`.
- Mascot: `<use href="#m">` (happy) and `#mw` (shocked), 230–300 px, appears 3–4 times.
- Layout: chapter chip at top (150 px), big word at 230–380 px, drawing in 450–1250 px,
  captions from 1290 px down (keep that zone clear).
- Hook: object pops in, mascot peeks, "WHAT'S INSIDE?" letter by letter. Teaser: next object
  with a "?", mascot slides in.
- Flat shapes, rounded corners, no gradients, no real brand logos or product names.
