from Storage import Storage
from Anime import Anime
from operator import itemgetter, attrgetter
from statistics import mean

import random
import csv


class Recommender:
    # Parse data method to get data from csv file
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def parseData(self, storage, filename):
        with open(filename, newline='', encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                storage.add(row['title'], row['type'], row['genre'], row['episodes'], 
                row['duration_min'], row['aired_from_year'], row['airing'], row['rating'], row['score'], 
                row['scored_by'], row['rank'], row['popularity'], row['members'], row['favorites'], row['background'])    
            return storage
    
    # This method filter the data then sort it with the maximum paramaters
    # Time Complexity => O(n log n)
    # Space Complexity => O(n)
    def generateListBasedHighestParam(self, data, userlist, type, genre, airedFrom):
        # Filter data by 1:type, 2:genre and 3:airedFrom
        filtered_data = []
        for title, anime in data.storage.items():
            if title not in userlist:
                if anime.getType() == type:
                    if genre in anime.getGenre(): 
                        if anime.getAiredFrom() >= str(airedFrom):
                            if anime != None:
                                filtered_data.append(anime)

        # Check if filterd_data not empty:
        # Sort data by 1:score, 2:popularity, 3:members, 4:favorites 
        if filtered_data != []:
            # Sort data by 1:score, 2:popularity, 3:members, 4:favorites
            filtered_data.sort(key=attrgetter('score'), reverse=True)
            sorted(filtered_data, key=attrgetter('popularity'))
            sorted(filtered_data, key=attrgetter('members'), reverse=True)
            sorted(filtered_data, key=attrgetter('favorites'), reverse=True)
            
            # Generate Top 10
            if len(filtered_data) < 10:
                count = 1
                for i in range(0, len(filtered_data)):
                    print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    filtered_data[i].getTitle(), filtered_data[i].genre, filtered_data[i].getAiredFrom(), filtered_data[i].getScore()))
                    count += 1 
            else:
                count = 1
                for i in range(0, 10):
                    print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    filtered_data[i].getTitle(), filtered_data[i].genre, filtered_data[i].getAiredFrom(), filtered_data[i].getScore()))
                    count += 1 
            
        else:
            print("Anime not found")   


    # This method filter the data then sort it with the average score
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def generateListBasedAverageParam(self, data, userlist, type, genre, airedFrom): 
        # Mean within the data based on  score, popularity, members, favorites
        mean_score = mean([anime.getScore() for title, anime in data.storage.items()])
        # mean_popularity = mean([anime.getPopularity() for title, anime in data.storage.items()])
        # mean_members = mean([anime.getMembers() for title, anime in data.storage.items()])
        # mean_favorites = mean([anime.getFavorites() for title, anime in data.storage.items()])

        # Filter data by 1:type, 2:genre and 3:airedFrom
        # Filter data by mean parameters
        filtered_data = []
        for title, anime in data.storage.items():
            if title not in userlist:
                if anime.getType() == type:
                    if genre in anime.getGenre(): 
                        if anime.getAiredFrom() >= str(airedFrom):
                            if mean_score - 1 <= anime.getScore() <= mean_score + 1:
                                if anime != None:                    
                                        filtered_data.append(anime)            

        if filtered_data != []:
            if len(filtered_data) < 10:
                count = 1
                for i in range(0, len(filtered_data)):
                    print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    filtered_data[i].getTitle(), filtered_data[i].genre, filtered_data[i].getAiredFrom(), filtered_data[i].getScore()))
                    count += 1 
            else:
                count = 1
                for i in range(0, 10):
                    n = random.choice(filtered_data)
                    print("{}.  Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    n.getTitle(), n.genre, n.getAiredFrom(), n.getScore()))
                    count += 1
        else:
            print("Anime not found")

    # This method filter the data then sort it with the minimum paramaters
    # Time Complexity => O(n log n)
    # Space Complexity => O(n)
    def generateListBasedLowestParam(self, data, userlist, type, genre, airedFrom): 
        # Filter data by 1:type, 2:genre and 3:airedFrom
        filtered_data = []
        for title, anime in data.storage.items():
            if title not in userlist:
                if anime.getType() == type:
                    if genre in anime.getGenre(): 
                        if anime.getAiredFrom() >= str(airedFrom):
                            if anime != None:
                                filtered_data.append(anime)
        
        if filtered_data != []:
            # Sort data by 1:score, 2:popularity, 3:members, 4:favorites
            filtered_data.sort(key=attrgetter('score'))
            sorted(filtered_data, key=attrgetter('popularity'), reverse=True)
            sorted(filtered_data, key=attrgetter('members'))
            sorted(filtered_data, key=attrgetter('favorites'))
            
            # Generate Top 10
            if len(filtered_data) < 10:
                count = 1
                for i in range(0, len(filtered_data)):
                    print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    filtered_data[i].getTitle(), filtered_data[i].genre, filtered_data[i].getAiredFrom(), filtered_data[i].getScore()))
                    count += 1 
            else:
                count = 1
                for i in range(0, 10):
                    print("{}. Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
                    filtered_data[i].getTitle(), filtered_data[i].genre, filtered_data[i].getAiredFrom(), filtered_data[i].getScore()))
                    count += 1 
            
        else:
            print("Anime not found")

    # This method generate list based on random parameters
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def generateListBasedRandom(self, data, userlist): 
        s = [anime for anime in data.storage.values() if anime not in userlist]
        
        count = 1
        for i in range(0, 10):
            n = random.choice(s)
            print("{}.  Title: {} - Genre: {} - Aired From: {} - Score: {}/10".format(count, 
            n.getTitle(), n.genre, n.getAiredFrom(), n.getScore()))
            count += 1



