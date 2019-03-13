"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player





def build_grid(dim):
    ''' 
    build an initial grid of zeroes for the score
    '''
    score = []
    for dummy_row in range(dim):
        row = []
        for dummy_col in range(dim):
            row.append(0)
        score.append(row)
    return score
    

# Add your functions here.
def mc_trial(board,player):
    '''
    Play a game of tic-tac-toe on the board provided
    '''
    player = player
    while board.check_win() == None:
        moves = board.get_empty_squares()
        move = random.choice(moves)
        board.move(move[0],move[1],player)
        player = provided.switch_player(player)


def mc_update_scores(scores,board,player):
    '''
    Update the scores_grid base on which player won
    '''
    count = board.get_dim()
    current_player = player
    other_player = provided.switch_player(player)
    if board.check_win() == current_player:
        for dummy_row in range(count):
            for dummy_col in range(count):
                if board.square(dummy_row,dummy_col) == current_player:
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                if board.square(dummy_row,dummy_col) == other_player:
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
    elif board.check_win() == other_player:
        for dummy_row in range(count):
            for dummy_col in range(count):
                if board.square(dummy_row,dummy_col) == current_player:
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
                if board.square(dummy_row,dummy_col) == other_player:
                    scores[dummy_row][dummy_col] += SCORE_OTHER

                    
def get_best_move(board, scores):
    '''
    given a board and a score_grid of the board,
    get the best possible move from empty squares
    '''
    moves = board.get_empty_squares()
    _dic = {}
    if moves == None:
        return None
    for move in moves:
        score = scores[move[0]][move[1]]
        if _dic.has_key(score):
            _dic[score].append([move[0],move[1]])
        else:
            _dic[score] = [[move[0],move[1]]]
    _list = _dic.keys()
    return tuple(random.choice(_dic[max(_list)]))

def mc_move(board,players,trials):
    '''
    Simulate the game for provided number of trials
    and return the best possible move
    '''
    scores_grid = build_grid(board.get_dim())
    for _dummy_i in range(trials):
        clone = board.clone()
        mc_trial(clone,players)
        mc_update_scores(scores_grid,clone,players)
    return get_best_move(board,scores_grid)
        
              
#mc_trial(clone, provided.PLAYERX)
#print clone
#print board_score(clone)

#mc_update_scores(scores_grid, clone, provided.PLAYERX)
#print scores_grid
#print get_best_move(clone, scores_grid)
#print mc_move(board, provided.PLAYERX, 500)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
