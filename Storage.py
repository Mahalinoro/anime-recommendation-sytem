from Anime import Anime

class Storage:
    def __init__(self):
        self.storage = {}
        self.size = 0
    
    def toString(self):
        count = 1
        for anime in self.storage.values():
            print("{}. {} => {}".format(count, anime.getTitle(), anime))
            count += 1
     
    def contains(self, title):
        if title in self.storage.keys():
            return True        
        return False

    def get(self, title):
        if self.contains(title):
            return self.storage[title]
        return "Not Found"

    def add(self, title, type, genre, episodeNumber, episodeDuration, airedFrom, airing, rating, score, scoredBy, rank, popularity, members,favorites, background):
        self.storage[title] = Anime(title, type, genre, int(episodeNumber), float(episodeDuration), airedFrom, airing, rating, float(score), scoredBy, rank, int(popularity), int(members), int(favorites), background)
        self.size += 1

    def delete(self, title):
        if title in self.storage.keys():
            self.storage.pop(title)
            self.size -= 1

    def search(self, toFind):
        return [anime.getTitle() for anime in self.storage.keys() if toFind in anime.getTitle()]

