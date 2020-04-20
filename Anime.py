class Anime:
    def __init__(self, title, type, genre, episodeNumber, episodeDuration, airedFrom, airing, rating, score, scoredBy, popularity, favorites, background, imageURL):
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
        self.popularity = popularity
        self.favorites = favorites
        self.background = background
        self.imageURL = imageURL
    
    def __str__(self):
        return "Title: {} (Type: {}, Genre: {} , Aired From: {}, Rating From Users: {})".format(self.getTitle, self.getType, self.genre, self.getAiredFrom, self.getRating)  

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
            return True        
        return False

    def getRating(self):
        return self.rating
    
    def getScore(self):
        return self.score
    
    def getScoredBy(self):
        return self.scoredBy

    def getPopularity(self):
        return self.popularity
    
    def getFavorites(self):
        return self.favorites
    
