# **Week 4: Analytics Engineering**

This week focuses on transforming raw data into structured analytical views using **dbt (Data Build Tool)**. We cover **data modeling**, the **ELT workflow**, and **dbt fundamentals** like materialization, testing, and deployment. By the end of this week, I’ll have built and deployed a functional **dbt project**, preparing data for real-world analysis and visualization.

---

## **Prerequisites**

Before diving into Analytics Engineering, ensure that:
- You have a running data warehouse (**BigQuery** or **Postgres**) – I am using **BigQuery**.
- Data ingestion pipelines are set up – See [Week 2 Notes](https://www.notion.so/Week-2-Workflow-Orchestration-17129780dc4a80148debf61e6453fffe?pvs=21) on how to use **Kestra** for workflow orchestration.
- The following datasets are ingested:
  - **Yellow taxi data** (2019, 2020)
  - **Green taxi data** (2019, 2020)
  - **FHV data** (2019)

🔗 **[Kestra Workflow for FHV Ingestion](https://github.com/Horeb136/Data-Engineering-ZoomCamp-2025/blob/main/Week02/flows/gcp_fhv_scheduled.yaml)**  
🔗 **[Quick Upload Hack (Video)](https://www.youtube.com/watch?v=Mork172sK_c&list=PLaNLNpjZpzwgneiI-Gl8df8GCsPYp_6Bs)**

---

## **Project Structure**
```
.
├── dbt_cloud_setup.md       # Instructions for setting up dbt with BigQuery
├── taxi_rides_ny       # The folder of the dbt hang on project
  ├── models/                  # SQL models for dbt transformations
  │   ├── staging/             # Staging models (cleaning raw data)
  │   ├── core/                # Fact and Dimension tables
  ├── macros/                  # Custom dbt macros for transformations
  ├── seeds/                   # CSV seed data (lookup tables)
  ├── packages.yml             # Installed dbt packages
  ├── dbt_project.yml          # Main dbt project configuration
└── README.md                # This file
```

---

## **My Notes**
🔗 [**Complete Notes on Notion**](https://spotted-hardhat-eea.notion.site/Week-4-Analytics-Engineering-18929780dc4a808692e4e0ee488bf49c?pvs=74)

---

## **Acknowledgments**
This week’s learning is based on **DataTalks.Club’s Data Engineering ZoomCamp**. Special thanks to:
- **Alexey Grigorev** & **Victoria Perez Mola**

Check out the **[official DataTalks.Club GitHub repo](https://github.com/DataTalksClub/data-engineering-zoomcamp)** for more details.
