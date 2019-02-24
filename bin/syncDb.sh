#!/usr/bin/bash

host=nuke@jarvis

echo 'Dumping DB on remote'
ssh $host 'pg_dump -O -F c flunkybot > flunkybot.dump'
echo 'Sync DB'
scp $host:flunkybot.dump ./

echo 'Drop and recreate DB'
dropdb flunkybot || true
createdb flunkybot

echo 'Restoring DB'
pg_restore -O -j 4 -F c -d flunkybot flunkybot.dump

echo 'Deleting dumps'
rm flunkybot.dump
ssh $host 'rm flunkybot.dump'
echo 'Done'
