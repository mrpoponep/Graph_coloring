from algorithm.Welsh_Powell import welsh_powell
from algorithm.new_dsatur import Dsatur
from algorithm.greedy_max import greedy_max_al
from algorithm.greedy_min import greedy_min_al
from algorithm.independent_set_copy import set2_coloring
from algorithm.independent_set import set1_coloring

import timeit
import os
import io
import numpy as np

def run_coloring_algorithms(graph):
    # Run Welsh-Powell algorithm
    welsh_powell_colors,welsh_powell_num_colors,welsh_powell_time = welsh_powell(graph)
    # Run greedy coloring algorithm
    greedy_max,greedy_max_colors,greedy_max_time = greedy_max_al(graph=graph)
    greedy_min,greedy_min_colors,greedy_min_time = greedy_min_al(graph=graph)
    # Run DSatur algorithm
    dsatur_colors,dsatur_num_colors,dsatur_time = Dsatur(graph)
    # Run independent_set algorithm
    independent2_colors,independent2_num_colors,independent2_time = set2_coloring(graph)
    independent1_colors,independent1_num_colors,independent1_time = set1_coloring(graph)
    min_colors = min(welsh_powell_num_colors, dsatur_num_colors, greedy_max_colors,greedy_min_colors,independent1_num_colors,independent2_num_colors)
    best_algorithm = None

    if min_colors == welsh_powell_num_colors:
        best_algorithm = "Welsh_Powell_Algorithm"
        return welsh_powell_colors,welsh_powell_num_colors,welsh_powell_time,best_algorithm
    elif min_colors == dsatur_num_colors:
        best_algorithm = "DSatur_Algorithm"
        return dsatur_colors,dsatur_num_colors,dsatur_time,best_algorithm
    elif min_colors == greedy_min_colors:
        best_algorithm = "Greedy_Algorithm_Min"
        return greedy_min,greedy_min_colors,greedy_min_time,best_algorithm
    elif min_colors == independent1_num_colors:
        best_algorithm = "Independent_set1"
        return independent1_colors,independent1_num_colors,independent1_time,best_algorithm
    elif min_colors == independent2_num_colors:
        best_algorithm = "Independent_set2"
        return independent2_colors,independent2_num_colors,independent2_time,best_algorithm
    else:
        best_algorithm = "Greedy_Algorithm_Max"
        return greedy_max,greedy_max_colors,greedy_max_time,best_algorithm


def main(input_file):
    start=timeit.default_timer()

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Lấy thông tin số đỉnh và số cạnh từ dòng đầu tiên
    num_vertices, num_edges = map(int, lines[0].split())

    # Tạo numpy array để lưu danh sách cạnh
    edges = np.zeros((num_edges, 2), dtype=int)

    for i in range(num_edges):
        u, v = map(int, lines[i+1].split())
        edges[i] = [u, v]

    graph = {}  

        #Dòng 1 là số đỉnh và số cạnh
    for i in range(1, int(num_vertices)+1):
        graph[i] = [[],0]

    for edge in edges:
        u, v = edge
        graph[u][0].append(v)
        graph[v][0].append(u)

    
    output_file = input_file.replace(".txt", "color.txt")
    print("\n")
    #print(graph)
    result, color_num,timei,algorithms=run_coloring_algorithms(graph=graph)
    #print(result,color_num)
    sorted_dict_by_key = dict(sorted(result.items(), key=lambda item: item[0]))
    print("--------------------------------------")
    print(f"Best algorithms: {algorithms}")
    print(f"Minimmum color used: {color_num}")
    with io.open(output_file, 'w', encoding='utf8') as file:
        file.write(f"{max(result.values())}\n")
        for i in sorted_dict_by_key.keys():
            output=f"{sorted_dict_by_key[i]}\n"
            file.write(output)
    with io.open("log.txt", 'a', encoding='utf8') as file:
        file.write(f"{input_file} {output_file} {color_num} {algorithms}\n")
    stop=timeit.default_timer()
    print('Time: ', stop - start) 

directory_path = "Dataset"

files = os.listdir(directory_path)
files = sorted(files, key=lambda x: int(x.split("_")[1]))

for file in files:
    if file.endswith(".txt") and not file.endswith("colored.txt") and not file.endswith("gc_10000_1_1.txt"):
        input_file = os.path.join(directory_path, file)
        print(input_file)
        main(input_file)

