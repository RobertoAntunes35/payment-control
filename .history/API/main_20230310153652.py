import pandas as pd 
import numpy as np 
import sys 
import os 




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


class Cheque:
    pass 


class CartaoCredito:
    pass 




class Debito:
    pass 



