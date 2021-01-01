import pandas as pd

from src.utils.base_task import GokartTask


class LoadTrainData(GokartTask):
    def run(self):
        self.dump(pd.read_csv('./data/train.csv'))
