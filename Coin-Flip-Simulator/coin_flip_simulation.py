from random import randint
import numpy as np
from matplotlib.pyplot import figure,plot,bar,show


class Coin:
    diez = 10

    def __init__(self):
        self.dinero = 0
        self.lanzamientos = 1000
        self.acumulado = np.zeros(self.lanzamientos)
        self.ocurrencias = ['' for i in range(self.lanzamientos)]

    def coin_flip(self):
        return ['Cara','Cruz'][randint(0,1)]

    def jugar_un_juego(self, num_de_lanzamientos):
        for i in range(num_de_lanzamientos):
            resultado = self.coin_flip()
            if i < 1:
                if resultado == 'Cara':
                    self.ocurrencias[i] = 'Cara'
                    self.acumulado[i] += 1
                else:
                    self.ocurrencias[i] = 'Cruz'
                    self.acumulado[i] -= 1
            else:
                if resultado == 'Cara':
                    self.ocurrencias[i] = 'Cara'
                    self.acumulado[i] = self.acumulado[i-1] + 1
                else:
                    self.ocurrencias[i] = 'Cruz'
                    self.acumulado[i] = self.acumulado[i-1] - 1
        return self.acumulado

    def distribucion_cara_cruz(self):
        '''Regresa (numero de caras, numero de cruces)'''
        caras = self.ocurrencias.count('Cara')
        cruces = self.ocurrencias.count('Cruz')
        return caras,cruces

    def resultados_de_juegos():
        #Cómo se comportan los resultados finales? Distribucion normal maybe
        return None


    def graficas_simulacion(self):
        figure()
        plot(self.acumulado)
        figure()
        bar(['Caras','Cruces'], self.distribucion_cara_cruz())
        show()
