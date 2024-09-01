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

    def busca_em_profundidade(self, vertice_inicial, visitados=None):
        if visitados is None:
            print("Busca em Profundidade:")
            visitados = set()

        visitados.add(vertice_inicial)
        print(vertice_inicial)

        for vizinho, _ in self.grafo.get(vertice_inicial, []):
            if vizinho not in visitados:
                self.busca_em_profundidade(vizinho, visitados)

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
    

    def __str__(self):
        return str(self.grafo)

grafo = Grafo()

grafo.adicionar_vertice('frankfurt')
grafo.adicionar_vertice('wurzburg')
grafo.adicionar_vertice('mannheim')
grafo.adicionar_vertice('karlsruhe')
grafo.adicionar_vertice('stuttgart')
grafo.adicionar_vertice('Ulm')
grafo.adicionar_vertice('Memmingen')
grafo.adicionar_vertice('basel')
grafo.adicionar_vertice('zurich')
grafo.adicionar_vertice('bern')
grafo.adicionar_vertice('nurnberg')
grafo.adicionar_vertice('bayreuth')
grafo.adicionar_vertice('munchen')
grafo.adicionar_vertice('rosenheim')
grafo.adicionar_vertice('innsbruck')
grafo.adicionar_vertice('landeck')
grafo.adicionar_vertice('salzburg')
grafo.adicionar_vertice('linz')
grafo.adicionar_vertice('passau')

grafo.adicionar_arco('frankfurt', 'wurzburg', 111)
grafo.adicionar_arco('frankfurt', 'mannheim', 85)
grafo.adicionar_arco('mannheim', 'karlsruhe', 67)
grafo.adicionar_arco('karlsruhe', 'stuttgart', 64)
grafo.adicionar_arco('wurzburg', 'stuttgart', 140)
grafo.adicionar_arco('wurzburg', 'ulm', 183)
grafo.adicionar_arco('stuttgart', 'ulm', 107)
grafo.adicionar_arco('ulm', 'memmingen', 55)
grafo.adicionar_arco('memmingen', 'zurich', 184)
grafo.adicionar_arco('karlsruhe', 'basel', 191)
grafo.adicionar_arco('basel', 'bern', 91)
grafo.adicionar_arco('basel', 'zurich', 85)
grafo.adicionar_arco('bern', 'zurich', 120)
grafo.adicionar_arco('memmingen', 'munchen', 115)
grafo.adicionar_arco('munchen', 'ulm', 123)
grafo.adicionar_arco('munchen', 'nurnberg', 170)
grafo.adicionar_arco('nurnberg', 'bayreuth', 75)
grafo.adicionar_arco('nurnberg', 'passau', 220)
grafo.adicionar_arco('passau', 'linz', 102)
grafo.adicionar_arco('munchen', 'passau', 189)
grafo.adicionar_arco('munchen', 'rosenheim', 59)
grafo.adicionar_arco('rosenheim', 'innsbruck', 93)
grafo.adicionar_arco('innsbruck', 'landeck', 73)
grafo.adicionar_arco('rosenheim', 'salzburg', 81)
grafo.adicionar_arco('salzburg', 'linz', 126)

print(grafo)

grafo.busca_em_largura('frankfurt')
grafo.busca_em_profundidade('frankfurt')
grafo.busca_uniforme('frankfurt')

{'frankfurt': [('wurzburg', 111), ('mannheim', 85)], 'wurzburg': [('frankfurt', 111)], 'mannheim': [('frankfurt', 85), ('karlsruhe', 67)], 'karlsruhe': [('mannheim', 67)]}