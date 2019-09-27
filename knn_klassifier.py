import math
import operator


def euclidean_distance(instance1, instance2):
    dist = 0
    for x in range(len(instance2) - 1):
        dist += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(dist)


def manhattan_distance(instance1, instance2):
    dist = 0
    for x in range(len(instance2) - 1):
        dist += abs(instance1[x] - instance2[x])
    return dist


DISTANCE_METHODS = {
    'manhattan': manhattan_distance,
    'euclidean': euclidean_distance
}


def get_neighbors(training_set, test_instance, k, method):
    distances = []
    for training_set_entry in training_set:
        dist = DISTANCE_METHODS[method](test_instance, training_set_entry)
        distances.append((training_set_entry, dist))
        distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def get_response(neighbors):
    votes = dict()
    for neigbor in neighbors:
        response = neigbor[-1]
        if response in votes:
            votes[response] += 1
        else:
            votes[response] = 1

    sorted_votes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]