PROJECT=${HOME}/projects/jboost
all:
	echo "hello"	

start : 
		echo $(PROJECT)/bin/activate \
	#start neo4j
	 	cd ${HOME}/bin-programs/neo4j-community-3.2.0/bin \
		./neo4j start &
	#start webserver
	 	python $(PROJECT)/src/jboost_app.py &
