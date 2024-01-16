x = input("Greeting: ")

new_x = x.lower().strip()

if 'hello' in x.lower().strip():
    print("$0")
elif  'h' ==new_x[0]:
    print("$20")
else:
    print("$100")