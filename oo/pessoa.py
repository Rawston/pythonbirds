class Pessoa:
    def __init__(self, *filhos, nome=None, idade=45):
        self.idade = idade
        self.nome=None
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Marinho = Pessoa(nome='Marinho')
    Rawston = Pessoa(Marinho, nome='Rawston')
    print(Pessoa.cumprimentar(Rawston))
    print(id(Rawston))
    print(Rawston.cumprimentar())
    print(Rawston.nome)
    print(Rawston.idade)
    for filho in Rawston.filhos:
        print(filho.nome)