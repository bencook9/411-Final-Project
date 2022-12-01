# Project created by: Ben Cook, Erik Konnath, James Coddington, Viet Ninh
# pip install mysql-connector, pip install wheel
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "movies_finder"
)

# cursor for executing queries to the database
cursor = connection.cursor()
    

def find_platforms(movie_name):

    query = f"""select platforms.platform_name from movies join on_platform on movies.movieId = on_platform.movie_id 
                join platforms on platforms.platform_id = on_platform.platform_id 
                where movies.name ='{movie_name}';"""
    cursor.execute(query)

    table = cursor.fetchall()

    # check if movie exists
    if not table:
        print(f"{movie_name} does not exist in our database")
    else:
        return table


def find_movies(platform_name):

    query = f"""SELECT movies.name FROM movies
                join on_platform on movies.movieId = on_platform.movie_id 
                join platforms on platforms.platform_id = on_platform.platform_id 
                where platforms.platform_name ='{platform_name}';"""
    cursor.execute(query)

    table = cursor.fetchall()
    # check if platform has movies
    if not table:
        print(f"{platform_name} does not have any movies in our database")
    else:
        return table


answer = input("Enter [m] if you want to search a movie. Enter [p] if you wish to search a platform:\n")

match answer.upper():
    case "M":
        movie_name = input("What movie would you like to search for?\n")
        # MAKE CALL TO METHOD movie_name.lower()
        platforms = find_platforms(movie_name)

        if platforms:
            print(platforms)
        
    case "P":
        platform_name = input("What platform would you like to search for?\n")
        # MAKE CALL TO METHOD platform_name.lower()
        movies = find_movies(platform_name)
        
        if movies:
            print(movies)

    case _:
        print("Input not recognized ending program")