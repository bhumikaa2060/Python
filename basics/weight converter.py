weight=input("Weight :")
typ=input("(l)bs or (k)g:")
if typ == "l":
    print("you are", float(weight) * 0.45)
elif typ == "k":
    print("you are", float(weight) / 0.45, "pounds")

