#
# i행 j열은 i번 점과 j번 점 사이의 거리를 나타냅니다. 위 행렬을 만족하도록 수직선 위에 점을 놓는 방법은 다음과 같이 두 가지가 있습니다.
#
# dots_3.png
#
# dots_2.png
#
# 예를 들면, 2번 점과 4번 점 사이의 거리는 2행 4열(또는 4행 2열)의 값이며, 이는 3입니다. 그림에서도 마찬가지로 2번점과 4번점 사이의 거리가 1 + 2 = 3이며, 이는 행렬의 값과 동일합니다. 그림에 표시된 점에 대해서 서로 다른 두 점 사이의 거리는 모두 행렬의 값을 만족합니다.
#
# 따라서 수직선 위에 놓인 점의 순서는 [1번, 2번, 0번, 4번 3번] 또는 [3번, 4번, 0번, 2번, 1번]이 되며, 이 외에 행렬에서 주어진 점 사이의 거리 값을 모두 만족하도록 점을 놓는 방법은 없습니다.
#
# 두 점 사이의 거리를 행렬 형태로 나타낸 2차원 정수 배열 dist가 매개변수로 주어집니다. 행렬의 값을 만족하도록 수직선 위에 점을 놓는 모든 방법에 대해서 점의 순서를 왼쪽부터 차례대로 담아 2차원 배열 형태로 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 2 ≤ dist의 행(세로) 길이 ≤ 100
# dist의 열(가로) 길이 = dist의 행(세로) 길이
# 0 ≤ dist의 원소 ≤ 100,000,000
# i = j일 때, dist[i][j] = 0
# i ≠ j일 때, dist[i][j] > 0
# 즉, 서로 다른 두 점이 같은 위치에 놓인 경우는 없습니다.
# 점의 번호는 0부터 (dist의 행(세로) 길이 - 1)까지입니다.
# 정답 배열의 각 행은 점의 순서가 사전 순으로 빠른 것부터 순서대로 담아야 합니다.
# 항상 정답이 존재하는 경우만 입력으로 주어집니다.
# 입출력 예
# dist	result
# [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]	[[1,2,0,4,3],[3,4,0,2,1]]
# [[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]	[[0,3,1,2],[2,1,3,0]]
# 입출력 예 설명
# 입출력 예 #1
#
# 문제의 예시와 같습니다.
#
# 입출력 예 #2
#
# 주어진 행렬은 다음과 같습니다.
#
# dots_6.png
#
# 위 행렬을 만족하도록 점을 배치하는 방법은 다음과 같이 2가지입니다.
#
# dots_4.png
#
# dots_5.png
#
# [0,3,1,2]와 [2,1,3,0]을 배열에 담으면 됩니다. 이때, [0,3,1,2]가 [2,1,3,0]보다 사전 순으로 빠르므로, [[0,3,1,2],[2,1,3,0]]을 return 하면 됩니다.