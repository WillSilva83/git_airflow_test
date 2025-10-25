"""
Simple Bash Example DAG
This DAG runs three simple bash commands in sequence.
"""
from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator


# ----------------------------------------------------------------------
# 1. Define Default Arguments
# These arguments apply to all tasks in the DAG by default.
# ----------------------------------------------------------------------
with DAG(
    dag_id="simple_bash_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None, # Set to None to make it a manually triggered DAG
    catchup=False,
    tags=["example", "bash", "tutorial"],
    doc_md=__doc__,
) as dag:
    
    # ------------------------------------------------------------------
    # 2. Define Tasks
    # Each operator defines a unit of work (a task).
    # ------------------------------------------------------------------

    # Task 1: Print the current date and time
    print_date = BashOperator(
        task_id="print_current_date",
        bash_command="echo 'Current date is: $(date)'",
    )

    # Task 2: Sleep for 5 seconds to simulate a short delay
    sleep_task = BashOperator(
        task_id="sleep_for_5_seconds",
        bash_command="sleep 5",
    )

    # Task 3: Print a simple completion message
    echo_complete = BashOperator(
        task_id="echo_dag_complete",
        bash_command="echo 'The DAG execution is now complete!'",
    )

    # ------------------------------------------------------------------
    # 3. Define Task Dependencies (The Workflow)
    # The '>>' operator is the modern way to define dependencies:
    # Task A >> Task B means Task B runs only after Task A succeeds.
    # ------------------------------------------------------------------
    print_date >> sleep_task >> echo_complete
