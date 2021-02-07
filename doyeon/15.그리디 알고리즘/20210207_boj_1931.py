import sys
def greedy(meeting):
  meeting_count = 0
  start_time = 0
  for time in meeting:
    if time[0] >= start_time:
      start_time = time[1]
      meeting_count += 1
  return meeting_count

mCount = int(sys.stdin.readline())
meeting = []
for i in range(mCount):
  start, end = map(int, sys.stdin.readline().split())
  meeting.append((start, end))
# 시작 시간 기준으로 정렬
meeting = sorted(meeting, key=lambda time: time[0])
# 종료 시간 기준으로 정렬
meeting = sorted(meeting, key=lambda time: time[1])
print(greedy(meeting))