# Assemble the long 16:9 video and the 9:16 Shorts from the rendered chapters.
# usage (from long/001-iphone): bash assemble.sh
set -e
OUT=out; mkdir -p $OUT
ORDER="c00-intro st01 c01-open st02 c02-brain st03 c03-board st04 c04-faceid st05 c05-battery st06 c06-taptic st07 c07-camera st08 c08-cooling st09 c09-frenemies st10 c10-parts st11 c11-price st12 c12-outro endscreen"

# ---------- long video ----------
INPUTS=""; FILT=""; n=0
for d in $ORDER; do INPUTS="$INPUTS -i $d/chapter.mkv"; FILT="$FILT[$n:v][$n:a]"; n=$((n+1)); done
ffmpeg -y -loglevel error $INPUTS -filter_complex "${FILT}concat=n=$n:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a pcm_s16le $OUT/long_raw.mkv
J=$(ffmpeg -i $OUT/long_raw.mkv -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -vn -f null - 2>&1 | sed -n '/^{/,/^}/p')
LN=$(echo "$J" | python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}\")")
ffmpeg -y -loglevel error -i $OUT/long_raw.mkv -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:$LN:linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart $OUT/little_electron_whats_inside_an_iphone.mp4
rm $OUT/long_raw.mkv
echo "long: $(ffprobe -v error -show_entries format=duration -of csv=p=0 $OUT/little_electron_whats_inside_an_iphone.mp4) s"

# ---------- chapter start times (for the YouTube description) ----------
t=0; : > $OUT/chapters.txt
for d in $ORDER; do
  case $d in c*) printf "%s %s\n" "$t" "$d" >> $OUT/chapters.txt;; esac
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $d/chapter.mkv); t=$(python3 -c "print($t+$dur)")
done

# ---------- Shorts: chapter + tail card, centre crop 608x1080 -> 1080x1920 ----------
for d in c01-open c02-brain c03-board c04-faceid c05-battery c06-taptic c07-camera c08-cooling c09-frenemies c10-parts c11-price; do
  ffmpeg -y -loglevel error -i $d/chapter.mkv -i tail/chapter.mkv -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a];[v]crop=608:1080:656:0,scale=1080:1920:flags=lanczos,setsar=1[vs]" -map "[vs]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a pcm_s16le $OUT/tmp_short.mkv
  J=$(ffmpeg -i $OUT/tmp_short.mkv -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -vn -f null - 2>&1 | sed -n '/^{/,/^}/p')
  LN=$(echo "$J" | python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}\")")
  ffmpeg -y -loglevel error -i $OUT/tmp_short.mkv -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:$LN:linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart $OUT/short_${d}.mp4
  echo "short $d: $(ffprobe -v error -show_entries format=duration -of csv=p=0 $OUT/short_${d}.mp4) s"
done
rm -f $OUT/tmp_short.mkv
cp thumb/thumbnail.png $OUT/thumbnail.png
