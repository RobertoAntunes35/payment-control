import pandas as pd 
import numpy as np 
import sys 
import os 
from datetime import datetime
from collections import namedtuple

from collections import UserDict, UserList

from configs import *
import schema as sch

class Debito:
    def __init__(self, valor:float, data_emissao:str, data_vencimento:str, fornecedor:str, pedido:str, status = "A VENCER") -> None:
        self._valor = valor 
        self._data_emissao = data_emissao
        self._data_vencimento = data_vencimento
        self._fornecedor = fornecedor
        self._pedido = pedido
        self.FMT = '%d/%m/%Y'
        self._status = status
    
    def __str__(self) -> str:
        return 'Valor do Título: %s \
                \nData Vencimento: %s\
                \nFornecedor: %s \
                \nNúmero Pedido: %s ' \
        % (self._valor, self._data_vencimento, self._fornecedor, self._pedido)

    # Getters
    def get_valor(self):
        if not isinstance(self._valor, float):
            raise TypeError("O valor de entrada do débito deve ser de tipo float.")
        return self._valor
                
    def get_data_emissao(self):
        try:
            return datetime.strptime(self._data_emissao, self.FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}')   
        return TypeError(f'Tipo não compativel. Data: {self._data_emissao}')       

    def get_data_vencimento(self):
        try:
            return datetime.strptime(self._data_vencimento, self.FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 
        return TypeError(f'Tipo não compativel. Data: {self._data_vencimento}')    

    def get_fornecedor(self):
        if not isinstance(self._fornecedor, str):
            raise TypeError("Tipo do fornecedor deve ser string.")    
        return self._fornecedor
    
    def get_pedido(self):
        if not isinstance(self._pedido, str):
            raise TypeError("Tipo do fornecedor deve ser string.")
        return self._pedido

    def get_status(self):
        if not isinstance(self._status, str):
            raise TypeError("Se atente ao tipo.")
        return self._status
     
    # Setters
    def set_valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("Valor não pode ser negativo.")
        self._valor = novo_valor

    def set_data_emissao(self, novo_valor):
        if not isinstance(novo_valor, str):
            raise TypeError("O tipo de entrada deve ser um STRING.")
        try:
            return datetime.strptime(novo_valor, self.FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 
    
    def set_data_vencimento(self, novo_valor):
        if not isinstance(novo_valor, str):
            raise TypeError("O tipo de entrada deve ser um STRING.")
        try:
            return datetime.strptime(novo_valor, self.FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 

    def set_fornecedor(self, novo_valor):
        if novo_valor is None:
            raise SyntaxError("Define valores para o novo fornecedor.")
        self._fornecedor = novo_valor

    def set_pedido(self, novo_valor):
        if novo_valor is None:
            raise SyntaxError("Defina valores para o novo pedido.")
        self._pedido = novo_valor

    def set_status(self, novo_valor):
        if novo_valor not in STATUS_PAGAMENTO.keys():
            raise KeyError("Se atente aos status de pagamento disponiveis.")
        self._status = novo_valor

class Cheque(Debito):
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, banco:str, numero_cheque:str, status = None) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido, status)
        self._numero_cheque = numero_cheque
        self._banco = banco 
        self._tipo = "BOLETO"

    @property
    def tipo(self):
        return self._tipo

    # Getters
    def get_numero_cheque(self):
        if not isinstance(self._numero_cheque, str):
            raise TypeError("O número do cheque deve ser uma string.")
        return self._numero_cheque
    
    def get_banco(self):
        if not isinstance(self._banco, str):
            raise TypeError("O nome do banco deve ser uma string.")
        return self._banco 

    # Setters
    def set_numero_cheque(self, novo_valor):
        if novo_valor is None:
            raise SyntaxError("Defina valores para o numero do cheque.")
        self._numero_cheque = novo_valor

    def set_banco(self, novo_valor):
        if novo_valor is None:
            raise SyntaxError("Defina valores para o numero do banco.")
        self._banco = novo_valor
    
class Boleto(Debito):

    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, numero_boleto: int, protesto: bool, dias_protesto: int, status=None ,parcelas = None) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido, status)
        self._numero_boleto = numero_boleto
        self._protesto = protesto
        self._dias_protesto = dias_protesto
        self._parcelas = parcelas
        self._tipo = "BOLETO"

    @property
    def tipo(self):
        return self._tipo
    
     
    # Getters
    def get_numero_boleto(self):
        return self._numero_boleto
    
    def get_protesto(self):
        return self._protesto
    
    def get_dias_protesto(self):
        return self._dias_protesto
    
    def get_parcelas(self):
        if self._parcelas is None:
            return 0
        return self._parcelas
    

    # Setters 
    def set_numero_boleto(self, novo_valor):
        if not isinstance(novo_valor, int):
            raise TypeError("Digite um número inteiro para alterar o número do boleto.")
        self._numero_boleto = novo_valor

    def set_protesto(self, novo_valor):
        if not isinstance(novo_valor, bool):
            raise TypeError("Digite verdadeiro ou falso para alteração a condição de protesto.")
        self._protesto = novo_valor

    def set_dias_protesto(self, novo_valor):
        if not isinstance(novo_valor, int):
            raise TypeError("Digite um número inteiro para a alteração dos dias.")
        self._dias_protesto = novo_valor

    def set_parcelas(self, novo_valor):
        if not isinstance(novo_valor, int):
            raise TypeError("Digite um número inteiro para a alteração das parcelas.")
        self._parcelas = novo_valor


