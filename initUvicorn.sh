#!/usr/bin/bash

UVI_PATH="/home/ubuntu"

echo "Starting init uvicorn process ..."

sudo systemctl stop uvicorn_app.service
sudo rm -rf $UVI_PATH/FastAPI-Telegram/
git clone https://github.com/alanmgg/FastAPI-Telegram.git $UVI_PATH/
