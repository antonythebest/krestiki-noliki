from Errors import ShipSizeError,ShipDirectionError

class Ship:
    __size = None
    __direction = None

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        try:
            if(int(value) > 4 or int(value)< 0):
                raise ShipSizeError(ShipSizeError.MSG)
            else:
                self.__size = value
        except ValueError as e:
           if isinstance(e,ValueError) == True:
               print('Введенное значение не соответствует требуемому типу данных')


    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, value):
        if isinstance(value,bool) == True:
            self.__direction = value
        else:
            raise ShipDirectionError(ShipDirectionError.MSG)



    def __init__(self, s, d):
        self.size = s
        self.direction = d


    def print_ship_info(self):
        print('длина корабля = ', self.size)
        print('расположен горизонтально = ', self.direction)
       # print('расположен вертикально = ',self.direction)

    @classmethod
    def test_create_ship(self,size,direction):
        try:
            test_ship = Ship(size,direction)
        except Exception as e:
            print(e)

Ship.test_create_ship(6,'f')



