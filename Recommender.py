from Storage import Storage
from Anime import Anime
from operator import itemgetter, attrgetter

import random
import csv


class Recommender:
    def parseData(self, storage, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                storage.add(row['title'], row['type'], row['genre'], row['episodes'], 
                row['duration_min'], row['aired_from_year'], row['airing'], row['rating'], row['score'], 
                row['scored_by'], row['rank'], row['popularity'], row['members'], row['favorites'], row['background'])    
            return storage

    def generateListBasedHighestParam(self, filename, type, genre, airedFrom):
        storage = Storage()
        data = self.parseData(storage, filename)
        # Filter data by 1:type, 2:genre and 3:(airedFrom)
        filtered_data = []
        for title, anime in data.storage.items():
            if anime.getType() == type:
                if genre in anime.getGenre(): 
                    if anime.getAiredFrom() >= str(airedFrom):
                        filtered_data.append(anime)

        # Sort data by 1:score, 2:popularity, 3:members, 4:favorites
        s = sorted(filtered_data, key=attrgetter('score'), reverse=True)
        sorted(s, key=attrgetter('popularity'))
        sorted(s, key=attrgetter('members'), reverse=True)
        sorted(s, key=attrgetter('favorites'), reverse=True)
        
        # Generate Top 10
        count = 1
        for i in range(0, 10):
            print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
            s[i].getTitle(), s[i].genre, s[i].getAiredFrom(), s[i].getScore()))
            count += 1

    def generateListBasedCustom(self, param): # Still needs to be considered
        pass
    

    def generateListBasedRandom(self, filename): 
        storage = Storage()
        data = self.parseData(storage, filename)
        s = [anime for anime in data.storage.values()]
        
        count = 1
        for i in range(0, 10):
            n = random.choice(s)
            print("{}.  Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
            n.getTitle(), n.genre, n.getAiredFrom(), n.getScore()))
            count += 1



    
