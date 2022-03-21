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

#문제7 문자열 재정렬
data = input()
result = []
value = 0

#문자를 하나씩 확인하여
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차 순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print("".join(result))