#!/bin/sh
echo 'Starting API + Redis Server and a Worker'
redis-server & python3 api.py & rq worker 
