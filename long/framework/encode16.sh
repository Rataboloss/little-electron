# usage: bash encode16.sh <chapter>   -> <chapter>/chapter.mp4 (1920x1080, raw mix, no loudnorm: normalise the full video at the end)
set -e
cd "$1"
ffmpeg -y -loglevel error -framerate 30 -i frames/f%05d.jpg -i mix.wav -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium -r 30 -c:a pcm_s16le -ar 48000 -shortest chapter.mkv
ffprobe -v error -show_entries format=duration -of csv=p=0 chapter.mkv
