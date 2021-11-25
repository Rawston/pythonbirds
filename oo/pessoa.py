class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
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
    Rawston.sobrenome= 'Pinto'## atibuto adicionado dinamicamente
    # del Rawston.sobrenome #Remoção
    # print(Rawston.__dict__) #conferir instancia de um objeto
    # print(Marinho.__dict__) #conferir instancia de um objeto
