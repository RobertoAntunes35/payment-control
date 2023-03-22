from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, Date

Base = declarative_base()

class Boleto(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, auto_increment = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(Date, nullable = False)
    dataPagamento = Column(Date, nullable = False)
    dataVencimento = Column(Date, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcelo = Column(Integer, nullable = True)

    class Meta:
        pass

class Cheque(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, auto_increment = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(Date, nullable = False)
    dataPagamento = Column(Date, nullable = False)
    dataVencimento = Column(Date, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcelo = Column(Integer, nullable = True)

    class Meta:
        pass

class Dinheiro(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, auto_increment = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(Date, nullable = False)
    dataPagamento = Column(Date, nullable = False)
    dataVencimento = Column(Date, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcelo = Column(Integer, nullable = True)

    class Meta:
        pass

class CartaoCredito(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, auto_increment = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(Date, nullable = False)
    dataPagamento = Column(Date, nullable = False)
    dataVencimento = Column(Date, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcelo = Column(Integer, nullable = True)

    class Meta:
        pass

class BancoConta(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, auto_increment = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(Date, nullable = False)
    dataPagamento = Column(Date, nullable = False)
    dataVencimento = Column(Date, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcelo = Column(Integer, nullable = True)

    class Meta:
        pass

