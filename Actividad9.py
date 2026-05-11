nota = float(input("introducir nota: "))


if nota < 5:
    print("insuficiwnte")
elif nota < 6:
    print("suficiente")
elif nota < 7:
    print("bien")
elif nota < 9:
    print("notable")
else:
    print("sobrealiente")