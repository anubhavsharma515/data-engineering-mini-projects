#Base Image - specifies commands needed to create a container - think template.
FROM python:3.9.1

#Build Layers on top of base image
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

# Add things from local filesystem to container filesystem
# Container can be thought of as a virtual machine
# Shares kernal, but can everything else is isolated, courtesy of image which
# holds all config/binaries/libraries/packages to build a runtime environemnt.
COPY ingest_data.py ingest_data.py

# Command to run as soon as the container is built
ENTRYPOINT [ "python", "ingest_data.py" ]
