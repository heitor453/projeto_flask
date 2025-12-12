class Professor:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf



class ProfessorService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1


       

    def adicionar(self, nome, cpf):
        id = self.proximo_id
        professor = Professor(id, nome, cpf)
        self.lista.append(professor)
        self.proximo_id += 1


    def listar(self):
        return self.lista
