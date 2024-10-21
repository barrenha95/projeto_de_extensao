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
        
            with open(self.path, "w") as outfile:
                outfile.write(json_object)

    def input_validation(self, first, last, id5):

        try:
            str(first)
        except: 
            raise Exception("First name must string type")
        
        try:
            str(last)
        except: 
            raise Exception("Last name must string type")

        try:
            int(id5)
        except: 
            raise Exception("The last five id numbers must be integer type")

        if len(first) > 10:
            raise Exception("Enter a first name with less than 10 characters")                

        if len(last) > 10:
            raise Exception("Enter a last name with less than 10 characters")                        
        
        if len(str(id5)) > 5:
            raise Exception("You entered more than 5 digits in the last five id")
        
        if len(str(id5)) < 5:
            raise Exception("You entered less than 5 digits in the last five id")
        
        if len(first) == 0:
            raise Exception("First name is blank.")
        
        if len(last) == 0:
            raise Exception("Last name is blank.")
        
        if len(str(id5)) == 0:
            raise Exception("Last five id is blank.")

    #def add_user(self, first, last, id5):
        
        

if __name__ == '__main__':
    jsonoperations = JsonOperations()
    jsonoperations.input_validation(first = 'teste', last = 'teste2', id5 = 12345)
