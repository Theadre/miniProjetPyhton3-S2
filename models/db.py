import json

class Db:
    dictionary: dict = {
        'cours': [],
        'étudiants': [],
        'notes': [],
    }

    @staticmethod
    def save(fileName):
        fileName = fileName if fileName != '' else 'data.json'

        f = open(fileName, "w")

        f.write(json.dumps(Db.dictionary))

        f.close()

    @staticmethod
    def load(fileName):
        fileName = fileName if fileName != '' else 'data.json'

        f = open(fileName, "+r")

        string_dectionary: str = f.read().replace("\'", "\"")

        f.close()

        try: 
            d = json.loads(string_dectionary)
            Db.dictionary['cours'] = d['cours'] if d['cours'] != None else []
            Db.dictionary['étudiants'] = d['etudiants'] if d['etudiants'] != None else []
            Db.dictionary['notes'] = d['notes'] if d['notes'] != None else []
        except:
            print("dictionary empty")
