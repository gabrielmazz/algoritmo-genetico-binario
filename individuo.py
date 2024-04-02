from rich.console import Console
from rich.table import Table 

# Individuo que sera utilizado no algoritmo genetico, criando um cromossomo X, um Y e um fitness
class Individuo:
    def __init__(self, x, y, fitness, num_x, num_y):
        self.x = x              # Cromossomo X
        self.num_x = num_x      # Numero do cromossomo X
        self.y = y              # Cromossomo Y
        self.num_y = num_y      # Numero do cromossomo Y
        self.fitness = fitness  # Fitness do individuo
        
    def print(self, i):
        console = Console()
        table = Table(title="Individuo {}" .format(i))
        table.add_column("X",style="cyan", width=70)
        table.add_column("Y", style="cyan", width=70)
        table.add_column("Fitness", style="cyan", width=40)
        table.add_row(f"{self.num_x} -> {self.x}", f"{self.num_y} -> {self.y}", f"{self.fitness}")
        console.print(table)
        
    def print_eleito(self):
        console = Console()
        table = Table(title="Individuo Eleito")
        table.add_column("X",style="yellow", width=70)
        table.add_column("Y", style="yellow", width=70)
        table.add_column("Fitness", style="yellow", width=40)
        table.add_row(f"{self.num_x} -> {self.x}", f"{self.num_y} -> {self.y}", f"{self.fitness}")
        console.print(table)
        
    def printa_terminal_eleito(self):
        print("Individuo eleito:")
        print("X: ", self.x)
        print("Y: ", self.y)
        print("Fitness: ", self.fitness)