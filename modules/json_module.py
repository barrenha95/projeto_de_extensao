import json
import os

class JsonOperations:
    """
    This class was created to center all operations related to JSON
    
    Operations:
    - Writing info into JSON that will work as database
    - Reading JSON + Lookup
    """

    def __init__(self):

        """
        Check if the database already exists, if the answer is false create the json file.
        """

        self.path = './database/users.json'
        check_file = os.path.isfile(self.path)
        
        if check_file == False:
            dictionary = {
                            "first":"user",
                            "last" :"admin",
                            "id5"  :"11111",
                            "match":"user_admin_11111"
            }
        
            json_object = json.dumps(dictionary, indent=4)
        
            with open('./database/users.json', "w") as outfile:
                outfile.write(json_object)



if __name__ == '__main__':
    
    jsonoperations = JsonOperations()
    