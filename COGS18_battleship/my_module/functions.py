import random
import os
import time
# from IPython.display import clear_output  ## only for notebooks

class Board():
    """A class for operations relating to the creation of a Battleship game baord and ships.
    
    Parameters
    ----------
    n_ships : int
        The number of ships to be generated.
    
    Attributes
    ----------
    n_ships : int, default=5
        The number of ships to be generated. 
    grid_size : int
        The dimensions of the n x n grid for the game board.
    ship_char : str
        The character used to indicate a ship/part of a ship.
    uni_grid_list :
        The universal grid to be used for placing, locating, and guessing ships.
    """
    
    def __init__(self, n_ships=5):
        self.n_ships = n_ships
        self.grid_size = 10
        self.ship_char = chr(9724)        
        self.uni_grid_list = []
        
    def create_board(self):
        """Initializes a grid grid_list in which each row is numbered
        and margins are added. 
            
        Parameters
        ----------
        None
            
        Returns
        -------
        None
        """
        
        self.grid_list = [[' '] * (self.grid_size + 1) for ncols in range(self.grid_size)]  # initializing grid
        row_num = 1
        for lst in self.grid_list:
            if row_num < 10:
                lst.insert(0, (str(row_num) + '  '))
            else:
                lst.insert(0, (str(row_num) + ' '))
            row_num += 1
                    
        self.grid_list.insert(0, '   ---------------------')  # adding necessary margins for adjacency check later
        self.grid_list.append('                         ')     
    
    def make_pretty(self):
        """Initializes a variable str_grid_list that turns a previously 
        defined variable grid_list into a string and adds user-friendly 
        visuals, then prints.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        
        str_grid_list = (['|'.join(lst) for lst in self.grid_list])       #  ...to redefine grid as a string
        str_grid_list.insert(0, '   ---------------------')
        print('    A B C D E F G H I J')
        print('\n'.join(str_grid_list))
        
    def place_ships(self):
        """Creates 'ships' of length 4 on a grid, where the ship run either
        vertically or horizontally and do not touch. Then saves the grid with
        the ship locations to the class instance uni_grid_list and prints out the 
        grid with the added ships. 
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        
        self.create_board()

        if self.n_ships > 6:
            print('You have added too many ships! Please input an integer from 1-6')
        else:

            n_vert_ships = random.randint(1, self.n_ships - 1)                ## vertical ships subsection
            v_ships = 0                                       
            while v_ships < n_vert_ships:
                row = random.randint(4,10)
                col = random.randint(1,10)

                row_check = [row + 1, row, row - 1, row - 2, row - 3, row - 4] # checking adjacent sqaures for ships
                col_check = [col + 1, col, col - 1]

                BREAK = False
                for item in row_check:
                    if self.grid_list[item][col + 1] == self.ship_char:
                        BREAK = True
                    elif self.grid_list[item][col] == self.ship_char:
                        BREAK = True
                    elif self.grid_list[item][col - 1] == self.ship_char:
                        BREAK = True
                if BREAK == True:
                    continue

                self.grid_list[row][col] = self.ship_char
                length = 0
                while length < 4:
                    self.grid_list[row][col] = self.ship_char
                    row -= 1
                    length += 1
                v_ships += 1 

            h_ships = 0                                                         ## horizontal ships subsection
            while h_ships < (self.n_ships - n_vert_ships):         
                row = random.randint(1,10)
                col = random.randint(1,7)

                row_check = [row + 1, row, row - 1] 
                col_check = [col - 1, col, col + 1, col + 2, col + 3, col + 4] # checking adjacent squares for ships
                BREAK = False

                for item in col_check:
                    if self.grid_list[row + 1][item] == self.ship_char:
                        BREAK = True
                    elif self.grid_list[row][item] == self.ship_char:
                        BREAK = True
                    elif self.grid_list[row - 1][item] == self.ship_char:
                        BREAK = True
                if BREAK == True:
                    continue

                self.grid_list[row][col] = self.ship_char
                length = 0
                while length < 4:
                    self.grid_list[row][col] = self.ship_char
                    col += 1
                    length += 1
                h_ships += 1
                
            del self.grid_list[0]                                         # deleting margins for adjacency check...
            del self.grid_list[-1]
            self.uni_grid_list.extend(self.grid_list)
