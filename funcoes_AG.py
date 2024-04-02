import individuo as ind
import random
import funcoes_extras as fe
import math
import numpy as np
import matplotlib.pyplot as plt
#import plotly.graph_objects as go

TEMPO = 1

def funcao_de_otimização(x, y):
    z = (math.pow(x, 2)) + (math.pow(y, 2)) + (math.pow((3*x) + (4*y) - 26, 2))
    
    return z

def gera_individuo(cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real):
    
    def testa_limites(num_x, num_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real, cromossomo_x, cromossomo_y):
        
        if num_x > 10.0:
            
            # Se o numero for maior que 10, ele recebe 10
            num_x = 10.0
            
            # Converte o numero para binario
            cromossomo_x = fe.converte_num_bin(num_x, cromossomo_gene_inteiro_x, cromossomo_gene_real)
        
        if num_y > 20.0:
            
            # Se o numero for maior que 20, ele recebe 20
            num_y = 20.0
            
            # Converte o numero para binario
            cromossomo_y = fe.converte_num_bin(num_y, cromossomo_gene_inteiro_y, cromossomo_gene_real)
            
        return num_x, num_y, cromossomo_x, cromossomo_y
    
    # Lista que sera o cromossomo X e Y
    cromossomo_x = []
    cromossomo_y = []
    
    # Gera um cromossomo X -> Cadeia binaria de bits de tamanho cromossomo_gene_inteiro_x
    cromossomo_x = random.choices([0, 1], k=cromossomo_gene_inteiro_x + cromossomo_gene_real)
    
    # Gera um cromossomo Y -> Cadeia binaria de bits de tamanho cromossomo_gene_inteiro_y
    cromossomo_y = random.choices([0, 1], k=cromossomo_gene_inteiro_y + cromossomo_gene_real)
    
    # Randomiza o cromossomo X e Y novamente
    #random.shuffle(cromossomo_x)
    #random.shuffle(cromossomo_y)
    
    # Converte o cromossomo X e Y para numero real
    num_x = fe.converte_bin_num(cromossomo_x, cromossomo_gene_inteiro_x)
    num_y = fe.converte_bin_num(cromossomo_y, cromossomo_gene_inteiro_y)
    
    # Testa os limites do numero, a função de X só pode ir de 0 a 10 e a função de Y de 0 a 20
    # se esse limite for ultrapassado, o cromossomo recebe o valor maximo
    num_x, num_y, cromossomo_x, cromossomo_y = testa_limites(num_x, num_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real, cromossomo_x, cromossomo_y)
    
    # Calcula o fitness do individuo
    fitness = funcao_de_otimização(num_x, num_y)

    # Cria o individuo
    individuo = ind.Individuo(cromossomo_x, cromossomo_y, fitness, num_x, num_y)
    
    return individuo

def eletista(populacao):
    
    # Copia a populacao para nao alterar a original
    populacao_aux = populacao.copy()
    
    # Seleciona o melhor individuo da populacao com base no seu fitness
    eleito = max(populacao_aux, key=lambda x: x.fitness)
    
    return eleito

def seleciona_pais_ranking(populacao):
    
    # A seleção é por ranking, ou seja a probabilidade de seleção é direta e aleatória
    # seleciona-se n indivíduos onde todos têm a mesma chance de serem selecionados
    
    # Declara uma lista auxiliar
    selecao_aux = []
    
    # Seleciona 5 individuos aleatoriamente dentro da população e os coloca em uma lista (PAI 1)
    for i in range(5):
        
        # Garante que o individuo nao seja o mesmo
        individuo = random.choice(populacao)
        
        while individuo in selecao_aux:
            individuo = random.choice(populacao)   
        
        selecao_aux.append(individuo)
    
    # Ordena com base no fitness
    selecao_aux = sorted(selecao_aux, key=lambda x: x.fitness, reverse=True)
    
    # Seleciona o primeiro individuo da lista
    pai1 = selecao_aux[0]
    
    # Enquanto o pai 1 for igual ao pai 2, ele seleciona outro pai 2
    while True:
        
        # Limpa a lista auxiliar
        selecao_aux = []
        
        # Seleciona 5 individuos aleatoriamente dentro da população e os coloca em uma lista (PAI 2)
        for i in range(5):
            
            # Garante que o individuo nao seja o mesmo
            individuo = random.choice(populacao)
            
            while individuo in selecao_aux:
                individuo = random.choice(populacao)   
            
            selecao_aux.append(individuo)
    
        # Ordena com base no fitness
        selecao_aux = sorted(selecao_aux, key=lambda x: x.fitness, reverse=True)
        
        # Seleciona o primeiro individuo da lista
        pai2 = selecao_aux[0]
        
        # Verifica se o pai 1 é != pai 2
        if pai1 != pai2:
            break
    
    return pai1, pai2

