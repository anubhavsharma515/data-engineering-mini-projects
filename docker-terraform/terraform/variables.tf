# run ./set_vars.sh
variable "credentials" {
  description = "File containing service account creds for the project."
}

variable "project" {
  description = "ID of the project"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  #Default needs to be unique across entirety of GCP
  default     = "terraform_demo_dataset_12345"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  #Default needs to be unique across entirety of GCP
  default     = "terraform-demo-bucket-12345"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
