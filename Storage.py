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

    # Search method return all the possible string that matches the title needed to be found
    # Time Complexity => O(n)
    # Space Complexity => O(n) 
    def search(self, toFind):
        matches = [anime for anime in self.storage.keys() if toFind in anime]
        if matches == []:
            print('Anime not found')
        else:
            count = 1
            for match in matches:
                print('{}. {}'.format(count, match))
                count += 1

