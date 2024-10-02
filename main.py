
#  User story.
#  As a user, I want to be able to ...
#  1. Add new movies to the my Collections.
#  2. View all the movies in my Collections.
#  3. Find a movie by its title.



# moview list
movies = []

# function to add a movie to the list
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

# function to show all the movies in the list
def show_movies():
    if not movies:
        print("The movie list is empty. Please add a movie.")
    else:
        for index, movie in enumerate(movies, 1):
            print(f"{index}. Title: {movie['title']}, Ditector: {movie['director']}, Year: {movie['year']}")

def main():
    while True:
        print("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, and 'q' to quit.")
        user_input = input("Enter your choice: ")

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            pass
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()