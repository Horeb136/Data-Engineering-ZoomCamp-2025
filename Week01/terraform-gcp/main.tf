terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.14.1"
    }
  }
}

provider "google" {
  #credentials = "./keys/my-creds.json" ##No need because we already export the path of the credentials into the path variables 
  project = "gold-yen-446410-g4"
  region  = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "gold-yen-446410-g4-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1 # In days 
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}