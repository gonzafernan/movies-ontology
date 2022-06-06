from owlready2 import *


onto = get_ontology("file://mymovies.owl")
base_onto = get_ontology("file://movies.owl").load()
onto.imported_ontologies.append(base_onto)

# Create MovieList class
with onto:
    class MovieList(Thing):
        pass

    class RecommendedList(MovieList):
        pass

    class WatchList(MovieList):
        pass

    class WatchedList(onto.MovieList):
        pass

    # Add properties
    # name for lists
    """
    class name(DataProperty):
        domain = [base_onto.data_properties().domain, MovieList]
        range = [str]
    """

    # Movie is in list
    class hasMovie(MovieList >> base_onto.Movie, FunctionalProperty, AsymmetricProperty, IrreflexiveProperty):
        pass

    class liked(hasMovie, FunctionalProperty, AsymmetricProperty, IrreflexiveProperty):
        domain = [WatchedList]
        range = [base_onto.Movie]

    class reallyLiked(hasMovie, FunctionalProperty, AsymmetricProperty, IrreflexiveProperty):
        domain = [WatchedList]
        range = [base_onto.Movie]

    class disliked(hasMovie, FunctionalProperty, AsymmetricProperty, IrreflexiveProperty):
        domain = [WatchedList]
        range = [base_onto.Movie]

    class reallyDisliked(hasMovie, FunctionalProperty, AsymmetricProperty, IrreflexiveProperty):
        domain = [WatchedList]
        range = [base_onto.Movie]


if __name__ == '__main__':
    print(onto.search(is_a=base_onto.Movie))
    usr_watchlist = WatchList("My_Watchlist")
    usr_watchlist.hasMovie = base_onto.The_Matrix

    usr_watched = WatchedList("AlreadyWatched")
    usr_watched.liked = base_onto.The_Matrix

    usr_recommend = RecommendedList("YouShouldWatch")

    # onto.WatchedList.hasMovie = [base_onto.The_Matrix, base_onto.Citizen_Kane]
    # onto.The_Matrix.is_a.append(onto.WatchedMovie)
    print(list(onto.hasMovie.get_relations()))
    onto.save()
