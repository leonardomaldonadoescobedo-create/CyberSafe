#=== CyberSafe ===

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
   
def password_analyzer():
    password = input("Introduce a password:")
    
    def analysis(operation, flag):
        try:
            return f"Minum {operation}: {flag}"
        except NameError:
            return "Variable inexistente"
    
    operation = ""
    flag = "PASS"
    
    if len(password) < 12:
        operation = "(12 caracters)"
        flag = "FAIL"
        print(analysis(operation, flag))
    else:
        operation = "(12 caracters)"
        flag = "PASS"
        print(analysis(operation, flag))
        
    flag_capital = False
    flag_lower_case = False
    flag_digit = False
    
    for i in password:
        if i.isupper():
            flag_capital = True
        if i.islower():
            flag_lower_case = True
        if i.isdigit():
            flag_digit = True
            
    if not flag_capital:
        operation = "(a capital)"
        flag = "FAIL"
        print(analysis(operation,flag))
    else:
        operation = "(a capital)"
        flag = "PASS"
        print(analysis(operation,flag))
        
    if not flag_lower_case:
        operation = "(a lowercase)"
        flag = "FAIL"
        print(analysis(operation, flag))
    else:
        operation = "(a lowercase)"
        flag = "PASS"
        print(analysis(operation, flag))
        
    if not flag_digit:
        operation = "(a digit)"
        flag = "FAIL"
        print(analysis(operation, flag))
    else:
        operation = "(a digit)"
        
        print(analysis(operation, flag))
  
def options():
    options_fuctions = {
        1: password_analyzer,
        2: "This feature is coming soon.",
        3: "This feature is coming soon.",
        4: "This feature is coming soon.",
        5: "This feature is coming soon.",
        0: ""
    }
    
    return options_fuctions
    
messages = options() 
        
while True:
    menu()
    try:
        option = int(input("Which option will you choose?:"))
        
        if option in range(1, 6):
            try:
                if option == 1:
                    messages[option]()
                else:
                    print(messages[option])
            except TypeError:
                print("Error")
                
        elif option == 0:
            break
        else:
            print("That option dosen´t exist")
    except ValueError:
        print("Error is not a number")
