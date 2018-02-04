sudo docker run -t -d \
    --publish=9000:7474 --publish=9001:7687 \
    --volume=$HOME/projects/jboost/neo4j/data:/data \
    --volume=$HOME/projects/jboost/neo4j/logs:/logs \
    --volume=$HOME/projects/jboost/neo4j/conf:/conf \
    --name jboost_neo4j neo4j:3.0

sudo docker run -t -d \
    --publish=9009:6379 \
    --volume=$HOME/projects/jboost/redis/data:/data \
    --name jboost_redis redis:4.0.7
