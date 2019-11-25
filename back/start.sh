#!/bin/sh
source activate stemify
echo 'Starting API + Redis Server and a Worker'
redis & python3 api.py & rq worker 
