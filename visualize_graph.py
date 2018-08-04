from graphviz import Digraph

def visualize_the_graph():
    u = Digraph('Water Jug', filename='water_jug.png')
    u.edge(str(( [0, 0, 0] )),str(( [1, 0, 3] )))
    u.edge(str(( [0, 0, 0] )),str(( [2, 4, 0] )))
    u.edge(str(( [1, 0, 3] )),str(( [3, 3, 0] )))
    u.edge(str(( [1, 0, 3] )),str(( [4, 4, 3] )))
    u.edge(str(( [2, 4, 0] )),str(( [5, 1, 3] )))
    u.edge(str(( [2, 4, 0] )),str(( [6, 4, 3] )))
    u.edge(str(( [3, 3, 0] )),str(( [7, 3, 3] )))
    u.edge(str(( [3, 3, 0] )),str(( [8, 4, 0] )))
    u.edge(str(( [4, 4, 3] )),str(( [9, 0, 3] )))
    u.edge(str(( [4, 4, 3] )),str(( [10, 4, 0] )))
    u.edge(str(( [5, 1, 3] )),str(( [11, 4, 0] )))
    u.edge(str(( [5, 1, 3] )),str(( [12, 4, 3] )))
    u.edge(str(( [5, 1, 3] )),str(( [13, 1, 0] )))
    u.edge(str(( [5, 1, 3] )),str(( [14, 0, 3] )))
    u.edge(str(( [6, 4, 3] )),str(( [15, 0, 3] )))
    u.edge(str(( [6, 4, 3] )),str(( [16, 4, 0] )))
    u.edge(str(( [7, 3, 3] )),str(( [17, 3, 0] )))
    u.edge(str(( [7, 3, 3] )),str(( [18, 4, 3] )))
    u.edge(str(( [7, 3, 3] )),str(( [19, 4, 2] )))
    u.edge(str(( [7, 3, 3] )),str(( [20, 0, 3] )))
    u.edge(str(( [8, 4, 0] )),str(( [21, 1, 3] )))
    u.edge(str(( [8, 4, 0] )),str(( [22, 4, 3] )))
    u.edge(str(( [9, 0, 3] )),str(( [23, 3, 0] )))
    u.edge(str(( [9, 0, 3] )),str(( [24, 4, 3] )))
    u.edge(str(( [10, 4, 0] )),str(( [25, 1, 3] )))
    u.edge(str(( [10, 4, 0] )),str(( [26, 4, 3] )))
    u.edge(str(( [11, 4, 0] )),str(( [27, 1, 3] )))
    u.edge(str(( [11, 4, 0] )),str(( [28, 4, 3] )))
    u.edge(str(( [12, 4, 3] )),str(( [29, 0, 3] )))
    u.edge(str(( [12, 4, 3] )),str(( [30, 4, 0] )))
    u.edge(str(( [13, 1, 0] )),str(( [31, 1, 3] )))
    u.edge(str(( [13, 1, 0] )),str(( [32, 4, 0] )))
    u.edge(str(( [14, 0, 3] )),str(( [33, 3, 0] )))
    u.edge(str(( [14, 0, 3] )),str(( [34, 4, 3] )))
    u.edge(str(( [15, 0, 3] )),str(( [35, 3, 0] )))
    u.edge(str(( [15, 0, 3] )),str(( [36, 4, 3] )))
    u.edge(str(( [16, 4, 0] )),str(( [37, 1, 3] )))
    u.edge(str(( [16, 4, 0] )),str(( [38, 4, 3] )))
    u.edge(str(( [17, 3, 0] )),str(( [39, 3, 3] )))
    u.edge(str(( [17, 3, 0] )),str(( [40, 4, 0] )))
    u.edge(str(( [18, 4, 3] )),str(( [41, 0, 3] )))
    u.edge(str(( [18, 4, 3] )),str(( [42, 4, 0] )))
    u.edge(str(( [19, 4, 2] )),str(( [43, 3, 3] )))
    u.edge(str(( [19, 4, 2] )),str(( [44, 4, 3] )))
    u.edge(str(( [19, 4, 2] )),str(( [45, 0, 2] )))
    u.edge(str(( [19, 4, 2] )),str(( [46, 4, 0] )))
    u.edge(str(( [20, 0, 3] )),str(( [47, 3, 0] )))
    u.edge(str(( [20, 0, 3] )),str(( [48, 4, 3] )))
    u.edge(str(( [21, 1, 3] )),str(( [49, 4, 0] )))
    u.edge(str(( [21, 1, 3] )),str(( [50, 4, 3] )))
    u.edge(str(( [21, 1, 3] )),str(( [51, 1, 0] )))
    u.edge(str(( [21, 1, 3] )),str(( [52, 0, 3] )))
    u.edge(str(( [22, 4, 3] )),str(( [53, 0, 3] )))
    u.edge(str(( [22, 4, 3] )),str(( [54, 4, 0] )))
    u.edge(str(( [23, 3, 0] )),str(( [55, 3, 3] )))
    u.edge(str(( [23, 3, 0] )),str(( [56, 4, 0] )))
    u.edge(str(( [24, 4, 3] )),str(( [57, 0, 3] )))
    u.edge(str(( [24, 4, 3] )),str(( [58, 4, 0] )))
    u.edge(str(( [25, 1, 3] )),str(( [59, 4, 0] )))
    u.edge(str(( [25, 1, 3] )),str(( [60, 4, 3] )))
    u.edge(str(( [25, 1, 3] )),str(( [61, 1, 0] )))
    u.edge(str(( [25, 1, 3] )),str(( [62, 0, 3] )))
    u.edge(str(( [26, 4, 3] )),str(( [63, 0, 3] )))
    u.edge(str(( [26, 4, 3] )),str(( [64, 4, 0] )))
    u.view()