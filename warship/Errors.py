class GameError(Exception):
    pass

class ShipSizeError(GameError):
    MSG = "Длина корабля не соответствует условиям, корабль не построен"

class ShipDirectionError(GameError):
    MSG = "Значение должно иметь тип boolean, корабль не построен"
