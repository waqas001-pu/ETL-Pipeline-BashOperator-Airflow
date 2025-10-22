# ETL Data Pipeline using BashOperator in Apache Airflow

## 📘 Project Overview

This project demonstrates how to design and orchestrate an **ETL (Extract, Transform, Load) data pipeline** using **Apache Airflow** with the **BashOperator**.
It was developed as part of the **IBM Data Engineering** hands-on lab, focusing on automating data consolidation from multiple file formats to a single, transformed dataset.

The pipeline automates data extraction from **CSV**, **TSV**, and **Fixed-Width** text files, applies transformations, and loads the clean data into a **staging area** for analytics.

---

## 🎯 Objectives

The ETL pipeline performs the following operations:

1. **Extract** data from multiple file formats:

   * `vehicle-data.csv`
   * `tollplaza-data.tsv`
   * `payment-data.txt`
2. **Transform** the dataset by standardizing formats and cleaning values.
3. **Load** the consolidated data into the **staging directory**.
4. **Schedule and monitor** the workflow using **Apache Airflow DAG**.

---

## ⚙️ Technologies Used

| Category               | Tools / Technologies         |
| ---------------------- | ---------------------------- |
| Workflow Orchestration | Apache Airflow               |
| Task Automation        | BashOperator                 |
| Programming Language   | Python 3                     |
| Operating System       | Linux / Ubuntu               |
| Commands & Utilities   | `curl`, `tar`, `paste`, `tr` |
| Data Handling          | CSV, TSV, Fixed-Width files  |

---

## 🎗️ Project Structure

```
ETL-Pipeline-BashOperator-Airflow/
│
├── dags/
│   └── ETL_toll_data.py              # Airflow DAG definition file
│
├── staging/                          # Final extracted and transformed data
│
├── screenshots/                      # Evidence of DAG creation and execution
│   ├── dag_args.jpg
│   ├── dag_definition.jpg
│   ├── unzip_data.jpg
│   ├── extract_data_from_csv.jpg
│   ├── extract_data_from_tsv.jpg
│   ├── extract_data_from_fixed_width.jpg
│   ├── consolidate_data.jpg
│   ├── transform.jpg
│   ├── task_pipeline.jpg
│   ├── submit_dag.jpg
│   ├── unpause_trigger_dag.jpg
│   ├── dag_tasks.jpg
│   ├── dag_runs.jpg
│
├── docs/
│   └── IBM_ETL_BashOperator_Project_Report.pdf
│
└── README.md
```

---

## 🧩 Workflow Explanation

| Step | Task ID                         | Operator     | Description                                                                       |
| ---- | ------------------------------- | ------------ | --------------------------------------------------------------------------------- |
| 1    | `unzip_data`                    | BashOperator | Unzips the raw toll dataset into the working directory.                           |
| 2    | `extract_data_from_csv`         | BashOperator | Extracts required fields from `vehicle-data.csv`.                                 |
| 3    | `extract_data_from_tsv`         | BashOperator | Extracts relevant fields from `tollplaza-data.tsv`.                               |
| 4    | `extract_data_from_fixed_width` | BashOperator | Parses data from `payment-data.txt`.                                              |
| 5    | `consolidate_data`              | BashOperator | Merges extracted files into a single dataset using `paste`.                       |
| 6    | `transform_data`                | BashOperator | Converts text fields to uppercase using `tr` and writes to the staging directory. |

---

## 🗂️ DAG Flow

```
unzip_data
    ↓
extract_data_from_csv
    ↓
extract_data_from_tsv
    ↓
extract_data_from_fixed_width
    ↓
consolidate_data
    ↓
transform_data
```

Each step executes sequentially under Airflow’s scheduling and monitoring environment.

---


## 🗼️ Screenshots

Key proof-of-execution images are stored in `/screenshots`, including:

* DAG definition and arguments setup
* Task creation and dependency pipeline
* Airflow DAG list and execution status
* Successful run confirmation from Airflow UI

---

## 🧠 Key Learnings

✅ Built an **end-to-end ETL workflow** using Apache Airflow
✅ Gained hands-on experience with **BashOperator** and Linux commands
✅ Automated **multi-format data extraction and transformation**
✅ Learned **DAG scheduling**, triggering, and monitoring in Airflow
✅ Strengthened understanding of **data engineering pipelines**

---

## 🚀 How to Run This Project

### Prerequisites

* Apache Airflow installed and configured
* Python ≥ 3.8
* Access to Linux or Cloud IDE environment

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ETL-Pipeline-BashOperator-Airflow.git
   cd ETL-Pipeline-BashOperator-Airflow
   ```
2. Copy the DAG file to your Airflow `dags/` directory.
3. Start Airflow:

   ```bash
   airflow standalone
   ```
4. Open **Airflow UI** (default: [http://localhost:8080](http://localhost:8080)) and trigger the DAG `ETL_toll_data`.
5. Verify all tasks execute successfully.

---

## 📜 License

This project is released under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

