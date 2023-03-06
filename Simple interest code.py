class Bank:
    bank_name='IB'
    rate_of_interest=12.5
    @staticmethod
    def simple_interest(p,n):
        si=(p*n*Bank.rate_of_interest)/100
        print(si)
        
p=float(input('enter the principle amount:'))
n=float(input('enter number of years :'))
Bank.simple_interest(p,n)

