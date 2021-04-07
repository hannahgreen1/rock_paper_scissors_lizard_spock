def get_preferred_option(player_1, player_2):
    if player_1.gesture == "Rock":
        if player_2.gesture == "Scissors" or player_2 == "Lizard":
            return player_1
        
    if player_1.gesture == "Scissors":
        if player_2.gesture == "Paper" or player_2 == "Lizard":
            return player_1
        
    if player_1.gesture == "Paper":
        if player_2.gesture == "Rock" or player_2 == "Spock":
            return player_1
    
    if player_1.gesture == "Lizard":
        if player_2.gesture == "Spock" or player_2 == "Paper":
            return player_1

    if player_1.gesture == "Spock":
        if player_2.gesture == "Scissors" or player_2 == "Rock":
            return player_1

    if player_1.gesture == player_2.gesture:
        return "draw"
        
    return player_2