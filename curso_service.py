class Curso:
     def __init__(self, id, nome, nivel):
         self.id = id
         self.nome = nome
         self.nivel = nivel 

class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1


        # ---- Dados iniciais (comente se não quiser) ----
        self.adicionar("Matemática", "Básico")
        self.adicionar("Física", "Intermediário")
        self.adicionar("Química", "Avançado")
        # -------------------------------------------------


    def adicionar(self, nome, nivel):
        id = self.proximo_id
        curso = Curso(id, nome, nivel)
        self.lista.append(curso)
        self.proximo_id += 1


    def listar(self):
        return self.lista


