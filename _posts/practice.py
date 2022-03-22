# #문제1 1이 될떄까지
# n, k = map(int, input().split())
# count = 0

# while n != 1:
#     if n // k > 1:
#         n = n // k
#         count += 1
#     else:
#         n -= 1
#         count += 1
        
        
# print(n)

# #문제2 곱하기 혹은 더하기
# n = list(input())
# total = 0
# for i in range(len(n)):
#     if int(n[i]) != 0 and total != 0:
#         total *= int(n[i])
#     else:
#         total += int(n[i])

# print(total)
    
# #문제3 모험가 길드
# n = int(input())
# m = sum(list(map(int, input().split())))
# print(m // n)

# #구현 방향 백터
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# # 현재 위치
# x, y = 2, 2

# for i in range(4):
#     # 다음 위치
#     nx = x + dx[i]
#     ny = y +dy[i]
#     print(nx, ny)

# #문제 4 여행가 문제
# # N 입력 받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx =[0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_type = ["L", "R", "U", "D"]

# # 이동 계획을 하나씩 확인하기
# for plan in plans:
#     #이동 후 좌표 구하기
#     for i in range(len(move_type)):
#         if plan == move_type[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
    
# print(x, y)

# #문제 5 시각
# # H 입력 받기
# h = int(input())

# count = 0
# for i in range(h +1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 "3" 이 포함되어 있다면 카운트 증가
#             if "3" in str(i) + str(j) + str(k):
#                 count += 1

# print(count)

# #문제 6 왕실의 나이트
# # 현재 나이트의 위치 입력 받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord("a")) + 1

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     #이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result +=1
        
# print(result)

# #문제7 문자열 재정렬
# data = input()
# result = []
# value = 0

# #문자를 하나씩 확인하여
# for x in data:
#     # 알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():
#         result.append(x)
#     # 숫자는 따로 더하기
#     else:
#         value += int(x)

# # 알파벳을 오름차 순으로 정렬
# result.sort()

# #숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))

# # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print("".join(result))

# #스택 구현 예제 
# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack[::-1])
# print(stack)

# #큐 구현 예제
# from collections import deque

# # 큐(Queue) 구현을 위해 deque 라이브러리 사용
# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)

# def recursive_funtion(i):
#     # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
#     if i == 100:
#         return
#     print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
#     recursive_funtion(i + 1)
#     print(i, '번째 재귀함수를 종료합니다.')

# recursive_funtion(1)

# # DFS 함수 정의
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#   [],
#   [2, 3, 8],
#   [1, 7],
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)