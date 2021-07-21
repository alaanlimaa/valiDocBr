import validate_docbr as vdoc
import re


class Cpf:

    def __init__(self, doc):
        self._doc = str(doc)
        if self.validate_cpf():
            self._cpf = self.digits_format()
        else:
            raise ValueError('CPF inválido!!!')

    def __str__(self):
        return self.format_cpf()

    def digits_format(self):
        if len(self._doc) > 14 or len(self._doc) < 11:
            raise ValueError('Quantidade de digitos inválidos (acima ou menor que 11)')
        else:
            standard = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}")
            match = re.search(standard, self._doc)
            cpf = str(match.group())
            if match:
                for char in cpf:
                    if char in '.-':
                        cpf = cpf.replace(char, '')
            if len(cpf) == 11:
                return cpf

    def validate_cpf(self):
        validation = vdoc.CPF()
        return validation.validate(self.digits_format())

    def format_cpf(self):
        formation = vdoc.CPF()
        return formation.mask(self._cpf)
