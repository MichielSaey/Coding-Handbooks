# imports
import csv
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Float, String

# Setings
path_companies = 'test/companies.csv'
company_table_name = 'companies'
financial_table_name = 'financial'
path_financial = 'test/financial.csv'
database_name = 'investor.db'

Base = declarative_base()

# Logger init
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
console_handler = logging.StreamHandler()
log_format = '%(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

# Database session
engine = create_engine(f'sqlite:///{database_name}',
                       # echo=True
                       )
connection = engine.connect()
logger.info(connection)

Session = sessionmaker(bind=engine)
session = Session()


class Company(Base):
    companies = []

    __tablename__ = company_table_name

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


class Financial(Base):
    financials = []

    __tablename__ = financial_table_name

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


Base.metadata.create_all(engine)


def read_data():
    with open(path_companies) as companies:
        file_reader = csv.DictReader(companies, delimiter=",",)
        for row in file_reader:
            for key, value in row.items():
                if value == '':
                    row[key] = None
            session.add(Company(**row))

    with open(path_financial) as financial:
        file_reader = csv.DictReader(financial, delimiter=",")
        for row in file_reader:
            for key, value in row.items():
                if value == '':
                    row[key] = None
            session.add(Financial(**row))

    session.commit()


def main():
    read_data()
    print('Database created successfully!')


if __name__ == "__main__":
    main()


# write your code here
def main_menu():
    while True:
        _print_main_menu()
        user_input = input('Enter an option:\n')
        if user_input == '0':
            print('Have a nice day!')
            exit()
        elif user_input == '1':
            crud_menu()
        elif user_input == '2':
            top_ten_menu()
        else:
            print('Invalid option!\n')


def crud_menu():
    _print_crud_menu()

    user_input = input('Enter an option:\n')
    if user_input == 0:
        pass
    elif user_input == '1':
        print('Not implemented!\n')
    elif user_input == '2':
        print('Not implemented!\n')
    elif user_input == '3':
        print('Not implemented!\n')
    elif user_input == '4':
        print('Not implemented!\n')
    elif user_input == '5':
        print('Not implemented!\n')
    else:
        print('Invalid option!\n')


def top_ten_menu():
    _print_top_ten_menu()
    user_input = input('Enter an option:\n')
    if user_input == 0:
        pass
    elif user_input == '1':
        print('Not implemented!\n')
    elif user_input == '2':
        print('Not implemented!\n')
    elif user_input == '3':
        print('Not implemented!\n')
    else:
        print('Invalid option!\n')


def _print_main_menu():
    print('MAIN MENU\n'
          '0 Exit\n'
          '1 CRUD operations\n'
          '2 Show top ten companies by criteria')


def _print_crud_menu():
    print('CRUD MENU\n'
          '0 Back\n'
          '1 Create a company\n'
          '2 Read a company\n'
          '3 Update a company\n'
          '4 Delete a company\n'
          '5 List all companies')


def _print_top_ten_menu():
    print('TOP TEN MENU\n'
          '0 Back\n'
          '1 List by ND/EBITDA\n'
          '2 List by ROE\n'
          '3 List by ROA')


if __name__ == '__main__':
    main_menu()
