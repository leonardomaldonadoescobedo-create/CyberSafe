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
    password = input("\nIntroduce a password:")
    
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
        return analysis(operation, flag)
    else:
        operation = "(a digit)"
        return analysis(operation, flag)
  
def text_analyzer():
    text = input("\nEnter a text:")
    
    print(f"Characters: {len(text)}")
    
    words = text.split()
    print(f"words: {len(words)}")

    try:
        letter = sum(1 for l in text if l.isalpha())
        uppercase = sum(1 for u in text if u.isupper())
        lowercase = sum(1 for lc in text if lc.islower())
        digit = sum(1 for d in text if d.isdigit())
        print(f"Letters: {letter}")
        print(f"Uppercase letters: {uppercase}")
        print(f"Lowecase letters: {lowercase}")
        return f"Digit: {digit}"
    
    except Exception as e:
        print(f"Error detected: {e}")
        
def options():
    options_fuctions = {
        1: password_analyzer,
        2: text_analyzer,
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
                if option in range(1, 3):
                    print(messages[option]())
                else:
                    print(messages[option])
        elif option == 0:
            break
        else:
            print("That option dosen´t exist")

    except ValueError:
        print("Error is not a number")

    except Exception as e:
        print(f"Error with {e}")
