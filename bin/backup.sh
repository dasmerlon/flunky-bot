#!/usr/bin/bash
host=nuke@jarvis
timestamp=`date +%Y-%m-%d_%H-%m`
dest="backup/flunkybot/flunkybot_${timestamp}.dump"

ssh $host "mkdir -p ~/backup/flunkybot"
ssh $host "pg_dump -F c flunkybot > ~/$dest"
