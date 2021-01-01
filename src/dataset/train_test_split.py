from sklearn.model_selection import train_test_split
import gokart

from src.utils.base_task import GokartTask


class TrainTestSplit(GokartTask):
    target = gokart.TaskInstanceParameter()

    def run(self):
        df = self.load('target')

        train_x, test_x, train_y, test_y = train_test_split(df,
                                                            df['target'],
                                                            test_size=0.2)
        train_x, val_x, train_y, val_y = train_test_split(train_x,
                                                          train_y,
                                                          test_size=0.2)

        self.dump({
            'train_x': train_x,
            'train_y': train_y,
            'test_x': test_x,
            'test_y': test_y,
            'val_x': val_x,
            'val_y': val_y
        })
