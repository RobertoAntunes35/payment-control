from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://<{user}>:<{password}>@<{host}>/<{database}>'.format(
    user = 'mondistribuidora',
    password = 'mon',
    host = 'localhost',
    port = '5534',
    database = 'payment_control'
))

STATUS_PAGAMENTO = {
    'A VENCER':1,
    'VENCIDO':2,
    'PROTESTADO':3,
    'PAGO':4
}

