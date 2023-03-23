from functions import row_guesser, col_guesser, miss_count
import mock
import builtins
import time

def test_row_guesser():
    """Tests for the row_guesser function."""

    # testing valid inputs
    with mock.patch.object(builtins, 'input', lambda _: '3'):
        num_coord, end_game = row_guesser()
        assert num_coord == 3
        assert end_game == False
        
     # testing quit    
    with mock.patch.object(builtins, 'input', lambda _: 'quit'):
        num_coord, end_game = row_guesser()
        assert num_coord == 0
        assert end_game == True  
     
    # testing quit capitalization   
    with mock.patch.object(builtins, 'input', lambda _: 'QuIt'):
        num_coord, end_game = row_guesser()
        assert num_coord == 0
        assert end_game == True
        
        
def test_col_guesser():
    """Tests for the col_guesser function."""

    # testing lowercase valid letters
    with mock.patch.object(builtins, 'input', lambda _: 'a'):
        let_coord = col_guesser()
        assert let_coord == 'A'
        
    # testing uppercase valid letters
    with mock.patch.object(builtins, 'input', lambda _: 'E'):
        let_coord = col_guesser()
        assert let_coord ==  'E'
        
    
def test_miss_count():
    """Tests for the miss_count function."""
     
    grid = [[1, ' ', 'O', ' '],[' ', 'O', 'O', 3]]
    
    m_count = miss_count(grid)
    
    assert m_count == 3
    
    
    
    
    
    
    
    
    
    