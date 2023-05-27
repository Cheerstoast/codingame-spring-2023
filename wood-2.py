import sys
import math
class Cell():
    @property
    def neighbors(self):
        return [self.n0,self.n1,self.n2,self.n3,self.n4,self.n5]

    def __init__(self,id,cell_type,initial_resources,n0,n1,n2,n3,n4,n5):
        self.id = id
        self.cell_type = cell_type
        self.resources = initial_resources
        self.n0 = n0
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        # other
        self.my_ants = 0
        self.opp_ants = 0
my_bases = []
opp_bases = []
class Matrix():
    def get_my_ants(self):
        ants = 0
        for i in self.stuff:
            ants += i.my_ants
        return ants

    def __init__(self,*information):
        if len(information)==1:
            information = information[0]
        self.stuff = []
        for index,information_of_cell in enumerate(information):
            self.stuff.append(Cell(index,information_of_cell[0],information_of_cell[1],information_of_cell[2],information_of_cell[3],information_of_cell[4],information_of_cell[5],information_of_cell[6],information_of_cell[7]))
    def get(self,id):
        for cell in self.stuff:
            if cell.id == id:
                return cell
    def distance(self,id1,id2):
        queue = [(self.get(id1), 0)]
        visited = set()
        while queue:
            # Dequeue the first cell and its distance
            cell, dist = queue.pop(0)
            # If the cell is the target cell, return the distance
            if cell.id == id2:
                return dist
            # If the cell has not been visited, mark it as visited and enqueue its neighbors with their distances
            if cell.id not in visited:
                visited.add(cell.id)
                for i in range(6):
                    # Get the neighbor at index i
                    neighbor = self.get(cell.neighbors[i])
                    # If the neighbor exists and is not None, enqueue it with its distance (dist + 1)
                    if neighbor and neighbor != "None":
                        queue.append((neighbor, dist + 1))
        # If the target cell is not found, return -1
        return -1
    def cell_score(self,id):
        return self.get(id).resources / (self.distance(my_bases[0],id)+2)

    def best_cells(self):
        scores = []
        for cell in self.stuff:
            scores.append(self.cell_score(cell.id))
        sorted_list = sorted(scores, reverse=True)
        return [scores.index(sorted_list[i]) for i in range(3)]

information = []

number_of_cells = int(input())
for i in range(number_of_cells):
    information.append(list(int(j) for j in input().split()))


MATRIX = Matrix(information)

number_of_bases = int(input())
for i in input().split():
    my_bases.append(int(i))
for i in input().split():
    opp_bases.append(int(i))



def move(id):
    print(f'LINE {my_bases[0]} {id} {7}')
def test(id):
    print(f'BEACON {id} {1}')


doing = None
while True:
    candidates = MATRIX.best_cells()

    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell

        resources, my_ants, opp_ants = [int(j) for j in input().split()]

        if i in candidates and resources <3:
            candidates.remove(i)
        MATRIX.get(i).resources = resources
        MATRIX.get(i).my_ants = my_ants
        MATRIX.get(i).opp_ants = opp_ants
        
            
    # WAIT
    # LINE <sourceIdx> <targetIdx> <strength>
    # BEACON <cellIdx> <strength>
    # MESSAGE <text>
    if doing and MATRIX.get(doing).resources < 5:
        doing = None
    if doing:
        if MATRIX.get(doing).my_ants > 7:
            print('WAIT')
        else:
            move(doing)
    elif candidates:
        for i in range(len(candidates)):
            if i == 0:
                doing = candidates[i]
                move(candidates[i])
    else:
        print('WAIT')
