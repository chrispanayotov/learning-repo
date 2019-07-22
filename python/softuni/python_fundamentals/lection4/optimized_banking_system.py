class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


data = input()

bank_accounts_list = []

while data != 'end':
    bank_name, client_name, balance = data.split(' | ')

    bank_account = BankAccount(client_name, bank_name, float(balance))
    bank_accounts_list.append(bank_account)

    data = input()

for account in sorted(bank_accounts_list, key=lambda acc: (-acc.balance, len(acc.bank))):
    print(f"{account.name} -> {account.balance:.2f} ({account.bank})")
