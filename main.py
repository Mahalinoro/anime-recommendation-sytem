from Storage import Storage
from Anime import Anime
from Recommender import Recommender
from AnimeScraper import AnimeScraper

import os
import random
import time

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t*************************************************")
    print("\t**                                             **")
    print("\t***    こんにちは、オタクゾーンへようこそ!    ***")
    print("\t***       Hello, Welcome to OtakuZone!        ***")
    print("\t**                                             **")
    print("\t*************************************************")

def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See Top 50 Airing Anime")
    print("[2] See Top 50 Upcoming Anime")
    print("[3] See Anime Recommendations")
    print("[4] Search for Anime")
    print("[q] Quit")
    
    return input("\n[?] Press any key to continue: ")

def get_recommendation_options():
    # Let users know what they can do.
    print("\n[1] Custom Recommendation")
    print("[2] I am feeling lucky")
    print("[m] Go back to main menu")
    print("[q] Quit")

    return input("\n[?] Press any key to continue: ")

def try_again():
    n = input("\n[?] Do you want to go back to main menu? [yes/no]: ")
    if n == 'yes':
        go_back_main_menu()
    else:
        quit()

def go_back_main_menu():
    main(recommender, scraper, data, airing_animes, upcoming_animes)

def quit():
    os.system('clear')
    print("\t*************************************************")
    print("\t**                                             **")
    print("\t***              ありがとう、またね!          ***")
    print("\t***       Thank you, See you next time!       ***")
    print("\t**                                             **")
    print("\t*************************************************")


def main(recommender, scraper, data, airing_animes, upcoming_animes):
    display_title_bar()
    choice = str(get_user_choice())

    if choice == '1':     
        print("\n\t*************************************************")
        print("\t****       TOP 50 Airing Anime (2020)        ****")
        print("\t*************************************************")
        print("")
        for index, value in airing_animes.items():
            print("{}. {} (Type: {}, Episodes: {}, Aired From: {})".format(index, value[0], value[1], value[2], value[3]))
        print("\n\t*************************************************")
        try_again()

    elif choice == '2':
        print("\n\t*************************************************")
        print("\t****       TOP 50 Upcoming Anime (2020)      ****")
        print("\t*************************************************")
        print("")
        for index, value in upcoming_animes.items():
            print("{}. {} (Type: {}, Episodes: {}, Airing On: {})".format(index, value[0], value[1], value[2], value[3]))
        print("\n\t*************************************************")
        try_again()

    elif choice == '3':
        display_title_bar()
        c = str(get_recommendation_options())
        if c == '1':
            # type, genre, airedFrom, airing
            print("")
            type = input('Anime Type [TV, OVA, ...]: ')
            genre = input('Anime Genre [Romance, Comedy, ...]: ')
            airedFrom = input('Anime Year Aired From [1999, 2017, ...]: ')

            n = random.randint(1, 3)
            print("\n\t*************************************************")
            print("\t****          Anime Recommendations         ****")
            print("\t*************************************************")
            print("")
            if n == 1:
                recommender.generateListBasedHighestParam(data, type, genre, airedFrom)
            elif n == 2:
                recommender.generateListBasedAverageParam(data, type, genre, airedFrom)
            elif n == 3:
                recommender.generateListBasedLowestParam(data, type, genre, airedFrom)
            print("\n\t*************************************************")
            try_again()

        elif c == '2':
            print("\n\t*************************************************")
            print("\t****          Anime Recommendations         ****")
            print("\t*************************************************")
            recommender.generateListBasedRandom(data)
            print("\n\t*************************************************")
            try_again()

        elif c == 'm':
            go_back_main_menu()

        elif c == 'q':
            quit()

    elif choice == '4':
        toFind = input('Type anime title to find: ')
        print("\n\t*************************************************")
        print("\t****              Search Results             ****")
        print("\t*************************************************")
        matches = data.search(toFind)     
        print("\n\t*************************************************")     
        try_again()        
    
    elif choice == 'q':
        quit()

    else:
        main(recommender, scraper, data, airing_animes, upcoming_animes)

if __name__ == "__main__":
    recommender = Recommender()
    scraper = AnimeScraper()
    data = Storage()

    data = recommender.parseData(data, 'DataSource.csv')
    airing_animes = scraper.fetchAnime('https://myanimelist.net/topanime.php?type=airing', 'airing')
    upcoming_animes = scraper.fetchAnime('https://myanimelist.net/topanime.php?type=upcoming', 'upcoming')

    main(recommender, scraper, data, airing_animes, upcoming_animes)