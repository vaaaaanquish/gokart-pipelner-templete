from gokart_pipeliner import GokartPipeliner
from src.dataset.load_train_data import LoadTrainData

pipeline = [LoadTrainData]

config_path_list = ['./conf/param.ini']
GokartPipeliner(config_path_list=config_path_list).run(pipeline)
