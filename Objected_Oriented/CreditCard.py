class CreditCard:
    """A representation of a credit card to practice OOP design patterns."""
    
    def __init__(self, customer: str, bank: str, account: str, limit: int) -> None:
        """Intializing a new instance of the credit card.
        
        The initial balance is 0.
        
        customer    the name of the customer (e.g., 'Marcel Lee')
        bank        the name of the bank (e.g., 'BOA')
        account     the account number (e.g., '1234 1234 1234 1234')
        limit       the credit limit in dollars (e.g., '5000')       
        """
        # below are like fields in java
        self._customer = customer #_ is used like protected in java (accessible only within class and by the subclasses).
        self._bank = bank #__ is used like private in java, only accessible within the class.
        self._account = account 
        self._limit = limit
        self._balance = 0
        
    def get_customer(self) -> str:
        """Return the name of the customer."""
        return self._customer
    
    def get_bank(self) -> str:
        """Return the name of the bank."""
        return self._bank
    
    def get_account(self) -> str:
        """Return the account number."""
        return self._account
    
    def get_limit(self) -> int:
        """Return the credit limit."""
        return self._limit
    
    def get_balance(self) -> int:
        """Return the balance."""
        return self._balance
    
    def charge(self, price: int) -> bool:
        """Charge the price to the card, given sufficient credit limit.
    
        Return True if the charge is processed; False if not.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount: int) -> None:
        """Process customer payment which would reduce the balance."""
        self._balance -= amount
    
if __name__ == '__main__':
    myCard = []
    myCard.append(CreditCard('Marcel Lee', 'Santander', '1234 5678 1234 1234', 5000))
    myCard.append(CreditCard('Marcel Lee', 'BOA', '1234 5678 2423 1234', 0))
    myCard.append(CreditCard('Marcel Lee', 'MNT', '1234 5678 5353 1234', 1000))
    myCard.append(CreditCard('Marcel Lee', 'WOORI', '1234 5678 4124 1234', 2400))
    
    for val in range(1, 17):
        myCard[0].charge(val)
        myCard[1].charge(2*val)
        myCard[2].charge(3*val)
        
    for c in range(3):
        print('Customer =', myCard[c].get_customer())
        print('Bank =', myCard[c].get_bank())
        print('Account =', myCard[c].get_account())
        print('Limit =', myCard[c].get_limit())
        print('Balance =', myCard[c].get_balance())
        while myCard[c].get_balance() > 100:
            myCard[c].make_payment(100)
            print('New balance =', myCard[c].get_balance())
        print()
            
            