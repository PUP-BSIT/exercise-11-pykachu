from pykachupackage import besa, bualat, maestre, salespara, serquina

def main():
    while True:
        # Main menu
        print("\nMain Menu")
        print("1. besa module")
        print("2. bualat module")
        print("3. maestre module")
        print("4. salespara module")
        print("5. serquina module")
        print("6. exit")

        choice = input("Enter your choice: ")

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("\nInvalid choice, please enter a number between 1 and 6.")
            # Prompt the user again if the input is invalid
            continue 
        
        match choice:
            case '1':
                # Call besa.py modeule 
                print("\nYou selected besa module")
                besa.show_manila_time()

            case '2':
                # Call bualat.py module
                print("\nYou selected bualat module")
                bualat.hero_num()
                bualat.hero_name()

            case '3':
                # Call maestre.py module
                print("\nYou selected maestre module")
                maestre.generate_fake_profile()

            case '4':
                # Call salespara.py module
                print("\nYou selected salespara module")
                salespara.give_joke()
                
            case '5':
                # Call serquina.py module
                print("\nYou selected serquina module")
                serquina.text_to_art()

            case '6':
                # Exit the program
                print("\nThank you for using the program. Goodbye!")
                exit()

if __name__ == "__main__":
    main()