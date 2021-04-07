def get_preferred_option(player_1, player_2):
    if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
        return player_1
        
    if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
        return player_1
        
    if player_1.gesture == "Paper" and player_2.gesture == "Rock":
        return player_1
    
    if player_1.gesture == player_2.gesture:
        return "draw"
        
    return player_2