# Makefile for Docker commands

URL = https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz

build-postgres:
	docker run -d postgres:13

build-pgadmin:
	docker run -d dpage/pgadmin4

build-image:
	docker build -t taxi_ingest:v001 .

build-network:
	docker network create pg-network

build-pg-container: build-network
	docker-compose up -d

build-container: build-pg-container build-image
	docker run -d \
	--network=pg-network \
	taxi_ingest:v001 \
	--user=root \
	--password=root \
	--host=pgdatabase \
	--port=5432 \
	--db=ny_taxi \
	--table_name=yellow_taxi_trips \
	--url=$(URL)