#             self.make_pretty()                                 # only for ease of testing

            
#     def no_overlap(self):                              ### no_overlap contents might be better as an assert test
#         grid_list = self.place_ships()
#         count = 0
#         for lst in grid_list:
#             for item in lst:
#                 if item == chr(9723) or item == chr(9724):
#                     count += 1
                    
    def blank_board(self):
        """Creates a blank board and adds the blank grid to the class
        instance uni_grid_list, then prints the blank board.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        
        self.create_board()
        del self.grid_list[0]                                         # deleting margins for adjacency check...
        del self.grid_list[-1]
        self.uni_grid_list.extend(self.grid_list)
        self.make_pretty()      
    
def row_guesser():
    """Takes the user's row input and returns it as an integer to determine
    the desired ship coordinates. If the user does not input an integer
    from 1 to 10, they are prompted to input a valid row number, unless the
    user inputs 'quit', which will store the variable end_game as True.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    num_coord : int
        The users input, an integer from 1 to 10.
    """
    end_game = False
    num_coord = str(input('Enter ship row 1-10: '))
    if num_coord.lower() == 'quit':
        num_coord = 0
        end_game = True
    else:
        while num_coord not in '12345678910' or num_coord == '':
            print ("\033[A                                  \033[A")
            print('Please enter a valid row number >:o')
            time.sleep(1.2)
            print ("\033[A                                   \033[A")
            num_coord = str(input('Enter ship row 1-10: '))
        num_coord = int(num_coord)

        while num_coord not in [1,2,3,4,5,6,7,8,9,10]:
            print ("\033[A                                  \033[A")
            print('Please enter a valid row number >:o')
            time.sleep(1.2)
            print ("\033[A                                   \033[A")
            num_coord = str(input('Enter ship row 1-10: '))
        
    return num_coord, end_game

def col_guesser():
    """ Takes user's column input and returns it as a capitalized string 
    character to determine the desired ship coordinates. If the user does 
    not input a letter from A to J (inclusive), they are prompted to input
    a valid column letter, unless they input 'quit', which will print
    'Goodbye!'.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    let_coord : str
        The users input, a capitalized character from A to J.
    """
    let_coord = input('Enter ship column A-J: ').upper()
    if let_coord == 'QUIT':
        let_coord = 'A'
        print('Goodbye!')
    else:
        while let_coord not in 'ABCDEFGHIJ' or let_coord == '':
            print ("\033[A                                  \033[A")
            print('Please enter a valid column letter >:o')
            time.sleep(1.2)
            print ("\033[A                                      \033[A")
            let_coord = input('Enter ship column A-J: ').upper()
        
    return let_coord

def location_guesser():          # angry at jupyter notebooks for not letting me reposition the cursor >:(
    """Takes the output from the row_guesser and col_guesser functions
    and assigns them to their correlated index on a grid.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    true_coords : tuple
        The output of the row_guesser function, as an int, minus 1,
        the value associated with the output of the col_guesser function,
        and the value of the end_game function grouped together.
    """
    
    letter_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10}
    
    num_coord, end_game = row_guesser()
    num_coord = int(num_coord) - 1
    let_coord = letter_dict[col_guesser()]
    true_coords = num_coord, let_coord, end_game
    
    return true_coords

def check_ships(first_board, second_board, in_row, in_col):
    """Checks if guessed row and column contain a ship unit on 
    the first board, and changes the second board to a hit or miss.
    
    Parameters
    ----------
    first_board : object
        An instance of the Board class.
    second_board : object
        A separate instance of the Board class.
    in_row : int
        The user's guessed row input.
    in_col : int
        The user's guessed column input.
    
    Returns
    -------
    second_board.uni_grid_list : list
        The second game board containing the guessed hit or miss. 
    """
    
    if first_board.uni_grid_list[in_row][in_col] == chr(9724):
        second_board.uni_grid_list[in_row][in_col] = chr(9724)
    elif first_board.uni_grid_list[in_row][in_col] != chr(9724):
        second_board.uni_grid_list[in_row][in_col] = 'O'
        
    return second_board.uni_grid_list
    
def miss_count(grid):
    """Counts the number of misses on the game board.
    
    Parameters
    ----------
    grid : list
        A 2D array to check for the miss character, 'O'.
        
    Returns
    -------
    m_count : int
        The number of miss characters, 'O', in a given 2D array.
    """
   
    m_count = 0
    
    for lst in grid:
        for item in lst:
              if item == 'O':
                    m_count += 1
    return m_count

def hit_count(grid):
    """Counts the number of hits on the game board.
    
    Parameters
    ----------
    grid : list
        A 2D array to check for the hit character, chr(9724).
        
    Returns
    -------
    h_count : The number of hit characters, chr(9724), in a given 2D array. 
    """
    
    h_count = 0
    
    for lst in grid:
        for item in lst:
            if item == chr(9724):
                h_count += 1
    
    return h_count

def print_instructions():
    """Prints instructions for the Battleship gameplay.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    
    instructions = "Welcome to Battleship!\n\
This is a single player, turn-based adaption of Battleship.\n\
Battleship is strategic guessing game, where you must guess the location of your \n\
opponent's ships by guessing coordinates on a blank grid. In this scenario, the ships are \n\
randomly generated. After guessing a coordinate, it is either a hit or a miss. If you \n\
hit a ship, the location will be marked on your board as a dark, square ship unit. If you \n\
miss a ship, the location will be marked on your board as an O. There are 5 ships in total \n\
and each ship is 4 units long. None of the ships touch, so if you uncover a ship, it is safe to \n\
assume that all surrounding sqaures do not contain any ships. You are allowed 20 misses, so \n\
choose your coordinates wisely!\n\n\
If you would like to change the allowed number of misses or the number of ships generated \n\
copy the following into the command line replacing the parentheses with an integer and press enter:\n\
to change only the number of allowed misses: python my_script.py --misses (desired # of misses)\n\
to change only the number of ships: python my_script.py --ships (desired # of ships)\n\
to change both: python my_script.py --both (desired # of misses) (desired # of ships)\n\
(For example: python my_script.py --both 15 4)\n\n\
To quit the game type 'quit' into both the row input and the column input.\n\n\n"
    
    print(instructions)
    
