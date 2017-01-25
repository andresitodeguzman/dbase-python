##
## DBase for Python
## Andresito de Guzman
## 2017
##

import json

class db:

    def __init__(self, path):
        self.path = str(path)
        try:
            setpath = self.path + ".dat"
            getfile = open(setpath)
            filestream = getfile.read()
            self.data = json.loads(filestream)
        except:
            return "Error getting the database file"

# GET - get a data from a column using a key-value match/lookup
    def get(self, col, key, val):
        data = self.data
        if data:
            for row in data:
                if row[key] == val:
                    if row[col]:
                        return row[col]
                    else:
                        return ""
                else:
                    return ""

        else:
            return ""
