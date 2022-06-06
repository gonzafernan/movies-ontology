from owlready2 import *

base_onto = get_ontology("file://movies.owl")
onto = get_ontology("file://mymovies.owl")
onto.imported_ontologies.append(base_onto.load())

onto.load()

if __name__ == '__main__':

    print(onto.base_iri)

    with onto:
        rule = Imp()
        rule.set_as_rule("""
        Movie(The_Matrix)^Movie(The_Matrix_Reloaded)^WatchedList(?w)^hasMovie(?w, The_Matrix)^RecommendedList(?r)->hasMovie(?r, The_Matrix_Reloaded)
        """)

    # sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)

    onto.save()
