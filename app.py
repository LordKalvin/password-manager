from os import system

def clear():
    system("clear")

def exit():
    system("exit")

def get_answer():
    answer = input("Input (1/2/3/4...) : ")
    return answer

print("1. Login\n2. Sign Up\n3. Exit")
answer = get_answer()

if answer == "1":
    pass
elif answer == "2":
    pass
else:
    exit()