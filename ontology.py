from owlready2 import *

import movie
from movie import Movie


onto_path.append("./")

# Load the base ontology created
onto = get_ontology("file://movies.owl").load()


def add_movie(movie_id):
    # Construct movie with info from TMDB
    mov = Movie(movie_id)
    mov.print_info()

    # Movie details
    mov_ind = onto.Movie(mov.title.replace(" ", "_"), namespace=onto, title=mov.title, tagline=mov.tagline,
                         budget=mov.budget, revenue=mov.revenue)

    # Movie cast
    cast_ind = onto.Cast(mov.title.replace(" ", "_") + "_Cast", namespace=onto)

    for actor in mov.cast:
        # actor.name not working
        # act_ind = onto.Actor(actor.name.replace(" ", "_"), namespace=onto, name=actor.name, gender=actor.gender,
        act_ind = onto.Actor(actor.name.replace(" ", "_"), namespace=onto, gender=actor.gender,
                             character=actor.character)
        cast_ind.hasActor = act_ind

    # Movie crew
    crew_ind = onto.Crew(mov.title.replace(" ", "_") + "_Crew", namespace=onto)

    for member in mov.crew:
        # member.name not working
        mem_ind = onto.Member(member.name.replace(" ", "_"), namespace=onto, gender=member.gender,
                              department=member.department, job=member.job)
        if member.job == "Director":
            crew_ind.hasDirector = mem_ind
        elif member.job == "Producer":
            crew_ind.hasProducer = mem_ind
        else:
            crew_ind.hasMember = mem_ind

    mov_ind.hasCrew = crew_ind

    # Save the ontology
    onto.save()


if __name__ == '__main__':
    # movie.search("The Matrix")
    add_movie(604)
