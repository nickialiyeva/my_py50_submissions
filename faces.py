def main():
    message = input()
    result = convert(message)
    print(result)

def convert(message):
    message1 = message.replace(":)", '🙂')
    message2 = message1.replace(":(", '🙁')
    return message2

main()