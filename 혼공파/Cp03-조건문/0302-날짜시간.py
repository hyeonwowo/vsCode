import datetime

# 날짜시간이용 - 1) 현재 날짜, 시간 출력

now = datetime.datetime.now()
print(f"NOW : {now.year}y {now.month}m {now.day}d {now.hour}h {now.minute}m {now.second}s")

# 날짜시간이용 - 2) 오전, 오후 구분

if now.hour < 12:
    print("오전")
else:
    print("오후")

# 날짜시간이용 - 3) 계절 구분

if 3 <= now.month <= 5:
    print("봄")
elif 6 <= now.month <= 8:
    print("여름")
elif 9 <= now.month <= 11:
    print("가을")
else:
    print("겨울")