from state import CellState
class Board:
    list_of_state = None
    size = None
    hidden = None
    cout_of_ships = None

    def __init__(self,size=6,hidden=False,count_of_ships=4):
        self.size = size
        self.hidden = hidden
        self.count_of_ships = count_of_ships
        self.list_of_state = [[CellState.MASK for j in range(6)] for i in range(6)]




    def show_board(self):
        print("\033[34m")
        print(' ',' 0',' 1',' 2','3',' 4','5')
        i=-1
        for row in self.list_of_state:
            i=i+1
            print("\033[34m",i,end = ' ' )
            for elem in row:
                print("\033[33m{}".format(elem),end = ' ')
            print()

board = Board()
board.show_board()



# создадим класс собаки
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
# т.к. метод помечен декоратором property, то нам не надо вызывать этот метод чтобы получить результат
print(jane.human_age)