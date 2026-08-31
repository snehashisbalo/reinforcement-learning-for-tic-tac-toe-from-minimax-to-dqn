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
    
    return np.zeros((3,3), dtype=int)

# Step 2 - encode_player
def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    # TODO: map 'X' to 1, 'O' to -1, 'empty' to 0
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    elif player == 'empty':
        return 0
    else:
        raise ValueError(f"Not a valid input player: {player}")

# Step 3 - print_board
import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    # TODO: render each cell as 'X' (1), 'O' (-1), or '.' (0) in a 3x3 grid
    for r in range(3):
        for c in range(3):
            if board[r][c] == 1:
                print('X', end = '')
            elif board[r][c] == -1:
                print('O', end = '')
            else:
                print('.', end = '')
            if c != 2:
                print(' ', end='')
        print()

# Step 4 - is_cell_empty
import numpy as np

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    # TODO: check whether the cell at (row, col) is empty
    if board[row][col] != 0 : 
        return False
    else:
        return True

# Step 5 - place_move
import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    # TODO: verify the cell is empty, then return a new board with the mark placed.
    if not is_cell_empty(board, row, col):
        raise ValueError(f"Cell at ({row}, {col}) is not empty")
    
    # Create a copy of the board to avoid modifying the original
    new_board = board.copy()
    new_board[row][col] = player
    return new_board

# Step 6 - get_legal_moves
import numpy as np

def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    # TODO: scan the 3x3 board in row-major order and collect coords of empties
    moves = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if is_cell_empty(board, r, c):
                moves.append((r, c))
    return moves

# Step 7 - check_row_win
import numpy as np

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    # TODO: detect whether the given player has three identical marks across any row
    return np.any(np.all(board == player, axis=1))

# Step 8 - check_column_win
import numpy as np

def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    # TODO: detect whether the given player has three-in-a-row across any column
    return np.any(np.all(board == player, axis=0))

# Step 9 - check_main_diagonal_win
import numpy as np

def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    # TODO: check whether the main diagonal of `board` is fully occupied by `player`...
    return np.all(np.diag(board)==player)

# Step 10 - check_anti_diagonal_win
import numpy as np

def check_anti_diagonal_win(board, player):
    # TODO: return True if `player` occupies all three anti-diagonal cells of the 3x3 board.
    return np.all(np.diag(np.fliplr(board))==player)

# Step 11 - is_winner
import numpy as np

def is_winner(board, player):
    """Return True if `player` has three-in-a-row on `board`."""
    # TODO: combine row, column, and diagonal win checks into a single boolean
    if check_row_win(board,player) or check_column_win(board,player) or check_anti_diagonal_win(board,player) or check_main_diagonal_win(board,player):
        return True
    else: return False

# Step 12 - is_draw
import numpy as np

def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    # TODO: combine a full-board check with a no-winner check
    if len(get_legal_moves(board)) > 0:
        return False 
    if is_winner(board, 1) or is_winner(board, -1):
        return False 
    
    return True

# Step 13 - get_game_status
import numpy as np

def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    # TODO: classify the board into one of the four status strings
    if is_winner(board, 1): return 'X_win'
    elif is_winner(board, -1): return 'O_win'
    elif is_draw(board): return 'draw'
    else:
        return 'ongoing'

# Step 14 - get_current_player
import numpy as np

def get_current_player(board):
    """Return 1 if X is to move, -1 if O is to move."""
    # TODO: infer whose turn it is from the counts of X and O marks on the board
    cnt1 = 0
    cnt2= 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                cnt1+=1
            elif board[r][c] == -1:
                cnt2+=1
    sum =  cnt1+cnt2
    if sum % 2 == 0:
        return 1
    else: return -1

# Step 15 - switch_player
def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    # TODO: return the opposite player given 1 for X and -1 for O.
    return -player

# Step 16 - play_hardcoded_game
import numpy as np

def play_hardcoded_game(moves):
    """Replay a fixed sequence of (row, col) moves and return (final_board, status)."""
    # TODO: start from an empty board with X to move, apply moves until terminal
    board = np.zeros((3,3), dtype=int)
    player = 1
    for row, col in moves:
        if get_game_status(board) != 'ongoing':
            break
        if not is_cell_empty(board, row, col ): continue
        board = place_move(board, row, col, player)
        player = -player
    return (board,get_game_status(board))

