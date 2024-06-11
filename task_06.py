
class RPS_Exception(Exception):


    def __init__(self, *args):
        self.massage = args[0] if args else None

    def __str__(self):
        return f'RPS_Exception: {self.massage}'


class WrongNumberOfPlayersError(RPS_Exception):


    def __str__(self):
        return f'WrongNumberOfPlayersError: {self.massage}'



class NoSuchStrategyError(RPS_Exception):


    def __str__(self):
        return f'NoSuchStrategyError: {self.massage}'




def rps_game_winner(array):

    possible_options = {'R' : 'S',
                        'S' : 'P',
                        'P' : 'R'}

    if not isinstance(array, list) or not all(isinstance(elem, list) for elem in array):
        raise TypeError \
            ('Неверный формат данных, на вход принимается массив следующей структуры: [ ["player1", "P"], ["player2", "S"] ]')
    if len(array) > 2:
        raise WrongNumberOfPlayersError('Допустимо участие только двух игроков')
    if not array[0][1] in possible_options or not array[1][1] in possible_options:
        raise NoSuchStrategyError("Допустимые варианты хода: 'P' - бумага, 'S' - ножницы, 'R' - камень")

    tour =  dict(array)

    if len(set(tour.values())) == 1:
        return ' '.join(array[0])

    for P1 ,P2 in possible_options.items():
        if [P1, P2] == list(tour.values()):
            return ' '.join(array[0])

    return ' '.join(array[1])



