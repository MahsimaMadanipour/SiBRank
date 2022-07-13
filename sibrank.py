import sibrenet
import srank

def SibRank(users_set, items_set, preference_database, u_target, k, n, damping_alpha=0.85):
    """
    summarizes the overall framework of SibRank that consists of five steps:
    SiBreNet construction of preference data, calculating SRank of the target user u, finding
    the neighbors, ranking inference, and Top-k recommendation.
    """
    
    def neighbors(srank, u_target, k):
        k_neigh = []
        u_index = u_target[0]
        similarity_vector = srank[:u_index] + [0] + srank[u_index:]
        similarity_matrix = [(i, sim) for i, sim in enumerate(similarity_vector)]
        similarity_matrix = reversed(sorted(similarity_matrix, key=lambda x: x[1]))
        k_neigh = similarity_matrix[:k]
        return k_neigh
    
    def inference_ranking():
        pass
    
    sibernet_graph = sibrenet.SiBreNet(users_set, items_set, preference_database)
    s = srank.SRank(sibernet_graph, u_target, damping_alpha)
    k_neighbors = neighbors(s, u_target, k)
    r = inference_ranking(neighbors, s)
    top_n_recom_list = r[:n]

    return top_n_recom_list
