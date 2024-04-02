# Algoritmo Genético

# Bibliotecas
import random

from rich.console import Console
from rich.table import Table 

# Arquivos locais
import individuo as ind
import funcoes_extras as fe
import funcoes_AG as ag

import matplotlib.pyplot as plt

TEMPO = 1

# MAIN
if __name__ == "__main__":
    
    # Lista usadas no AG
    populacao = []
    fitness_medio_geracao = []
    
    # Parametros iniciais
    tamanho_populacao = int(input("Digite o tamanho da populacao: "))
    geracoes = int(input("Digite o numero de geracoes: "))
    probabilidade_cruzamento = float(input("Digite a probabilidade de cruzamento: "))
    probabilidade_mutacao = float(input("Digite a probabilidade de mutacao: "))
    
    fe.parametros_iniciais(tamanho_populacao, geracoes, probabilidade_mutacao, probabilidade_cruzamento)
    
    print("\n")
    
    # Parametros do cromossomo
    cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real = fe.parametros_cromossomo()
    
    print("\n")
    
    # Gera a populacao inicial
    for i in range(tamanho_populacao):
        individuo = ag.gera_individuo(cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real)
        populacao.append(individuo)
        
    # Salva a primeira geracao
    primeira_geracao = populacao.copy()

    # Janela do gráfico
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.show(block=False)

    # Plota a base do grafico
    ax = ag.plota_grafico_geracional(populacao, ax, 0)
    plt.pause(TEMPO)

    melhores_individuos = []

    # Algoritmo Genetico (MAIN)
    for ger in range(geracoes):
        
        # Define a lista para os novos individuos
        populacao_nova = []
        
        # Aplica o elitismo
        eleito = ag.eletista(populacao)
        
        # Adiciona o eleito na nova populacao
        populacao_nova.append(eleito)
        melhores_individuos.append(eleito)
        
        # Define uma nova geração
        for j in range(int(len(populacao)/2)):
            
            # Seleciona os pais
            pai1, pai2 = ag.seleciona_pais_ranking(populacao)
            
            # Cruzamento (Crossover)
            filho1_x, filho2_x, filho1_y, filho2_y = ag.crossover(pai1, pai2, probabilidade_cruzamento,
                                                                  cromossomo_gene_inteiro_x + cromossomo_gene_real,
                                                                  cromossomo_gene_inteiro_y + cromossomo_gene_real)
            
            # Mutação
            filho1_x, filho1_y, filho2_x, filho2_y = ag.mutacao(filho1_x, filho1_y, 
                                                                filho2_x, filho2_y, 
                                                                probabilidade_mutacao)
            
            # Adiciona os filhos na nova populacao
            individuo1 = ag.gera_novo_individuo(filho1_x, filho1_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real)
            individuo2 = ag.gera_novo_individuo(filho2_x, filho2_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real)
            
            # Adiciona o individuo na nova populacao
            populacao_nova.append(individuo1)
            populacao_nova.append(individuo2)
            
        # Sortea um individuo para sair da populacao, para manter o tamanho da populacao
        # e evitar que a populacao cresça. O individuo não pode ser o eleito (melhor individuo)
        # que está na primeira posição da nova população
        individuo_drop = random.choice(populacao_nova[1:])
        populacao_nova.remove(individuo_drop)
        
        # Calcula a media do fitness da geracao, pega toda a populacao e calcula a media
        # Calcula a media dos fitness da populacao
        fitness_medio = 0
        for i in range(len(populacao_nova)):
            fitness_medio += populacao_nova[i].fitness
            
        # Adiciona o fitness medio da geracao na lista
        fitness_medio_geracao.append(fitness_medio/len(populacao_nova))
        
        # Apaga a populacao antiga
        populacao.clear()
        
        # Atualiza a populacao, copia a populacao nova para a populacao
        populacao = populacao_nova.copy()
        
        # Plota o grafico da geracao atualizando em cima do outro
        ax = ag.plota_grafico_geracional(populacao, ax, ger)
        
        # Limpa a populacao, o eleito
        populacao_nova.clear()
 
    ultimate_geracao = populacao.copy()

    # Fecha a janela do gráfico
    plt.close(fig)

    # Ordena a populacao inicial e a populacao final
    primeira_geracao.sort(key=lambda x: x.fitness, reverse=True)
    ultimate_geracao.sort(key=lambda x: x.fitness, reverse=True)

    # Printa em forma de tabela a primeira geracao e a ultima geração lado a lado, apenas o fitness e o individuo
    console = Console()
    table = Table(title="Primeira Geracao x Ultima Geracao - Fitness")
    table.add_column("Individuo", style="cyan", width=70)
    table.add_column("Primeira Geração", style="cyan", width=70)
    table.add_column("Ultima Geração", style="cyan", width=70)

    # Coloca o primeiro individuo da primeira geracao e da ultima geracao em amarelo na tabela
    table.add_row("1", f"{primeira_geracao[0].fitness}", f"{ultimate_geracao[0].fitness}", style="yellow")

    for i in range(1, len(primeira_geracao)):
        table.add_row(f"{i + 1}", f"{primeira_geracao[i].fitness}", f"{ultimate_geracao[i].fitness}")
    console.print(table)
    
    plt.close('all')
    
    # Criação dos subplots 3D
    fig = plt.figure(figsize=(18, 5))
    
    # Primeiro subplot
    ax1 = fig.add_subplot(131, projection='3d')
    ag.plota_grafico_ultima_geracao(ultimate_geracao, ax1)
    
    ax2 = fig.add_subplot(132, projection='3d')
    ag.plota_grafico_ideal(ax2)

    ax3 = fig.add_subplot(133)
    ag.plota_grafico_media(fitness_medio_geracao, melhores_individuos, ax3)
    
    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    
    # Exibição dos gráficos
    plt.show()

