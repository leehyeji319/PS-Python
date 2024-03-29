from collections import deque

N, M, V = map(int, input().split())

board = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

for i in range(len(board)):
    board[i].sort()

# DFS 구현하기
# index로 받아오기
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
visited = [False] * (N + 1)

dfs(board, V, visited)
print()

# bfs 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N + 1)

bfs(board, V, visited)