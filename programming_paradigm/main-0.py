# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Initialize the account with a starting balance of $100
    account = BankAccount(100) 

    # Check if the user provided command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and the amount (split by ':')
    command_params = sys.argv[1].split(':')
    command = command_params[0]
    
    # Handle the amount safely (if provided)
    amount = float(command_params[1]) if len(command_params) > 1 else None

    # Logic to execute commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
        
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
            
    elif command == "display":
        account.display_balance()
        
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()