# Step 17 - play_interactive_game
def play_interactive_game():
    """Play a full game with two humans entering moves via stdin and return the final status."""
    player = 1
    board = np.zeros((3, 3), dtype=int)

    while True:
        print_board(board)
        if get_game_status(board) != 'ongoing':
            break

        try:
            line = input().strip()
            if not line:
                continue
            row, col = map(int, line.split())
        except (EOFError, ValueError):
            break

        try:
            board = place_move(board, row, col, player)
            player = -player
        except ValueError:
            print("illegal move, try again", file=sys.stderr)
            continue

    return get_game_status(board)

# Step 18 - TicTacToeGame
# ── Step 018  TicTacToeGame ──
class TicTacToeGame:
    """Stateful Tic-Tac-Toe environment wrapping the Part 1 engine."""

    def __init__(self):
        # initialize board, current_player, and status fields.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'

    def reset(self):
        # return board to empty starting state.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'
        return self.board

    def legal_moves(self):
        # list of (row, col) tuples still playable.
        return get_legal_moves(self.board)

    def is_terminal(self):
        # True once status is no longer 'ongoing'.
        return self.status != 'ongoing'

    def step(self, row, col):
        # play current player's move, refresh status, switch player if still ongoing.
        if self.is_terminal():
            raise ValueError("Game is already over")

        self.board = place_move(self.board, row, col, self.current_player)
        self.status = get_game_status(self.board)

        if self.status == 'ongoing':
            self.current_player = switch_player(self.current_player)

        return self.board, self.status

# Step 19 - random_move_agent
def random_move_agent(board, player, rng):
    legal_moves = get_legal_moves(board)
    idx = rng.integers(len(legal_moves))
    return tuple(int(x) for x in legal_moves[idx])

# Step 20 - play_random_vs_random_game
import numpy as np

def play_random_vs_random_game(rng):
    """Simulate one full random-vs-random game and return the final status."""
    board = np.zeros((3,3), dtype=int)
    player = 1
    status = 'ongoing'
    
    while status == 'ongoing':
        legal_moves = get_legal_moves(board)
        if legal_moves:
            move_idx = rng.integers(len(legal_moves)) 
            row, col = legal_moves[move_idx]
            board = place_move(board, row, col, player)
            player = -player
            status = get_game_status(board)
        
    
    return status

# Step 21 - play_random_vs_random_matches
def play_random_vs_random_matches(n_games, rng):
    """Run n_games random-vs-random games and return the list of outcome strings."""
    # TODO: run n_games independent random-vs-random games and collect outcomes.
    arr = []
    for _ in range(n_games):

        arr.append(play_random_vs_random_game(rng))
    return arr

# Step 22 - compute_outcome_rates (not yet solved)
# TODO: implement

# Step 23 - minimax_terminal_score (not yet solved)
# TODO: implement

# Step 24 - minimax_value (not yet solved)
# TODO: implement

# Step 25 - minimax_recursive (not yet solved)
# TODO: implement

# Step 26 - minimax_max_min_step (not yet solved)
# TODO: implement

# Step 27 - minimax_best_move (not yet solved)
# TODO: implement

# Step 28 - minimax_alpha_beta (not yet solved)
# TODO: implement

# Step 29 - play_minimax_vs_random_matches (not yet solved)
# TODO: implement

# Step 30 - play_minimax_vs_minimax_matches (not yet solved)
# TODO: implement

# Step 31 - encode_board_state_key (not yet solved)
# TODO: implement

# Step 32 - canonical_board_key (not yet solved)
# TODO: implement

# Step 33 - initialize_q_table (not yet solved)
# TODO: implement

# Step 34 - get_q_value (not yet solved)
# TODO: implement

# Step 35 - set_q_value (not yet solved)
# TODO: implement

# Step 36 - choose_learning_rate_alpha (not yet solved)
# TODO: implement

# Step 37 - choose_discount_factor_gamma (not yet solved)
# TODO: implement

# Step 38 - choose_initial_epsilon (not yet solved)
# TODO: implement

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

