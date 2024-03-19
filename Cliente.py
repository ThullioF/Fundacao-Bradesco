class Cliente:
    def __init__(self,nome,fone):

        self._nome = nome
        self._telefone = fone

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self,nome):
            self._nome = nome