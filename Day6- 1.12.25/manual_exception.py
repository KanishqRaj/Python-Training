class InvalidBalanceError(Exception):
    pass

def transaction(amount,balance):
    if amount > balance:
        raise InvalidBalanceError("You have insufficient balance")
    return balance - amount
