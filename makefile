update_database:
	python3 src/GameStatsExtraction.py

# generate_player_report: 

# generate_team_report:


update_airflow:
	python3 ~/airflow/dags/audl_reports_pipeline.py
	# python3 pipeline.py
	airflow db migrate
	airflow scheduler

