class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade #atributos
        self.nome = nome #atributos
        self.filhos = list(filhos) #atributos

    def cumprimentar(self): # Metodod intancia
        return f'Olá {id(self)}'

    @staticmethod #Decorate
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atribtos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(Pessoa.metodo_estatico(), Rawston.metodo_estatico())
    print(Pessoa.nome_e_atribtos_de_classe(), Rawston.nome_e_atribtos_de_classe())
