from rich.console import Console
from rich.table import Table 

def parametros_iniciais(tamanho_populacao, geracoes, probabilidade_mutacao, probabilidade_cruzamento):

    def printa_parametros_iniciais(tamanho_populacao, geracoes, probabilidade_mutacao, probabilidade_cruzamento):
        console = Console()
        table = Table(title="Parametros Iniciais")
        table.add_column("Tamanho da Populacao", style="cyan", width=70)
        table.add_column("Geracoes", style="cyan", width=70)
        table.add_column("Probabilidade de Mutacao", style="cyan", width=70)
        table.add_column("Probabilidade de Cruzamento", style="cyan", width=70)
        table.add_row(f"{tamanho_populacao}", f"{geracoes}", f"{probabilidade_mutacao}", f"{probabilidade_cruzamento}")
        console.print(table)
    
    
    #tamanho_populacao = 100
    #geracoes = 10

    #probabilidade_mutacao = 0.01
    #probabilidade_cruzamento = 0.7

    # Printa os parametros iniciais
    printa_parametros_iniciais(tamanho_populacao, geracoes, probabilidade_mutacao, probabilidade_cruzamento)

def parametros_cromossomo():
    
    def printa_parametros_cromossomo(cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real):
        console = Console()
        table = Table(title="Parametros Cromossomo")
        table.add_column("Cromossomo Gene Inteiro X", style="cyan", width=70)
        table.add_column("Cromossomo Gene Inteiro Y", style="cyan", width=70)
        table.add_column("Cromossomo Gene Real", style="cyan", width=70)
        table.add_row(f"{cromossomo_gene_inteiro_x}", f"{cromossomo_gene_inteiro_y}", f"{cromossomo_gene_real}")
        console.print(table)
    
    cromossomo_gene_inteiro_x = 4
    cromossomo_gene_inteiro_y = 5
    cromossomo_gene_real = 10
    
    # Printa os parametros do cromossomo
    printa_parametros_cromossomo(cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real)
    
    return cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real
 
def converte_bin_num(num, cromossomo_gene_inteiro):
        
    # A função em si, pega a cadeia binária e converte para número real
    # os 4 primeiros bits são a parte inteira e os 10 ultimos a parte fracionaria
    # por fim ele concatena a parte inteira com a parte fracionaria e retorna o número real
    
    # Separa a cadeia binaria em parte inteira e parte fracionaria
    inteiro_bin = num[:cromossomo_gene_inteiro]
    fracionario_bin = num[cromossomo_gene_inteiro:]
    
    # Converte as duas partes em inteiro
    inteiro = int(''.join(map(str, inteiro_bin)), 2)
    inteiro = str(inteiro)
    
    fracionario = int(''.join(map(str, fracionario_bin)), 2)
    fracionario = str(fracionario)
    
    # Concatena as duas partes e retorna o numero real
    num = inteiro + "." + fracionario
    num = float(num)        
    
    return num
  
def converte_num_bin(num, cromossomo_gene_inteiro, cromossomo_gene_real):

    # Converte um número decimal em sua representação binária, dividindo-o em 
    # parte inteira e parte fracionária.

    # Separa a parte inteira do numero
    inteiro = int(num)

    # Separa a parte real do numero
    real = num - inteiro

    # Converte a parte inteira para binario
    inteira_binaria = bin(inteiro)[2:].zfill(cromossomo_gene_inteiro)

    # Converter parte fracionária para binário (12 bits)
    parte_fracionaria = real
    parte_fracionaria_binaria = ""
    for _ in range(cromossomo_gene_real):
        parte_fracionaria *= 2
        if parte_fracionaria >= 1:
            parte_fracionaria_binaria += "1"
            parte_fracionaria -= 1
        else:
            parte_fracionaria_binaria += "0"

    # Concatena o sinal, a parte inteira e a parte real
    num = inteira_binaria + parte_fracionaria_binaria

    # Normaliza o cromossomo no padrao
    num = list(map(int, num))

    return num
    
def printa_populacao(populacao):
    
    for i in range(len(populacao)):
        populacao[i].print(i)
        
def printa_comparacao(primeira_geracao, ultima_geracao):
    
    # Printa em forma de tabela a primeira geracao e a ultima geração lado a lado, apenas o fitness e o individuo
    console = Console()
    table = Table(title="Primeira Geracao x Ultima Geracao - Fitness")
    table.add_column("Individuo", style="cyan", width=70)
    table.add_column("Primeira Geração", style="cyan", width=70)
    table.add_column("Ultima Geração", style="cyan", width=70)

    # Coloca o primeiro individuo da primeira geracao e da ultima geracao em amarelo na tabela
    table.add_row("1", f"{primeira_geracao[0].fitness}", f"{ultima_geracao[0].fitness}", style="yellow")

    for i in range(1, len(primeira_geracao)):
        table.add_row(f"{i + 1}", f"{primeira_geracao[i].fitness}", f"{ultima_geracao[i].fitness}")
    console.print(table)