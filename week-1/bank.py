text = input("Introduce a phrase ===> ").lower()


if text.startswith("hola"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")