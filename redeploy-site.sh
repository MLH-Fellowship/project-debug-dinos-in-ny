#!/bin/bash

cd /root/mlh-portfolio

git fetch && git reset --hard  origin/main

source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl restart myportfolio.service
