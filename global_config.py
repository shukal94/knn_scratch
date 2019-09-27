import os
from os import getcwd

CONFIG = {
    'dataset_path': os.path.join(getcwd(), 'iris.data'),
    'data_script_path': os.path.join(getcwd(), 'data', 'get_data.sh'),
    'method': 'manhattan',
    'split': 0.8
}
