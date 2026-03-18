from database import get_connection


def add_author(name):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO authors (name) VALUES (:1)",
            (name,)
        )
        
        conn.commit()
        print(f"{name} müəllifi əlavə edildi.")
        return True
    
    except Exception as e:
        print(f"Xəta: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def add_book(book_name, author_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO books (book_name, author_id) VALUES (:1, :2)",
            (book_name, author_id)
        )

        conn.commit()
        print(f"{book_name} kitabı əlavə edildi.")
        return True
    except Exception as e:
        print(f"Xəta: {e}")
        return False
    
    finally:
        cursor.close()
        conn.close()