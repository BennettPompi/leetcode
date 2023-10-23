class account:
    def __init__(self, accountID, balance):
        self.ID = accountID
        self.balance = balance

jeremy = account("jeremy", 25)

accountDict = {}
accountDict["jeremy"] = account("jeremy", 45)
print(accountDict["jeremy"].balance)