import re

class TelefoneBr:

    def __init__(self, number):
        if self.validate_number(number):
            self._number = number
        else:
            raise ValueError('Número incorreto')

    def validate_number(self, number):
        standard = re.compile("[(]{0,1}[0-9]{0,2}[)]{0,1}[0-9]{4,5}[-]?[0-9]{4}")
        match = re.search(standard, number)
        if match:
             return True
        else:
            raise ValueError("Número não esta nos parâmetros")

    def __str__(self):
        standard = re.compile("([(]{0,1}[0-9]{0,2}[)]{0,1})?([0-9]{4,5}[-]{0,1})([0-9]{4})")
        match = re.search(standard, self._number)
        if '-' in match.group(2):
            sub = match.group(2).replace('-', '')
            return f'Número: +55 (11){sub}-{match.group(3)}'
        elif match.group(1):
            return f'Número: +55 (11){match.group(2)}-{match.group(3)}'
        else:
            return f'Número: +55 ({match.group(1)}){match.group(2)}-{match.group(3)}'
