# Airflow Custom Operator

This project provides a custom Apache Airflow operator, `CustomLivyOperator`, designed to extend the functionality of Airflow workflows. 

## Overview

The `CustomLivyOperator` attempts to fix the integration issues observed when using the LivyOperator in Microsoft Fabric. The issues would require workarounds that utilised LivyHooks to put update code in the DAG - which is untidy.

This version specialises the normal LivyOperator to embed these changes so that the DAG can be much more clean.


## Installation

To install the custom operator, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd airflow-custom-operator
pip install -r requirements.txt
```

## Usage

To use the `CustomLivyOperator` in your Airflow DAG, you can import it as follows:

```python
from airflow import DAG
from datetime import datetime
from custom_operator.my_custom_operator import CustomLivyOperator

with DAG(
    dag_id="Livy_Custom_Op",
    schedule_interval="@daily",
    start_date=datetime(2025, 4, 7, hour=14, minute=28),
    catchup=False,
) as dag:


    livy_job = CustomLivyOperator(
     task_id="livy_job",
     fabric_conn_id = "fabric",
     livy_conn_id='fabric_livy', # Livy Connection with api endpoint (not including /batches or /sessions) as host
     file='abfss://JJTest2@onelake.dfs.fabric.microsoft.com/lhJohn.Lakehouse/Files/code/spark-query-lh.py', # File in lakehouse to run
     polling_interval=60,
     dag=dag
    )
    
    livy_job
```

## Testing

Unit tests for the `CustomLivyOperator` are located in the `tests` directory. You can run the tests using:

```bash
pytest tests/
```

## Building for the Package for Distribution
The package needs to be built and it is this package that the Airflow DAGs use:

```bash
python setup.py sdist bdist_wheel
```

## Use Inside Apache Airflow in Microsoft Fabric
To use this inside a Microsoft Fabric hosted Apache Airflow session, two things need to be done:

1. The source for the DAGs needs to be GitHub hosted.
2. The path to the packaged Operator needs to be added to the Apache Airflow requirements.

### Using a GitHub Repository
The source for all code for Airflow needs to point to a source code source. As this repository is in GitHub, this needs to be set. The Airflow configuration is read-only, so if the repository is public-faced, then no credentials are needed. For private repositories, credentials will be needed.
![alt text](./images/airflow-git.png "Airflow GitHub Settings")

### Apache Airflow requirements
This is configured in the environment variables section and a path the the packaged version of the Operator needs to be added.
This follows a specific pattern as described in [Install a Private Package as a requirement in Apache Airflow job](https://learn.microsoft.com/en-us/fabric/data-factory/apache-airflow-jobs-install-private-package)
![alt text](./images/airflow-requirements.png "Airflow requirements")

## License

This project is licensed under the MIT License. See the LICENSE file for details.
