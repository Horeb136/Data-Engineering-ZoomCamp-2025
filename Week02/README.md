# Week 2: Workflow Orchestration

## Overview

In Week 2 of the **Data Engineering Zoomcamp**, the focus was on understanding **workflow orchestration**, implementing ETL pipelines, and integrating **Kestra** for managing complex workflows. The week covered conceptual material on orchestration, hands-on projects with PostgreSQL and GCP, and advanced techniques like scheduling and backfilling.

---

## Learning Objectives

- Understand the fundamentals of workflow orchestration and how it differs from automation.
- Learn how Kestra facilitates orchestration through its YAML-based configurations.
- Build ETL pipelines for both PostgreSQL and GCP.
- Schedule workflows and backfill historical data.
- Integrate dbt for data transformations.

---

## Topics Covered

### 1. **Conceptual Material**

#### Introduction to Orchestration

Workflow orchestration involves coordinating tasks, managing dependencies, and ensuring smooth execution of pipelines. Unlike automation, which focuses on individual tasks, orchestration oversees multiple processes to work together as a system. Key use cases include:

- **Data Pipelines**: Ensures consistency and handles dependencies.
- **CI/CD Pipelines**: Automates software delivery processes.
- **Distributed Systems**: Manages microservices and their interactions.
- **Resource Provisioning**: Automates cloud infrastructure setup.

#### Introduction to Kestra

Kestra was introduced as a flexible, event-driven orchestration platform with a user-friendly interface and robust plugin ecosystem. Key features include YAML-based flow definitions, seamless integration with tools, and support for triggers and inputs.

More information: [Kestra Documentation](https://kestra.io/docs)

### 2. **Hands-On Projects**

#### ETL Pipelines with PostgreSQL

- Built workflows to process [NYC taxi data](https://github.com/DataTalksClub/nyc-tlc-data/releases), including data extraction, staging, and merging into PostgreSQL tables.
- Utilized SQL tasks for table creation, updates, and merges.

#### Scheduling and Backfilling

- Set up schedules to run workflows periodically.
- Learned to backfill data for historical periods, focusing on green taxi data for 2019 (because of the heavy size of Yellow taxi).

#### ETL Pipelines with GCP

- Transitioned workflows to Google Cloud, leveraging:
  - **GCS**: For intermediate file storage.
  - **BigQuery**: For querying and storing partitioned data.
- Introduced external tables in BigQuery to query data directly from GCS.

#### Data Transformations with dbt

- Integrated dbt into Kestra workflows to transform raw data.
- Synced dbt models from GitHub and executed `dbt build` commands for model transformations. We will learn more about dbt in Week04

---

## Folder Structure

```plaintext
.
├── docker-compose.yml                    # Setup for Kestra and related services (Postgres and pgAdmin)
├── flows                                 # YAML files defining Kestra workflows
│   ├── 01_getting_started_data_pipeline.yaml
│   ├── 02_postgres_taxi.yaml
│   ├── 02_postgres_taxi_scheduled.yaml
│   ├── 03_postgres_dbt.yaml
│   ├── 04_gcp_kv.yaml
│   ├── 05_gcp_setup.yaml
│   ├── 06_gcp_taxi.yaml
│   ├── 06_gcp_taxi_scheduled.yaml
│   └── 07_gcp_dbt.yaml
├── pgadmin-data                          # Directory for pgAdmin configurations
├── pgpassfile                            # PostgreSQL credentials file
└── servers.json                          # Server configuration for pgAdmin

```

---

## Commands Summary

### Docker Setup

To launch the Docker Compose file (`docker-compose.yml`), follow these steps:

1. Prepare the directory for pgAdmin data storage:

   ```bash
   mkdir -p pgadmin-data
   sudo chown -R 5050:5050 pgadmin-data
   sudo chmod -R 700 pgadmin-data
   ```

2. Launch Docker containers:

   ```bash
   docker-compose up -d
   ```

Access the Kestra web interface at [http://localhost:8080](http://localhost:8080).

### Running Kestra Workflows

Access Kestra’s UI at [http://localhost:8080](http://localhost:8080). Define and execute workflows directly from the web interface.

### pgAdmin Configuration

pgAdmin is pre-configured via the `servers.json` file in the repository. To access pgAdmin:

1. Open [http://localhost:8090](http://localhost:8090) in your browser.

2. Log in using the following credentials:

   - **Email**: [admin@admin.com](mailto\:admin@admin.com)
   - **Password**: root

3. Once logged in, you’ll find a pre-configured server named "Local Database" connecting to the PostgreSQL instance.

---

## Resources

- [My Notes on Notion](https://www.notion.so/Week-2-Workflow-Orchestration-17129780dc4a80148debf61e6453fffe?pvs=4)
- [Kestra Documentation](https://kestra.io/docs)
- [Kestra Installation Guide](https://kestra.io/docs/installation/docker)
- [Course Playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

---

## Notes

- Ensure `.gitignore` includes sensitive files like `pgpassfile`, `pgadmin-data`, and `04_gcp_kv.yaml`.
- Use the Kestra web UI to visualize workflow execution and debug tasks.
- Refer to the `flows` directory for YAML examples of all Kestra workflows.

---

## Acknowledgments

Special thanks to [DataTalks.Club](https://datatalks.club/) and the course instructors for providing this incredible learning opportunity.