def crossover(pai1, pai2, probabilidade_cruzamento, tam_cromossomo_x, tam_cromossomo_y):
    
    if random.random() < probabilidade_cruzamento:

        # Sorteia dois pontos de corte 
        # Apenas o primeiro ponto de corte
        ponto_corte1_x = random.randint(1, tam_cromossomo_x - 1)
        
        # Sorteia o segundo ponto de corte, mas verifica se é diferente do primeiro
        while True:
            ponto_corte2_x = random.randint(1, tam_cromossomo_x - 1)
            
            # Verifa se são iguais
            if ponto_corte1_x != ponto_corte2_x:
                break   
        
        # Agora sorteia apenas o primeiro ponto de corte pro Y
        ponto_corte1_y = random.randint(1, tam_cromossomo_y - 1)
        
        # Sorteia o segundo ponto de corte, mas verifica se é diferente do primeiro
        while True:
            ponto_corte2_y = random.randint(1, tam_cromossomo_y - 1)
            
            # Verifa se são iguais
            if ponto_corte1_y != ponto_corte2_y:
                break
        
        # Verica se o ponto 1 é maior que o ponto 2, se for inverte
        if ponto_corte1_x > ponto_corte2_x:
            aux = ponto_corte1_x
            ponto_corte1_x = ponto_corte2_x
            ponto_corte2_x = aux
            
        # Verica se o ponto 1 é maior que o ponto 2, se for inverte
        if ponto_corte1_y > ponto_corte2_y:
            aux = ponto_corte1_y
            ponto_corte1_y = ponto_corte2_y
            ponto_corte2_y = aux
            
        # Divide o cromossomo em 3 partes (PAI 1) e (PAI 2)
            
        # 1 - Do inicio até o ponto de corte 1
        parte1_x_pai1 = pai1.x[:ponto_corte1_x]
        parte1_y_pai1 = pai1.y[:ponto_corte1_y]
        
        parte1_x_pai2 = pai2.x[:ponto_corte1_x]
        parte1_y_pai2 = pai2.y[:ponto_corte1_y]

        # 2 - Do ponto de corte 1 até o ponto de corte 2
        parte2_x_pai1 = pai1.x[ponto_corte1_x:ponto_corte2_x]
        parte2_y_pai1 = pai1.y[ponto_corte1_y:ponto_corte2_y]
        
        parte2_x_pai2 = pai2.x[ponto_corte1_x:ponto_corte2_x]
        parte2_y_pai2 = pai2.y[ponto_corte1_y:ponto_corte2_y]
        
        # 3 - Do ponto de corte 2 até o final
        parte3_x_pai1 = pai1.x[ponto_corte2_x:]
        parte3_y_pai1 = pai1.y[ponto_corte2_y:]
        
        parte3_x_pai2 = pai2.x[ponto_corte2_x:]
        parte3_y_pai2 = pai2.y[ponto_corte2_y:]
        
        # Cria os filhos
        filho1_x = parte1_x_pai1 + parte2_x_pai2 + parte3_x_pai1
        filho1_y = parte1_y_pai1 + parte2_y_pai2 + parte3_y_pai1
        
        filho2_x = parte1_x_pai2 + parte2_x_pai1 + parte3_x_pai2
        filho2_y = parte1_y_pai2 + parte2_y_pai1 + parte3_y_pai2
        
    else:
        filho1_x = pai1.x
        filho1_y = pai1.y
        
        filho2_x = pai2.x
        filho2_y = pai2.y

    return filho1_x, filho1_y, filho2_x, filho2_y

def mutacao(filho1_x, filho1_y, filho2_x, filho2_y, probabilidade_mutacao):
    
    # Passa por todos os genes do filho e faz a mutacao de acordo com a probabilidade
    # se for menor que a probabilidade de mutacao, ele muda o gene trocando de 0 para 1 e vice-versa
    
    for i in range(len(filho1_x)):
        if random.random() < probabilidade_mutacao:
            if filho1_x[i] == 0:
                filho1_x[i] = 1
            else:
                filho1_x[i] = 0
                
    for i in range(len(filho1_y)):
        if random.random() < probabilidade_mutacao:
            if filho1_y[i] == 0:
                filho1_y[i] = 1
            else:
                filho1_y[i] = 0
                
    for i in range(len(filho2_x)):
        if random.random() < probabilidade_mutacao:
            if filho2_x[i] == 0:
                filho2_x[i] = 1
            else:
                filho2_x[i] = 0
                
    for i in range(len(filho2_y)):
        if random.random() < probabilidade_mutacao:
            if filho2_y[i] == 0:
                filho2_y[i] = 1
            else:
                filho2_y[i] = 0
        
    return filho1_x, filho1_y, filho2_x, filho2_y

