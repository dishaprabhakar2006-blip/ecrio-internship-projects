import logging
import unittest

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("transactions1.log"),logging.StreamHandler()])
logger=logging.getLogger(__name__)

class Transaction:
    def __init__(self,amount,category,date):
        self.amount=amount
        self.category=category
        self.date=date

    def display_info(self):
        try:
            if(self.amount<0):
                raise ValueError("Amount can't be negative")
            info=(f"Amount:{self.amount},"
                  f"Category:{self.category},"
                  f"Date:{self.date}")
            print(info)
            logger.info(info)
            return info
        except Exception as e:
            logger.error(e)
            print("Error:",e)

class Income(Transaction):
    def display_income(self):
        print("Income Transaction")
        return self.display_info()
    
class Expense(Transaction):
    def display_expense(self):
        print("Expense Transaction")
        return self.display_info()

#User Input    
def run_transaction():
    try:
        amount=float(input("Enter Amount:"))
        category=input("Enter Category:")
        date=input("Enter date in the format dd/mm/yyyy:")
        transaction_type=input("Income or Expense:").lower()

        if transaction_type=='income':
            obj=Income(amount,category,date)
            obj.display_income()
        elif transaction_type=='expense':
            obj=Expense(amount,category,date)
            obj.display_expense()
        else:
            print("Invalid Transaction Type!")

    except ValueError:
        print("Invalid Input!")

#Unit Test
class TransactionTest(unittest.TestCase):
    def test_display_info(self):
        t=Transaction(10000,"Food","15/4/2026")
        result=t.display_info()
        self.assertIn("Amount:10000",result)

    def test_income_class(self):
        i=Income(5000,"Salary","28/5/2026")
        result=i.display_income()
        self.assertIn("Salary",result)

    def test_expense_class(self):
        e=Expense(2000,"Clothes","16/8/2026")
        result=e.display_expense()
        self.assertIn("Clothes",result)

    def test_negative_amount(self):
        a=Transaction(-200,"Travel","30/7/2026")
        result=a.display_info()
        self.assertIsNone(result)

if __name__=="__main__":
    run_transaction()
    print("\nRunning Tests...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


