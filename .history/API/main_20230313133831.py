import pandas as pd 
import numpy as np 
import sys 
import os 
from datetime import datetime



class BoletoBancario:
    
    def __init__(self, valor, vencimento, fornecedor, data_entrada, numero_boleto, protesto, dias_protesto) -> None:
        self._valor = valor 
        self._vencimento = vencimento
        self._fornecedor = fornecedor
        self._data_entrada = data_entrada
        self._numero_boleto = numero_boleto
        self._protesto = protesto 
        self._dias_protesto = dias_protesto 

    @property
    def valor(self):
        return self._valor 
    @property.setter
    def valor(self, novo_valor):
        pass

class Dinheiro:
    pass 
class Boleto:
    pass 
class CartaoCredito:
    pass 
class Cheque:
    pass 

class Debito:
    def __init__(self, valor, data_emissao, data_vencimento, fornecedor, pedido) -> None:
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

    
    




