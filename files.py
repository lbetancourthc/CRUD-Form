import json
import os

class Files:

    def saveJSON(file, data):
        # Making and download JSON file from data dict
        data_json = json.dumps(data)        # Dict to JSON
        json_file = open(file, 'w')         # Creating the file
        json_file.write(data_json)          # Writing data
        json_file.close()                   # Saving data JSON as data.json
        print('Saving data JSON file...')

    def chechkJSON(file):
        data = {}
        if not os.path.exists(file):
            with open(file, 'w') as outfile:  
                json.dump(data, outfile)