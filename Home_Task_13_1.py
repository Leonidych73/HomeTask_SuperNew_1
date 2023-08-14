class MyCard:

    def __init__(self, card_num, name, surname, expare_month, expare_year, cvv, pin, balance=0):
        self.set_card_num(card_num)
        self.set_person(name, surname)
        self.set_expare_month(expare_month)
        self.set_expare_year(expare_year)
        self.set_cvv(cvv)
        self.set_pin(pin)
        self.balance = balance

    def set_card_num(self, card_num):
        if self.valid_number(card_num):
            self.card_num = card_num
        else:
            raise ValueError("The card must be a 16-digit number.")

    def get_card_num(self):
        return self.card_num

    @staticmethod
    def valid_number(card_num):
        return isinstance(card_num, int) and len(str(card_num)) == 16

# __________person__________
    def set_person(self, name, surname):
        if self.valid_person(name) and self.valid_person(surname):
            self.name = name
            self.surname = surname
        else:
            raise ValueError("First name  and surname must contain only Latin characters and be up to 20 characters long.")

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    @staticmethod
    def valid_person(text_name):
        return text_name.isalpha() and len(text_name) <= 20

# _________expare_month___________
    def set_expare_month(self, expare_month):
        if self.valid_month(expare_month):
            self.expare_month = expare_month
        else:
            raise ValueError("expare_month must be a number between 1 and 12")

    @staticmethod
    def valid_month(expare_month):
        return isinstance(expare_month, int) and 0 < expare_month < 13

    def get_expare_month(self):
        return self.expare_month

# ________expare_year_________
    def set_expare_year(self, expare_year):
        if self.valid_year(expare_year):
            self.expare_year = expare_year
        else:
            raise ValueError("expare_year must be a number between 2024 and 2029")

    @staticmethod
    def valid_year(expare_year):
        return isinstance(expare_year, int) and 2023 < expare_year <= 2029

    def get_expare_year(self):
        return self.expare_year

# ________сvv________
    def set_cvv(self, cvv):
        if self.valid_cvv(cvv):
            self.cvv = cvv
        else:
            raise ValueError("CVV must have 3 digits")

    @staticmethod
    def valid_cvv(cvv):
        return isinstance(cvv, int) and len(str(cvv)) == 3

    def get_cvv(self):
        return self.cvv

# __________PIN___________
    def set_pin(self, pin):
        if self.valid_pin(pin):
            self.pin = pin
        else:
            raise ValueError("CVV must have 3 digits")

    def valid_pin(self, pin):
        return isinstance(pin, int) and len(str(pin)) == 4

    def get_pin(self):
        return self.pin

# ________account replenishment ___________
    def account_replenishment(self, refill_amount):
        self.balance += refill_amount
        print(f'Account was refilled for $ {refill_amount}, Balance: {self.balance}')

# ________payment________
    def payment(self, pay_amount):
        if self.balance >= pay_amount:
            self.balance -= pay_amount
            print(f'Payment has been made in the amount of ${pay_amount}, the available balance on your account: ${self.balance}')
        else:
            print(f'The available balance on your account ${self.balance}  is less than the payment amount ${pay_amount}')


if __name__ == '__main__':
    n1 = MyCard(1234567890123456, 'Dmytro', 'Popov', 12, 2029, 333, 5555)
    print(f'Card number: {n1.get_card_num()}\nCard holder: {n1.get_name()} {n1.get_surname()}\n'
          f'Expare month: {n1.get_expare_month()}\nExpare year: {n1.get_expare_year()}\n'
          f'CVV: {n1.get_cvv()}\nPIN: {n1.get_pin()}')

    print('_' * 50)
    n1.account_replenishment(200)
    n1.account_replenishment(500)
    n1.payment(600)
