import timeit

def Dsatur(graph):
    #sắp xếp đỉnh theo thứ tự Dsatur
  
  start=timeit.default_timer()
  distinct_color={v:set() for v in graph.keys() }
  vertices = list(dict(sorted(graph.items(), key=lambda x: (-len(x[1][0])))))
  colour_graph = {}
  saturtation={}
  while vertices:
    if len(saturtation)>1:
        vertex = max(vertices, key=lambda v: (saturtation[v], len(graph[v][0])))
    else:
       vertex = max(vertices, key=lambda v: (len(graph[v][0])))
    #print(vertex)
    unused_colours = 1000 * [True]
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
    for neibour in graph[vertex][0]:
       distinct_color[neibour].add(colour_graph[vertex]) 
    #update thứ tự đỉnh Dsatur
    
    saturtation={v:len(c) for v,c in distinct_color.items() if v not in colour_graph.keys()}
    vertices.remove(vertex)
  stop=timeit.default_timer()
  for key in colour_graph:
        colour_graph[key] += 1
  
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
    result=Dsatur(graph=graph)
    print(result)