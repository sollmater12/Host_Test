import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

# изначально подключение не запущено
__factory = None


def global_init(db_file):
    global __factory

    # запуск должен происходить только один раз!
    if __factory:
        return

    # проверки на ошибки в бд
    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    # формирование строки подключения
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    # движок для работы с SQLite базами данных (если передать  echo со значением True, в консоль будут выводиться все SQL-запросы)
    engine = sa.create_engine(conn_str, echo=False)
    # создание сесиии подключения
    __factory = orm.sessionmaker(bind=engine)

    from . import all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
