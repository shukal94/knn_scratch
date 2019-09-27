import sys
from pprint import pprint

from data import load_dataset
from global_config import CONFIG

from knn_klassifier import get_neighbors, get_response
from metrics import get_accuracy

split = CONFIG['split']
dataset_path = CONFIG['dataset_path']
distance_method = CONFIG['method']

train_set, test_set = load_dataset(dataset_path, split)


if not sys.argv[1]:
    raise RuntimeError('k is missing')

try:
    k = int(sys.argv[1])
except TypeError as e:
    print('You havent passed k in a correct format')
    print(e.__traceback__)
    sys.exit(1)


def classify(train_set, test_set, k):
    predictions = list()
    result_list = list()
    for test_set_entry in test_set:
        neighbors = get_neighbors(train_set, test_set_entry, k, distance_method)
        result = get_response(neighbors)
        predictions.append(result)
        res_string = '> predicted=' + result + ', actual=' + test_set_entry[-1]
        result_list.append(res_string)
    accuracy = get_accuracy(test_set, predictions)
    return result_list, accuracy


predictions, accuracy = classify(train_set, test_set, k)
pprint(predictions)
print('Accuracy: ' + repr(accuracy) + '%')
