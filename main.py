def display_menu():
    print("---- Menu ----")
    print("1) Choice 1")
    print("2) Choice 2")
    print("3) Choice 3")
    print("Q) Quit.")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        choice = choice.lower()
        print()

        if choice == "1":
            print("Choice one")
            print()

        elif choice == "2":
            print("Choice two")
            print()

        elif choice == "3":
            print("Choice three")
            print()

        elif choice == "q":
            break

if __name__ == "__main__":
    main()