import mysql.connector

def show_books():
    global cursor
    text = "select * from books"
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passeord="0000",
            databse="library"
        )
        cursor = connection.cursor()
        try:
            cursor.execute(text)
        except:
            print("Bazaga murojat qilishda xatolik")

        try:
            result = cursor.fetchall()
            return result
        except:
            print("Natija olishda xatolik")

        cursor.close()
        connection.close()

    except:
        print("Database ga ulanishda xatilik")


def show_students():
    global cursor
    text = "select * from students"
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passeord="0000",
            databse="library"
        )
        cursor = connection.cursor()
        try:
            cursor.execute(text)
        except:
            print("Bazaga murojat qilishda xatolik")

        try:
            result = cursor.fetchall()
            return result
        except:
            print("Natija olishda xatolik")

        cursor.close()
        connection.close()

    except:
        print("Database ga ulanishda xatilik")
