from Animeclass import *

class animes:
    def __init__(self, title, type, genre, episodeNumber, episodeDuration, airedFrom, airing, rating, score, scoredBy, rank, popularity, members, favorites, background,name):
        self.title = title
        self.type = type
        self.genre = genre
        self.episodeNumber = episodeNumber
        self.episodeDuration = episodeDuration
        self.airedFrom = airedFrom
        self.airing = airing
        self.rating = rating
        self.score = score
        self.scoredBy = scoredBy
        self.rank = rank
        self.popularity = popularity
        self.favorites = favorites
        self.members = members
        self.background = background
        # self.imageURL = imageURL
        self.name = name

    def getTitle(self ,title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Title']

    def getType(self, title):
        dict = Anime.animeobject("slef", title)
        print(dict['Type'])
        return dict['Type']


    def getGenre(self, title):
        dict = Anime.animeobject("slef" ,title)
        print(dict['Genre'])
        return dict['Genre']

    def getEpisodeNumber(self , title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Episode Number']

    def getEpisodeDuration(self , title):
        dict = Anime.animeobject("slef" ,title)

    def getAiredFrom(self , title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Aired_from_year']

    def getAiringStatus(self, title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Airing']


    def getScore(self, title):
        dict = Anime.animeobject("slef" ,title)
        print( dict['Score'])
        return dict['Score']

    def getScoredBy(self, title):
        dict = Anime.animeobject("slef", title)
        return dict['Scored_by']

    def getRank(self, title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Rank']

    def getPopularity(self, title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Popularity']

    def getMembers(self, title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Members']

    def getFavorites(self, title):
        dict = Anime.animeobject("slef" ,title)
        return dict['Favorites']

    def getBackground(self, title):
        return self.background

