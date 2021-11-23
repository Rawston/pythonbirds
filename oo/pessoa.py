class Pessoa:
    def __init__(self, nome=None, idade=45):
        self.idade = idade
        self.nome=None

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Rawston')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.nome)
    p.nome= 'renzo' #Alterar o None
    print(p.idade)