#!/bin/bash

sudo apt-get install tmux

tmux kill-server
cd mlh-portfolio

git fetch && git reset origin/main --hard

python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s 
