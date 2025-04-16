from utils.model import users
from utils.controler import get_user_data


def main():
    while True:

        print("MENU")
        print("0 - zakoncz program ")
        print("1 - pokaz co u znajomych")
        print("==============================")
        choice = input("wybierz opcje menu")
        if choice == "0": break
        if choice == "1": geu_user_info(info)


if __name__ == "__main__":
    main()