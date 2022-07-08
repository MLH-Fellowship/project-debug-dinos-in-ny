#!/bin/bash

cd

cd proj-ddinny

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new -d -s site

tmux send -t site "flask run --host=0.0.0.0" Enter

#systemctl daemon-reload
#systemctl restart myportfolio
