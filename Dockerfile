FROM apache/airflow:2.2.3
RUN python:3.9

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . /app
WORKDIR /app
CMD ["python3", "src/audl_reports_pipeline.py"]
