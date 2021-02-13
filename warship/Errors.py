class GameError(Exception):
    """Base class for exceptions in this module."""
    pass

class ShipSizeError(GameError):
    MSG = "Длина корабля не соответствует условиям, корабль не построен"

class ShipDirectionError(GameError):
    MSG = "Значение должно иметь тип boolean, корабль не построен"
