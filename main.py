'''
TITLE: MOVIE NIGHT SELECTOR
DEVELOPER(S): Isai Flores
COLLABORATORS: Lecture Videos
DATE: 04/23/2026
'''

"""
This program will select a favorite movie to watch based on the genre of movie selected.

The program will read a list of my favorite movies from a text file and convert to a dictionary. Program will create a dictionary, and ask the user/me to view the list, to select a movie genre, and a movie will be selected for me to watch.
Program will also ask user if they would like to add a different genre or replace a current genre with a new movie. 
 
"""

##########################################
# IMPORTS:
# <list of modules needed for the program and their purpose>
##########################################
# <replace this line with import statement(s)>
##########################################
# FUNCTIONS:
##########################################
def movie_dictionary(in_file):
    '''This function will turn the text input file into a dictionary '''
    movie_dict = {}
    with open(in_file, 'r') as file:
        for line in file:
            if "~" in line:
                key, value = line.strip().split("~",1)
                movie_dict[key] = value
    
    return movie_dict

def check_dict (key, dictionary):
    '''This function takes a string and looks it up in the dictionary, and validates if the string text is a key in the dictionary., Will return the key if true'''
    if key in dictionary:
        x = dictionary.get(key)
        return x
    else:
        return "No reult found. Please try again"


def show_genre(key_dict):
    '''This function will iterate through the dictionary and print key-value pair'''
    print()
    print(f"{'Genre':<20} {'Movie':<25}\n")
    for (k,v) in key_dict.items():
        print (f"{k:<20} {v:<25}")
    print()
    return

def select_genre (dictionary):
    '''This function will iterate through the dictionary and print the value of the user's choice (key)'''

    user = input ("Please input the name of the genre (stop to end): ")

    if user == 'stop' or user == 'Stop' or user == "STOP":
        print ("Exiting genre selection.\n")
       
    else:
        print("Movie Genre:", check_dict(user, dictionary))
        print()
        select_genre(dictionary) 
    

def dictionary_edit(dictionary):

    '''This function will allow the user to modify their current dictionary of movies, and will give them the option to update a genre value, or to add a new genre with a value'''
    user_option = 0
    while user_option!= 4:
        try:
            user_option = int( input (f"Please select from the following list of choices:\n 1.) Edit Movie Title\n 2.) Delete genre and movie title\n 3.) Add new genre and movie title\n 4.) Exit Edit\n "))
            if user_option < 1 or user_option > 4:
                print("Invalid Input: Please enter correct value\n")
        except ValueError:
            print ("Please input a number from the menu.\n")
       
        if user_option == 1:
            genre_edit = input ("Please type in the genre for which you will edit your favorite movie: ")
            if genre_edit in dictionary:
                movie_edit = input ("Type in the movie title: ")

                dictionary [genre_edit] = movie_edit
                print(f"Your new favorite movie has been updated for {genre_edit}\n")
                return dictionary
            else:
                print ("Invalid: Please type in genre correctly.\n")

        elif user_option == 2:
            genre_del = input ("Please type in the genre you want to delete (movie will also be deleted): ")
            if genre_del in dictionary:
                del dictionary[genre_del]
                return dictionary
            else:
                print ("Invalid: Please type in genre correctly.\n")

        elif  user_option == 3:
            genre_add = input ("Please type in the genre you want to add: ")
            movie_add = input ("Please type in the movie title you would like to add: ")
      
            dictionary[genre_add] = movie_add  # Adds a new key/movie title 'genre_add' with value movie_add
            return dictionary
        elif user_option == 4:
            print ("Exiting Edit")

def write_to_file (out_file_name, text_to_write):
    '''This function will write to an output file'''
    file = open (out_file_name + '.txt', 'w') 
    file.write(text_to_write)
    file.close()


##########################################
# MAIN PROGRAM:
##########################################
def main():
    #CALL THE IMPORT FILE FUNCTION TO LOAD IN YOUR MOVIE LIST .TXT FILE AND SAVE IN PROGRAM AS A DICTIONARY 
    dict = movie_dictionary ('fav_movies.txt')
    print()
    print ("Welcome to the Movie Selector!\n")

#############################################################################
    #WHILE LOOP KEEPS ITERATING THE MENU UNTIL YOU PROMPT IT TO EXIT
    choice = 0
    while choice!= 4:
        try:
            choice = int( input (f"Please select from the following list of choices:\n 1.) View list of genres/movies\n 2.) Select genre\n 3.) Edit movie list\n 4.) Exit Menu\n "))
            #DATA VALIDATION 
            if choice < 1 or choice > 4:
                print("Invalid Input: Please enter correct value")
                input("Press ENTER to return to the main menu")
        except ValueError:
            print("Invalid Input: Please enter a number from the menu.\n")
            choice = 0
            continue

        #CALL THE FUNCTION TO VIEW THE LIST OF GENRES AND MOVIES
        if choice == 1:
            show_genre(dict)
        #CALL THE FUNCTION TO TYPE IN A GENRE AND OUTPUT YOUR FAVORITE MOVIE FROM THAT GENRE
        elif choice == 2:
            select_genre(dict)
        #CALL THE FUNCTION TO EDIT YOUR IMPORTED MOVIE DICTIONARY
        elif  choice == 3:
            dictionary_edit (dict)
    else:
        print ("Menu Closed")
    #SAVE UPDATED LIST TO A NEW FILE
    string = ""
    for (k,v) in dict.items():  #ITERATE OVER EACH KEY-VALUE PAIR, AND BUILD UP THE EMPTY STRING THROUGH EACH ITERATION
        string = string + f"{k}, {v}\n"
    file_out = input("Type the filename for your updated list: ")
    write_to_file (file_out, string)       #CALL FUNCTION TO EXPORT YOUR DICTIONARY INTO A .TXT FILE

main()