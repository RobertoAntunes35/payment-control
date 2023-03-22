import pandas as pd 
import numpy as np 
import sys 
import os 
from datetime import datetime
from collections import namedtuple

from configs import STATUS_PAGAMENTO

class Debito:
    def __init__(self, valor:float, data_emissao:str, data_vencimento:str, fornecedor:str, pedido:str, status = "A VENCER") -> None:
        self._valor = valor 
        self._data_emissao = data_emissao
        self._data_vencimento = data_vencimento
        self._fornecedor = fornecedor
        self._pedido = pedido
        self.FMT = '%d/%m/%Y'
        self._status = status
        

    # Getters
    def get_valor(self):
        return self._valor
    
    def get_data_emissao(self):
        try:
            return datetime.strptime(self._data_emissao, self.FMT)
        except SyntaxError as error:
            print(f'Erro apresentado: {error}')   
        return self._data_emissao
    
    def get_data_vencimento(self):
        try:
            return datetime.strptime(self._data_vencimento, self.FMT)
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 
        return self._data_vencimento

    def get_fornecedor(self):
        return self._fornecedor
    
    def get_pedido(self):
        return self._pedido

    def get_status(self):
        return self._status
    # 
    
    # Setters
    def set_valor(self, novo_valor):
        if novo_valor < 0:
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
    #

class Cheque(Debito):
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, banco:str, numero_cheque:str) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido)
        self._numero_cheque = numero_cheque
        self._banco = banco 
    class Meta:
        tipo = "CHEQUE"
        
    # Getters
    def get_numero_cheque(self):
        return self._numero_cheque
    
    def get_banco(self):
        return self._banco
    # 

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
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, numero_boleto: int, protesto: bool, dias_protesto: int, parcelas = None) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido)
        self._numero_boleto = numero_boleto
        self._protesto = protesto
        self._dias_protesto = dias_protesto
        self._parcelas = parcelas

    class Meta:
        tipo = "BOLETO"

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
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido)
    
    class Meta:
        tipo = "DINHEIRO"

class CartaoCredito(Debito):
    def __init__(self, valor: float, data_emissao: str, data_vencimento: str, fornecedor: str, pedido: str, parcelas: int, fechamento_fatura: str) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido)
        self._parcelas = parcelas
        self._fechamento_fatura = fechamento_fatura

    class Meta:
        tipo = "CARTAO DE CREDITO"

    # Getters
    def get_parcelas(self):
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
    def __init__(self):
        self._banco_informacoes = []
    
    def __str__(self) -> str:
        for i in self._banco_informacoes:
            print('Título: %s' % i)

    def get_banco_informacoes(self):
        return self._banco_informacoes

    def inclusao_titulo(self, value):
        self._banco_informacoes.append(value)

    def exclusao_titulo(self):
        pass
    def alteracao_titulo(self):
        pass 
    def pagamento_titulo(self):
        pass 
    def consulta_titulo(self):
        pass

if __name__ == '__main__':
    conta_cheque = Cheque(
        valor=1500.00,
        data_emissao='13/03/2023',
        data_vencimento='13/04/2023',
        fornecedor='BELLPAR',
        pedido='123ABC',
        banco='BRADESCO',
        numero_cheque='15ABC'
    )
    conta_boleto = Boleto(
        valor=1500.00,
        data_emissao='13/03/2023',
        data_vencimento='13/04/2023',
        fornecedor='REFRIX',
        pedido='123ABC',
        dias_protesto=5,
        numero_boleto=123,
        protesto=True
    )

    ContaMon = ContaEmpresa()
    ContaMon.inclusao_titulo(conta_boleto)
    print(ContaMon.get_banco_informacoes())
    

    




    
    




