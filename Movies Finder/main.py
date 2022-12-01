# Project created by: Ben Cook, Erik Konnath, James Coddington, Viet Ninh
# pip install mysql-connector, pip install wheel
import mysql.connector

def database_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movies"
    )

    return connection
    

def find_platforms(movie_name):
    connection = database_connection()

    # cursor for executing queries to the database
    cursor = connection.cursor()

    query = f"select platforms from movies WHERE name = '{movie_name}'"
    cursor.execute(query)

    table = cursor.fetchall()

    # check if movie exists
    if not table:
        print(f"{movie_name} does not exist in our database")
    else:
        # table is a list(tuple()) so we just want to return the values in the tuple
        return table[0][0]


def find_movies(platform_name):
    pass



answer = input("Would you like to search for a movie? [y/n]")

if answer.upper() == "Y":
    movie_name = input("What movie would you like to search for?\n")
    platforms = find_platforms(movie_name)

    if platforms:
        platforms = platforms.replace(",", "\n")
        print(f"The movie {movie_name} can be found on: \n{platforms}")

elif answer.upper() == "N":
    new_answer = input("Would you like to see a catalogue of movies on a platform? [y/n]")
    
    if new_answer.upper() == "Y":
        platform_name = input("What platform would you like to search for?\n")
        movies = find_movies(platform_name)
    
    elif new_answer.upper() == "N":
        print("Exiting the application...")
else:
    print("Input not recognized ending program")