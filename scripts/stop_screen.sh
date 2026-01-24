#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")"/.. && pwd)"
DEFAULT_NAME="$(basename "$PROJECT_DIR")"
SESSION_NAME="${SESSION_NAME:-$DEFAULT_NAME}"

if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  tmux kill-session -t "$SESSION_NAME"
  echo "Stopped tmux session '$SESSION_NAME'."
else
  echo "tmux session '$SESSION_NAME' not found."
fi
#!/usr/bin/env bash
if [[ $# -eq 0 ]]; then
  echo 'COMMAND required as first argument. python3.6 ...'
  exit 0
fi

SCREEN_NAME=$1

screen -X -S "${SCREEN_NAME}" stuff "^C"
screen -X -S "${SCREEN_NAME}" quit

