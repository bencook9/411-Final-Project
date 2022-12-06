# Project created by: Ben Cook, Erik Konnath, James Coddington, Viet Ninh
# pip install mysql-connector, pip install wheel
import sqlite3

connection = sqlite3.connect("MoviesFinder.db")

# cursor for executing queries to the database
cursor = connection.cursor()


def find_platforms(movie_name):

    query = f"""select platforms.platform_name from movies
                 join on_platform on movies.movie_id = on_platform.movie_id 
                join platforms on platforms.platform_id = on_platform.platform_id 
                where movies.name ='{movie_name}';"""
    cursor.execute(query)

    table = cursor.fetchall()

    # check if movie exists
    if not table:
        print(f"{movie_name} does not exist in our database \n")
        query = f"SELECT movies.name FROM movies;"
        cursor.execute(query)
        table = cursor.fetchall()
        entries = []
        for entry in table:
            for platform in entry:
                entries.append(platform)
        print("Please select one of these movies from our database: \n")
        print(f'\n'.join(entries))

    else:
        entries = []
        for entry in table:
            for platform in entry:
                entries.append(platform)
        return entries


def find_movies(platform_name):

    query = f"""SELECT movies.name FROM movies
                join on_platform on movies.movie_id = on_platform.movie_id 
                join platforms on platforms.platform_id = on_platform.platform_id 
                where platforms.platform_name ='{platform_name}';"""
    cursor.execute(query)

    table = cursor.fetchall()
    
    # check if platform has movies
    if not table:
        print(f"{platform_name} does not have any movies in our database")
        query = f"SELECT platforms.platform_name FROM platforms;"
        cursor.execute(query)
        table = cursor.fetchall()
        entries = []
        for entry in table:
            for platform in entry:
                entries.append(platform)
        print("Please select one of these platforms from our database: \n")
        print(f'\n'.join(entries))

    else:
        entries = []
        for entry in table:
            for movie in entry:
                entries.append(movie)
        return entries


answer = input("Enter [m] if you want to search a movie. Enter [p] if you wish to search a platform:\n")

match answer.upper():
    case "M":
        movie_name = input("What movie would you like to search for?\n")
        platforms = find_platforms(movie_name.upper())

        if platforms:
            print(f"""\nHere are the platforms for the movie "{movie_name}":\n""")
            print(f'\n'.join(platforms))
        
    case "P":
        platform_name = input("What platform would you like to search for?\n")
        movies = find_movies(platform_name.upper())
        
        if movies:
            print(f"""\nHere are the movies from "{platform_name}":\n""")
            print(f'\n'.join(movies))

    case _:
        print("Input not recognized ending program")