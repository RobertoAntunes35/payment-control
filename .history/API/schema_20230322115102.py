from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime

Base = declarative_base()

class Boleto(Base):
    __tablename__ = 'boleto'

    idBoleto = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(DateTime, nullable = False)
    dataPagamento = Column(DateTime, nullable = False)
    dataVencimento = Column(DateTime, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroBoleto = Column(Integer, nullable = False)
    protesto = Column(Boolean, nullable = False)
    parcela = Column(Integer, nullable = True)

    class Meta:
        pass

class Cheque(Base):
    __tablename__ = 'cheque'

    idBoleto = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(DateTime, nullable = False)
    dataPagamento = Column(DateTime, nullable = False)
    dataVencimento = Column(DateTime, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    numeroCheque = Column(Integer, nullable = False)
    banco = Column(String(50), nullable = False)

    class Meta:
        pass

class Dinheiro(Base):
    __tablename__ = 'dinheiro'

    idBoleto = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(DateTime, nullable = False)
    dataPagamento = Column(DateTime, nullable = False)
    dataVencimento = Column(DateTime, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    class Meta:
        pass

class CartaoCredito(Base):
    __tablename__ = 'cartaocredito'

    idBoleto = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    valor = Column(Float, nullable = False)
    dataEmissao = Column(DateTime, nullable = False)
    dataPagamento = Column(DateTime, nullable = False)
    dataVencimento = Column(DateTime, nullable = False)
    fornecedor = Column(String(50), nullable = False)
    pedido = Column(String(15), nullable = False)
    statusPagamento = Column(Boolean, nullable = False)

    class Meta:
        pass

class BancoConta(Base):
    __tablename__ = 'bancoconta'

    idContas = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    tipo = Column(String(40), nullable = False)
    idCheque = Column(Integer, nullable = False)
    idBoleto = Column(Integer, nullable = False)
    idDinheiro = Column(Integer, nullable = False)
    idPix = Column(Integer, nullable = False)
    idCartao = Column(Integer, nullable = False)

    class Meta:
        pass

