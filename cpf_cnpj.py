from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_doc(doc):
        if len(doc) == 11:
            return DocCpf(doc)
        elif len(doc) == 14:
            return DocCnpj(doc)
        else:
            raise ValueError('Quantidade de digitos inválidos')


class DocCpf:
    def __init__(self, doc):
        if self.valida(doc):
            self._cpf = doc
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def valida(self, doc):
        validation = CPF()
        return validation.validate(doc)

    def format(self):
        formation = CPF()
        return formation.mask(self._cpf)


class DocCnpj:
    def __init__(self, doc):
        if self.valida(doc):
            self._cnpj = doc
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def valida(self, doc):
        validation = CNPJ()
        return validation.validate(doc)

    def format(self):
        formation = CNPJ()
        return formation.mask(self._cnpj)
