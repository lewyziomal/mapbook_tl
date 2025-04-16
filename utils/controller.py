def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twoj znajomy {user['name']}! z miejscowosci {user['location']} opublikował {user['posts']} postów")


user_name = input("podaj imie nowego uzytkownika: "),
user_location = input("podaj lokalizacje znajomego"),
user_posts = input("oidaj liczbe postow"),
users_data.append({"name": user_name, "location": user_location, "posts": user_posts})


def remove_user(useers_data: list) -> None:
    user_name = imput("podaj imie  uzytkownika do usuniecia: ")
    for user in users_data
        if user['name'] == user_name:
            users.remove(user)