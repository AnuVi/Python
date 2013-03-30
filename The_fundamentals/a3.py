'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    '''
    return word in wordlist

 


def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    '''
    get_board = board[row_index]   
    return ''.join(get_board)


def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    '''
    board_length = len(board)
    i = 0
    column=''
    while(i<=board_length-1):
        column+= column.join(board[i][column_index])
        i=i+1
    return column

def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''
    board_length = len(board)
    i=0
    v=False
    for i in range(len(board[i])):
        if (word in make_str_from_column(board,i)):
            v=True
            i = i+1
            
    return v
def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appars in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''
    
   
    if(board_contains_word_in_row(board,word)==False and board_contains_word_in_column(board,word)==False):
        contains=False
    else:
        contains=True
        
    return contains

def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    '''
    points = ''
    word_length = len(word)
    if (word_length < 3):
            points=0
    elif (3 <= word_length <= 6):
            points=1*word_length
    elif (7 <= word_length <= 9):
            points=2*word_length
    elif (word_length>=10):
            points=3*word_length
    return points
    

def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    pl_info=[player_info[0],player_info[1] + word_score(word)]
    
    
    
    return (pl_info,word)

def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    words_length = len(words)
    count=0
    for i in range(len(words)):
        if (board_contains_word(board,words[i])==True):
            count= count+1
       
            i=i+1
    return count
   

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    lines=''
    line_file = open('wordlist1.txt' , 'r')
    for line in line_file:
        lines = lines + line

    print(lines)
    line_file.close()

def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''
    lines=''
    line_file = open('board1.txt' , 'r')
    for line in line_file:
        lines = lines + line

    print(lines)
    line_file.close()
