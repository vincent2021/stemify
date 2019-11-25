#!/bin/sh
source activate stemify
redis & python3 api.py & rq worker 
echo 'Starting API + Redis Server and a Worker'
