def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"Twoj znajomy {user['name']}! z miejscowosci {user['location']} opublikował {user['posts']} postów")
