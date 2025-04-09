import requests

class OnlineAI:
    CONNECT4_URL = "https://kevinalbs.com/connect4/back-end/index.php"

    def __init__(self):
        self.get_moves_endpoint = f"{self.CONNECT4_URL}/getMoves"
        self.has_won_endpoint = f"{self.CONNECT4_URL}/hasWon"

    def get_best_move(self, board_data, player=1):
        response = requests.get(self.get_moves_endpoint, params={"board_data": board_data, "player": player})
        if response.status_code == 200:
            moves = response.json()
            best_move = max(moves, key=moves.get)
            return int(best_move)
        else:
            print(f"Error communicating with the Connect Four API: {response.status_code} - {response.text}")
            return None

    def has_won(self, board_data, player, i, j):
        response = requests.get(self.has_won_endpoint, params={
            "board_data": board_data,
            "player": player,
            "i": i,
            "j": j
        })
        if response.status_code == 200:
            return response.json()  # Returns True or False
        else:
            print(f"Error communicating with the Connect Four API: {response.status_code} - {response.text}")
            return False