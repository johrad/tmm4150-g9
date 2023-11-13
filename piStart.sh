#!/bin/bash
echo "starting program"
cd "~/tmm4150-g9"
while true; do
    python3 main.py
    if [[ "$?" != "0" ]]; then
        echo "main.py crashed with exit code $?. Respawning.." >&2
        sleep 1
    else
        break
    fi
    echo "crashed, restarting"
done
