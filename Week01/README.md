
# Week 1: Containerization and Infrastructure as Code

## Overview

This week focuses on setting up the development environment, containerization with Docker, interacting with PostgreSQL, and managing infrastructure using Terraform. The goal is to create and manage databases and cloud resources effectively.

---

## Learning Objectives

- Set up Docker and PostgreSQL containers.
- Ingest data into PostgreSQL using Python scripts.
- Configure pgAdmin to interact with the database.
- Automate infrastructure setup with Terraform.
- Introduce GCP console and services.

---

## Prerequisites

- **Tools Installed:**
  - Python 3 (recommended: Anaconda)
  - Docker and Docker Compose
  - Google Cloud SDK
  - Terraform
  - Git
- Basic knowledge of SQL and Python.

---

## Folder Structure

```
── docker_sql
│   ├── docker-compose.yaml       # Docker setup for PostgreSQL and pgAdmin
│   ├── ingest_data.py            # Python script for data ingestion
│   ├── pipeline.py               # Just a draft file for data ingestion 
│   ├── pgpassfile                # Credentials for PostgreSQL (excluded via .gitignore)
│   ├── servers.json              # pgAdmin server configuration file
│   ├── output.csv                # Example processed data in csv format (excluded via .gitignore)
│   ├── output.parquet            # Example data in parquet format (excluded via .gitignore)
── terraform-gcp
│   ├── main.tf                   # Terraform config for GCP resources
│   ├── variables.tf              # Terraform variable definitions
│   ├── keys/my-creds.json        # GCP credentials (excluded via .gitignore)
```

---

### Docker Setup
To launch the Docker Compose file (`docker-compose.yaml`), follow these steps:

1. Create a `.env` file to store environment variables (e.g., `POSTGRES_PASSWORD`).  
2. Create a `pgpassfile` for PostgreSQL credentials:
   ```plaintext
   pgdatabase:5432:ny_taxi:root:<password>
   ```
   (Replace `<password>` with your PostgreSQL password.)

3. Prepare the directory for pgAdmin data storage:
   ```bash
   mkdir -p pgadmin-data
   sudo chown -R 5050:5050 pgadmin-data
   sudo chmod -R 700 pgadmin-data
   ```

4. Launch Docker containers:
   ```bash
   docker-compose up -d
   ```

### Terraform Setup
1. Create a **GCP Account** and enable billing.

2. Create a **GCP Project**.

3. Create a **Service Account** and download the key file.

4. Place the key file in the `keys/` directory as `my-creds.json`.

5. Initialize Terraform and apply configurations:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

---

## Topics Covered

### 1. Docker and PostgreSQL

- **Docker Basics:** Create and manage containers.
- **PostgreSQL Setup:** Run PostgreSQL inside Docker and connect via `pgcli`.
- **Data Ingestion:** Use Python scripts to load data into PostgreSQL.
- **pgAdmin Configuration:** Manage databases visually through pgAdmin.

### 2. Infrastructure as Code with Terraform

- Create a Google Cloud Platform (GCP) bucket and a BigQuery database.
- Manage resources with Terraform scripts (`main.tf` and `variables.tf`).
- Use `terraform init`, `plan`, and `apply` to deploy resources.

### 3. Virtual Machines and Remote Access

- Set up GCP Virtual Machines.
- Use SSH keys and configure remote access with VS Code.
- Install Jupyter, Terraform, and Docker on VM.

---


## Commands Summary
**See my [notes on notion](https://spotted-hardhat-eea.notion.site/Week-1-Containerization-and-Infrastructure-as-Code-15729780dc4a80a08288e497ba937a37) for more details.**

---

## Resources

- [My Notes on Notion](https://spotted-hardhat-eea.notion.site/Week-1-Containerization-and-Infrastructure-as-Code-15729780dc4a80a08288e497ba937a37)
- [Course Playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [Course Materials](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)

---

## Notes

- Ensure `.gitignore` excludes sensitive files like credentials and database data.

- Use SSH keys for secure access to remote VMs.

- Refer to the `docker_sql` and `terraform-gcp` directories for examples and scripts.


---

## Acknowledgments

Special thanks to [DataTalks.Club](https://datatalks.club/) and the course instructors for providing the resources and materials.
