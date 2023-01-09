from avancado.Filme import Filme
from avancado.Serie import Serie

vingadores = Filme('vingadores - gerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes}: {programa.likes}')