users=dict()
users_number=1
users_quantity=5

def user_strings(ask_for:str,users_number:int,ask_for_2='')->str:
    """Returns an string of alphabet characters.

        Parameters
        ----------
        ask_for : str
            The user primary info to ask for:name,last name,ocupation.
        users_number : int
            The user number.
        ask_for_2: str
            The user secondarly info to ask for:middle name & second last name
            in case.
        
        Returns
        -------
        str
            User info asked for.

        """    
    while True:
        word=input(f"enter your {ask_for} user #{users_number}:")
        if word.isalpha()==True:
            return word.title()
            break
        else:
            not_letters=[]
            for character in word:
                if character not in 'abcdefghijklmnopqrstuvwxyz':
                    not_letters.append(character)
            print(f"{not_letters} ARE NOT LETTERS,write your {ask_for} again user_{users_number}.")
            
            
def user_age(ask_for:str,users_number:int)->int:
    """
    Returns the user age in numbers

    Parameters
    ----------
    ask_for : str
        The user info to ask for.
    users_number : int
        The user number.

    Returns
    -------
    int
        The age in numbers.

    """
    while True:
        try:
            age=int(input(f"enter your {ask_for} user #{users_number}:"))
            if  0 < age <=130:
                return age
            else:
                print("Please insert the age number in the correct range 0 to 130:")
        except ValueError:
            print("Please write a number")
            
            
    
while users_number <=users_quantity:
    user_dict_number=users_number
    user_dict_number=dict()
    
# #get the user name
#     name=user_strings('name',users_number)
#     user_dict_number['name']=name
    
# #last_name
#     last_name=user_strings('last name',users_number)
#     user_dict_number['last name']=last_name
      
#age
    age=user_age('age', users_number)
    user_dict_number['age']=age
        
# #ocupation
#     ocupation=user_strings('ocupation',users_number)
#     user_dict_number['ocupation']=ocupation
    
    
    users[users_number]=user_dict_number
    users_number+=1
    
    
print(users)