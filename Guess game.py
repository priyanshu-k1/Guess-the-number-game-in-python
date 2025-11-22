import random
import time

"""
The theme of the game is made using Gemmini.
eg:freezing,hot,warm,cold,etc are suggested by Gemini....

"""


class GuessTheNumber:
    
    def __init__(self):
        self.score = 0
        self.games_played = 0
        self.total_guesses = 0
        
    def display_banner(self):
        print("\n" + "="*50)
        print("GUESS THE NUMBER GAME".center(50))
        print("="*50 + "\n")
    
    def choose_difficulty(self):
        print("Choose Difficulty Level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        print("4. Expert (1-500, 7 attempts)")
        
        while True:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                return 1, 50, 10, "Easy"
            elif choice == '2':
                return 1, 100, 7, "Medium"
            elif choice == '3':
                return 1, 200, 5, "Hard"
            elif choice == '4':
                return 1, 500, 7, "Expert"
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")
    
    def get_hint(self, target, guess, attempts_left):
        diff = abs(target - guess)
        
        if diff == 0:
            return "Correct!"
        elif diff <= 5:
            return "You're on fire! Very close!"
        elif diff <= 10:
            return "Hot! Getting warmer!"
        elif diff <= 20:
            return "Warm! You're in the vicinity!"
        elif diff <= 50:
            return "Cold! Not quite there yet!"
        else:
            return "Freezing! Way off!"
    
    def play_round(self):
        min_num, max_num, max_attempts, difficulty = self.choose_difficulty()
        target = random.randint(min_num, max_num)
        attempts = 0
        guesses_list = []
        
        print(f"\n{'='*50}")
        print(f"Difficulty: {difficulty}")
        print(f"I'm thinking of a number between {min_num} and {max_num}")
        print(f"You have {max_attempts} attempts to guess it!")
        print(f"{'='*50}\n")
        
        start_time = time.time()
        
        while attempts < max_attempts:
            attempts_left = max_attempts - attempts
            print(f"Attempt {attempts + 1}/{max_attempts} | Attempts left: {attempts_left}")
            
            if guesses_list:
                print(f"Your previous guesses: {guesses_list}")
            
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < min_num or guess > max_num:
                    print(f"Please guess between {min_num} and {max_num}!\n")
                    continue
                
                attempts += 1
                guesses_list.append(guess)
                
                if guess == target:
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 2)
                    
                    print("\n" + "<>"*25)
                    print("<> CONGRATULATIONS! YOU WON! <>".center(50))
                    print("<>"*25)
                    print(f"\n✓ You guessed the number {target} correctly!")
                    print(f"✓ It took you {attempts} attempt(s)")
                    print(f"✓ Time taken: {time_taken} seconds")
                    
                    # Calculate score
                    points = (max_attempts - attempts + 1) * 10
                    if difficulty == "Hard":
                        points *= 2
                    elif difficulty == "Expert":
                        points *= 3
                    
                    self.score += points
                    print(f"✓ Points earned: +{points}")
                    print(f"✓ Total score: {self.score}\n")
                    
                    self.games_played += 1
                    self.total_guesses += attempts
                    return True
                
                elif guess < target:
                    hint = self.get_hint(target, guess, attempts_left - 1)
                    print(f"Too low! {hint}\n")
                else:
                    hint = self.get_hint(target, guess, attempts_left - 1)
                    print(f"Too high! {hint}\n")
                    
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
                continue
        
        # Game over - ran out of attempts
        print("\n" + "*"*25)
        print("GAME OVER!".center(50))
        print("*"*25)
        print(f"\n✗ You've used all {max_attempts} attempts!")
        print(f"✗ The number was: {target}")
        print(f"✗ Your guesses: {guesses_list}\n")
        
        self.games_played += 1
        self.total_guesses += attempts
        return False
    
    def show_statistics(self):
        if self.games_played == 0:
            print("\nNo games played yet!\n")
            return
        
        avg_guesses = round(self.total_guesses / self.games_played, 2)
        
        print("\n" + "="*50)
        print("YOUR STATISTICS".center(50))
        print("="*50)
        print(f"Games Played: {self.games_played}")
        print(f"Total Score: {self.score}")
        print(f"Total Guesses: {self.total_guesses}")
        print(f"Average Guesses per Game: {avg_guesses}")
        print("="*50 + "\n")
    
    def main_menu(self):
        self.display_banner()
        
        while True:
            print("Main Menu:")
            print("1. Play Game")
            print("2. View Statistics")
            print("3. How to Play")
            print("4. Exit")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                print()
                self.play_round()
                
                play_again = input("\nPlay again? (y/n): ").strip().lower()
                if play_again != 'y':
                    print("\nThanks for playing! 👋")
                    self.show_statistics()
                    break
                print()
                
            elif choice == '2':
                self.show_statistics()
                
            elif choice == '3':
                print("\n" + "="*50)
                print("HOW TO PLAY".center(50))
                print("="*50)
                print("1. Choose a difficulty level")
                print("2. The computer will pick a random number")
                print("3. Guess the number within the given attempts")
                print("4. Get hints after each guess:")
                print("Very close (within 5)")
                print("Hot (within 10)")
                print("Warm (within 20)")
                print("Cold (within 50)")
                print("Freezing (more than 50 away)")
                print("5. Win points based on difficulty and attempts!")
                print("="*50 + "\n")
                
            elif choice == '4':
                print("\nThanks for playing! 👋")
                self.show_statistics()
                break
                
            else:
                print("\nInvalid choice! Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    game = GuessTheNumber()
    game.main_menu()