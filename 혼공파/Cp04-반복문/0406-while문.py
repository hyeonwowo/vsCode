# while문 기초

i = 0
while i < 10:
    print(f"{i}번째 반목문")
    i += 1
print()

# while 반복문 : break / continue

i = 0
while True:
    input_text = input("QUIT ? (Y/N) : ")
    result = input_text.upper()
    if result == "Y":
        print("QUIT REPEAT.")
        print(f"Total repeat count : {i}")
        break
    else:
        print(f"REPEAT AGAIN {i}")
        i += 1
        continue