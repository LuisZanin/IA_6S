from collections import deque
import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_arco(self, vertice_origem, vertice_destino, peso=1):
        if vertice_origem in self.grafo:
            self.grafo[vertice_origem].append((vertice_destino, peso))
        else:
            self.grafo[vertice_origem] = [(vertice_destino, peso)]
        
        if vertice_destino in self.grafo:
            self.grafo[vertice_destino].append((vertice_origem, peso))
        else:
            self.grafo[vertice_destino] = [(vertice_origem, peso)]

    def busca_em_largura(self, vertice_inicial):
        print("Busca em Largura:")
        visitados = set()
        fila = deque([vertice_inicial])
        while fila:
            vertice = fila.popleft() #primeiro vertice da fila
            if vertice not in visitados:
                print(vertice)
                visitados.add(vertice)

                # adiciona os vizinhos ainda nao visitados
                for vizinho, _ in self.grafo.get(vertice, []):
                    if vizinho not in visitados:
                        fila.append(vizinho)

    
    
    def busca_em_largura_caminho(self, vertice_inicial, vertice_final):
        print("Busca em largura por estado inicial e final:")
        visitados = set()
        fila = deque([vertice_inicial])

        percorridos = {vertice_inicial: None}

        while fila:
            vertice = fila.popleft() 

            if vertice == vertice_final:
                caminho_largura = []
                while vertice is not None:
                    caminho_largura.append(vertice)
                    vertice = percorridos[vertice]
                caminho_largura.reverse()
                return caminho_largura
            
            if vertice not in visitados:
                print(vertice)
                visitados.add(vertice)

                for vizinho, _ in self.grafo.get(vertice, []):
                    if vizinho not in visitados:
                        percorridos[vizinho] = vertice
                        fila.append(vizinho)




    def busca_em_profundidade(self, vertice_inicial, visitados=None):
        if visitados is None:
            print("Busca em Profundidade:")
            visitados = set()

        visitados.add(vertice_inicial)
        print(vertice_inicial)

        for vizinho, _ in self.grafo.get(vertice_inicial, []):
            if vizinho not in visitados:
                self.busca_em_profundidade(vizinho, visitados)



    def busca_em_profundidade_caminho(self, vertice_inicial, vertice_final, visitados=None, caminho_profundidade=None):
        if visitados is None:
            visitados = set()
        if caminho_profundidade is None:
            caminho_profundidade = []

        visitados.add(vertice_inicial)
        caminho_profundidade.append(vertice_inicial)

        if vertice_inicial == vertice_final:
            return caminho_profundidade

        for vizinho, _ in self.grafo.get(vertice_inicial, []):
            if vizinho not in visitados:
                resultado = self.busca_em_profundidade_caminho(vizinho, vertice_final, visitados, caminho_profundidade)
                if resultado:
                    return resultado
        caminho_profundidade.pop()


    def busca_uniforme(self, vertice_inicial):
        print("Busca de Custo Uniforme: ")
        fila_prioridade = [(0, vertice_inicial)]
        visitados = set()

        while fila_prioridade:
            custo_atual, vertice = heapq.heappop(fila_prioridade)

            if vertice in visitados:
                continue

            print(f"Visitando {vertice} com custo {custo_atual}")
            visitados.add(vertice)
            for vizinho, peso in self.grafo.get(vertice, []):
                if vizinho not in visitados:
                    novo_custo = custo_atual + peso
                    heapq.heappush(fila_prioridade, (novo_custo, vizinho))


    def busca_uniforme_caminho(self, vertice_inicial, vertice_final):
        print("Busca de Custo Uniforme: ") 
        fila_prioridade = [(0, vertice_inicial, [])]
        visitados = set()

        while fila_prioridade:
            custo_atual, vertice, caminho_atual = heapq.heappop(fila_prioridade)

            if vertice in visitados:
                continue

            caminho_atual = caminho_atual + [vertice]

            if vertice == vertice_final:
                print(f"O Caminho Percorrido foi {caminho_atual} com  o custo total de ${custo_atual}")
                return ""
            
            visitados.add(vertice)
            for vizinho, peso in self.grafo.get(vertice, []):
                if vizinho not in visitados:
                    novo_custo = custo_atual + peso
                    heapq.heappush(fila_prioridade, (novo_custo, vizinho, caminho_atual))
    
    

    def __str__(self):
        return str(self.grafo)

grafo = Grafo()

grafo.adicionar_vertice('frankfurt')
grafo.adicionar_vertice('wurzburg')
grafo.adicionar_vertice('mannheim')
grafo.adicionar_vertice('karlsruhe')
grafo.adicionar_vertice('stuttgart')
grafo.adicionar_vertice('ulm')
grafo.adicionar_vertice('nurnberg')
grafo.adicionar_vertice('basel')

grafo.adicionar_arco('frankfurt', 'wurzburg', 111)
grafo.adicionar_arco('frankfurt', 'mannheim', 85)
grafo.adicionar_arco('mannheim', 'nurnberg', 230)
grafo.adicionar_arco('mannheim', 'karlsruhe', 67)
grafo.adicionar_arco('karlsruhe', 'stuttgart', 64)
grafo.adicionar_arco('karlsruhe', 'basel', 191)
grafo.adicionar_arco('stuttgart', 'wurzburg', 140)
grafo.adicionar_arco('stuttgart', 'ulm', 107)
grafo.adicionar_arco('ulm', 'wurzburg', 183)
grafo.adicionar_arco('ulm', 'nurnberg', 171)
grafo.adicionar_arco('nurnberg', 'wurzburg', 104)



print(grafo)

#Busca em Largura por caminho
#caminho_largura = grafo.busca_em_largura_caminho('ulm', 'frankfurt')
#print("Caminho:", caminho_largura)

#Busca em Profundidade por caminho
#caminho_profundidade = grafo.busca_em_profundidade_caminho('ulm', 'frankfurt')
#print("Caminho:", caminho_profundidade)

caminho_uniforme = grafo.busca_uniforme_caminho('ulm' , 'frankfurt')
print(caminho_uniforme)