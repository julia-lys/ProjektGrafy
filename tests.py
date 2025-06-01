import graphs
from main import FindTheLongestCycle

test_cases = [

    ("directed_graph_1", graphs.directed_graph_1, 3),
    ("directed_graph_2", graphs.directed_graph_2, 0),
    ("directed_graph_3", graphs.directed_graph_3, 6),
    ("directed_graph_4", graphs.directed_graph_4, 3),
    ("directed_graph_5", graphs.directed_graph_5, 4),
    ("directed_graph_6", graphs.directed_graph_6, 2),
    ("directed_graph_7", graphs.directed_graph_7, 1),
    ("directed_graph_8", graphs.directed_graph_8, 6),
    ("directed_graph_9", graphs.directed_graph_9, 3),
    ("directed_graph_10", graphs.directed_graph_10, 3),
]

for name, graph, expected in test_cases:
    
        result = len(FindTheLongestCycle(graph))
        print(f"{name} | Expected result: {expected} | Result: {result}")
   