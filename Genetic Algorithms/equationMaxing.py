import numpy as np

inputs = [4, -2, 3.5, 5, -11, -4.7]
num_weights = 6
sol_per_pop = 8
pop_size = (sol_per_pop, num_weights)
new_pop = np.random.uniform(low=-4.0, high=4.0, size=pop_size)

num_gen = 5
num_parents_mating=4


def calFitness(equation_inputs, pop):
    fitness = np.sum(pop*equation_inputs, axis=1)
    return fitness


def selectMatingPool(new_pop, fitness, num_parents_mating):
    parents = []
    fitness_copy = np.copy(fitness)
    for i in range(num_parents_mating):
        index = fitness_copy.argmax()
        parents.append(new_pop[index])
        fitness_copy[index] = -9999999
    return parents


def crossover(parents, offspringSize):
    offspringCrossover = np.copy(parents)
    cross_over_point = int(np.round(offspringSize[1]/2))
    for i in range(offspringSize[0]):
        parent_1_section = parents[i%len(parents)][cross_over_point:]
        parent_2_section = parents[(i+1)%len(parents)][cross_over_point:]
        if sum(parent_1_section) > sum(parent_2_section):
            offspringCrossover[(i+1)%len(parents)][cross_over_point:] = parent_1_section
        elif sum(parent_1_section) < sum(parent_2_section):
            offspringCrossover[i%len(parents)][cross_over_point:] = parent_2_section
        else:
            pass
    return offspringCrossover


def mutation(offSpringMutation):
    mutationPoint = 4
    for i in range(len(offSpringMutation)):
        #mutationPoint = np.random.randint(0, 6)
        mutation = np.random.uniform(-1, 1, size=1)
        offSpringMutation[i][mutationPoint] = offSpringMutation[i][mutationPoint] + mutation
    return offSpringMutation


print("Best randomly generated output is " + str(sum(calFitness(inputs, new_pop))) + ".")
print("Finding best fit weights.")
gen_count = 1
for generation in range(num_gen):
    print("Generation: " + str(gen_count))
    gen_count = gen_count + 1
    fitness = calFitness(inputs, new_pop)
    parents = selectMatingPool(new_pop, fitness, num_parents_mating)
    offSpringCrossover = crossover(parents, offspringSize=(pop_size[0] - len(parents), num_weights))
    offSpringMutation = mutation(offSpringCrossover)
    new_pop[0:int(sol_per_pop/2), :] = parents
    new_pop[int(sol_per_pop/2):, :] = offSpringMutation

print("Final generation is \n" + str(new_pop) + " \n with best pop being " +
      str(new_pop[np.argmax(calFitness(inputs, new_pop))]) + " \n with equation output being " +
      str(sum(calFitness(inputs, new_pop))))