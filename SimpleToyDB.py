# Import needed package
# We will use JSON as DB
import json # Because DB will be in JSON
import os # For path handling


# Create class for toy
class SimpleToyDB(object):

    # Basic Function

    def __init__(self , location):
        # Function to create database in location
        self.location = os.path.expanduser(location)
        self.load(self.location)



    def load(self , location):
        # Function to load database in location
       if os.path.exists(location):
           # If path exist load the DB
           self._load()
       else:
           # If path not exist then create empty DB
            self.db = {}
       return True


    def _load(self):
        # Load DB
        self.db = json.load(open(self.location , "r"))



    def dumpdb(self):
        # Function to write the DB to database file
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False


    def set(self , key , value):
        # Function to input new data
        try:
            self.db[str(key)] = value
            self.dumpdb()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        # Function to get data from DB by key
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False


    def delete(self , key):
        # Function to delete data from DB by key
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True


    def resetdb(self):
        # Function to reset the DB to empty
        self.db={}
        self.dumpdb()
        return True

    def printDB(self):
        # Function to print DB in monitor
        print(self.db)
        return True