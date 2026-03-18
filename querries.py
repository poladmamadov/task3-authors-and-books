from database import create_tables
from insert import add_author, add_book

create_tables()

def querry():
    while True:
        print("\n--- Kitab və Müəllif İdarəetmə Sistemi ---")
        print("1. Müəllif əlavə et")
        print("2. Kitab əlavə et")
        print("3. Çıxış")

        choice = input("Seçim: ")

        if choice == "1":
            name = input("Müəllif adı: ")
            if add_author(name):
                print("Müəllif əlavə edildi!")
            else:
                print("Müəllif əlavə etmək alınmadı!")
        
        elif choice == "2":
            book_name = input("Kitab adı: ")
            try:
                author_id = int(input("Müəllif ID: "))
                if add_book(book_name, author_id):
                    print("Kitab əlavə edildi!")
                else:
                    print("Kitab əlavə etmək alınmadı!")
            except ValueError:
                print("Xəta: Müəllif ID-rəqəm olmalıdır!")
        
        elif choice == "3":
            print("Çıxış edilir...")
            break

querry()