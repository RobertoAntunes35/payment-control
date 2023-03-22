from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://<{user}>:<{password}>@<{host}>/<{database}>'.format(
    user = 'root',
    password = 'mondistribuidora',
    host = 'localhost',
    database = 'payment_control'
))

STATUS_PAGAMENTO = {
    'A VENCER':1,
    'VENCIDO':2,
    'PROTESTADO':3,
    'PAGO':4
}

