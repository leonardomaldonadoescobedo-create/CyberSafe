#=== Cyber Safe ===

def options():
    options_fuctions = {
        1: "This feature is coming soon.",
        2: "This feature is coming soon.",
        3: "This feature is coming soon.",
        4: "This feature is coming soon.",
        5: "This feature is coming soon.",
        0: ""
    }
    
    return options_fuctions
    
messages = options()
    
def menu():
    options_menu = [
        "=== CyberSafe ===\n",
        "1. Password Analyzer",
        "2. Text Analyzer",
        "3. Security Data Manager",
        "4. Analysis History",
        "5. About CyberSafe",
        "\n0. Exit"
        ]
    
    for i in options_menu:
        print(i)
        
while True:
    menu()
    try:
        option = int(input("Which option will you choose?:"))
        
        if option in range(1, 6):
            print(messages[option])
        elif option == 0:
            break
        else:
            print("That option dosen't exist")
    except ValueError:
        print("Error is not a number")
