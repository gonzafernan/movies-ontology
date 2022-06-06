import tmdbsimple as tmdb
from keys import API_KEY

tmdb.API_KEY = API_KEY


def search(name):
    search = tmdb.Search()
    response = search.movie(query=name)
    for movie in search.results:
        print(movie['title'], movie['id'], movie['release_date'])


class Person:
    name = ""
    gender = ""
    job = ""


class CrewMember(Person):
    department = ""

    def __init__(self, name, gender, department, job):
        self.name = name
        self.gender = gender
        self.department = department
        self.job = job


class Actor(Person):
    character = ""

    def __init__(self, name, gender, character):
        self.name = name
        self.gender = gender
        self.character = character


class Movie:
    title = ""
    tagline = ""
    budget = 0
    revenue = 0
    crew = []
    cast = []

    def __init__(self, id):
        # Movie details
        movie = tmdb.Movies(id)
        response = movie.info()
        self.title = movie.title
        self.tagline = movie.tagline
        self.budget = movie.budget
        self.revenue = movie.revenue

        # Movie cast
        for actor in movie.credits()["cast"]:
            # Gender number to string (easily to understand)
            if actor['gender'] == 1:
                gender = "Female"
            elif actor['gender'] == 2:
                gender = "Male"
            else:
                gender = "Not specified"

            # Add member to crew list
            self.cast.append(Actor(actor['name'], gender, actor['character']))

        # Movie crew
        for member in movie.credits()["crew"]:
            # Gender number to string (easily to understand)
            if member['gender'] == 1:
                gender = "Female"
            elif member['gender'] == 2:
                gender = "Male"
            else:
                gender = "Not specified"

            # Add member to crew list
            self.crew.append(CrewMember(member['name'], gender, member['department'], member['job']))

    def print_info(self):
        print("Title: " + self.title)
        print("Tagline: " + self.tagline)
        print("Budget: " + str(self.budget))
        print("Revenue: " + str(self.revenue))


if __name__ == '__main__':
    mov = Movie(603)
    mov.print_info()

    """
    movie = tmdb.Movies(603)
    response = movie.info()

    print("List of actors (cast):")
    for actor in movie.credits()["cast"]:
        print("Name: " + actor["name"] + "\t Character: " + actor["character"] + "\t Gender: " + str(actor["gender"]))

    print("List of crew member:")
    for actor in movie.credits()["crew"]:
        print("Name: " + actor["name"] + "\t\t\tDepartment: " + actor["department"] + "\t\t\tGender: " + str(actor["gender"])
              + "\t\t\tJob: " + str(actor["job"]))
    """
