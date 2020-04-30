# criando uma função utilizando decoradores para saber a velocidade da instrução.

from time import time


def run(funcao):
    '''criamos uma f interna'''

    def interna(*args, **kwargs):
        '''essa f. interna utiliza o tempo atual
        depois recebe os argumentos que vão ser
        gerados, utiliza
        o tempo final, e por último calcula
        o tempo que levou para ser gerada.
            '''
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000

        print(f'\n a funcao {funcao.__name__} levou {tempo:.2f} ms')

        return resultado

    return interna

@run
def demora():
    for i in pass:
        print(i, end='')
