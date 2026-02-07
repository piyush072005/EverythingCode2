from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Game state
game_state = {
    'board': ['', '', '', '', '', '', '', '', ''],
    'current_player': 'X',
    'game_over': False,
    'winner': None
}

def check_winner(board):
    """Check if there's a winner"""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    return None

def is_board_full(board):
    """Check if board is full"""
    return '' not in board

def reset_game():
    """Reset game state"""
    global game_state
    game_state = {
        'board': ['', '', '', '', '', '', '', '', ''],
        'current_player': 'X',
        'game_over': False,
        'winner': None
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/game', methods=['GET'])
def get_game():
    """Get current game state"""
    return jsonify(game_state)

@app.route('/api/move', methods=['POST'])
def make_move():
    """Make a move on the board"""
    global game_state
    
    data = request.json
    position = data.get('position')
    
    # Validate move
    if position < 0 or position > 8 or game_state['board'][position] != '':
        return jsonify({'error': 'Invalid move'}), 400
    
    if game_state['game_over']:
        return jsonify({'error': 'Game is over'}), 400
    
    # Make the move
    game_state['board'][position] = game_state['current_player']
    
    # Check for winner
    winner = check_winner(game_state['board'])
    if winner:
        game_state['winner'] = winner
        game_state['game_over'] = True
    # Check for draw
    elif is_board_full(game_state['board']):
        game_state['game_over'] = True
    else:
        # Switch player
        game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    
    return jsonify(game_state)

@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the game"""
    reset_game()
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
