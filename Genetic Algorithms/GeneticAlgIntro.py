import numpy as np

def rand():
    genes = []
    for i in range(5):
        if np.random.random_integers(1000) % 6 == 0:
            genes.append(1)
        else:
            genes.append(0)
    return genes


class Population():
    population_size = 10
    individuals = []
    fittest = 0

    def __init__(self):
        for pop in range(self.population_size):
            self.individuals.append(rand())

    def print(self):
        for pop in range(len(self.individuals)):
            print(self.individuals[pop])

    def get_fittest(self):
        maxFitIndex = 0
        for individual in range(len(self.individuals)):
            if sum(self.individuals[maxFitIndex]) < sum(self.individuals[individual]):
                maxFitIndex = individual
        return self.individuals[maxFitIndex], maxFitIndex

    def get_second_fittest(self):
        maxFitIndex = 0
        secondFitIndex = 0
        for individual in range(len(self.individuals)):
            if sum(self.individuals[maxFitIndex]) < sum(self.individuals[individual]):
                secondFitIndex = maxFitIndex
                maxFitIndex = individual
            elif sum(self.individuals[secondFitIndex]) < sum(self.individuals[individual]):
                secondFitIndex = individual
        return self.individuals[secondFitIndex], secondFitIndex

    def append(self, chromosome):
        self.individuals.append(chromosome)

    def selection(self):
        first, firstIndex = self.get_fittest()
        second, secondIndex = self.get_second_fittest()
        return first, second, firstIndex, secondIndex

    def nextGeneration(self):
        split = np.random.randint(0,4)
        first, second, firstIndex, secondIndex = self.selection()
        firstborn = first.copy()
        secondborn = second.copy()
        for gene in range(5):
            if gene < split:
                pass
            elif gene >= split:
                hold = firstborn[gene]
                firstborn[gene] = secondborn[gene]
                secondborn[gene] = hold

        point = np.random.randint(0,5)
        if firstborn[point] == 0:
            firstborn[point] = 1
        elif firstborn[point] == 1:
            firstborn[point] = 0

        point = np.random.randint(0,5)
        if secondborn[point] == 0:
            secondborn[point] = 1
        elif secondborn[point] == 1:
            secondborn[point] = 0
        self.individuals.append(firstborn)
        self.individuals.append(secondborn)


europe = Population()
print(europe.get_fittest())
generation = 0
while sum(europe.get_fittest()[0]) != 5:
    generation = generation + 1
    print("Generation: " + str(generation))
    europe.nextGeneration()
print("Gene achieved after " + str(generation) + " generations with " + str(europe.get_fittest()) + " being the final chromosome.")

