# elif 응용

score = float(input("type your score >> "))

if score == 4.5:
    print("A+")
elif score >= 4.3:
    print("A0")
elif score >= 4.0:
    print("A-")
elif score >= 3.5:
    print("B+")
elif score >= 3.3:
    print("B0")
elif score >= 3.0:
    print("B-")
else:
    print("F")