def play_game(allowed_misses=20, n_ships=5):
    """Runs a single player, turn-based Battleship game that allows for
    changes in allowed misses and number of ships generated. 
    
    Parameters
    ----------
    allowed_misses : int, default=10
        The number of misses the player can have before game over.
    n_ships : int, default=5
        The number of ships generated on the game board; will only
        run with 1-6.
        
    Returns
    -------
    None
    """
    
    print_instructions()
    
    if n_ships > 6:
        print('You have added too many ships! Please input an integer from 1-6 and rerun.')
    elif allowed_misses < 1 or allowed_misses > (100 - n_ships*4):
        print('You have allowed too many or too little misses. Please input an integer \n\
from 1 to ' + str(100 - n_ships*4) + '.')
    else:
        hidden = Board(n_ships)
        shown = Board(n_ships)

        hidden.place_ships() 
        shown.blank_board()

        turns_given = allowed_misses
        turns_left = allowed_misses
        while turns_left >= 0:

            check_row, check_col, end_game = location_guesser()
            if end_game == True:
                break
                
            updated_board = check_ships(hidden, shown, check_row, check_col)

            miss_count_var = miss_count(updated_board) 
            hit_count_var = hit_count(updated_board)
            
#             clear_output(True)                                           ##only for notebooks >:(
            time.sleep(.3)
            os.system('clear')
            
            print_instructions()
            
            turns_left = turns_given - miss_count_var
            print('Misses remaining: ' + str(turns_left) + '\n')
            
            str_updated_board = (['|'.join(lst) for lst in updated_board]) 
            str_updated_board.insert(0, '   ---------------------')
            print('    A B C D E F G H I J')
            print('\n'.join(str_updated_board))

            
            
            if turns_left == 0:
                print('\nYou have run out of turns:( \n        Game Over')
                break
            elif hit_count_var == n_ships * 4:
                print('\nYou have sunk all the ships! Congratulations!')
                break