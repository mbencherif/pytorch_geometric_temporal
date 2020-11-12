from typing import Union 
from torch_geometric_temporal.data.discrete.static_graph_discrete_signal import StaticGraphDiscreteSignal


def discrete_train_test_split(data_iterator, train_ratio: float=0.8):

    train_snapshots = int(train_ratio*len(data_iterator.features))

    if type(data_iterator) == StaticGraphDiscreteSignal:
        train_iterator = StaticGraphDiscreteSignal(data_iterator.edge_index,
                                                   data_iterator.edge_weight,
                                                   data_iterator.features[0:train_snapshots],
                                                   data_iterator.targets[0:train_snapshots])

        test_iterator = StaticGraphDiscreteSignal(data_iterator.edge_index,
                                                  data_iterator.edge_weight,
                                                   data_iterator.features[0:test_snapshots],
                                                   data_iterator.targets[0:test_snapshots])
    return 1