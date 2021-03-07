import random
# import numpy as np

# Number of Individual in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '''

# Target string to be generated
TARGET = "Rudrakshya Barman"


class Individual(object):

    # Class representing individual in population
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        ''' create random gene for mutation '''
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):
        ''' create chromosome '''
        global TARGET
        gnome_length = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_length)]

    def mate(self, parent2):
        '''
        Perform mateing and produce new offspring
        '''

        # Chromosome for offspring

        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, parent2.chromosome):
            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)

    def cal_fitness(self):
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt:
                fitness += 1
        return fitness


def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # Create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        # print(gnome)
        population.append(Individual(gnome))

    # p = np.array(population)
    # print(p)

    while not found:

        # sort the population
        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness <= 0:
            found = True
            break

        new_generation = []

        s = int((90 * POPULATION_SIZE) / 100)

        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            # print(child)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\t String: {}\t Fitness: {}". \
              format(generation, "".join(population[0].chromosome),
                     population[0].fitness))

        generation += 1

    print("Generation: {}\t String: {}\t Fitness: {}". \
          format(generation, "".join(population[0].chromosome),
                 population[0].fitness))


if __name__ == '__main__':
    main()
