#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")"/.. && pwd)"
DEFAULT_NAME="$(basename "$PROJECT_DIR")"
SESSION_NAME="${SESSION_NAME:-$DEFAULT_NAME}"

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is not installed. On macOS, install via: brew install tmux"
  exit 1
fi

if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  echo "tmux session '$SESSION_NAME' already exists."
else
  tmux new-session -d -s "$SESSION_NAME"
  echo "Started tmux session '$SESSION_NAME'."
fi

if [[ "${ATTACH:-0}" == "1" ]]; then
  tmux attach -t "$SESSION_NAME"
fi
#!/usr/bin/env bash
if [[ $# -eq 0 ]] ; then
    echo 'COMMAND required as first argument. python3.6 ...'
    exit 0
fi

SCREEN_NAME=$1
SCREEN_CMD=$2

screen -X -S "${SCREEN_NAME}" stuff "^C"
screen -X -S "${SCREEN_NAME}" quit
screen -d -m -S "${SCREEN_NAME}"
screen -S "${SCREEN_NAME}" -p 0 -X stuff "${SCREEN_CMD}$(printf \\r)"