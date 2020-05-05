from password_hash import hash_password

import json


class User:
    def __init__(self, username, password, watched_list=[]):
        self.username = username
        self.password = password
        self.watched_list = watched_list
    
    def getUsername(self):
        return self.username
    
    def getWatchedList(self):
        return self.watched_list
    

class UserStorage:
    def __init__(self):
        self.user_storage = {}
        self.size = 0
    
    def __str__(self):
        return self.user_storage

    def addUser(self, name, password, watched_list):
        new_user = User(name, password, watched_list)
        self.user_storage[name] = {"username":new_user.username, "password":hash_password(new_user.password), "watched_list":watched_list}
        self.size += 1        
    
    def removeUser(self, username):
        if username in self.user_storage.keys():
            self.user_storage.pop(username)
            self.size -= 1

    def addToWatchedList(self, username, anime):
        self.user_storage[username].getWatchedList().append(anime)
    
    def save(self):
        """Convert the dictionary into json and save it to userCollection.json"""
        with open('userCollection.json', 'w') as fp:
            json.dump(self.user_storage, fp, indent=4)

    def load(self):
        """Time Complexity => O(n)"""
        """Space Complexity => O(n)"""
        with open('userCollection.json', 'rb') as f:
            self.user_storage = json.load(f)


