import unittest

from Anime import Anime
from AnimeScraper import AnimeScraper
from Storage import Storage
from User import User, UserStorage
from password_hash import verify_password
from Recommender import Recommender

class TestUnitCase(unittest.TestCase):
    def test_anime_object(self):
        """Anime Class Testing"""
        anime1 = Anime('Naruto', 'TV', 'Shounen', 600, 24, 2006, "FALSE", 4, 8.7, 1258970, 4, 6, 1582963, 12574, 'Ninja Anime')
        self.assertEqual(anime1.getTitle(), 'Naruto')
        self.assertEqual(anime1.getType(), 'TV')
        self.assertEqual(anime1.getEpisodeNumber(), 600)
        self.assertEqual(anime1.getMembers(), 1582963)
        self.assertEqual(anime1.getAiringStatus(), 'no')
    
    def test_anime_scraper(self):
        """Anime Scraper Class Testing"""
        url = AnimeScraper()
        data1 = url.fetchAnime('https://myanimelist.net/topanime.php?type=airing', 'airing')
        data2 = url.fetchAnime('https://myanimelist.net/topanime.php?type=upcoming', 'upcoming')

        self.assertEqual(data1.__len__(), 50)
        self.assertEqual(data2.__len__(), 50)

    def test_storage_object(self):
        """Storage Class Testing"""
        s = Storage()
        s.add('Naruto', 'TV', 'Shounen', 600, 24, 2006, "FALSE", 4, 8.7, 1258970, 4, 6, 1582963, 12574, 'Ninja Anime')
        self.assertEqual(s.get('Naruto'), 'Naruto')
        self.assertEqual(s.contains('Naruto'), True)
        s.delete('Naruto')
        self.assertEqual(s.contains('Naruto'), False)

    def test_user_object(self):
        """User Class Testing"""
        user1 = User('hello', 'helloworld', ['Naruto', 'Kimetsu no Yaiba'])
        self.assertEqual(user1.getUsername(), 'hello')
        self.assertEqual(user1.getWatchedList(), ['Naruto', 'Kimetsu no Yaiba'])

    def test_user_storage_object(self):
        """User Storage Class Testing"""
        s = UserStorage()
        user1 = User('hello', 'helloworld', ['Naruto', 'Kimetsu no Yaiba'])
        s.addUser(user1.getUsername(), user1.password, user1.getWatchedList())
        self.assertEqual('hello' in s.user_storage.keys(), True)
        self.assertEqual(verify_password(s.user_storage['hello']['password'], 'helloworld'), True)
        s.removeUser('hello')
        self.assertEqual('hello' in s.user_storage.keys(), False)

    def test_parse_data(self):
        """Recommender Class Testing"""
        r = Recommender()
        s = Storage()
        r.parseData(s, 'DataSource.csv')
        self.assertEqual(s != {}, True)       


if __name__ == "__main__":
    unittest.main()