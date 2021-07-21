from datetime import datetime

class DateBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_date()

    def month_registration(self):
        mes_do_ano = [
            "janeiro", "fevereiro",
            "março", "abril", "maio",
            "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        return mes_do_ano[mes_cadastro]

    def weekday_registration(self):
        dia_semana_lista = [
            "segunda-feira", "terça-feira",
            "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_date(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada