import timeit
import os
import numpy as np
def greedy_max_al(graph):
    start=timeit.default_timer()
    #sắp xếp đỉnh theo thứ tự bậc cao đến thấp
    
    vertices = list(dict(sorted(graph.items(), key=lambda x: len(x[1][0]),reverse=True)))
    
    colour_graph = {}
    for vertex in vertices:
        unused_colours = len(vertices) * [True]
        #xét mỗi đỉnh kề nếu màu đó đã được sử dụng thì đặt màu đó thành False
        
        for neighbor in graph[vertex][0]:
            if neighbor in colour_graph:
                colour = colour_graph[neighbor]
                unused_colours[colour] = False
        #nếu màu đó không được dùng sau khi xét tất cả đỉnh kế thì sẽ dùng màu đó
        for colour, unused in enumerate(unused_colours):
            
            if unused:
                colour_graph[vertex] = (colour)
                break
    stop=timeit.default_timer()

    # Dùng vòng lặp để cập nhật giá trị
    for key in colour_graph:
        colour_graph[key] += 1

    return colour_graph,max(colour_graph.values()),(stop-start)

if __name__ == '__main__':
    def main(input):
        print(input)
        with open(input, 'r') as file:
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
            
        _,result,_=greedy_max_al(graph)
        print((result))

    directory_path = "maniual_test"
    files = os.listdir(directory_path)
    for file in files:
        if file.endswith(".txt") and not file.endswith("tomau.txt"):
            input_file = os.path.join(directory_path, file)
            main(input_file)