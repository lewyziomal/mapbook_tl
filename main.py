from tkinter import *
import tkintermapview


users:list = []


def add_user():
    zmienna_imie=entry_name.get()
    zminna_nazwisko=entry_surname.get()
    zminna_miejscowosc=entry_location.get()
    zminna_posty=entry_posts.get()

    users.append({"name":zmienna_imie, "surname":zminna_nazwisko, "location": zminna_miejscowosc, "posts": zminna_posty})
    print(users)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_location.delete(0, END)
    entry_posts.delete(0, END)
    entry_name.focus()
    show_users()

def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate (users):
        listbox_lista_obiektow.insert(idx,f"{idx+1}. {user["name"]} {user["surname"]}")


def remove_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    users.pop(i)
    show_users()

def show_user_details():
    i=listbox_lista_obiektow.index(ACTIVE)
    user_name=users[i]["name"]
    surname=users[i]["surname"]
    location=users[i]["location"]
    posts=users[i]["posts"]
    label_name_szcegoly_obiektow_wartosc.configure(text=user_name)
    label_surname_szcegoly_obiektow_wartosc.configure(text=surname)
    label_posts_szcegoly_obiektow_wartosc.configure(text=posts)
    label_location_szcegoly_obiektow_wartosc.configure(text=location)

def edit_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    user_name=users[i]["name"]
    surname=users[i]["surname"]
    location=users[i]["location"]
    posts=users[i]["posts"]
    entry_name.insert(0, users[i])
    entry_surname.insert(0, users[i])
    entry_location.insert(0, users[i])
    entry_posts.insert(0, users[i])

    button_dodaj_obiekt.config(text="zapisz",command=lambda: update_user(i))

def update_user(i):
    zmienna_imie=entry_name.get()
    zminna_nazwisko=entry_surname.get()
    zminna_miejscowosc=entry_location.get()
    zminna_posty=entry_posts.get()
    users[i]['name'] = zmienna_imie
    users[i]['surname'] = zminna_nazwisko
    users[i]['location'] = zminna_miejscowosc
    users[i]['posts'] = zminna_posty
    show_users()

    button_dodaj_obiekt.config(text="dodaj użytkownika",command=add_user)

    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_location.delete(0, END)
    entry_posts.delete(0, END)
    entry_name.focus()







root = Tk()
root.geometry("1200x800")
root.title("mapbook_tl")

ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="lista obiektow")
label_lista_obiektow.grid(row=0, column=0, columnspan=2)
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=60, height=15)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text="pokaż szczegóły", command=show_user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt = Button(ramka_lista_obiektow, text="usuń obiekt", command=remove_user)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="edytuj", command=edit_user)
button_edytuj_obiekt.grid(row=2, column=2)



# ramka_formularz
label_ramka_formularz = Label (ramka_formularz, text=" formularz")
label_ramka_formularz.grid(row=0, column=0, sticky=W)
label_name = Label(ramka_formularz, text=" imie")
label_name.grid(row=1, column=0, sticky=W)
label_surname = Label(ramka_formularz, text=" nazwisko")
label_surname.grid(row=2, column=0, sticky=W)
label_location = Label(ramka_formularz, text=" miejscowosc")
label_location.grid(row=3, column=0, sticky=W)
label_posts = Label(ramka_formularz, text=" posty")
label_posts.grid(row=4, column=0, sticky=W)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname = Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_location = Entry(ramka_formularz)
entry_location.grid(row=3, column=1)
entry_posts = Entry(ramka_formularz)
entry_posts.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text="dodaj uzytkownika", command=add_user)
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

# sczegoly_obiektu
label_szczegoly_obiektow = Label(ramka_szczegoly_obiektow, text=" szczegóły obiektu:")
label_szczegoly_obiektow.grid(row=0, column=0)
label_name_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text=" imie")
label_name_szcegoly_obiektow.grid(row=1, column=0)
label_name_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text=" .......")
label_name_szcegoly_obiektow_wartosc.grid(row=1, column=1)
label_surname_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text=" nazwisko")
label_surname_szcegoly_obiektow.grid(row=1, column=2)
label_surname_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text=" .......")
label_surname_szcegoly_obiektow_wartosc.grid(row=1, column=3)
label_location_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text=" miejscowosc")
label_location_szcegoly_obiektow.grid(row=1, column=4)
label_location_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text=" .......")
label_location_szcegoly_obiektow_wartosc.grid(row=1, column=5)
label_posts_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text=" posty")
label_posts_szcegoly_obiektow.grid(row=1, column=6)
label_posts_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text=" .......")
label_posts_szcegoly_obiektow_wartosc.grid(row=1, column=7)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=600, corner_radius=5)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)
map_widget.grid(row=0, column=0, columnspan=2)







root.mainloop()