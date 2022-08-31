import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale


Base = declarative_base()

DSN = "postgresql://postgres:280468Br@@localhost:5432/HomeWork"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()



def searching_publisher_name():
    request_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    request_publisher_name = input('Введите имя издателя: ')
    request_result = request_join.filter(Publisher.publisher_name == request_publisher_name)
    for result in request_result.all():
        print(f'Издатель "{request_publisher_name}" найден в магазине "{result.name}" с идентификатором {result.id}')


def searching_publisher_id():
    request_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    request_publisher_name = input('Введите идентификатор (id) издателя: ')
    request_result = request_join.filter(Publisher.id_publisher == request_publisher_name)
    for result in request_result.all():
        print(
            f'Издатель c id: {request_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')


if __name__ == '__main__':
    searching_publisher_name()
    searching_publisher_id()


session.close()
