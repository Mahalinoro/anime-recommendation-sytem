class Anime:
    def __init__(self, title, type, genre, episodeNumber, episodeDuration, airedFrom, airing, rating, score, scoredBy, rank, popularity, members, favorites, background):
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
    
    def __str__(self):
        return "Type: {}, Genre: {}, Aired From: {}, Score From Users: {}, Rank: {}".format(self.getType(), self.genre, self.getAiredFrom(), self.getScore(), self.getRank())  

    def getTitle(self):
        return self.title 
    
    def getType(self):
        return self.type
    
    def getGenre(self):
        genres = self.genre.split(", ")
        return genres
    
    def getEpisodeNumber(self):
        return self.episodeNumber
    
    def getEpisodeDuration(self):
        return self.episodeDuration
    
    def getAiredFrom(self):
        return self.airedFrom
    
    def getAiringStatus(self):
        if self.airing == "TRUE":
            return 'yes'        
        return 'no'

    def getRating(self):
        return self.rating
    
    def getScore(self):
        return self.score
    
    def getScoredBy(self):
        return self.scoredBy
    
    def getRank(self):
        return self.rank

    def getPopularity(self):
        return self.popularity
    
    def getMembers(self):
        return self.members

    def getFavorites(self):
        return self.favorites
    
    def getBackground(self):
        return self.background
    
    # def getImageURL(self):
    #     return self.imageURL