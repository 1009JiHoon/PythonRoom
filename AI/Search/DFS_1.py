# 그래프를 인접 리스트 형태로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS 알고리즘
def dfs(node, visited):
    if node not in visited:
        print(node)  # 노드를 방문할 때 출력
        visited.add(node)  # 방문한 노드를 추가
        for neighbor in graph[node]:  # 인접 노드에 대해 재귀 호출
            dfs(neighbor, visited)

# 실행 예시
visited_nodes = set()
dfs('A', visited_nodes)
