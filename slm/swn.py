import os
import pandas as pd
from .utils import str_to_datetime
class Swn:
    _cached_df = pd.DataFrame()
    def __init__(self, swn_filename, mode='MAX'):
        self.swn_filename = swn_filename
        self.mode = mode
    
    def _df(self):
        if self._cached_df.empty:
            return self.swn_to_df()
        else:
            return self._cached_df
    
    @property
    def df(self):
        return self._df()

    def swn_to_df(self):
        """Parse swn file and read the 'mode' series 
        """
        swn_filename = self.swn_filename
        with open(swn_filename) as h:
            lines = h.readlines()
            cols = lines[11].rstrip().split(',')
        df = pd.read_csv(swn_filename, skiprows=13, delimiter='\t')
        df.columns = cols
        df = df.dropna()
        df['Date'] = df['Date'].astype(int)
        df['Time'] = df['Time'].astype(int)
        df['date_and_time'] = df[['Date', 'Time']].apply(lambda x: f"{x['Date']} {x['Time']}", axis=1)
        df['date_and_time'] = df['date_and_time'].apply(str_to_datetime)
        self._cached_df = df
        return df

    def plot(self, **kwargs):
        col_to_plot = [col for col in self.df.columns if self.mode in col][0]
        ax = self.df.plot(x='date_and_time', y=col_to_plot, **kwargs)
        print(type(ax))
        self.df['average_per_minute'] = self.df[col_to_plot].rolling(window=60).mean()
        return self.df.plot(x='date_and_time', y='average_per_minute', ax=ax, style = 'r', label = 'Average per minute')

