import networkx as nx
import random
import matplotlib.pyplot as plt

# Numero de rainhas (tamanho tabuleiro) e seed para o random
SEED = 44
NUM_VERTICES = 10
random.seed(SEED)

def gerar_grafo():
    
    G = nx.Graph()
    
    G.add_nodes_from(range(NUM_VERTICES))
    
    for i in range(NUM_VERTICES):
        for j in range(i + 1, NUM_VERTICES):
            if random.random() > 0.5:
                G.add_edge(i, j)
    
    return G

def colorir_grafo(grafo):
    cor_dos_vertices = {}
    
    for vertice in grafo.nodes():
        cores_vizinhos = {cor_dos_vertices[vizinho] for vizinho in grafo.neighbors(vertice) if vizinho in cor_dos_vertices}
        
        cor = 0
        while cor in cores_vizinhos:
            cor += 1
        
        cor_dos_vertices[vertice] = cor
    
    return cor_dos_vertices

def plotar_grafo_colorido(grafo, cores):
    pos = nx.spring_layout(grafo)
    
    cor_nos = [cores[no] for no in grafo.nodes()]
    
    nx.draw(grafo, pos, with_labels=True, node_color=cor_nos, node_size=3000, cmap=plt.cm.rainbow, edge_color='gray', font_size=15)
    
    plt.show()

grafo = gerar_grafo()
cores = colorir_grafo(grafo)

print(f"Grafo: {grafo}")


plotar_grafo_colorido(grafo, cores)
