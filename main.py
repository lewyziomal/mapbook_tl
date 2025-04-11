users:list = [
    {"name":"Tomasz","location":"Prudnik","posts":400},
    {"name":"Adrian","location":"Toruń","posts":500},
    {"name":"Bartek","location":"Giżycko","posts":700},
    {"name":"Bernard","location":"Ełk","posts":200}
]



def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"Twoj znajomy {user['name']}! z miejscowosci {user['location']} opublikował {user['posts']} postów")

get_user_info(users)