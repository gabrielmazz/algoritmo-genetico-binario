# <p aling="center"> Algoritmo Genético Binário </p>

#### <p aling="center"> Trabalho de Otimização Combinatória, faculdade de Ciência da Computação, Universidade Estadual do Oeste do Paraná - UNIOESTE, campus de Cascavel. </p>

#### <p aling="center"> Desenvolvido por: [Gabriel Mazzuco](https://github.com/gabrielmazz) </p> 

## Indice

- [Descrição do Projeto](#descrição-do-projeto)
    - [O que é um algoritmo genético?](#o-que-é-um-algoritmo-genético)
    - [Como funciona um algoritmo genético?](#como-funciona-um-algoritmo-genético)
    - [Especificação do problema proposto](#especificação-do-problema)
        - [Especificações do problema para a implementação](#especificações-do-problema-para-a-implementação)
- [Como foi implementado](#como-foi-implementado)
    - [Individuo.py](#individuopy)
    - [Funcoes_extras.py](#funcoes_extraspy)
    - [Funcoes_AG.py](#funcoes_agpy)
- [Pré-requisitos](#pré-requisitos)
    - [Requisitos para o projeto](#requisitos-para-o-projeto)
    - [Requisitos mínimos de hardware](#requisitos-mínimos-de-hardware)
- [Como usar](#como-usar)
- [Referências](#referências)

## Descrição do Projeto

### O que é um algoritmo genético?

Algoritmos genéticos são uma técnica de otimização que utiliza conceitos da teoria da evolução de Darwin para encontrar soluções para problemas complexos. Eles são baseados em uma população de indivíduos que representam possíveis soluções para o problema em questão. Cada indivíduo é representado por um cromossomo, que é uma sequência de genes. Os genes são os parâmetros que definem a solução proposta pelo indivíduo.

### Como funciona um algoritmo genético?

O funcionamento de um algoritmo genético pode ser resumido em cinco etapas:

1. **Inicialização**: Uma população inicial de indivíduos é gerada aleatoriamente.
2. **Avaliação**: Cada indivíduo é avaliado de acordo com sua aptidão para resolver o problema em questão.
3. **Seleção**: Indivíduos mais aptos são selecionados para reprodução.
4. **Recombinação**: Os indivíduos selecionados são combinados para gerar novos indivíduos.
5. **Mutação**: Os novos indivíduos sofrem mutações aleatórias para introduzir diversidade na população.

Essas etapas são repetidas por um número fixo de gerações ou até que uma solução satisfatória seja encontrada.

### Especificação do problema

O problema proposto consiste em encontrar a melhor solução, ou seja, o conjunto de indivíduos que alcançam a convergência para o valor ótimo da função de aptidão, conforme as gerações foram passando.

#### Especificações do problema para a implementação

<table align="center">

  <tr>
    <th>Codificação</th>
    <th>Seleção</th>
    <th>Cruzamento</th>
    <th>Mutação</th>
    <th>Elitismo</th>
  </tr>
  <tr>
    <td>Binária</td>
    <td>Ranking</td>
    <td>2 Pontos aleatórios</td>
    <td>Inversão binária</td>
    <td>1 indivíduo por geração</td>

</table>

<div align="center">

  Função de otimização é dada por: 
  
  $$
  Z = x^2 + y^2 + (3x + 4y - 26)^2
  $$
  
  Os valores de x e y possuem restrições que devem ser seguidas:
  
  $x \in [0, 10]$ | $y \in [0, 20]$ 


</div>


- **Codificação binária**: Cada indivíduo é representado por um cromossomo binário. Cada gene do cromossomo pode assumir o valor 0 ou 1, nos cromossomos X, temos 4 bits para parte inteira e 10 bits para parte fracionária, e nos cromossomos Y, temos 5 bits para parte inteira e 9 bits para parte fracionária. No final das contas, geramos um número real quando passamos para a função de otimização
    - Exemplo: 
        - X = [1, 0, 1, 1,| 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
        - Y = [0, 1, 1, 0, 1,| 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]

- **Seleção por ranking**: A seleção dos indivíduos é direta e aleatória, selecionando n indivíduos da população onde todos possuem a mesma chance

- **Cruzamento de 2 pontos aleatórios**: Dois pontos aleatórios são escolhidos nos cromossomos dos pais, e os segmentos entre esses pontos são trocados para gerar os cromossomos dos filhos.

- **Mutação por inversão binária**: Um gene aleatório do cromossomo do indivíduo sofre uma inversão de valor.

- **Elitismo**: Um indivíduo da população é selecionado para ser mantido na próxima geração, garantindo que a melhor solução encontrada até o momento não seja perdida.

## Como foi implementado

A implementação do código foi feita em python, para a execução do programa, na pasta raiz deve ter os arquivos <code>individuo.py</code>; <code>funcoes_extras.py</code> e o mais importante, o <code>funcoes_AG.py</code>.

### Individuo.py

div align="center">
    <p> O arquivo <code>individuo.py</code> é responsável por criar a classe <code>Individuo</code>, que é responsável por criar um indivíduo com as características necessárias para a execução do algoritmo genético. Dentro dele serão armazenados os valores de x e y, o fitness do indivíduo e o seu cromossomo binário </p>
</div>

<div>

```python
class Individuo:
    def __init__(self, x, y, fitness, num_x, num_y):
        self.x = x              # Cromossomo X
        self.num_x = num_x      # Numero do cromossomo X
        self.y = y              # Cromossomo Y
        self.num_y = num_y      # Numero do cromossomo Y
        self.fitness = fitness  # Fitness do individuo
```

</div>

### Funcoes_extras.py

<div align="center">
    <h4><code>funcoes_extras.py</code></h4>
</div>

<div align="center">
    <p> O arquivo <code>funcoes_extras.py</code> é responsável por criar funções que são utilizadas para a execução do algoritmo genético mas que não são diretamente ligadas a ele. Dentro dele definimos o input dos parametro iniciais, como o cromossomo é montado. Também é feito de forma genérica a conversão de binário para decimal e vice-versa que é algo necessário para a execução do algoritmo genético binário. </p>
</div>

<div>

```python
tamanho_populacao = int(input("Digite o tamanho da populacao: "))
geracoes = int(input("Digite o numero de geracoes: "))
probabilidade_mutacao = float(input("Digite a probabilidade de mutacao: "))
probabilidade_cruzamento = float(input("Digite a probabilidade de cruzamento: "))
```

<br>

```python	
cromossomo_gene_inteiro_x = 4
cromossomo_gene_inteiro_y = 5
cromossomo_gene_real = 10
```

<br>

```python
# Converte a cadeia binária em sua representação decimal, dividindo-a em parte inteira e parte fracionária.
def converte_bin_num(num, cromossomo_gene_inteiro):
```

<br>

```python
# Converte um número decimal em sua representação binária, dividindo-o em parte inteira e parte fracionária.
def converte_num_bin(num, cromossomo_gene_inteiro, cromossomo_gene_real)
```

</div>

### Funcoes_AG.py

<div align="center">
    <h4><code>funcoes_AG.py</code></h4>
</div>

<div align="center">
    <p> O arquivo <code>funcoes_AG.py</code> é responsável por criar as funções que são utilizadas de fato no algoritmo genético. Dentro dele definimos as funções de otimização, seleção, cruzamento, mutação e elitismo. Além disto, é gerado os indivíduos que serão adicionados a população </p>
</div>

<div>

```python
def funcao_de_otimização(x, y):
    z = (math.pow(x, 2)) + (math.pow(y, 2)) + (math.pow((3*x) + (4*y) - 26, 2))
    return z
```

<br>

```python
def gera_individuo(cromossomo_gene_inteiro_x, cromossomo_gene_inteiro_y, cromossomo_gene_real):

    # Gera um cromossomo X -> Cadeia binaria de bits de tamanho cromossomo_gene_inteiro_x
    cromossomo_x = random.choices([0, 1], k=cromossomo_gene_inteiro_x + cromossomo_gene_real)

    # Gera um cromossomo Y -> Cadeia binaria de bits de tamanho cromossomo_gene_inteiro_y
    cromossomo_y = random.choices([0, 1], k=cromossomo_gene_inteiro_y + cromossomo_gene_real)
```

<br>

```python
# Função aonde é determinado o melhor individuo da população
def eletista(populacao):
```

<br>

```python
# A seleção é por ranking, ou seja a probabilidade de seleção é direta e aleatória
# seleciona-se n indivíduos onde todos têm a mesma chance de serem selecionados
def seleciona_pais_ranking(populacao):
```

<br>

```python	
# Função de cruzamento de 2 pontos aleatórios, aonde é feito a troca de genes entre os pais
# separando o cromossomo em 3 partes e trocando a parte do meio
def crossover(pai1, pai2, probabilidade_cruzamento, tam_cromossomo_x, tam_cromossomo_y):
    # Cria os filhos
    filho1_x = parte1_x_pai1 + parte2_x_pai2 + parte3_x_pai1
    filho1_y = parte1_y_pai1 + parte2_y_pai2 + parte3_y_pai1
    
    filho2_x = parte1_x_pai2 + parte2_x_pai1 + parte3_x_pai2
    filho2_y = parte1_y_pai2 + parte2_y_pai1 + parte3_y_pai2
```

<br>

```python	
# Passa por todos os genes do filho e faz a mutacao de acordo com a probabilidade
# se for menor que a probabilidade de mutacao, ele muda o gene trocando de 0 para 1 e vice-versa
def mutacao(filho1_x, filho1_y, filho2_x, filho2_y, probabilidade_mutacao):
```

</div>



## Pré-requisitos

### Requisitos para o projeto

Para executar o projeto, você precisará ter instalado em sua máquina as seguintes ferramentas:

- [Python](https://www.python.org/downloads/), versão 3.8 ou superior
    - 'sudo apt-get install python3.8'

- [Rich](https://pypi.org/project/rich/), versão 10.6.0 ou superior
    - 'pip install rich'

- [Matplotlib](https://matplotlib.org/), versão 3.4.3 ou superior
    - 'pip install matplotlib'

### Requisitos mínimos de hardware

- **Sistema operacional**: Windows 10 ou superior com WSL, Linux
- **Processador**: Intel Core dual-core ou superior
- **Memória RAM**: 4 GB ou superior
- **Espaço em disco**: 1 GB ou superior

## Como usar

1. Clone o repositório
    - 'git clone
2. Acesse a pasta do projeto
    - 'cd algoritmo-genetico'
3. Execute o arquivo principal
    - 'python3 main.py' ou abra o arquivo algoritmo-genetico.ipynb no Jupyter Notebook
4. Determine os parâmetros iniciais do algoritmo genético
    - 'Digite o número de gerações: '
    - 'Digite o tamanho da população: '
    - 'Digite a taxa de mutação: '
    - 'Digite o número de indivíduos selecionados para reprodução: '
5. Aguarde a execução do algoritmo genético
6. Visualize os resultados obtidos
    - Será exibido 3 gráficos:
        - Gráfico de dispersão com a população final
        - Gráfico ideal para a função de otimização
        - Gráfico do fitness médio da população por geração


## Referências

- [Algoritmo Genético: Princípios e Aplicações](https://www.inf.ufsc.br/~mauro.roisenberg/ine5377/Cursos-ICA/CE-intro_apost.pdf)
- [Algoritmo genético](https://pt.wikipedia.org/wiki/Algoritmo_genético)
- [OpenAI. (2024). GPT-3.5: Modelo de Linguagem Pré-Treinado](https://openai.com/blog/chatgpt)
- [OpenAI e GitHub. (2024). GitHub Copilot: Ferramenta de Autocompletar de Código](https://copilot.github.com/)