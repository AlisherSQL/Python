1.Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student

import json

def load_json(par):
    with open(par) as f:
        global j_obg
        j_obg=json.load(f)
        return j_obg
load_json("students.json")

2. Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) 
and print relevant information 
(temperature, humidity, etc.)

import requests

def ob_hav(shahar, api_kalit):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={shahar}&appid={api_kalit}&units=metric&lang=uz"

    df=requests.get(url)
    
    if df.status_code==200:
        q=df.json()
        nomi = q['name']
        harorat=q['main']['temp']
        print(f'{nomi}')
        print(f'{harorat}')
    else:   
        print('no')
api_kalit='92d4009968335bea71e87bf9d4333c4f'
ob_hav('london',api_kalit)


3. Task: JSON Modification 
Write a program that allows users to add new books, update existing book information, and delete books 
from the books.json JSON file.


  import json
import os

FILE_NAME = "books.json"

# Fayl mavjud bo'lmasa, bo'sh ro'yxat bilan yaratamiz
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_books(books):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def add_book():
    books = load_books()
    book_id = int(input("Kitob ID raqamini kiriting: "))
    title = input("Kitob nomini kiriting: ")
    author = input("Muallif ismini kiriting: ")
    year = int(input("Yilni kiriting: "))

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    })

    save_books(books)
    print("✅ Kitob qo'shildi.")

def update_book():
    books = load_books()
    book_id = int(input("Tahrirlanadigan kitob ID raqamini kiriting: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input(f"Yangi nom ({book['title']}): ") or book["title"]
            book["author"] = input(f"Yangi muallif ({book['author']}): ") or book["author"]
            year_input = input(f"Yangi yil ({book['year']}): ")
            book["year"] = int(year_input) if year_input else book["year"]
            save_books(books)
            print("✅ Kitob yangilandi.")
            return
    print("❌ Kitob topilmadi.")

def delete_book():
    books = load_books()
    book_id = int(input("O‘chiriladigan kitob ID raqamini kiriting: "))
    books = [book for book in books if book["id"] != book_id]
    save_books(books)
    print("✅ Kitob o‘chirildi.")

def main():
    while True:
        print("\n--- Kitoblar bilan ishlash ---")
        print("1. Yangi kitob qo‘shish")
        print("2. Kitobni tahrirlash")
        print("3. Kitobni o‘chirish")
        print("4. Chiqish")
        choice = input("Tanlang (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            break
        else:
            print("❗ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

if __name__ == "__main__":
    main()


4.Task: Movie Recommendation System
Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre


import requests
import random

API_KEY = "SIZNING_API_KEY"  # Bu yerga OMDb API kalitini yozing
OMDB_URL = "http://www.omdbapi.com/"

def film_topish(janr):
    # Qidirish uchun ba'zi ommabop so'zlardan foydalanamiz
    so‘zlar = ["love", "war", "future", "man", "woman", "life", "death", "city", "story"]
    filmlar = []

    for s in so‘zlar:
        params = {
            "apikey": API_KEY,
            "s": s,
            "type": "movie"
        }
        javob = requests.get(OMDB_URL, params=params)
        data = javob.json()

        if "Search" in data:
            for film in data["Search"]:
                # Har bir film haqida batafsil ma’lumot so‘raymiz
                imdbID = film["imdbID"]
                tafsilot = requests.get(OMDB_URL, params={"apikey": API_KEY, "i": imdbID}).json()
                if janr.lower() in tafsilot.get("Genre", "").lower():
                    filmlar.append(tafsilot)

    if filmlar:
        tanlangan = random.choice(filmlar)
        print("\n🎬 Sizga tavsiya: ")
        print(f"Nomi: {tanlangan['Title']}")
        print(f"Yili: {tanlangan['Year']}")
        print(f"Janr: {tanlangan['Genre']}")
        print(f"Rejissor: {tanlangan.get('Director', 'Noma’lum')}")
        print(f"IMDb reyting: {tanlangan.get('imdbRating', 'Yo‘q')}")
        print(f"Qisqacha: {tanlangan.get('Plot', 'Ma’lumot yo‘q')}")
    else:
        print("❌ Afsuski, bu janrga mos film topilmadi.")

def asosiy():
    print("🎥 Film tavsiya dasturi")
    janr = input("Qaysi janrdagi film kerak? (masalan: Action, Comedy, Drama): ")
    film_topish(janr)

if __name__ == "__main__":
    asosiy()




















  
