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
                        "user_admin_11111": {"first":"user","last" :"admin","id5"  :"11111"}
            }
        
            json_object = json.dumps(dictionary, indent=4)
        
            with open(self.path, "w") as outfile:
                outfile.write(json_object)

    def input_validation(self, first, last, id5):

        """
        Validation of the inputs:
        - first name must be str with less than 10 characters
        - last name must be str with less than 10 characters
        - last 5 id numbers must be int and have 5 characters
        """        

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

    def read_file(self):
        with open(self.path, 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

    def check_user(self, first, last, id5):
        """
        Check if the given user info already exists:
        - Call read function
        - If the "match" column matches with the JSON means the user already exists
        """          
        match = first + "_" + last + "_" + str(id5)
        file = self.read_file()

        try:
            finder = list(file.keys())[list(file.keys()).index(match)]
            #print(finder)
        except:
            #print(0)
            return 0
        
        if finder == match:
            #print(1)
            return 1
    
    def merge(a: dict, b: dict, path=[]):
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    merge(a[key], b[key], path + [str(key)])
                elif a[key] != b[key]:
                    raise Exception('Conflict at ' + '.'.join(path + [str(key)]))
            else:
                a[key] = b[key]
        return a

    def add_user(self, first, last, id5):
        """
        Add a new user in the database
        - Call the check user function
        - if user already exists return error message
        - if it's a new user add it to the database
        """     

        user_check = self.check_user(first, last, id5)
        
        match = first + "_" + last + "_" + str(id5)

        if user_check == 0:

            file = self.read_file()
            
            file[match] = {
                            "first":first,
                            "last" :last,
                            "id5"  :str(id5)
                            }

            json_object = json.dumps(file, indent=4)
            
            with open(self.path, "w") as outfile:
                outfile.write(json_object)

            print("User added.")

        if user_check == 1:
            print("User already exists.")
    
        
        

if __name__ == '__main__':
    jsonoperations = JsonOperations()
    jsonoperations.input_validation(first = 'teste', last = 'teste2', id5 = 12345)
    jsonoperations.read_file()

    #jsonoperations.check_user(first = 'teste', last = 'teste2', id5 = 12345)
    #jsonoperations.check_user(first = 'user', last = 'admin', id5 = 11111)

    jsonoperations.add_user(first = 'teste3', last = 'teste4', id5 = 22222)
