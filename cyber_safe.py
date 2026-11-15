import sys
print(sys.version)   

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

weak = 0
weak_password = [
    1,
    "Weak Password Detected",
    "Password Analyzer",
    "SAFE"
]
weak_text = [
    2, 
    "Weak Text Detected",
    "Text Analyzer",
    "SAFE"
]

def password_analyzer(weak, weak_password):
    password = input("\nIntroduce a password:")

    def analysis(operation, flag):
        try:
            return f"Minimum {operation}: {flag}"

        except NameError:
            return "Variable inexistente"

    operation = ""
    flag = "PASS"
    length = "PASS"

    if len(password) < 12:
        operation = "(12 characters)"
        flag = "FAIL"
        length = "FAIL"
        print(analysis(operation, flag))
    else:
        operation = "(12 characters)"
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
        flag = "PASS"
        print(analysis(operation, flag))

    list_flag = [
         length,
         flag_capital,
         flag_lower_case,
         flag_digit
    ]

    if all(list_flag[1:4]) and list_flag[0] == "PASS":
         print("The password is secure")
    else:
         weak += 1
         weak_password.append(password)
         weak_password[3] = "WARNING"

    return weak

def text_analyzer(weak, weak_text):

    text = input("\nEnter a text:")
    print(f"Characters: {len(text)}")

    words = text.split()
    print(f"words: {len(words)}")

    try:
        weak2 = 0

        letter_boolean = True
        uppercase_boolean = True
        lowercase_boolean = True
        digit_bolean = True
        flag_letter = False

        list_letters = [
             letter_boolean,
             uppercase_boolean,
             lowercase_boolean,
             digit_bolean,
             flag_letter
        ]

        if all(list_letters[0:4]):
            letter = sum(1 if i.isalpha() else 0  for i in text)
            uppercase = sum(1 if i.isupper() else 0 for i in text)
            lowercase = sum(1 if i.islower() else 0 for i in text)
            digit = sum(1 if i.isdigit() else 0  for i in text)

        if list_letters[4] == False:
             weak2 += 1
             weak += weak2
             weak_text.append(text)
             weak_text[3] = "WARNING"


        print(f"Letters: {letter}")
        print(f"Uppercase letters: {uppercase}")
        print(f"Lowercase letters: {lowercase}")
        print(f"Digit: {digit}")


    except Exception as e:
        print(f"Error detected: {e}")


    return weak


def security_data_manager(weak, weak_password, weak_text):
    def add_security_record(weak, weak_password, weak_text):
            try:
                if weak_password[3] == "WARNING" or weak_password[3] == "SAFE":
                     events_password = {
                        "Event_id": weak_password[0],
                        "Event": weak_password[1],
                        "Module": weak_password[2],
                        "Status": weak_password[3]
                     }

                     for key, value in events_password.items():
                             print(key, value)

                if weak_text[3] == "WARNING" or weak_text[3] == "SAFE":
                     events_text = {
                          "\nEvent_id": weak_text[0],
                          "Event": weak_text[1],
                          "Module": weak_text[2],
                          "Status": weak_text[3]
                     }

                     for key, value in events_text.items():
                            print(key, value)

            except Exception as e:
                 print(f"Error with {e}")

    def view_all_records():
            return ""

    def search_record():
            return 3

    def update_record():
            return 4

    def delete_record():
            return 5

    security_menu = [
        "1. Add Security Record",
        "2. View All Records",
        "3. Search Record",
        "4. update Record",
        "5. Delete Record",
        "\n0. Return to Menu"
    ]

    record = {
            1: add_security_record,
            2: view_all_records,
            3: search_record,
            4: update_record,
            5: delete_record,
            0:""
        }

    while True:
         for i in security_menu:
              print(i)
         try:
              security_option = int(input("Which option will you choose?:"))

              if security_option == 1:
                   record[security_option](weak, weak_password, weak_text)
              elif security_option in range(2, 6):
                   print("This option is coming soon.")
              elif security_option == 0:
                  break
              else:
                   print("That option dosen´t exist")
         except Exception as e:
                 print(f"Error with {e}")

def options():
    options_fuctions = {
        1: password_analyzer,
        2: text_analyzer,
        3: security_data_manager,
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
                if option in range(4, 6):
                    print(messages[option])
                elif option == 1:
                     messages[option](weak, weak_password)
                elif option == 2:
                      messages[option](weak, weak_text)
                elif option == 3:
                     messages[option](weak, weak_password, weak_text)
                else:
                    print(messages[option])
        elif option == 0:
            break
        else:
            print("That option dosen't exist")

    except ValueError:
        print("Error is not a number")

    except Exception as e:
        print(f"Error with {e}")
