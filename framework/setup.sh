# One-time setup of a fresh session (about 1 minute). Run from the repo root: bash framework/setup.sh
set -e
pip install --break-system-packages -q kokoro-onnx soundfile numpy playwright 2>&1 | tail -1 || true
python3 -c "from playwright.sync_api import sync_playwright" || (pip install --break-system-packages -q playwright && python3 -m playwright install chromium)
mkdir -p models fonts
[ -s models/kokoro-v1.0.onnx ] || curl -sSL -o models/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
[ -s models/voices-v1.0.bin ] || curl -sSL -o models/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
[ -s fonts/Fredoka.ttf ] || curl -sSL -o fonts/Fredoka.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/fredoka/Fredoka%5Bwdth%2Cwght%5D.ttf"
which ffmpeg >/dev/null
echo setup ok
