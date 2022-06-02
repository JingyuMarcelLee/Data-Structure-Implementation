from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to the CreditCard that compounds interest and fees."""
    
    def __init__(self, customer, bank, account, limit, apr) -> None:
        """Initilize a new predatory credit card instance.
        
        The initial balance is 0.
        
        customer    the name of the customer (e.g., 'Marcel Lee')
        bank        the name of the bank (e.g., 'BOA')
        account     the account number (e.g., '1234 1234 1234 1234')
        limit       the credit limit in dollars (e.g., '5000') 
        apr         the anuual percentage interest rate (e.g. 0.05 for 5% APR)      
        """
        
        super().__init__(customer, bank, account, limit)
        self._apr = apr
        
    def charge(self, price) -> bool:
        """Charge the given price to the card, assuming there is sufficient credit limit
        
        Return True if charge was processed.
        Return False and take $5 transaction fee if the charge is denied.
        """
        
        success = super().charge(price)             # call method from parent
        if not success:
            self._balance += 5                      # assess penalty
        return success                              # caller expects return value
    
    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if balance is potitive APR is applied
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

def main():
    P = PredatoryCreditCard("Marcel", "BOA", "1234 1234 1234 1111", 1400, 0.025)
    print(isinstance(P, CreditCard))
    P.charge(500)
    print(P.get_balance())
    P.process_month()
    print(P.get_balance())

if __name__ == '__main__':
    main()