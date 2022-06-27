#!/bin/bash

tmux new -s redis -d
tmux send-keys -t redis 'redis-server redis_config/redis_master.conf' C-m
tmux split-window -t redis
tmux send-keys -t redis 'redis-server redis_config/redis_local_mirror.conf' C-m
tmux a -t redis

tmux kill-server
cd mlh-portfolio

git fetch && git reset origin/main --hard

python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s 
systemctl restart myporfolio.service
