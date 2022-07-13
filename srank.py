import numpy as np

def SRank(graph, target, damp_factor=0.85):

    """
    an algorithm called SRank that adopts signed multiplicative rank propagation for similarity calculation in recommender systems. 
    SRank exploits a personalized random walk in an undirected signed graph for calculating similarities among nodes, and is based on some 
    ideas from social balance theory. Social balance theory refers to the fact that for a person, friends of friends, and, enemies of 
    enemies are friends, while, friends of enemies, and, enemies of friends are enemies
    """
    
    epsilon = 0.001
    vertices = graph["vertices"]
    edges = graph["edges"]
    q = [0 for _ in range(len(edges))]
    q[target] = 1
    abs_edges = [list(map(abs, edge)) for edge in edges]
    transition = [[0 for _ in range(len(edges[0]))] for t in range(len(edges))]
    transition_pos = [[0 for _ in range(len(edges[0]))] for t in range(len(edges))]
    transition_neg = [[0 for _ in range(len(edges[0]))] for t in range(len(edges))]
    s_pos = np.random.rand(len(edges))
    s_neg = np.random.rand(len(edges))

    for j in range(len(edges[0])):
        col = sum(list(zip(*abs_edges[j])))
        for i in range(len(edges)):
            transition[i][j] = [abs_edges[i, j] / col]
            transition_pos[i][j] = [transition[i][j] if edges[i][j] > 0 else 0]
            transition_neg[i][j] = [transition[i][j] if edges[i][j] < 0 else 0]

    s_pos = s_pos / (np.sum(s_pos) + np.sum(s_neg))
    s_neg = s_neg / (np.sum(s_pos) + np.sum(s_neg))

    convergence = False
    while not convergence:
        s_pos_temp = s_pos
        s_neg_temp = s_neg
        s_pos = damp_factor * (np.matmul(s_pos, transition_pos) + np.matmul(s_neg, transition_neg)) + ((1 - damp_factor) * q)
        s_neg = damp_factor * (np.matmul(s_pos, transition_neg) + np.matmul(s_neg, transition_pos))

        if np.linalg.norm(s_pos - s_pos_temp) <= epsilon and np.linalg.norm(s_neg - s_neg_temp) <= epsilon:
            convergence = True

    sRank = (s_pos - s_neg) / (s_pos + s_neg)

    return sRank