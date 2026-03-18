from database import create_tables, get_connection
from insert import add_author, add_book

create_tables()

def querry():
    while True:
        print("\n--- Kitab və Müəllif İdarəetmə Sistemi ---")
        print("1. Müəllif əlavə et")
        print("2. Kitab əlavə et")
        print("3. Müəllifləri və kitablarını göstər")
        print("4. Müəlliflərin kitab sayını göstər")
        print("0. Çıxış")

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
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.name, b.book_name
                FROM authors a
                LEFT JOIN books b ON a.id = b.author_id
                ORDER BY a.name
            """)
            print("\n--- Müəllif və Kitabları ---")
            for row in cursor:
                print(f"Müəllif: {row[0]}, Kitab: {row[1] if row[1] else 'Kitab yoxdur'}")
            cursor.close()
            conn.close()

        elif choice == "4":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.name, COUNT(b.id) AS kitab_sayi
                FROM authors a
                LEFT JOIN books b ON a.id = b.author_id
                GROUP BY a.name
                ORDER BY kitab_sayi DESC
            """)
            print("\n--- Müəlliflərin Kitab Sayı ---")
            for row in cursor:
                print(f"Müəllif: {row[0]}, Kitab sayı: {row[1]}")
            cursor.close()
            conn.close()
        
        elif choice == "0":
            print("Çıxış edilir...")
            break

querry()
