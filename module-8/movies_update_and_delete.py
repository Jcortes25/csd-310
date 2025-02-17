import mysql.connector

def connect_to_db():
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL username
        password="password",  # Update with your MySQL password
        database="movies"  # Update with your database name
    )
    return connection

def show_films(cursor, label):
    print(label)
    query = """
        SELECT film_name AS Name, director_name AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    # Print the result in a formatted manner
    print(f"{'Name':<30}{'Director':<30}{'Genre':<20}{'Studio Name'}")
    print("="*80)
    for film in films:
        print(f"{film[0]:<30}{film[1]:<30}{film[2]:<20}{film[3]}")
    print("="*80)

def insert_film(cursor, connection):
    # Insert a new film record (Example: Inserting 'The Matrix')
    query = """
        INSERT INTO film (film_name, director_name, genre_id, studio_id)
        VALUES ('The Matrix', 'The Wachowskis', 1, 1);  # Assumes 1 is a valid genre and studio ID
    """
    cursor.execute(query)
    connection.commit()

def update_film(cursor, connection):
    # Update the genre of the film "Alien" to "Horror"
    query = """
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien';
    """
    cursor.execute(query)
    connection.commit()

def delete_film(cursor, connection):
    # Delete the movie "Gladiator"
    query = "DELETE FROM film WHERE film_name = 'Gladiator';"
    cursor.execute(query)
    connection.commit()

def main():
    # Connect to the database
    connection = connect_to_db()
    cursor = connection.cursor()

    # Display the films before any operation
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film
    insert_film(cursor, connection)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERTION")

    # Update the genre of 'Alien' to 'Horror'
    update_film(cursor, connection)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the movie 'Gladiator'
    delete_film(cursor, connection)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")

    # Close the connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
