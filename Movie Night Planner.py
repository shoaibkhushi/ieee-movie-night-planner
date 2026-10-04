import csv

#movies class
class Movies:
    def __init__(self,title,genre,rating,duration):
        self.title = title
        self.genre = genre
        self.rating = float(rating)
        self.duration = int(duration)
    #detail Method    
    def get_details(self):
        return f"{self.title} | {self.genre} | Rating: {self.rating} | {self.duration} Minute"
    def __str__(self):
        return self.get_details()
    #movies detail
    def load_movies(filename = "movies.csv"):
        movies = []
        #exception handling
        try:
            with open(filename,newline="",encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies.append(
                        Movies(row["title"],row["genre"],row["rating"],row["duration"])
                    )
        except FileNotFoundError:
            print(f"Error: {filename} not found")
        return movies
        #view all mnovie

    def view_all(movies):
        print("-----All Movies-----")
        for i, movies in enumerate(movies,start = 1): 
             print(f"{i}. {movies}")
    #filter movie
    def filter_by_genre(movies,genre):
        return [m for m in movies if m.genre.lower() == genre.lower()]

    #filter by rating
    def filter_by_rating(movies,min_rating):
        return [m for m in movies if m.rating >= min_rating]
 #class Watchlist
class Watchlist:
    def __init__(self):
        self.movies = []
    def add(self,movie):
        if any(m.title.lower() == movie.title.lower() for m in self.movies):
            print(f"'{movie.title}' is Already in your watchlist.")
            return
        self.movies.append(movie)
        print(f"Added '{movie.title}' to your Watchlist.")
    #remove Movies
    def remove(self,title):
        for m in self.movies:
            if m.title.lower() == title.lower():
                self.movies.remove(m)
                print(f"Removed '{m.title}' form your Watchlist.")
                return
        print(f"{title} is not in your watchist.") 
    #show Watchlist
    def show(self):
        print("----Your Watch list")
        if not self.movies:
            print("Your Watchlist is empty.")
            return
        for m in self.movies:
            print(f"-{m}")
    def total_duration(self):
        return sum(m.duration for m in self.movies)

    def average_duration(self):
        if not self.movies:
            return 0.0
        return sum(m.rating for m in self.movies) / len(self.movies)
    def show_analytics(self): 
        print("---- Watchlist Analytics ----")
        print(f"Total duration : {self.total_duration()} minutes")
        print(f"Average rating : {self.average_duration():.2f}")

    def find_movies(movies, title):
        for m in movies:
            if m.title.lower() == title.lower():
                return m
        return None

    #main menu
    def print_menu():
        print("="*50)
        print("==== Movies Night Planer ====")
        print("1:View all Movies")
        print("2:Filter By Genre")
        print("3:Filter By Minimum Rating")
        print("4:Add Movies to Watchlist")
        print("5:Remove Movies from watchlist")
        print("6:View Watchlist")
        print("7:Watchlist Analytics")
        print("8:Exist")
        print("="*50)

    def show_results(resultes):
        if not resultes:
            print("No Movies Found")
        for m in resultes:
            print(f"-{m}")

    #main
def main():
        movies = Movies.load_movies("movies.csv")
        if not movies:
            return
        main1 = Watchlist()
        while True:
            Watchlist.print_menu() 
            choice = input("Enter Your Choice: ").strip()

            if choice == "1":
               Movies.view_all(movies)
            elif choice == "2":
                genre = input("Enter Genre: ").strip()
                Watchlist.show_results(Movies.filter_by_genre(movies,genre))
            elif choice == "3":
                try:
                    min_rating = float(input("Enter Minimum rating (e.g. 8.0)"))
                    Watchlist.show_results(Movies.filter_by_rating(movies,min_rating))
                except ValueError:
                    print("Please enter a Valid Number. ")
            elif choice == "4":
                titile = input("Movie title to add: ").strip()
                movie = Watchlist.find_movies(movies, titile) 

                if movie:
                    main1.add(movie)
                else:
                    print("Movie not found in list.")
            elif choice == "5":
                main1.remove(input("Movie title to remove: ").strip()) 
            elif choice == "6":
                main1.show()
            elif choice == "7":
                main1.show_analytics() 
            elif choice == "8":
                print("Enjoy Night Movie")
                break
            else:
                print("Invalid Option. Try Again.")

if __name__ == "__main__":
    main()