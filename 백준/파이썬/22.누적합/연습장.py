import sys

starttime = [i for i in range(0,25)]
endtime = [i for i in range(0,25)]

diftime = []
n = int(sys.stdin.readline())

for _ in range(n):
    st,ed = map(int, sys.stdin.readline().split())
    diftime.append((st,ed,ed-st))

diftime.sort(key=lambda x:x[2])

for element in diftime:
    start,end,_ = element[0],element[1],element[2]
    if start
