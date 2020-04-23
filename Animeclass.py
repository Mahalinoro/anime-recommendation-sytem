import ast
from userinput import *
from firebasedb import *

class Anime:

    def __init__(self,id,  popular, members, favorite):
        self.popular = popular
        self.id = id
        self.members = members
        self.favorite = favorite

    # returns movie id
    def getid(self):
        return getid()
    # gets anime id and return its objects
    def animegetter(self, id):
        doc_ref = db.collection(u'Animess').document(getid(id))
        doc = doc_ref.get()
        if doc.exists:
            return  (u'Document data : {} '.format(doc.to_dict()))
        else:
            print("No such movie")
            return (u'No such document!')
    # gets a sorted list of popular id movies and prints them out
    def sortbypopularity(self, popular ):
        for i in popular:
            print(Anime.animegetter("self", str(i)))
            return Anime.animegetter("self", str(i))
    # gets a sorted list of id movies with most pple and prints them out
    def sortbymembers(self, members ):
        for i in members:
            print(Anime.animegetter("self", str(i)))
            return Anime.animegetter("self", str(i))
    # gets a sorted list of id movies which alot of pple have put on fav and prints/returns them
    def sortbyfavorite(self, favorite):
        for i in favorite:
            print(Anime.animegetter("self", str(i)))
            return Anime.animegetter("self", str(i))

    def animeobject(self, title) :
        dic = (Anime.animegetter("set", title))[16:-1]
        return ast.literal_eval(dic)

# //TODO
# #     impement a method that returns sorted list of ids  by:
#       1 by popularity
#       2 by Genre
# #     3 by rank
#       4 by favorites
#       5 by members


