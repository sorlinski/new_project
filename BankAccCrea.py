import random
import os
import json

class BankAccount:
    def __init__(self, name, accountType, pin, balance=0, accountNumber=None):
        self.name = name
        self.accountType = accountType
        self.pin = pin
        self.balance = balance
        self.accountNumber = accountNumber if accountNumber else random.randint(100000, 999999)
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        
        if not os.path.exists(self.filename):
            self._log_transaction("SHINRA ACCOUNT INITIALIZED")

    def to_dict(self):
        return {
            "name": self.name, "accountType": self.accountType,
            "pin": self.pin, "balance": self.balance,
            "accountNumber": self.accountNumber
        }

    def get_info(self):
        return f"""
        === SHINRA CUSTOMER DOSSIER ===
        Holder Name   : {self.name}
        Account ID    : {self.accountNumber}
        Account Type  : {self.accountType}
        ===============================
        """

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"CREDIT: +{amount} Gil")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._log_transaction(f"DEBIT: -{amount} Gil")
            return True
        return False 

    def _log_transaction(self, message):
        with open(self.filename, "a") as f:
            f.write(f"{message} | Ledger Balance: {self.balance} Gil\n")

    def get_transaction_history(self):
        with open(self.filename, "r") as f:
            return f.read()

class BankManager:
    def __init__(self):
        self.db_file = "shinra_database.json"
        self.accounts = {}
        self.load_data()

    def save_data(self):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        with open(self.db_file, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                raw = json.load(f)
                for k, v in raw.items():
                    self.accounts[int(k)] = BankAccount(v['name'], v['accountType'], v['pin'], v['balance'], v['accountNumber'])

    def create_account(self):
        print("\n--- SHINRA NEW ENROLLMENT ---")
        name = input("Enter Name: ")
        a_type = input("Account Type (SOLDIER/Citizen): ")
        pin = input("Set 4-digit Security PIN: ")
        try:
            bal = float(input("Initial Credit Deposit (Gil): "))
            new_acc = BankAccount(name, a_type, pin, bal)
            self.accounts[new_acc.accountNumber] = new_acc
            self.save_data()
            print(f"Success. Registration complete. ID: {new_acc.accountNumber}")
        except ValueError:
            print("Processing Error: Invalid Gil format.")

    def delete_account(self):
        print("\n--- ACCOUNT TERMINATION PROTOCOL ---")
        acc = self.login() 
        if acc:
            confirm = input(f"Are you sure you want to terminate account {acc.accountNumber}? (yes/no): ").lower()
            if confirm == 'yes':
                if os.path.exists(acc.filename):
                    os.remove(acc.filename)
                
                del self.accounts[acc.accountNumber]
                self.save_data()
                print("Record expunged from Shinra Archives.")
            else:
                print("Termination cancelled.")

    def login(self):
        name = input("Identify Holder Name: ").strip().lower()
        matches = [acc for acc in self.accounts.values() if acc.name.lower() == name]
        
        if not matches:
            print("Access Denied: No record found.")
            return None
        
        acc = matches[0]
        if len(matches) > 1:
            uid = int(input("Multiple matches. Enter Account ID: "))
            acc = self.accounts.get(uid)

        if acc and input(f"Enter Security PIN for {acc.name}: ") == acc.pin:
            return acc
        print("Access Denied: Invalid Authentication.")
        return None

# --- RUNNING THE SYSTEM ---
manager = BankManager()

while True:
    print("\n================================")
    print("    SHINRA BANKING SYSTEMS    ")
    print("================================")
    print("1. New Enrollment")
    print("2. Secure Login")
    print("3. Terminate Account (Delete)")
    print("4. Shutdown Terminal")
    choice = input("\nSelect Command: ")

    if choice == "1":
        manager.create_account()
    elif choice == "2":
        user = manager.login()
        if user:
            while True:
                print(f"\n--- AUTHORIZED ACCESS: {user.name} ---")
                print("1. Credit (Deposit) | 2. Debit (Withdraw) | 3. Account Balance")
                print("4. View Customer Info | 5. Transaction Ledger | 6. Logout")
                
                act = input("\nSelect Action: ")
                
                if act == "1":
                    try:
                        amt = float(input("Amount in Gil: "))
                        if user.deposit(amt):
                            manager.save_data()
                            print(f"Credits added: {amt} Gil")
                    except ValueError:
                        print("Invalid Amount.")
                elif act == "2":
                    try:
                        val = input("Amount in Gil (or type 'all'): ").lower()
                        amt = user.balance if val == 'all' else float(val)
                        if user.withdraw(amt):
                            manager.save_data()
                            print(f"Credits debited: {amt} Gil")
                        else:
                            print(f"Insufficient funds. Assets: {user.balance} Gil")
                    except ValueError:
                        print("Invalid Amount.")
                elif act == "3":
                    print(f"\n>>> TOTAL ASSETS: {user.balance} Gil")
                elif act == "4":
                    print(user.get_info())
                elif act == "5":
                    print(f"\n--- LEDGER HISTORY: {user.accountNumber} ---")
                    print(user.get_transaction_history())
                elif act == "6":
                    break
    elif choice == "3":
        manager.delete_account()
    elif choice == "4":
        print("Connection Terminated. Glory to Shinra.")
        break