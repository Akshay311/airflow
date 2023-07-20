FROM python:3.8

ENV AIRFLOW_HOME=/usr/local/airflow

USER root

RUN apt-get update -y
RUN apt-get install -y unixodbc-dev wait-for-it

#COPY ./pv_ev  ${AIRFLOW_HOME}

RUN mkdir -p ${AIRFLOW_HOME}
RUN pip3 install 'apache-airflow[mysql,crypto,celery]' mysql-connector-python celery==4.4.6 pymongo pyodbc redis psycopg2-binary

RUN useradd -m -d ${AIRFLOW_HOME} airflow
RUN chown -R airflow: ${AIRFLOW_HOME}
COPY ./requriments.txt ./
RUN python3 -m pip install -r /requriments.txt

USER root

COPY airflow.cfg ${AIRFLOW_HOME}/

WORKDIR ${AIRFLOW_HOME}
