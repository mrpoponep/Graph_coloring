import timeit
import copy
def welsh_powell(graph,):
    # Sắp xếp các đỉnh của đồ thị theo thứ tự giảm dần của bậc

    start=timeit.default_timer()

    sorted_vertices = sorted(graph, key=lambda v: len(graph[v][0]), reverse=True)
    # Khởi tạo một từ điển để theo dõi màu của từng đỉnh
    colour_graph = {}

    # Khởi tạo màu đầu tiên
    color = 1

    for vertex in sorted_vertices:
        # Nếu đỉnh chưa được tô màu
        if vertex not in colour_graph:
            # Gán màu cho đỉnh hiện tại
            colour_graph[vertex] = (color)
            neirbours=set(graph[vertex][0])
            # Duyệt qua các đỉnh còn lại
            for other_vertex in sorted_vertices:
                # Nếu đỉnh chưa được tô màu, không kề với đỉnh hiện tại và không cùng màu với đỉnh hiện tại
                if (
                    other_vertex not in colour_graph
                    and other_vertex not in neirbours
                ):
                    # Gán màu cho đỉnh khác
                    colour_graph[other_vertex] = color
                    neirbours.update(graph[other_vertex][0])
            # Tăng màu lên 1 để tô màu cho các đỉnh tiếp theo
            color += 1
    stop=timeit.default_timer()
    return colour_graph,max(colour_graph.values()),(stop-start)

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
             11: [[10, 10], 0],
             12: [[13], 0],
             13: [[10, 12], 0]}
    print(graph)
    result=welsh_powell(graph)
    print(result)
    print(graph)