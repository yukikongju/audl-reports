
[link to pipeline](https://docs.google.com/drawings/d/1IdWRcp2mRWDZX7EwqnIUUZ3jFeHZ4ynZm599IL8uahc/edit)

Todos:
- [O] ETL Pipeline
    - [O] Define Tables schema in mysql:
	- [X] `player_throws` table
	- [X] `player_game_stats` table: individual statistic for each game
	- [X] `team_game_stats` table
    - [X] define row level security in supabase
    - [X] rpc for distinct game_ids
    - [ ] later: create read tables policy for authenticated users
- [.] Setup data orchestration: Airflow
    - [X] write airflow
    - [ ] activate dag in 'list'
    - [ ] Docker file
	- [ ] docker composer
- [ ] setup data validation: the great expectation
- [ ] Player Profile Report
    - [ ] Makefile to generate profile report from terminal
- [ ] Team Profile Report
    - [ ] Makefile to generate team report

**Errors**

- [ ] team_ext_id missing

```
postgrest.exceptions.APIError: {'code': '23502', 'details': 'Failing row contains (2023-05-19-SD-HTX, null, null, null, 1, Pull, null, 80, 0, 80, null, null, null, 2024-01-29 21:40:26.009173+00, 310).', 'hint': None, 'message': 'null value in column "team_ext_id" of relation "throws_distribution" violates not-null constraint'}

Games with errors:

'2023-05-05-CAR-ATL',
'2023-05-19-SD-HTX',
'2023-06-18-SEA-LA',
'2023-06-09-CAR-DAL',
'2023-06-11-DET-PIT',
'2023-06-17-SEA-SD',
'2023-06-24-SD-LA',
'2023-06-11-BOS-MTL',
'2023-06-04-PIT-MAD',
'2023-06-17-POR-CHI',
'2023-06-23-DET-CHI',
'2023-07-01-COL-SEA',
'2023-07-23-DET-MIN',
'2023-07-25-DAL-CAR',
'2023-07-22-DET-MAD',
'2023-07-15-HTX-DAL',
'2023-07-08-POR-OAK',
'2023-07-02-PHI-MTL',
'2023-07-01-DAL-ATX',
'2023-07-08-ATX-DAL',
'2023-07-07-POR-SLC',
'2023-07-15-SD-SEA',
'2023-07-15-TOR-DET'
```


**Row Level Security in supabase**

- to manage database ETL jobs, I need to use secret token and not the public token

**RPC Functions**

In 'SQL Editor'. Functions can be seen in `Database > Functions`

```
-- Create a function that returns distinct keys from a table
CREATE OR REPLACE FUNCTION public.get_distinct_keys(table_name text, key_column text)
RETURNS SETOF text AS
$$
BEGIN
    RETURN QUERY EXECUTE
        'SELECT DISTINCT ' || key_column || ' FROM ' || table_name;
END;
$$
LANGUAGE plpgsql;

-- select * from get_distinct_keys('team_game_stats', 'game_id');
```


**Airflow Setup**

```
airflow db init
airflow config
airflow webserver
airflow scheduler
```


