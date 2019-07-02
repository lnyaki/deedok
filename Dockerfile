FROM python:3.7.3-alpine3.10

#------------------------------------------------
#------    Dependency installation phase
#------------------------------------------------
RUN apk --no-cache --update-cache add \
	build-base \
	gcc \
	freetype-dev \
	gfortran \
	libpng-dev \
	musl-dev \
	openblas-dev \
	python \
	python-dev \
	py-pip \
	
	wget
	
 

#------------------------------------------------
#------    Program installation phase
#------------------------------------------------
RUN pip3 install flask==1.0.2 \
	virtualenv

#------------------------------------------------
#------    Source code provisioning 
#------------------------------------------------
WORKDIR /var/www

# Put the content of the app in its proper directory
COPY ./src /var/www/src
COPY requirements.txt . 

#------------------------------------------------
#------    Application installation
#------------------------------------------------
RUN pip3 install -r requirements.txt


#CMD ["ls"]
CMD ["python3", "src/jboost_app.py"]
#CMD ["echo", "i'm a freeman"]