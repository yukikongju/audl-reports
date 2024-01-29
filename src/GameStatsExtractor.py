import pandas as pd
import numpy as np

from audl.stats.endpoints.gamestats import GameStats
from utils import load_supabase_client
from tables.constants import PLAYER_GAME_STATS_TABLE_NAME, TEAM_GAME_STATS_TABLE_NAME, THROWS_DISTRIBUTION_TABLE_NAME


class GameStatsExtractor(object):

    """
    Class which:
    - extract game stats data from audl api
    - push data to supabase database
    """

    def __init__(self, game_id: str):
        self.game_id = game_id
        self.game = GameStats(game_id)
        self.client = load_supabase_client()


    def update_supabase(self):
        """ 
        function which fetch and update supabase database for the following 
        tables:
        - throws_distribution
        - player_game_stats
        - team_game_stats
        """
        self._update_throws_distribution_table()
        self._update_player_game_stats_table()
        self._update_team_game_stats_table()

    def _update_throws_distribution_table(self):
        # --- get formated dataframe columns
        data_dct = self.__get_formated_throws_distribution_dict()
        
        # --- upsert in table
        data = self.client.table(THROWS_DISTRIBUTION_TABLE_NAME).upsert(data_dct).execute()

    def __get_formated_throws_distribution_dict(self):
        # --- fetch from audl api
        df_throws = self.game.get_throws_dataframe()

        # --- format dataframe
        cols_dict = {'game_id': 'game_id', 'team_ext_id': 'team_ext_id',
                     'thrower_ext_id': 'thrower_ext_id', 
                     'receiver_ext_id': 'receiver_ext_id', 
                     'point': 'point_id',
                     'throw_type': 'throw_type', 'throw_side': 'throw_side', 
                     'throw_distance': 'throw_distance', 
                     'x': 'x', 'y': 'y', 'angle_degrees': 'angle_degrees',
                     'x_field': 'x_field', 'y_field': 'y_field', 
                    }
        df_throws = df_throws.rename(columns=cols_dict)
        df_throws = df_throws[cols_dict.values()]

        # --- add throw_id for database
        df_throws['throw_id'] = list(range(df_throws.shape[0]))

        # --- replace all nan by None
        df_throws = df_throws.replace({np.nan: None})

        # --- convert to dictionary
        dct = df_throws.to_dict(orient='records')
        return dct
        
    def _update_player_game_stats_table(self): 
        # --- fetch from audl api
        df = self.game.get_roster_stats()

        # --- format dataframe
        cols_dict = {
                'gameID': 'game_id',
                'player_ext_id': 'player_ext_id',
                'team_ext_id': 'team_ext_id',
                'assists': 'assists',
                'goals': 'goals',
                'hockeyAssists': 'hockey_assists',
                'completions': 'completions',
                'throwaways': 'throwaways',
                'stalls': 'stalls',
                'throwsAttempted': 'throws_attempted',
                'catches': 'catches',
                'drops': 'drops',
                'blocks': 'blocks',
                'callahans': 'callahans',
                'pulls': 'pulls',
                'obPulls': 'ob_pulls',
                'recordedPulls': 'recorded_pulls',
                'recordedPullsHangtime': 'recorded_pulls_hangtime',
                'oPointsPlayed': 'offensive_points_played',
                'oPointsScored': 'offensive_points_scored',
                'dPointsPlayed': 'defensive_points_played',
                'dPointsScored': 'defensive_points_scored',
                'secondsPlayed': 'seconds_played',
                'yardsReceived': 'yards_received',
                'yardsThrown': 'yards_thrown',
                'hucksAttempted': 'hucks_attempted',
                'hucksCompleted': 'hucks_completed',
                }
        df = df.rename(columns=cols_dict)
        df = df[cols_dict.values()]

        # --- convert to dictionary
        dct = df.to_dict(orient='records')

        # --- upsert to database
        data = self.client.table(PLAYER_GAME_STATS_TABLE_NAME).upsert(dct).execute()


    def _update_team_game_stats_table(self): 
        # --- fetch from audl api
        df = self.game.get_team_stats()

        # --- format dataframe
        cols_dict = {
                'game_id': 'game_id',
                'team_ext_id': 'team_ext_id',
                'isHome': 'is_home',
                'startOnOffense': 'start_on_offense',
                'completionsNumer': 'completions_numer',
                'completionsDenom': 'completions_denom',
                'hucksNumer': 'hucks_numer',
                'hucksDenom': 'hucks_denom',
                'blocks': 'blocks',
                'turnovers': 'turnovers',
                'oLineScores': 'offensive_line_scores',
                'oLinePoints': 'offensive_line_points',
                'oLinePossessions': 'offensive_line_possessions',
                'dLineScores': 'defensive_line_scores',
                'dLinePoints': 'defensive_line_points',
                'dLinePossessions': 'defensive_line_possessions',
                'redZoneScores': 'red_zone_scores',
                'redZonePossessions': 'red_zone_possessions',
                'completionsPerc': 'completions_perc',
                'hucksPerc': 'hucks_perc',
                'holdPerc': 'hold_perc',
                'oLineConversionPerc': 'offensive_line_conversion_perc',
                'dLineConversionPerc': 'defensive_line_conversion_perc',
                'breakPerc': 'break_perc',
                'redZoneConversionPerc': 'red_zone_conversion_perc'
                }

        df = df.rename(columns=cols_dict)
        df = df[cols_dict.values()]

        # --- convert to dictionary
        dct = df.to_dict(orient='records')

        # --- upsert into dataframe
        data = self.client.table(TEAM_GAME_STATS_TABLE_NAME).upsert(dct).execute()
        
