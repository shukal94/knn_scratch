import csv
import random

from global_config import CONFIG
from util import execute_bash_script


def load_dataset(filename, split):
    execute_bash_script(CONFIG['data_script_path'])
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        training_set = list()
        test_set = list()
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                training_set.append(dataset[x])
            else:
                test_set.append(dataset[x])
        return training_set, test_set
