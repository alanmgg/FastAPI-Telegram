#!/usr/bin/bash

UVI_BIN_DIR="/usr/local/bin"
UVI_PATH="/home/ubuntu/FastAPI-Telegram"
UVI_LOGS="/home/ubuntu/logs"

echo "Starting uvicorn process ..."

$UVI_BIN_DIR/uvicorn --app-dir $UVI_PATH apiServer:app --reload > $UVI_LOGS/uvicorn.log 2>&1