class Dinheiro(Debito):
    tipo = "DINHEIRO"
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, status = None) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido, status)
        self._tipo = "CHEQUE"

    @property
    def tipo(self):
        return self._tipo


class CartaoCredito(Debito):
    tipo = "CARTAO DE CREDITO"
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, parcelas: int, fechamento_fatura: str, status = None) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido, status)
        self._parcelas = parcelas
        self._fechamento_fatura = fechamento_fatura

        self._tipo = "CARTAO DE CREDITO"

    @property
    def tipo(self):
        return self._tipo

    # Getters
    def get_parcelas(self):
        if not isinstance(self._parcelas, int):
            raise TypeError("As parcelas devem ser um valor inteiro.")
        return self._parcelas
    
    def get_fechamento_fatura(self):
        try:
            return datetime.strptime(self._fechamento_fatura, self.FMT)
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 
        return self._fechamento_fatura
    
    # Setters
    def set_parcelas(self, novo_valor):
        if not isinstance(novo_valor, int):
            raise TypeError("Digite um número inteiro para as parcelas.")
        
    def set_fechamento_fatura(self, novo_valor):
        if not isinstance(novo_valor, str):
            raise TypeError("O tipo de entrada deve ser uma STRING.")
        try:
            return datetime.strptime(novo_valor, self.FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}')

class ContaEmpresa:
    def __init__(self, controlador_bd, schema) -> None:
        self._controlador_bd = controlador_bd
        self._schema = schema
    
    def __str__(self) -> str:
        pass 

    def add_titulos(self, classTitulo, bdTitulo):
        consulta_titulos = self._controlador_bd.query(self._schema).filter(self._schema.idTitulos == bdTitulo.id).all()
        if consulta_titulos:
            print('O título já existe na base de dados.')
        else:
            add_titulo = self._schema(
                tipo = classTitulo.tipo,
                idTitulos = bdTitulo.id
            )
            self._controlador_bd.add(add_titulo)
            self._controlador_bd.commit()
            self._controlador_bd.close()
        
    def add_boleto(self, dados_boleto):
        novo_boleto =  sch.Boleto(
        valor = dados_boleto.get_valor(),
        dataEmissao = dados_boleto.get_data_emissao(),
        dataPagamento = dados_boleto.get_data_emissao(),
        dataVencimento = dados_boleto.get_data_vencimento(),
        fornecedor = dados_boleto.get_fornecedor(),
        pedido = dados_boleto.get_pedido(),
        statusPagamento = dados_boleto.get_status(),
        numeroBoleto = dados_boleto.get_numero_boleto(),
        protesto = dados_boleto.get_protesto()
    )
        self._controlador_bd.add(novo_boleto)
        self._controlador_bd.commit()
        self.add_titulos(dados_boleto, novo_boleto)
    def add_cheque(self, dados_cheque):
        pass 
    def add_dinheiro(self, dados_dinheiro):
        pass 
    def add_cartao(self, dados_cartao):
        pass 
    def alter_titulos(self):
        pass 
    def pay_titulos(self):
        pass 


if __name__ == '__main__':
    
    titulo_boleto = Boleto(
        valor=1500.00,
        data_emissao='13/03/2023',
        data_vencimento='13/04/2023',
        fornecedor='REFRIX',
        pedido='123ABC',
        dias_protesto=5,
        numero_boleto=123,
        protesto=True,
        status="A VENCER"
    )

    Session = sessionmaker(bind = engine)
    session = Session()
    ContaMon = ContaEmpresa(session, sch.BancoConta)
    

    
    






    
    




