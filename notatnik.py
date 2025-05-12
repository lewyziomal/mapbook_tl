users:list = [ {"name":"Zuzia","location":"Radzyń_Podlaski","posts":700}]

print(users)

def update_user(users_data: list)->None:

    user_name=input("podaj imię użytkownika którego dane chcesz zaktualizować: ")
    for user in users_data:
        if user["name"] == user_name:
            user["name"] = input("podaj nowe imię użytkownika: ")
            user["location"] = input("podaj nową lokalizaję użytkownika: ")
            user["posts"] = int(input("podaj nową liczbę postów użytkownika : "))


update_user(users)




print(users)