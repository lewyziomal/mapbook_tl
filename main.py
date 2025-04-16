from utils.model import users
from utils.controller import get_user_data, add_user


def main():
    while True:

        print("MENU")
        print("0 - zakoncz program ")
        print("1 - pokaz co u znajomych")
        print("2 - dodaj nowego znajomego")
        print("==============================")
        choice = input("wybierz opcje menu")
        if choice == "0": break
        if choice == "1": geu_user_info(info)
        if choice == "2": add_user(users)


if __name__ == "__main__":
    main()