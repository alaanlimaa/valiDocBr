from cpf_chars import Cpf
from cpf_cnpj import Documento
from datas import DateBR
from telefone import TelefoneBr
from cep import BuscaEndereco


# ===== Validando CPF com caracteres "-" e "." =====


# CASO 01
cpf = "083.735.418-88"
object_cpf = Cpf(cpf)
print(object_cpf) # OUT → 083.735.418-88

# CASO 02
cpf = "083735.418-88"
object_cpf = Cpf(cpf)
print(object_cpf) # OUT → 083.735.418-88

# CASO 03
cpf = "083735.41888"
object_cpf = Cpf(cpf)
print(object_cpf) # OUT → 083.735.418-88


# ===== Validando CPF & CNPJ sem caracteres especiais =====


cpf = "08373541888"
cnpj = "47295521000187"
obj_cpf = Documento.cria_doc(cpf)
obj_cnpj = Documento.cria_doc(cnpj)
print(obj_cpf) # OUT → 083.735.418-88
print(obj_cnpj) # OUT → 47.295.521/0001-87


# ===== Validando TELEFONE sem caracteres especiais =====


# CELULAR
celular = "1194568-0125"
object_telefone = TelefoneBr(celular)
print(object_telefone) # OUT → Número: +55 (11)94568-0125

# TELEFONE RESIDENCIAL
telefone = "4568-0125"
object_telefone = TelefoneBr(telefone)
print(object_telefone) # OUT → Número: +55 (11)4568-0125


# =====  DATAS  =====

registro = DateBR()
print(registro) # OUT → 21/07/2021 17:15
print(registro.weekday_registration()) # OUT → quarta-feira
print(registro.month_registration()) # OUT → julho


# =====  CEP  =====

cep = 12850970 # Gerador CEP site 4devs.com.br
obj = BuscaEndereco(cep)
print(obj) # OUT →  CEP: 12850-970 CIDADE: Bananal UF: SP
