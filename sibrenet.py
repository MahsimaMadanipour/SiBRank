#Construction of SibreNet
#users_set: a 2D list that each row belogs to a user and its data ([i][0] returns the index(id) of the user)
#items_set: a 2D list that each row belogs to an item and its data ([i][0] returns the index(id) of the item and [i][2] return the name of the item)
#preference_database: a 2D list that a row is a user and a column is an item ([i][j] returns a number that shows the preference of user ith about item jth)
def SiBreNet(users_set, items_set, preference_database): 
    
    """
    SiBreNet is a bipartite Graph (<V, E, W>) where V is the set of nodes and E is the set relations among nodes, 
    V is composed of two subsets: user nodes U and preference nodes P; V = U union P. 
    Each edge (u,p) is labeled with a weight , that indicates the agreement (W u,p = 1) or disagreement (W u,p = -1) of user u to preference p.
    """

    def agreement(user, pref):
        if preference_database[user[0]][pref[0][0]] - preference_database[user[0]][pref[1][0]] > 0:
            return 1
        elif preference_database[user[0]][pref[0][0]] - preference_database[user[0]][pref[1][0]] < 0:
            return -1
        else:
            return 0

    users = users_set
    items = sorted(list(set([items_set[i][2] for i in range(len(items_set))])))
    
    preferences = []
    for i in range(len(items)-1):
        for j in range(i, len(items)):
            preferences.append((items[i], items[j]))
    
    positive_edges = []
    negative_edges = []
    edge_weight = [[0 for i in range(len(users))] for i in range(len(preferences))]
    for user in users:
        for pref in preferences:
            if agreement(user, pref) == 1:
                positive_edges.append((user, pref))
            else:
                negative_edges.append((user, pref))
            edge_weight[user[0]][preferences.index(pref)] = agreement(user, pref)

    edges = [*positive_edges, *negative_edges]

    vertices = [*users, *preferences]
    signed_bipartite_preference_network = [vertices, edges, edge_weight] #Bipartite Graph(<V, E, W>)
    return signed_bipartite_preference_network
 