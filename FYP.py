import random
import numpy

Population_Size = 8
NoofElite = 1
tournamentSelectionSize = 4
mutation_rate = 0.25
Target_Chromosome = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]

slots = ["1", "2", "3", "4", "5"]
slots1 = []

CS = ["A", "B", "C", "D", "F"]
CS1 = []

EE = ["V", "W", "X", "Y", "Z"]
EE1 = []

BBA = ["J", "K", "L", "M", "N"]
BBA1 = []

LH = ["LH1", "LH2", "LH3"]

chromosomes = []

class Chromosome:
    def __init__(self):
        self._genes = []
        self.collisions = 0
        self.A = []
        self.B = []
        self.C = []
        i = 0
        while i < 5:
            newA = []
            sl = random.choice(slots)
            newA.append(sl)
            slots1.append(sl)
            slots.remove(sl)
            l = random.choice(LH)
            newA.append(l)
            c = random.choice(CS)
            newA.append(c)
            CS1.append(c)
            CS.remove(c)
            # e = random.choice(EE)
            # newA.append(e)
            # EE1.append(e)
            # EE.remove(e)
            # b = random.choice(BBA)
            # newA.append(b)
            # self.A.append(sl, l, c, e, b)

            newB = []

            newB.append(slots[i])
            newB.append(random.choice(EE))
            newB.append(random.choice(LH))
            self.B.append(newB)
            newC = []

            newC.append(slots[i])
            newC.append(random.choice(BBA))
            newC.append(random.choice(LH))
            self.C.append(newC)
            i += 1
        self._genes.append(self.A)
        self._genes.append(self.B)
        self._genes.append(self.C)

    def get_genes(self):
        return self._genes

    def get_fitness(self):
        self.collisions = 0
        for i in range(5):
            if self.A[i][1] == self.B[i][1] == self.C[i][1]:
                self.collisions += 2
            elif (self.A[i][1] == self.B[i][1]) | (self.B[i][1] == self.C[i][1]) | (self.A[i][1] == self.C[i][1]):
                self.collisions += 1

            if self.A[i][2] == self.B[i][2] == self.C[i][2]:
                self.collisions += 2
            elif (self.A[i][2] == self.B[i][2]) | (self.B[i][2] == self.C[i][2]) | (self.A[i][2] == self.C[i][2]):
                self.collisions += 1
        return self.collisions

    def __str__(self):
        return self._genes.__str__()


class Population:
    def __init__(self, size):
        i = 0
        while i < size:
            chromosomes.append(Chromosome())
            i += 1

    def get_chromosomes(self):
        return chromosomes


class GeneticAlgorithm:
    @staticmethod
    def evolve(pop):
        return GeneticAlgorithm._mutate_population(GeneticAlgorithm._crossover_population(pop))

    @staticmethod
    def _crossover_population(pop):
        crossover_pop = Population(0)
        for i in range(NoofElite):
            crossover_pop.get_chromosomes().append(pop.get_chromosomes()[i])
        i = NoofElite;
        while i < Population_Size:
            chromosome1 = GeneticAlgorithm._tournament_population(pop).get_chromosomes()[0]
            chromosome2 = GeneticAlgorithm._tournament_population(pop).get_chromosomes()[0]
            crossover_pop.get_chromosomes().append(GeneticAlgorithm._crossover_chromosome(chromosome1, chromosome2))
            i += 1
        return crossover_pop

    @staticmethod
    def _mutate_population(pop):
        for i in range(NoofElite, Population_Size):
            GeneticAlgorithm._mutate_chromosome(pop.get_chromosomes()[i])
        return pop

    @staticmethod
    def _crossover_chromosome(chromosome1, chromosome2):
        crossover_chrom = Chromosome()
        for i in range(5):
            if random.random() >= 0.5:
                crossover_chrom.get_genes()[i] = chromosome1.get_genes()[i]
            else:
                crossover_chrom.get_genes()[i] = chromosome2.get_genes()[i]
        return crossover_chrom

    @staticmethod
    def _mutate_chromosome(chromosome):
        ''''''

    @staticmethod
    def _tournament_population(pop):
        tournament_pop = Population(0)
        i = 0
        while i < tournamentSelectionSize:
            tournament_pop.get_chromosomes().append(pop.get_chromosomes()[random.randrange(0, Population_Size)])
            i += 1
        tournament_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


def _print_population(pop, gen_number):
    print("\n---------------------------")
    print("Generation #", gen_number, "| Fittest chromosome fitness:", pop.get_chromosomes()[0].get_fitness())
    print("Target Chromosome:", Target_Chromosome)
    print("------------------------------")
    i = 0
    for x in pop.get_chromosomes():
        print("Chromosome #", i, " :", x, "| Fitness: ", x.get_fitness())
        i += 1


'''
population = Population(Population_Size)
population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
_print_population(population, 0)
generation_number = 1;
while population.get_chromosomes()[0].get_fitness() < Target_Chromosome.__len__():
    population = GeneticAlgorithm.evolve(population)
    population.get_chromosomes().sort(key = lambda x: x.get_fitness(), reverse=True)
    _print_population(population, generation_number)
    generation_number += 1


def _print_population(pop, gen_number):
    print("\n-----------------------------")
    print("Generation # ", gen_number, " | Fittest finess: ", pop.get_chromosomes()[0].get_fitness())
    print("-----------------------------------------")
    i = 0
    for x in pop.get_chromosomes():
        print("Chromosome #", i, " :",x," | Fitness: ", x.get_fitness())
        i+=1
population = Population(Population_Size)
population.get_chromosomes().sort(key=lambda x:x.get_fitness(), reverse=False)
_print_population(population, 0)
'''
chromosme = Chromosome()
print(chromosme.A)
print(chromosme.get_genes())
print(chromosme.get_fitness())
