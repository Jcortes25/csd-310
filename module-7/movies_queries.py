import mysql.connector

db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password",
    database="movies" 
)

cursor = db.cursor()

print("Query 1: Select all fields from the studio table")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(studio)
print("\n")

print("Query 2: Select all fields from the genre table")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(genre)
print("\n")

print("Query 3: Select movie names where the runtime is less than 2 hours")
cursor.execute("SELECT movie_name FROM movie WHERE runtime < 120") 
movies_under_2_hours = cursor.fetchall()
for movie in movies_under_2_hours:
    print(movie[0]) 
print("\n")

print("Query 4: List of film names and directors, grouped by director")
cursor.execute("SELECT director, GROUP_CONCAT(movie_name) FROM movie GROUP BY director")
directors_movies = cursor.fetchall()
for director in directors_movies:
    print(f"Director: {director[0]} \nMovies: {director[1]}")
print("\n")

cursor.close()
db.close()
