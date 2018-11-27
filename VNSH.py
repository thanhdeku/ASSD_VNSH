import random
import sys

import LocalSearch
from Block import Block

class VNSH(object):
    def computeTardy(self, block_list):
        fitness = 0
        for i in range(len(block_list)):
            block = block_list[i]
            for j in range(len(block)):
                sensor = block[j]
                fitness += max(0, block.start_time + sensor.process_time - sensor.due_date)
        return fitness

    def localSearch(self, solution):
        max = 10
        solution_VNSH = solution
        solution_T = solution
        m = 0
        fitness = self.computeTardy(solution)
        while m < max:
            options = {0: LocalSearch.swapS,
                       1: LocalSearch.shilfS,
                       2: LocalSearch.swapB,
                       3: LocalSearch.swapB,
                       4: LocalSearch.combineB,
                       5: LocalSearch.breakdownB}
            i = random.randint(6)
            back_up = []
            for i in range(solution):
                block = Block(solution[i].sensor_list, solution[i].start_time)
                back_up.append(block)
            if i < 5 :
                i1 = random.randint(len(solution))
                i2 = random.randint(len(solution))
                if i1 is not i2:
                    i2 = random.randint(len(solution))
                options[i](solution,i1,i2)
            elif i is 5:
                i = random.randint(len(solution))
                options[5](solution,i)
            else:
                print("invalid i")
            newFitness = self.computeTardy(solution)
            if   newFitness < fitness:
                solution_VNSH = solution
                fitness = newFitness
                m = 0
            else:
                solution_T = solution_VNSH
                m += 1
















