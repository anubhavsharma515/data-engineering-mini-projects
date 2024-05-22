terraform {
  
  ## Providers maintain and create the "resource" code, basically an import package statement 
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

## Basically initializing an instance of the imported package
provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

## components of infrastructure
resource "google_storage_bucket" "terraform-demo-bucket" {

  ## Infra properties
  name          = var.gcs_bucket_name
  location      = var.region
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 30
    }
  action {
    type = "Delete"
    }
  }
}

resource "google_bigquery_dataset" "terraform-demo-dataset" {

  dataset_id = var.bq_dataset_name
  location   = var.region
}
