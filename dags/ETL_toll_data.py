from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# -----------------------------
# Default arguments
# -----------------------------
default_args = {
    'owner': 'waqas',
    'start_date': datetime(2025, 10, 10),  # Use a fixed date
    'email': ['dummy_email@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# -----------------------------
# Define DAG
# -----------------------------
with DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task 1: Unzip data
    unzip_data = BashOperator(
        task_id='unzip_data',
        bash_command='tar -xvf /home/airflow/gcs/data/tolldata.tgz -C /home/airflow/gcs/data/',
    )

    # Task 2: Extract CSV data
    extract_data_from_csv = BashOperator(
        task_id='extract_data_from_csv',
        bash_command="""
        cut -d',' -f1,2,3,4 /home/airflow/gcs/data/vehicle-data.csv > /home/airflow/gcs/data/csv_data.csv
        """,
    )

    # Task 3: Extract TSV data
    extract_data_from_tsv = BashOperator(
        task_id='extract_data_from_tsv',
        bash_command="""
        cut -f5,6,7 /home/airflow/gcs/data/tollplaza-data.tsv | tr "\\t" "," > /home/airflow/gcs/data/tsv_data.csv
        """,
    )

    # Task 4: Extract Fixed Width data
    extract_data_from_fixed_width = BashOperator(
        task_id='extract_data_from_fixed_width',
        bash_command="""
        awk '{print substr($0, 59, 3) "," substr($0, 63, 3)}' /home/airflow/gcs/data/payment-data.txt > /home/airflow/gcs/data/fixed_width_data.csv
        """,
    )

    # Task 5: Consolidate extracted data
    consolidate_data = BashOperator(
        task_id='consolidate_data',
        bash_command="""
        paste -d',' \
        /home/airflow/gcs/data/csv_data.csv \
        /home/airflow/gcs/data/tsv_data.csv \
        /home/airflow/gcs/data/fixed_width_data.csv \
        > /home/airflow/gcs/data/extracted_data.csv
        """,
    )

    # Task 6: Transform data
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command="""
        awk -F',' 'BEGIN{OFS=","} { $4=toupper($4); print }' \
        /home/airflow/gcs/data/extracted_data.csv > /home/airflow/gcs/data/staging/transformed_data.csv
        """,
    )

    # Task dependencies
    unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