def gera_novo_individuo(filho_x, filho_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real):
    
    def testa_limites(num_x, num_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real, cromossomo_x, cromossomo_y):
        
        if num_x > 10.0:
            
            # Se o numero for maior que 10, ele recebe 10
            num_x = 10.0
            
            # Converte o numero para binario
            cromossomo_x = fe.converte_num_bin(num_x, cromossomo_gene_inteiro_x, cromossomo_gene_real)
        
        if num_y > 20.0:
            
            # Se o numero for maior que 20, ele recebe 20
            num_y = 20.0
            
            # Converte o numero para binario
            cromossomo_y = fe.converte_num_bin(num_y, cromossomo_gene_inteiro_y, cromossomo_gene_real)
            
        return num_x, num_y, cromossomo_x, cromossomo_y
    
    # Lista que sera o cromossomo X e Y
    cromossomo_x = []
    cromossomo_y = []
    
    # Traz o cromossomo do filho
    cromossomo_x = filho_x
    cromossomo_y = filho_y
    
    # Converte o cromossomo X e Y para numero real
    num_x = fe.converte_bin_num(cromossomo_x, cromossomo_gene_inteiro_x)
    num_y = fe.converte_bin_num(cromossomo_y, cromossomo_gene_inteiro_y)
    
    # Testa os limites do numero, a função de X só pode ir de 0 a 10 e a função de Y de 0 a 20
    # se esse limite for ultrapassado, o cromossomo recebe o valor maximo
    num_x, num_y, cromossomo_x, cromossomo_y = testa_limites(num_x, num_y, cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real, cromossomo_x, cromossomo_y)
    
    # Calcula o fitness do individuo
    fitness = funcao_de_otimização(num_x, num_y)
    
    # Cria o individuo
    individuo = ind.Individuo(cromossomo_x, cromossomo_y, fitness, num_x, num_y)
    
    return individuo

def plota_grafico_geracional(populacao, ax, geracao_atual):
    
    # Limpa a figura atual
    ax.clear()
    
    x = []
    y = []
    fitness = []
    
    x = [populacao[i].num_x for i in range(len(populacao))]
    y = [populacao[i].num_y for i in range(len(populacao))]
    fitness = [populacao[i].fitness for i in range(len(populacao))]
    
    melhor_individuo = fitness.index(max(fitness))
    
    x_melhor = x.pop(melhor_individuo)
    y_melhor = y.pop(melhor_individuo)
    fitness_melhor = fitness.pop(melhor_individuo)
    
    ax.scatter(x, y, fitness, c=fitness, cmap='viridis')
    ax.scatter(x_melhor, y_melhor, fitness_melhor, c='red', marker='x', s=100)
    
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 20])
    ax.set_zlim([0, 8000])
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness')
    
    # Verifica se a variavel geração atual é um tipo int
    if isinstance(geracao_atual, int):
        ax.set_title(f"Gráfico da geração {geracao_atual+1}")
        plt.draw()
        plt.pause(TEMPO)

        return ax
    else:
        ax.set_title(f"Gráfico da geração {geracao_atual}")
        plt.draw()
        plt.pause(TEMPO+10)
        
        return ax
  
def plota_grafico_ultima_geracao(populacao, ax1):
    
    x = []
    y = []
    fitness = []
    
    x = [populacao[i].num_x for i in range(len(populacao))]
    y = [populacao[i].num_y for i in range(len(populacao))]
    fitness = [populacao[i].fitness for i in range(len(populacao))]
    
    melhor_individuo = fitness.index(max(fitness))
    
    x_melhor = x.pop(melhor_individuo)
    y_melhor = y.pop(melhor_individuo)
    fitness_melhor = fitness.pop(melhor_individuo)
    
    ax1.scatter(x, y, fitness, c=fitness, cmap='viridis')
    ax1.scatter(x_melhor, y_melhor, fitness_melhor, c='red', marker='x', s=100)
    
    ax1.set_xlim([0, 10])
    ax1.set_ylim([0, 20])
    ax1.set_zlim([0, 8000])
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Fitness')
    
    ax1.set_title(f"Gráfico da última geração")

    plt.draw()
  
def plota_grafico_ideal(ax2):

    # Data
    x = np.arange(0, 10, 1)
    y = np.arange(0, 20, 1)

    # Meshgrid
    X, Y = np.meshgrid(x, y)

    # Monta a lista de z
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            z.append(funcao_de_otimização(x[i], y[j]))

    # Converte z para um array numpy e remodela para a mesma forma que X e Y
    Z = np.array(z).reshape(X.shape)
    
    ax2.plot_surface(X, Y, Z, cmap='viridis')
    
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Fitness')
    
    ax2.set_title(f"Gráfico da função de otimização")
    
    plt.draw()
    
def plota_grafico_media(fitness_medio_geracao, melhores_individuos, ax3):
    
    fitness_melhores = []
    for i in range(len(melhores_individuos)):
        fitness_melhores.append(melhores_individuos[i].fitness)
    
    # Gera um grafico de linha com a media do fitness da populacao ao longo das geracoes
    ax3.plot(fitness_medio_geracao, marker='o')
    
    # Mostra o grid
    ax3.grid(True)
    
    ax3.set_title(f"Fitness médio das gerações")
    
    ax3.set_xlabel('Gerações')
    ax3.set_ylabel('Fitness médio')

    # Adiciona uma linha de tendência
    z = np.polyfit(range(len(fitness_medio_geracao)), fitness_medio_geracao, 1)
    p = np.poly1d(z)
    ax3.plot(range(len(fitness_medio_geracao)), p(range(len(fitness_medio_geracao))), "r--")

    # Printa uma outra linha com os melhores individuos
    ax3.plot(fitness_melhores, marker='x')
    
    ax3.legend(['Fitness médio', 'Tendência', 'Melhores individuos'])
    plt.draw()
