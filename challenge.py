def shortest_route(lst):
    path = []
    for a in lst:
        for b in a:
            if b not in path:
                path.append(b)
    return path
    
    
paths = [["a","b"],["b","c"],["c","d"]]
print(shortest_route(paths))

def matrices(matrix, n):
    answer = True
    for a in matrix:
        for number in a:
            if number not in range(1,n+1):
                answer = False
    return answer
        
matrix = [[1,2,6], [3,2,1],[2,3,1]]
print(matrices(matrix, 3))