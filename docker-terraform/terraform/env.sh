#!/bin/bash
# Sets the project ID to build the resources into
export TF_VAR_project=$(gcloud config get project)
export TF_VAR_credentials="./creds.json"
