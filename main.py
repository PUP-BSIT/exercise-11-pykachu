from pykachupackage import besa, bualat, serquina, maestre

def main():
    while True:
        print("\nMain Menu")
        print("1. besa module")
        print("2. bualat module")
        print("3. maestre module")
        print("4. salespara module")
        print("5. serquina module")
        print("6. exit")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                print("\nYou selected besa module")
                besa.show_manila_time()
            case '2':
                print("\nYou selected bualat module")
                bualat.hero_num()
                bualat.hero_name()
            case '3':
                print("\nYou selected maestre module")
                maestre.generate_fake_profile()
            case '4':
                print("\nYou selected salespara module")
            case '5':
                print("\nYou selected serquina module")
                serquina.text_to_art()
            case '6':
                print("Thank you for using the program. Goodbye!")
                exit()
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()