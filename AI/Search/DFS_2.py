# 그래프 정의
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# DFS 함수 정의
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    
    path.append(start)  # 현재 노드 추가

    if start == goal:
        return path  # 목표 노드에 도달한 경우 경로 반환

    for neighbor in graph[start]:
        if neighbor not in path:  # 이미 방문한 노드는 제외
            result = dfs_path(graph, neighbor, goal, path)
            if result:  # 경로가 발견된 경우
                return result

    path.pop()  # 백트래킹
    return None  # 경로를 찾지 못한 경우

# 경로 찾기
start_node = 'A'
goal_node = 'E'
path = dfs_path(graph, start_node, goal_node)

# 결과 출력
if path:
    print(f"경로: {' -> '.join(path)}")
else:
    print("경로를 찾을 수 없습니다.")
