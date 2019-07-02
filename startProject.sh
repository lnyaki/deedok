#!/bin/sh

# Activate virtualenv (seems not to work in script)
#source bin/activate

# Start docker elements (neo4j, redis)
./scripts/dockerStart.sh

# Start server
./scripts/startApp.sh
