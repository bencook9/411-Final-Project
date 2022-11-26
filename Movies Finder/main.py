# Project created by: Ben Cook, Erik Konnath, James Coddington, Viet Ninh
# pip install mysql-connector, pip install wheel
import mysql.connector


def find_platforms(movie_name):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movies"
    )

    cursor = connection.cursor()

    query = f"select platforms from platforms WHERE name = '{movie_name}'"
    cursor.execute(query)

    table = cursor.fetchall()

    # check if movie exists
    if not table:
        print(f"{movie_name} does not exist in our database")
    else:
        # table is a list(tuple()) so we just want to return the values in the tuple
        return table[0][0]


movie_name = input("What movie would you like to search for?\n")

platforms = find_platforms(movie_name)

if platforms:
    platforms = platforms.replace(",", "\n")
    print(f"The movie {movie_name} can be found on: \n{platforms}")