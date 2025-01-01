variable "project_id" {
  description = "The ID of the GCP project"
  default     = "gold-yen-446410-g4"
}

variable "project_region" {
  description = "Region of the project"
  default     = "us-central1"
}

variable "credentials_file" {
  description = "Path to the GCP credentials JSON file"
  default     = "./keys/my-creds.json"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "BigQuery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "gold-yen-446410-g4-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}