#!/bin/bash
echo "starting program"
while true; do
    python3 pi-side/main.py
    if [[ "$?" != "0" ]]; then
        echo "main.py crashed with exit code $?. Respawning.." >&2
        sleep 1
    else
        break
    fi
    echo "crashed, restarting"
done
