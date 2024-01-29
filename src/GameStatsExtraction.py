import logging

from audl.stats.endpoints.gamestats import GameStats
from audl.stats.endpoints.seasonschedule import SeasonSchedule

from GameStatsExtractor import GameStatsExtractor

from utils import load_supabase_client
from tables.constants import TEAM_GAME_STATS_TABLE_NAME


def get_missing_game_ids(start_date: str, end_date: str, season: str) -> [str]:
    """
    Function that determine game_ids missing from database

    """
    # --- get game_ids within given season
    seasonschedule = SeasonSchedule(season)
    df_schedule = seasonschedule.get_schedule()
    is_between_date = (df_schedule['startTimestamp'] >= start_date) & (df_schedule['startTimestamp'] <= end_date)
    season_game_ids = set(df_schedule[is_between_date]['gameID'])

    # --- get game_ids in database
    client = load_supabase_client()
    db_game_ids = client.rpc('get_distinct_keys', {'table_name': TEAM_GAME_STATS_TABLE_NAME, 'key_column': 'game_id'}).execute()
    db_game_ids = set(db_game_ids.data)

    # --- get game_ids not in database
    missing_games = list(season_game_ids - db_game_ids)
    return missing_games


def main(start_date: str, end_date: str, season: str):
    #  missing_games = ["2023-08-26-SLC-NY"]
    missing_games = get_missing_game_ids(start_date, end_date, season)
    logging.log(0, f"Missing Games: {missing_games}")
    failed_games_ids = []

    for game_id in missing_games:
        try: 
            logging.log(0, f"Extracting {game_id}")
            game_extractor = GameStatsExtractor(game_id=game_id)
            game_extractor.update_supabase()
            logging.log(0, f"Successfully inserted {game_id} into database")
        except:
            logging.warn(f"Failed {game_id}. Skipping")
            failed_games_ids.append(game_id)

    logging.log(0, f"Failed extraction for games: {failed_games_ids}")



if __name__ == "__main__":
    #  START_DATE_STR, END_DATE_STR = '2023-04-28', '2023-08-12'
    #  START_DATE_STR, END_DATE_STR = '2023-05-01', '2023-05-12'
    #  START_DATE_STR, END_DATE_STR = '2023-05-20', '2023-05-30'
    #  START_DATE_STR, END_DATE_STR = '2023-05-31', '2023-06-30'
    #  START_DATE_STR, END_DATE_STR = '2023-07-01', '2023-07-31'
    START_DATE_STR, END_DATE_STR = '2023-08-01', '2023-09-01'
    SEASON = 2023
    main(start_date=START_DATE_STR, end_date=END_DATE_STR, season=SEASON)

