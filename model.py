"""
Reinforcement Learning for Tic-Tac-Toe: From Minimax to DQN

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - create_empty_board
import numpy as np

def create_empty_board():
    """Return an empty 3x3 Tic-Tac-Toe board as an int numpy array of zeros."""
    # TODO: return a (3, 3) integer numpy array filled with zeros
    arr = np.zeros((3,3),dtype="int32")
    return arr
    pass

# Step 2 - encode_player
def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    # TODO: map 'X' to 1, 'O' to -1, 'empty' to 0
    if player=='X':
        return 1
    if player=='O':
        return -1;
    if player=="empty":
        return 0;
    pass

# Step 3 - print_board
import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    # TODO: render each cell as 'X' (1), 'O' (-1), or '.' (0) in a 3x3 grid
    for row in board:
        line = []
        for num in row:
            if num==1:
                line.append('X')
            if num==-1:
                line.append('O')
            if num==0:
                line.append('.')
        print(" ".join(line))
    pass

# Step 4 - is_cell_empty
import numpy as np

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    # TODO: check whether the cell at (row, col) is empty
    if board[row][col]==0:
        return True
    else:
        return False
    pass

# Step 5 - place_move
import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    # TODO: verify the cell is empty, then return a new board with the mark placed.
    if is_cell_empty(board, row, col):
        new_board = board.copy()
        new_board[row][col] = player
        return new_board
    else:
        raise ValueError
    pass

# Step 6 - get_legal_moves
import numpy as np

def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    # TODO: scan the 3x3 board in row-major order and collect coords of empties
    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                list.append((i,j))
    return list
    pass

# Step 7 - check_row_win
import numpy as np

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    # TODO: detect whether the given player has three identical marks across any row
    for i in range(3):
        index = 1
        for j in range(3):
            if board[i][j]!=player:
                index = 0
        if index==1:
            return True
    return False
    pass

# Step 8 - check_column_win
import numpy as np

def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    # TODO: detect whether the given player has three-in-a-row across any column
    for i in range(3):
        index = 1
        for j in range(3):
            if board[j][i]!=player:
                index = 0
        if index==1:
            return True
    return False
    pass

# Step 9 - check_main_diagonal_win
import numpy as np

def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    # TODO: check whether the main diagonal of `board` is fully occupied by `player`...
    if (board[0][0]==player)&(board[1][1]==player)&(board[2][2]==player):
        return True
    else:
        return False
    pass

# Step 10 - check_anti_diagonal_win
import numpy as np

def check_anti_diagonal_win(board, player):
    # TODO: return True if `player` occupies all three anti-diagonal cells of the 3x3 board.
    if (board[0][2]==player)and(board[1][1]==player)and(board[2][0]==player):
        return True
    else:
        return False
    pass

# Step 11 - is_winner
import numpy as np

def is_winner(board, player):
    """Return True if `player` has three-in-a-row on `board`."""
    # TODO: combine row, column, and diagonal win checks into a single boolean
    if check_anti_diagonal_win(board,player) or check_column_win(board,player) or check_main_diagonal_win(board,player) or check_row_win(board,player):
        return True
    else:
        return False
    pass

# Step 12 - is_draw
import numpy as np

def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    # TODO: combine a full-board check with a no-winner check
    index = 1
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                index = 0
    if index==1 and (not is_winner(board,1)) and (not is_winner(board,-1)):
        return True
    else:
        return False
    pass

# Step 13 - get_game_status
import numpy as np

def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    # TODO: classify the board into one of the four status strings
    if is_draw(board):
        return "draw"
    else:
        if is_winner(board,1):
            return "X_win"
        elif is_winner(board,-1):
            return "O_win"
        else:
            return "ongoing"
    pass

# Step 14 - get_current_player
import numpy as np

def get_current_player(board):
    """Return 1 if X is to move, -1 if O is to move."""
    # TODO: infer whose turn it is from the counts of X and O marks on the board
    num_x = 0
    num_o = 0
    for row in board:
        for num in row:
            if num==-1:
                num_o += 1
            if num==1:
                num_x += 1
    if num_o<num_x:
        return -1
    else:
        return 1
    pass

# Step 15 - switch_player
def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    # TODO: return the opposite player given 1 for X and -1 for O.
    if player==1:
        return -1
    if player==-1:
        return 1
    pass

# Step 16 - play_hardcoded_game
import numpy as np

def play_hardcoded_game(moves):
    """Replay a fixed sequence of (row, col) moves and return (final_board, status)."""
    # TODO: start from an empty board with X to move, apply moves until terminal
    board = create_empty_board()
    player = 1
    for move in moves:
        if get_game_status(board)!="ongoing":
            return (board,get_game_status(board))
        else:
            board = place_move(board,move[0],move[1],player)
            player = switch_player(player)
    return (board,get_game_status(board))
    pass

# Step 17 - play_interactive_game
def play_interactive_game():
    """Play a full game with two humans entering moves via stdin and return the final status."""
    # TODO: loop printing the board, reading 'row col' from stdin, applying moves until terminal
    board = create_empty_board()
    print_board(board)
    player = 1
    while True:
        try:
            line = input()
        except EOFError:
            break
        parts = line.strip().split()
        row = int(parts[0])
        col = int(parts[1])
        try:
            board = place_move(board, row, col, player)
        except ValueError:
            print_board(board)
            continue
        print_board(board)
        player = switch_player(player)
    return get_game_status(board)
    pass

# Step 18 - TicTacToeGame
class TicTacToeGame:
    """Stateful Tic-Tac-Toe environment wrapping the Part 1 engine."""

    def __init__(self):
        # 绑定到self，保存实例状态
        self.board = create_empty_board()
        self.current_player = 1
        self.status = get_game_status(self.board)

    def reset(self):
        # 重置实例内部状态，返回空棋盘
        self.board = create_empty_board()
        self.current_player = 1
        self.status = get_game_status(self.board)
        return self.board

    def legal_moves(self):
        # 传入当前实例棋盘
        return get_legal_moves(self.board)

    def is_terminal(self):
        # 判断游戏是否结束
        return self.status != "ongoing"

    def step(self, row, col):
        if self.is_terminal():
            raise ValueError("Game is already terminal")
        # 执行落子
        self.board = place_move(self.board, row, col, self.current_player)
        self.status = get_game_status(self.board)

        # 仅当游戏还在进行，才切换玩家
        if self.status == "ongoing":
            self.current_player = switch_player(self.current_player)

        return self.board, self.status

# Step 19 - random_move_agent
import numpy as np

def random_move_agent(board, player, rng):
    """Return a uniformly random legal (row, col) move for `player`."""
    # TODO: sample a uniformly random legal move using rng and return it as (row, col)
    legal_moves = get_legal_moves(board)
    select_move = rng.choice(legal_moves)
    row = int(select_move[0])
    col = int(select_move[1])
    return (row,col)
    pass

# Step 20 - play_random_vs_random_game
def play_random_vs_random_game(rng):
    """Simulate one full random-vs-random game and return the final status."""
    # TODO: loop until terminal, alternating random moves between X and O
    board = create_empty_board()
    player = 1
    state = get_game_status
    while True:
        legal_moves = get_legal_moves(board)
        select_move = rng.choice(legal_moves)
        row = int(select_move[0])
        col = int(select_move[1])
        board = place_move(board, row, col, player)
        if get_game_status(board)!="ongoing":
            break;
        player = switch_player(player)
    return get_game_status(board)
    pass

# Step 21 - play_random_vs_random_matches
def play_random_vs_random_matches(n_games, rng):
    """Run n_games random-vs-random games and return the list of outcome strings."""
    # TODO: run n_games independent random-vs-random games and collect outcomes.
    outcomes = []
    for _ in range(n_games):
        outcomes.append(play_random_vs_random_game(rng))
    return outcomes
    pass

# Step 22 - compute_outcome_rates
def compute_outcome_rates(outcomes):
    """Return {'x_win_rate','o_win_rate','draw_rate'} from a list of outcome labels."""
    # TODO: count occurrences of each outcome and divide by total games
    x_win = float(0)
    o_win = float(0)
    draw = float(0)
    num = float(0)
    for outcome in outcomes:
        num += 1.0
        if outcome=="X_win":
            x_win += 1.0
        if outcome=="O_win":
            o_win += 1.0
        if outcome=="draw":
            draw += 1.0
    if num>0:
        dic = {"x_win_rate":x_win/num,"o_win_rate":o_win/num,"draw_rate":draw/num}
    else:
        dic = {"x_win_rate":0.0,"o_win_rate":0.0,"draw_rate":0.0}
    return dic
    pass

# Step 23 - minimax_terminal_score
def minimax_terminal_score(status):
    """Return +1 for 'X_win', -1 for 'O_win', 0 for 'draw'."""
    # TODO: map a terminal status string to its minimax leaf value.
    if status=="X_win":
        return 1
    if status=="O_win":
        return -1
    if status=="draw":
        return 0
    pass

# Step 24 - minimax_value
def minimax_value(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: terminal -> minimax_terminal_score; else max (X) / min (O) over recursive child values
    state = get_game_status(board)
    if state!="ongoing":
        return minimax_terminal_score(state)
    legal_moves = get_legal_moves(board)
    child_value = []
    for (r,c) in legal_moves:
        new_board = place_move(board,r,c,player)
        value = minimax_value(new_board,-player)
        child_value.append(value)
    if player==1:
        return max(child_value)
    else:
        return min(child_value)
    pass

# Step 25 - minimax_recursive
def minimax_recursive(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: recurse over legal moves, max for X (+1), min for O (-1), terminal via minimax_terminal_score
    if not hasattr(minimax_recursive,"cache"):
        minimax_recursive.cache = {}
    cache_key = (board.tobytes(),player)
    if cache_key in minimax_recursive.cache:
        return minimax_recursive.cache[cache_key]
    minimax_recursive.cache[cache_key] = minimax_value(board,player)
    return minimax_value(board,player)
    pass

# Step 26 - minimax_max_min_step
import numpy as np

def minimax_max_min_step(board, player):
    """Return (best_score, best_move) after expanding one minimax level."""
    # TODO: iterate legal moves, recurse, pick max if player == 1 else min...
    best_score = None
    best_move = None
    legal_moves = get_legal_moves(board)
    for legal_move in legal_moves:
        (r,c) = legal_move
        new_board = place_move(board,r,c,player)
        if best_score==None:
            best_score = minimax_recursive(new_board,-player)
            best_move = legal_move
        else:
            if player==1:
                if minimax_recursive(new_board,-player)>best_score:
                    best_score = minimax_recursive(new_board,-player)
                    best_move = legal_move
            else:
                if minimax_recursive(new_board,-player)<best_score:
                    best_score = minimax_recursive(new_board,-player)
                    best_move = legal_move
    return (best_score,best_move)
    pass

# Step 27 - minimax_best_move
def minimax_best_move(board, player):
    """Return the optimal (row, col) move for `player` via minimax."""
    # TODO: use the minimax max/min step to pick the best legal move for player
    (score,(r,c)) = minimax_max_min_step(board, player)
    return (r,c)
    pass

# Step 28 - minimax_alpha_beta
import numpy as np

def minimax_alpha_beta(board, player, alpha, beta):
    """Return (best_score, best_move) for `player` using alpha-beta pruning."""
    # TODO: search the game tree with alpha-beta pruning and return (score, move)
    status = get_game_status(board)
    if status!="ongoing":
        return (minimax_terminal_score(status),None)
    
    legal_moves = get_legal_moves(board)
    best_move = None

    if player==1:
        best_score = -float('inf')
        for r,c in legal_moves:
            new_board = place_move(board,r,c,player)
            score,_ = minimax_alpha_beta(new_board,-player,alpha,beta)
            if score>best_score:
                best_score = score
                best_move = (r,c)
            alpha = max(alpha,best_score)
            if alpha>=beta:
                break;
    else:
        best_score = float('inf')
        for r,c in legal_moves:
            new_board = place_move(board,r,c,player)
            score,_ = minimax_alpha_beta(new_board,-player,alpha,beta)
            if score<best_score:
                best_score = score
                best_move = (r,c)
            beta = min(beta,best_score)
            if alpha>=beta:
                break;

    return (best_score,best_move)
    pass

# Step 29 - play_minimax_vs_random_matches
def play_minimax_vs_random_matches(n_games, minimax_plays_x, rng):
    # TODO: run n_games of minimax vs random and return aggregated outcome rates.
    outcomes = []
    if minimax_plays_x:
        minimax_player = 1
    else:
        minimax_player = -1
    random_player = -minimax_player
    for _ in range(n_games):
        board = create_empty_board()
        status = get_game_status(board)
        current_player = 1
        alpha = -float("inf")
        beta = float("inf")
        while status=="ongoing":
            if current_player==minimax_player:
                _,(r,c) = minimax_alpha_beta(board,current_player,alpha,beta)
            else:
                (r,c) = random_move_agent(board,current_player,rng)
            board = place_move(board,r,c,current_player)
            status = get_game_status(board)
            current_player = -current_player
        outcomes.append(status)
    return compute_outcome_rates(outcomes)
    pass

# Step 30 - play_minimax_vs_minimax_matches
def play_minimax_vs_minimax_matches(n_games):
    """Play n_games minimax-vs-minimax games and report outcome rates plus an all_draws flag."""
    # TODO: simulate n_games minimax-vs-minimax games and aggregate outcome rates.
    if n_games==0:
        rates = {'x_win_rate':0.0,'o_win_rate':0.0,'draw_rate':0.0,'all_draws':True}
        return rates
    outcomes = []
    for _ in range(n_games):
        board = create_empty_board()
        status = get_game_status(board)
        current_player = 1
        alpha = -float("inf")
        beta = float("inf")
        while status=="ongoing":
            _,(r,c) = minimax_alpha_beta(board,current_player,alpha,beta)
            board = place_move(board,r,c,current_player)
            status = get_game_status(board)
            current_player = -current_player
        outcomes.append(status)
        rates = compute_outcome_rates(outcomes)
        rates["all_draws"] = all(outcome == 'draw' for outcome in outcomes)
        return rates
    pass

# Step 31 - encode_board_state_key
import numpy as np

def encode_board_state_key(board):
    """Encode a 3x3 board as a length-9 string over {'0','1','2'} in row-major order."""
    # TODO: map each cell (0, 1, -1) to a single character and join row-major.
    key = ""
    for raw in board:
        for num in raw:
            if num==0:
                key += '0'
            if num==1:
                key += '1'
            if num==-1:
                key += '2'
    return key
    pass

# Step 32 - canonical_board_key
def canonical_board_key(board):
    # TODO: return the lex-smallest encoded key over all 8 symmetries of the board.
    # 辅助：顺时针旋转90度（3x3固定索引映射，高效直观）
    def rotate_90(b):
        return [
            [b[2][0], b[1][0], b[0][0]],
            [b[2][1], b[1][1], b[0][1]],
            [b[2][2], b[1][2], b[0][2]]
        ]
    
    # 辅助：水平镜像翻转（左右反射）
    def reflect_horizontal(b):
        return [row[::-1] for row in b]
    
    candidate_keys = []
    
    # 第一组：原棋盘的4次旋转
    current = board
    for _ in range(4):
        candidate_keys.append(encode_board_state_key(current))
        current = rotate_90(current)
    
    # 第二组：镜像后棋盘的4次旋转
    current = reflect_horizontal(board)
    for _ in range(4):
        candidate_keys.append(encode_board_state_key(current))
        current = rotate_90(current)
    
    # 取字典序最小的编码作为唯一规范键
    return min(candidate_keys)

    pass

# Step 33 - initialize_q_table
from collections import defaultdict

def initialize_q_table():
    """Create an empty Q-table that returns 0.0 for unseen (state, action) keys."""
    # TODO: return a mapping where missing (state_key, action) lookups yield 0.0
    q_table = defaultdict(float)
    return q_table
    pass

# Step 34 - get_q_value
def get_q_value(q_table, state_key, action):
    # TODO: return Q(state_key, action), or 0.0 if the pair is not in the table
    return q_table.get((state_key,action),0.0)
    pass

# Step 35 - set_q_value
def set_q_value(q_table, state_key, action, value):
    """Write a new Q-value for a (state, action) pair into the Q-table."""
    # TODO: store value under the (state_key, action) key in q_table.
    q_table[(state_key,action)] = value
    pass

# Step 36 - choose_learning_rate_alpha
def choose_learning_rate_alpha():
    """Return the learning rate alpha (float in (0, 1]) for tabular Q-learning."""
    # TODO: return a float in (0, 1] to use as the Q-learning step size.
    return 0.1
    pass

# Step 37 - choose_discount_factor_gamma
def choose_discount_factor_gamma():
    """Return the discount factor gamma in [0, 1] for Q-learning."""
    # TODO: return a float discount factor in [0, 1] for tabular Q-learning.
    return 0.9
    pass

# Step 38 - choose_initial_epsilon
def choose_initial_epsilon():
    """Return the starting exploration rate epsilon for epsilon-greedy."""
    # TODO: return the starting exploration rate in [0, 1] favoring exploration
    return 1.0
    pass

# Step 39 - epsilon_decay_schedule (not yet solved)
# TODO: implement

# Step 40 - epsilon_greedy_explore_move (not yet solved)
# TODO: implement

# Step 41 - epsilon_greedy_select_action (not yet solved)
# TODO: implement

# Step 42 - greedy_argmax_over_legal_actions (not yet solved)
# TODO: implement

# Step 43 - random_tie_break_argmax (not yet solved)
# TODO: implement

# Step 44 - tic_tac_toe_reward (not yet solved)
# TODO: implement

# Step 45 - q_learning_nonterminal_target (not yet solved)
# TODO: implement

# Step 46 - q_learning_terminal_target (not yet solved)
# TODO: implement

# Step 47 - q_learning_update (not yet solved)
# TODO: implement

# Step 48 - episode_reset_game (not yet solved)
# TODO: implement

# Step 49 - episode_agent_pick_action (not yet solved)
# TODO: implement

# Step 50 - episode_apply_action (not yet solved)
# TODO: implement

# Step 51 - episode_apply_q_update (not yet solved)
# TODO: implement

# Step 52 - episode_check_terminate (not yet solved)
# TODO: implement

# Step 53 - train_q_learning_agent (not yet solved)
# TODO: implement

# Step 54 - compute_batched_outcome_stats (not yet solved)
# TODO: implement

# Step 55 - self_play_episode (not yet solved)
# TODO: implement

# Step 56 - flip_board_perspective (not yet solved)
# TODO: implement

# Step 57 - perspective_reward_sign (not yet solved)
# TODO: implement

# Step 58 - train_q_agent_self_play (not yet solved)
# TODO: implement

# Step 59 - evaluate_q_agent_vs_random (not yet solved)
# TODO: implement

# Step 60 - evaluate_q_agent_vs_minimax (not yet solved)
# TODO: implement

# Step 61 - inspect_q_values_for_state (not yet solved)
# TODO: implement

# Step 62 - serialize_q_table_to_dict (not yet solved)
# TODO: implement

# Step 63 - deserialize_q_table_from_dict (not yet solved)
# TODO: implement

# Step 64 - encode_board_flat_length_nine (not yet solved)
# TODO: implement

# Step 65 - encode_board_one_hot_length_eighteen (not yet solved)
# TODO: implement

# Step 66 - build_mlp_architecture (not yet solved)
# TODO: implement

# Step 67 - initialize_mlp_parameters (not yet solved)
# TODO: implement

# Step 68 - mlp_forward_pass (not yet solved)
# TODO: implement

# Step 69 - mask_illegal_actions_neg_inf (not yet solved)
# TODO: implement

# Step 70 - argmax_action_from_q_values (not yet solved)
# TODO: implement

# Step 71 - mse_loss_on_chosen_action (not yet solved)
# TODO: implement

# Step 72 - mlp_backward_pass (not yet solved)
# TODO: implement

# Step 73 - adam_update_step (not yet solved)
# TODO: implement

# Step 74 - create_replay_buffer (not yet solved)
# TODO: implement

# Step 75 - append_transition_to_buffer (not yet solved)
# TODO: implement

# Step 76 - cap_buffer_size_drop_oldest (not yet solved)
# TODO: implement

# Step 77 - sample_minibatch_from_buffer (not yet solved)
# TODO: implement

# Step 78 - build_target_network_copy (not yet solved)
# TODO: implement

# Step 79 - compute_target_q_with_target_network (not yet solved)
# TODO: implement

# Step 80 - sync_target_network_periodically (not yet solved)
# TODO: implement

# Step 81 - dqn_select_action (not yet solved)
# TODO: implement

# Step 82 - dqn_train_step (not yet solved)
# TODO: implement

# Step 83 - train_dqn_agent (not yet solved)
# TODO: implement

# Step 84 - compare_dqn_tabular_random_minimax (not yet solved)
# TODO: implement

# Step 85 - sarsa_on_policy_update (not yet solved)
# TODO: implement

# Step 86 - train_sarsa_agent (not yet solved)
# TODO: implement

# Step 87 - reinforce_log_prob_of_action (not yet solved)
# TODO: implement

# Step 88 - reinforce_collect_episode_returns (not yet solved)
# TODO: implement

# Step 89 - reinforce_policy_gradient_update (not yet solved)
# TODO: implement

# Step 90 - train_reinforce_agent (not yet solved)
# TODO: implement

# Step 91 - compare_value_vs_policy_learners (not yet solved)
# TODO: implement

# Step 92 - symmetry_augmented_training (not yet solved)
# TODO: implement

