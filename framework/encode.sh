# usage: bash framework/encode.sh episodes/<slug> output.mp4   (needs mix.wav and frames/)
set -e
cd "$1"
J=$(ffmpeg -i mix.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
II=$(echo "$J"|python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}\")")
ffmpeg -y -loglevel error -i mix.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11:$II:linear=true" -ar 48000 mixn.wav
ffmpeg -y -loglevel error -framerate 30 -i frames/f%05d.png -i mixn.wav -c:v libx264 -pix_fmt yuv420p -crf 20 -preset medium -c:a aac -b:a 192k -movflags +faststart -shortest "$2"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact "$2"
ffmpeg -i "$2" -af ebur128 -vn -f null - 2>&1 | grep -E "^\s+I:" | tail -1
