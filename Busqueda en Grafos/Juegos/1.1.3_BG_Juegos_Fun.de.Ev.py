""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Juegos---> Función de Evaluación
Este programa implementa una función de evaluación simple para el juego
de tic-tac-toe. La función de evaluación asigna una puntuación al estado
actual del tablero basado en las combinaciones ganadoras. """

import random

class TicTacToe:
    def __init__(self):
        # Inicializa el tablero vacío
        self.board = [' ' for _ in range(9)]
        # Define las combinaciones ganadoras (filas, columnas y diagonales)
        self.win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

    def print_board(self):
        # Imprime el tablero en la consola
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

    def evaluate(self):
        # Evalúa el estado actual del tablero
        score = 0
        for combination in self.win_combinations:
            if all(self.board[i] == 'X' for i in combination):
                score -= 10
            elif all(self.board[i] == 'O' for i in combination):
                score += 10
        return score

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
            computer_move = random.choice(self.available_moves())
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
