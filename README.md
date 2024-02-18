# AUDL Report

Generating reports for AUDL

## Technologies

- Markdown
    * `tufte` Databases
- Database
    * [planetscale](https://planetscale.com/docs/onboarding/create-an-account)
    * [supabase](https://supabase.com/dashboard/projects)
- Hosts
    * [railway](https://docs.railway.app/)
    * [vercel]
- Data Orchestration
    * [airflow]
    * [dagster]
- Data Observability
    * [the great expectation]



M1:
1. Computing in R with reticulate
2. Outputing PDF directly

M2: [ THIS ]
1. Generate csv in python 
2. Create PDF in RMarkdown with tufte

**Requirements**

- railway: nodejs, npm
- astro

## Bundles


**Bundle 1: Game Descriptive Analysis**

- [ ] Which player over/under/stable performed?
- [ ] Play by play (?)
- [ ] 

**Bundle 2: Player Profile - Scouting**

- [ ] Summary
    - Full name
    - number
    - AUDL debut
    - accolades: top 10 in <stats> for <season>; all-stars; mvp
- [ ] Throws distributions
    - what types of throws player throws
    - what types of throws player receives
- [ ] Player distributions
    - to who player pass to
    - from who player receives from

**Bundle 3: Team Profile - Scouting**

- [ ] Top throwers/receivers
    - for each types of throw
- [ ] Connections to watch out
- [ ] Social Network Analysis

**Bundle 4: Player/Team Optimization**

- [ ] Lineup Optimization
- [ ] What path player A should emulate to become the best 


**Bundle 5: Meta Analysis (Free)**

- [ ] Clustering: which player/teams are the most similar
- [ ] Learning optimal strategy through reinforcement learning
- [ ] Find you siamese player

## Supabase setup

Create `.env` file with `SUPABASE_URL` and `SUPABASE_KEY`


```
# astro installation
curl -sSL install.astronomer.io | sudo bash -s

# --- airflow installation
pip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
airflow db migrate

# export AIRFLOW_HOME
export AIRFLOW_HOME="/home/yukikongju/airflow/dags"

# create user login
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

# 
airflow scheduler
airflow webserver --port 8080

# create symbolic link to ~/airflow/dags/audl_reports_pipeline.py
ln -s audl_reports_pipeline.py ~/airflow/dags/audl_reports_pipeline.py
```


## Ressources

**Tufte**

- [Tufte - RMarkdown](https://bookdown.org/yihui/rmarkdown/tufte-handouts.html)

**Supabase**

- [Supabase crashcourse for python dev](https://www.youtube.com/watch?v=M6cfT2pqpSc)

**Docker**

- [build an AI app with fastAPI and Docker](https://www.youtube.com/watch?v=iqrS7Q174Ac)
- [Supabase Functions](https://www.youtube.com/watch?v=MJZCCpCYEqk&t=122s)

**Apache Airflow**

- [Airflow - Fundamental Concepts](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html)
- [A complete Apache Airflow tutorial](https://theaisummer.com/apache-airflow-tutorial/)
- [Airflow Setup with Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [Airflow Installation with PyPi](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)
- [Data with Marc - Getting Started with Airflow for Beginners](https://www.youtube.com/watch?v=xUKIL7zsjos)

**Astro**

- [Astro Installation]()

