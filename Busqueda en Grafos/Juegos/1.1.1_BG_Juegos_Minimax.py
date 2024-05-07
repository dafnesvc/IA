""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Juegos---> Minimax
Este programa implementa el juego de tic-tac-toe y utiliza el algoritmo
Minimax para que la computadora tome decisiones sobre qué movimiento hacer. 
El juego se juega entre el jugador humano (X) y la computadora (O)."""

import random

class TicTacToe:
    def __init__(self): # Inicializa el tablero vacío
        self.board = [' ' for _ in range(9)]
        # Define las combinaciones ganadoras (filas, columnas y diagonales)
        self.win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

    def print_board(self): # Imprime el tablero en la consola
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))
            if i < 6:
                print('-----')

    def available_moves(self):
        # Devuelve una lista de índices de las casillas vacías en el tablero
        return [i for i, val in enumerate(self.board) if val == ' ']

    def winner(self):
        # Comprueba si hay un ganador o un empate
        for player in ['X', 'O']:
            for combination in self.win_combinations:
                if all(self.board[i] == player for i in combination):
                    return player
        if ' ' not in self.board:
            return 'Tie'
        return None

    def minimax(self, depth, is_maximizing):
        # Retorna el mejor movimiento para el jugador dado un tablero
        if self.winner() == 'X':
            return -10 + depth, None
        elif self.winner() == 'O':
            return 10 - depth, None
        elif self.winner() == 'Tie':
            return 0, None

        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for move in self.available_moves():
                self.board[move] = 'O'
                score, _ = self.minimax(depth+1, False)
                self.board[move] = ' '
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for move in self.available_moves():
                self.board[move] = 'X'
                score, _ = self.minimax(depth+1, True)
                self.board[move] = ' '
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

    def play(self):
        # Inicia el juego
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner():
            self.print_board()
            player_move = int(input("Enter your move (0-8): "))
            self.board[player_move] = 'X'
            if self.winner():
                break
            print("Computer is thinking...")
            _, computer_move = self.minimax(0, True)
            self.board[computer_move] = 'O'
        self.print_board()
        result = self.winner()
        if result == 'Tie':
            print("It's a tie!")
        else:
            print(f"{result} wins!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
