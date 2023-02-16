'''
COP3410 - Classes and OOP
Modelling a credit card class - Parts taken from "Data Structures and Algorithms in Python"

'''


################ Parent class of any credit card ##############################

class CreditCard:
    '''A consumer credit card.'''     #docstring, the first set of comments after the name of class is considered the help for that class. help(CreditCard)  

    def __init__ (self, customer, bank, acnt, limit, balance = 0):   #The constructor is the very first method
        '''Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt : the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        balance: creates a nonzero balance (e.g., $100)
        '''
        self._customer = customer 
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance         # we start with a balance of zero, this is private, nobody can change it

    def get_customer(self):   #The get functions are a must, they're called accessor functions (methods)
        '''Return name of the customer.'''
        return self._customer

    def get_bank(self):
        '''Return the bank s name.'''
        return self._bank

    def get_account(self):
        '''Return the card identifying number (typically stored as a string).'''
        return self._account

    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit

    def get_balance(self):
        '''Return current balance.'''
        return self._balance
    
    def set_balance(self,balance):
        ''' newly created: change the balance and limit'''
        
        self._balance = balance
        self._limit -= balance

    def set_limit(self, limit):
        self._limit = limit
        

    def charge(self, purchase):
        '''
        A modification to charge method that would also decrement the limit
        '''

        if isinstance(purchase, (int, float)):
            if (purchase + self._balance) <= self._limit:
                self._balance += purchase
                self._limit -= purchase
                return True
            else:
                return False
        else:
            raise TypeError('purchase must be numeric')
        
    def make_payment(self, payment):
        '''Process customer payment that reduces balance.'''

        if payment < 0:
            raise ValueError('payment cannot be negative')
        elif isinstance(payment, (int, float)):
            self._balance -= payment
            self._limit += payment
        else:
            raise TypeError('payment must be numeric')
        

        

############### Testing the class ########################################     
        
if __name__ == "__main__":       #uses test cases to test the class inside the same script file

    wallet = [ ]   #empty list will store three instances of creditcard (3 new credit cards)
    CS = wallet.append(CreditCard( 'John Bowman' , 'California Savings' , '5391 0375 9387 5309' , 2500) )
    CF = wallet.append(CreditCard( 'John Bowman' , 'California Federal' , '3485 0399 3395 1954' , 3500) )
    CF2 = wallet.append(CreditCard( 'John Bowman' , 'California Finance' , '5391 0375 9387 5309' , 5000) )
 

    for val in range(1, 100):
       wallet[0].charge(val)   #invoking a method to charge the card
       wallet[1].charge(val)
       wallet[2].charge(val)

    for c in range(3):   #for all 3 cards
        print( 'Customer =' , wallet[c].get_customer( ))
        print( 'Bank = ', wallet[c].get_bank())
        print( 'Account = ', wallet[c].get_account( ))
        print( 'Available Credit = ', wallet[c].get_limit( ))
        print( 'Balance =' , wallet[c].get_balance())
        if wallet[c].get_balance( ) > 1:
            wallet[c].make_payment(0)
            print( 'New_balance = ', wallet[c].get_balance())
            print( 'Available_Credit = ', wallet[c].get_limit())
        print( )









    
