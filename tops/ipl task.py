import random
teams = ['CSK', 'KXIP', 'KKR', 'RR', 'RCB']
opponent_team = random.choice([teams])
toss_choice = input("Toss time! What's your call? (H/T): ")
toss_result = random.choice(['H', 'T'])

if toss_choice == toss_result:
    print("Congratulations! You won the toss.")
    batting_choice = input("What do you want to do? (1 - Bat / 2 - Ball): ")
    
    if batting_choice == '1':
        print("You chose to bat first!")
        score = 0
        wickets = 0
       
        for i in range(6):
            ball_score = random.choice([1, 2, 3, 4, 6, 'WICKET', 'NO BALL', 'WIDE'])
            
            if ball_score == 'WICKET':
                wickets += 1
                print(f"Wicket down! Total wickets lost: {wickets}")
                if wickets == 10:
                    print("All out!")
                    break
            elif ball_score == 'NO BALL':
                score += 1
                print("No ball! Free hit coming up!")
            elif ball_score == 'WIDE':
                score += 1
                print("Wide ball! Extra run added!")
            else:
                score += ball_score
            
            print(f"Ball {i+1}: {ball_score}")
            
        print(f"Your score: {score} for {wickets} wickets.")
        
    elif batting_choice == '2':
        print("You chose to ball first!")
     
        pass
    
    else:
        print("Invalid choice. Please try again.")
        
else:
    print("Oops! You lost the toss. Better luck next time.")
 
    pass
