import json

class Db:
    dictionary: dict = {
        'cours': [],
        'etudiants': [],
        'notes': [],
    }

    @staticmethod
    def save(fileName):
        fileName = fileName if fileName != '' else 'data.txt'

        f = open(fileName, "w")

        f.write(json.dumps(Db.dictionary))

        f.close()

    @staticmethod
    def load(fileName):
        fileName = fileName if fileName != '' else 'data.txt'

        f = open(fileName, "+r")

        string_dictionary: str = f.read().replace("\'", "\"")

        f.close()

        try: 
            d = json.loads(string_dictionary)
            Db.dictionary['cours'] = d['cours'] if d['cours'] != None else []
            Db.dictionary['etudiants'] = d['etudiants'] if d['etudiants'] != None else []
            Db.dictionary['notes'] = d['notes'] if d['notes'] != None else []
        except:
            print("dictionary empty")
