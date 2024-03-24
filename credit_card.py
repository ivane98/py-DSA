class CreditCard:
    def __init__(self, customer, bank, acnt, limit, b=None):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

        if b:
            self._balance = b

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        price = float(price)
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError('amount must be more then zero')
        self._balance -= amount



class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)

        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            
