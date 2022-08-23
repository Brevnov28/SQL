import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:280468Br@@localhost:5432/book_store_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
publisher_1 = Publisher(name="Hueber")
publisher_2 = Publisher(name="Langenscheidt")
publisher_3 = Publisher(name="Cambridge University Press")
publisher_4 = Publisher(name="Oxford University Press")
# session.add_all([publisher_1, publisher_2, publisher_3, publisher_4])

shop_1 = Shop(name="Читай город")
shop_2 = Shop(name="Буквоед")
shop_3 = Shop(name="Лабиринт")
# session.add_all([shop_1, shop_2, shop_3])

book_1 = Book(title="Miteinander! Deutsch für Alltag und Beruf A2.1", id_publisher=11)
book_2 = Book(title="Beim Kinderarzt", id_publisher=11)
book_3 = Book(title="5 Minuten Spanisch", id_publisher=12)
book_4 = Book(title="Krimis für Kids - Where is Mrs Parker?", id_publisher=12)
book_5 = Book(title="Cambridge Discovery Education Interactive Readers", id_publisher=13)
book_6 = Book(title="The Friendship Bench", id_publisher=14)
# session.add_all([book_1, book_2, book_3, book_4, book_5, book_6])

stock_1 = Stock(id_shop=1, id_book=25, count=500)
stock_2 = Stock(id_shop=1, id_book=26, count=600)
stock_3 = Stock(id_shop=1, id_book=27, count=700)
stock_4 = Stock(id_shop=2, id_book=28, count=800)
stock_5 = Stock(id_shop=2, id_book=29, count=900)
stock_6 = Stock(id_shop=2, id_book=30, count=100)
stock_7 = Stock(id_shop=3, id_book=25, count=200)
stock_8 = Stock(id_shop=3, id_book=26, count=300)
stock_9 = Stock(id_shop=3, id_book=27, count=400)
# session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7, stock_8, stock_9])

sale_1 = Sale(price=1000.99, date_sale="2022-06-23", id_stock=1, count=10)
sale_2 = Sale(price=1200.99, date_sale="2022-06-22", id_stock=2, count=20)
sale_3 = Sale(price=1500.99, date_sale="2022-06-21", id_stock=3, count=30)
sale_4 = Sale(price=1900.99, date_sale="2022-06-20", id_stock=4, count=40)
sale_5 = Sale(price=2000.99, date_sale="2022-06-19", id_stock=5, count=50)
sale_6 = Sale(price=1100.99, date_sale="2022-06-19", id_stock=6, count=60)
sale_7 = Sale(price=1300.99, date_sale="2022-06-18", id_stock=7, count=70)
sale_8 = Sale(price=1400.99, date_sale="2022-06-17", id_stock=8, count=80)
sale_9 = Sale(price=1560.99, date_sale="2022-06-16", id_stock=9, count=90)
# session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7, sale_8, sale_9])

# фиксируем изменения
session.commit()
session.close()


# Выводит издателя (publisher), имя или идентификатор которого принимается через input()
# запросы
q = session.query(Publisher).filter(Publisher.name == input("Введите название издателя "))
for s in q.all():
    print(s.id, s.name)


q = session.query(Publisher).filter(Publisher.id == input("Введите идентификатор (id) издателя "))
for s in q.all():
    print(s.id, s.name)


subq = session.query(Shop).all()
for s in subq:
    print(s.id, s.name)
