import pandas as pd
import numpy as np

from audl.stats.endpoints.gamestats import GameStats
from utils import load_supabase_client


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
        
        # --- delete from table

        # --- upsert in table
        data = self.client.table('throws_distribution').upsert(data_dct).execute()

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
        


    def _update_player_game_stats_table(self): # TODO
        pass

    def _update_team_game_stats_table(self): # TODO
        pass
        
