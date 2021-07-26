import requests as rq


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acesso_viacepAPI(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        acess = rq.get(url)
        dados = acess.json()
        return dados

    def __str__(self):
        cep = self.acesso_viacepAPI()['cep']
        cidade = self.acesso_viacepAPI()['localidade']
        uf = self.acesso_viacepAPI()['uf']
        return f'CEP: {cep}\nCIDADE: {cidade}\nUF: {uf}'