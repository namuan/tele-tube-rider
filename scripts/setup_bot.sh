cd tele-tube-rider || exit
python3 -m venv venv
venv/bin/pip3 install -r requirements/base.txt
bash ./scripts/start_screen.sh tele-tube-rider 'venv/bin/python3 main.py'