import json

class ReadJson():
 
    def read_json(self,path):
        with open(path,"r") as json_file:
            data = json.load(json_file)
        return data['credentials']
                