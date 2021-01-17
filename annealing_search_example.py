import random
import math



def annealing_search(initial_state):
    initial_temp = 100
    final_temp = 0.0
    decrease = 0.50

    current_temp = initial_temp
    solution = initial_state

    while current_temp > final_temp:
        neighbors = get_neighbors(solution)
        cost_diff = get_cost(neighbors) - get_cost(solution)
        if cost_diff > 0:
            solution = neighbors
        else:
            if random.uniform(0, 1) < math.exp(cost_diff / current_temp):
                solution = neighbors
        current_temp -= decrease
    return solution


def get_cost(neighbors):
    x1 = neighbors[0]
    x2 = neighbors[1]
    fx = (math.sin(x1 - x2 / 8) ** 2 + math.sin(x2 + x1 / 8) ** 2) / (math.sqrt((x1 - 8.6998) ** 2 + (x2 - 6.7665) ** 2) + 1)
    return fx

def get_neighbors(state):
    x1_x2_binary = decimalToBinary(state[0]),decimalToBinary(state[1])
    neighbors = create_neighbors(x1_x2_binary)
    chose_int = random.randint(0,len(neighbors)-1)
    chosen = neighbors[chose_int]
    cur_state = binaryToDecimal(chosen[0]),binaryToDecimal(chosen[1])
    return cur_state

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def binaryToDecimal(n):
    return int(n,2)

def create_neighbors(binary_value):
    neighbors_list = flipper(binary_value)
    return neighbors_list

def flipper(binary_value):
    count = 0
    neighbors_list = []
    x1_string = str(binary_value[0])
    x2_string = str(binary_value[1])
    x1_x2_string = (x1_string, x2_string)
    for i in x1_x2_string:
        count += 1
        for j in range(len(i)):
            if i[j] == "1":
                cem = list(i)
                cem.pop(j)
                cem.insert(j,"0")
                listToStr = ''.join([str(elem) for elem in cem])
                if count == 1:
                    neighbors_list.append((listToStr,binary_value[1]))
                elif count == 2:
                    neighbors_list.append((binary_value[0], listToStr))
            else:
                cem = list(i)
                cem.pop(j)
                cem.insert(j, "1")
                listToStr = ''.join([str(elem) for elem in cem])
                if count == 1:
                    neighbors_list.append((listToStr, binary_value[1]))
                elif count == 2:
                    neighbors_list.append((binary_value[0], listToStr))
    return neighbors_list


def main():


    x1 = random.randint(0,64)
    x2 = random.randint(0,64)
    fx = (math.sin(x1 - x2 / 8) ** 2 + math.sin(x2 + x1 / 8) ** 2) / (math.sqrt((x1 - 8.6998) ** 2 + (x2 - 6.7665) ** 2) + 1)

    print(fx)
    solution = annealing_search((x1,x2))
    print(solution)
    print(get_cost(solution))

if __name__ == '__main__':
    main()