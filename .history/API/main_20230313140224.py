import pandas as pd 
import numpy as np 
import sys 
import os 
from datetime import datetime

class Debito:
    def __init__(self, valor:float, data_emissao:str, data_vencimento:str, fornecedor:str, pedido:str) -> None:
        self._valor = valor 
        self._data_emissao = data_emissao
        self._data_vencimento = data_vencimento
        self._fornecedor = fornecedor
        self._pedido = pedido

    # Getters
    def get_valor(self):
        return self._valor
    
    def get_data_emissao(self):
        return self._data_emissao
    
    def get_data_vencimento(self):
        return self._data_emissao
    
    def get_fornecedor(self):
        return self._fornecedor
    
    def get_pedido(self):
        return self._pedido

    # Setters
    def set_valor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Valor não pode ser negativo.")
        self._valor = novo_valor

    def set_data_emissao(self, novo_valor):
        FMT = '%d/%m/%Y'
        if not isinstance(novo_valor, str):
            raise TypeError("O tipo de entrada deve ser um STRING.")
        try:
            return datetime.strptime(novo_valor, FMT).date()
        except SyntaxError as error:
            print(f'Erro apresentado: {error}') 
    
    def set_data_vencimento(self, novo_valor):
        FMT = '%d/%m/%Y'
        if not isinstance(novo_valor, str):
            raise TypeError("O tipo de entrada deve ser um STRING.")
        try:
            return datetime.strptime(novo_valor, FMT).date()
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

class Cheque(Debito):
    def __init__(self, valor, data_emissao, data_vencimento, fornecedor, pedido, banco,numero_cheque) -> None:
        super().__init__(valor, data_emissao, data_vencimento, fornecedor, pedido)
        self._numero_cheque = numero_cheque
        self._banco = banco 
    # Getters
    def get_numero_cheque(self):
        return self._numero_cheque
    def get_banco(self):
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


if __name__ == '__main__':
    primeira_conta = Cheque(
        valor=1500.00,
        data_emissao='13/03/2023',
        data_vencimento='13/04/2023',
        fornecedor='BELLPAR',
        pedido='123ABC',
        banco='BRADESCO',
        numero_cheque='15ABC'
    )
    print(primeira_conta.get_valor())




    
    




