game_scores = {

     "hangman"        : 0 ,
     "RPS"            : 0 ,
     "heads_tails"    : 0 ,

}

def game_score(hangman_score , RPS_score , HeadsTails_score) :

     global game_scores
     total_score = 0
     game_scores["hangman"]       = hangman_score
     game_scores["heads_tails"]   = HeadsTails_score
     game_scores["RPS"]           = RPS_score

     for games in game_scores :
          total_score += game_scores[games]
     {     
     "code-runner.ignoreSelection": True
     }
     return total_score