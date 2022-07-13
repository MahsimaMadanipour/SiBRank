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
        """
        To infer a total ranking, SibRank first estimates the preference matrix of the target user based on his neighbors, 
        then it infers a total ranking by aggregating the elements of the estimated preference matrix. To do this, 
        SibRank exploits exponential ranking of items in the signed graph with adjacency matrix of A. Exponential ranking calculates the ranking of item
        through PageRank calculation of a weighted graph with adjacency matrix of M. Finally, SibRank recommends the Top N items that have the highest ranks.
	    """
    
    sibernet_graph = sibrenet.SiBreNet(users_set, items_set, preference_database)
    s = srank.SRank(sibernet_graph, u_target, damping_alpha)
    k_neighbors = neighbors(s, u_target, k)
    r = inference_ranking(neighbors, s)
    top_n_recom_list = r[:n]

    return top_n_recom_list
