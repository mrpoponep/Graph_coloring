import timeit
import copy
def get_subgraph(graph, remaining_vertices):
    subgraph = {}
    for vertex in remaining_vertices:
        if vertex in graph:
            subgraph[vertex] = copy.deepcopy(graph[vertex])
            subgraph[vertex][0] = [v for v in subgraph[vertex][0] if v in remaining_vertices]
    return subgraph

def largest_independent(graph):
    independent_set = set()
    remaining = set(graph)
    while remaining:
        graph = get_subgraph(graph,remaining) 
        min_degree_vertex=min(remaining, key = lambda x: (len(graph[x][0]),-x))
        #print(min_degree_vertex,len(graph[min_degree_vertex][0]))
        independent_set.add(min_degree_vertex)
        remaining -= set(graph[min_degree_vertex][0]) | {min_degree_vertex}
    
    return independent_set

def set2_coloring(graph):
    start = timeit.default_timer()
    remain=set(graph)
    
    color=1
    color_graph={}
    while remain:
        sub_graph = get_subgraph(graph,remain)
        #print(sub_graph)
        independent_set=largest_independent(sub_graph)
        #print(independent_set)
        for i in independent_set:
            color_graph[i]=color
            remain.remove(i)
        color+=1
    stop = timeit.default_timer()
    
    return color_graph,max(color_graph.values()),(stop-start)
    

if __name__ == '__main__':
    graph = {1: [[6, 2, 3, 7], 0],
             2: [[1], 0],
             3: [[1, 6], 0],
             4: [[5], 0],
             5: [[4, 7, 6], 0],
             6: [[1, 5, 3], 0],
             7: [[5, 1], 0],
             8: [[9], 0],
             9: [[8], 0],
             10: [[13, 11, 11], 0],
             11: [[10], 0],
             12: [[13], 0],
             13: [[10, 12], 0]}
    #print(graph)
    result = set2_coloring(graph)
    #print(result)