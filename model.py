import gym
from gym import spaces
from gym.spaces import Discrete, Box
from stable_baselines3 import PPO
import random
import numpy as np


class MyEnv(gym.Env):

    metadata = {'render.modes': ['console']}
    # Definimos las constantes
    POSICION0 = 0
    POSICION1 = 1
    POSICION2 = 2
    POSICION3 = 3
    POSICION4 = 4
    POSICION5 = 5
    POSICION6 = 6
    POSICION7 = 7
    POSICION8 = 8

    def __init__(self):
        # Actions we can take, down, stay, up
        self.JUGADO0 = False
        self.JUGADO1 = False
        self.JUGADO2 = False
        self.JUGADO3 = False
        self.JUGADO4 = False
        self.JUGADO5 = False
        self.JUGADO6 = False
        self.JUGADO7 = False
        self.JUGADO8 = False
        self.lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.action_space = Discrete(9)
        # Temperature array
        self.observation_space = Box(low=np.zeros(9), high=np.ones(9))
        # Set start temp
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def reset(self):
        """
        Importante: la observación devuelta debe ser un array de numpy
        :return: (np.array) 
        """
        self.JUGADO0 = False
        self.JUGADO1 = False
        self.JUGADO2 = False
        self.JUGADO3 = False
        self.JUGADO4 = False
        self.JUGADO5 = False
        self.JUGADO6 = False
        self.JUGADO7 = False
        self.JUGADO8 = False
        self.state = np.zeros(9)
        # Se inicializa el agente a la derecha de la grilla
        #self.agent_pos = self.grid_size - 1
        # convertimos con astype a float32 (numpy) para hacer más general el agente
        # (en caso de que querramos usar acciones continuas)
        return np.array([self.state]).astype(np.float32)

    def jugar_random(self):
        # self.render()
        # for index in rng.integers(low=0, high=9, size=100):
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(indices)
        indices
        for index in indices:
            if self.state[index] == 0:
                self.state[index] = 2
                if index == 0:
                    self.JUGADO0 == True
                if index == 1:
                    self.JUGADO1 == True
                if index == 2:
                    self.JUGADO2 == True
                if index == 3:
                    self.JUGADO3 == True
                if index == 4:
                    self.JUGADO4 == True
                if index == 5:
                    self.JUGADO5 == True
                if index == 6:
                    self.JUGADO6 == True
                if index == 7:
                    self.JUGADO7 == True
                if index == 8:
                    self.JUGADO8 == True

                break

    def step(self, action):
        reward = 0
        if action == 0 and self.state[0] == 2 and self.JUGADO0 == False:
            self.JUGADO0 == True
            reward = reward-100
        if action == 1 and self.state[1] == 2 and self.JUGADO1 == False:
            self.JUGADO1 == True
            reward = reward-100
        if action == 2 and self.state[2] == 2 and self.JUGADO2 == False:
            self.JUGADO2 == True
            reward = reward-100
        if action == 3 and self.state[3] == 2 and self.JUGADO3 == False:
            self.JUGADO3 == True
            reward = reward-100
        if action == 4 and self.state[4] == 2 and self.JUGADO4 == False:
            self.JUGADO4 == True
            reward = reward-100
        if action == 5 and self.state[5] == 2 and self.JUGADO5 == False:
            self.JUGADO5 == True
            reward = reward-100
        if action == 6 and self.state[6] == 2 and self.JUGADO6 == False:
            self.JUGADO6 == True
            reward = reward-100
        if action == 7 and self.state[7] == 2 and self.JUGADO7 == False:
            self.JUGADO7 == True
            reward = reward-100
        if action == 8 and self.state[8] == 2 and self.JUGADO8 == False:
            self.JUGADO8 == True
            reward = reward-100

        if action == self.POSICION0 and self.state[0] == 0 and self.JUGADO0 == False:
            self.state[0] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO0 = True
        if action == self.POSICION1 and self.state[1] == 0 and self.JUGADO1 == False:
            self.state[1] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO1 = True
        if action == self.POSICION2 and self.state[2] == 0 and self.JUGADO2 == False:
            self.state[2] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO2 = True
        if action == self.POSICION3 and self.state[3] == 0 and self.JUGADO3 == False:
            self.state[3] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO3 = True
        if action == self.POSICION4 and self.state[4] == 0 and self.JUGADO4 == False:
            self.state[4] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO4 = True
        if action == self.POSICION5 and self.state[5] == 0 and self.JUGADO5 == False:
            self.state[5] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO5 = True
        if action == self.POSICION6 and self.state[6] == 0 and self.JUGADO6 == False:
            self.state[6] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO6 = True
        if action == self.POSICION7 and self.state[7] == 0 and self.JUGADO7 == False:
            self.state[7] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO7 = True
        if action == self.POSICION8 and self.state[8] == 0 and self.JUGADO8 == False:
            self.state[8] = 1
            if not self.check_win():
                self.jugar_random()
            self.JUGADO8 = True
        else:
            pass
            #raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        # Evitamos que el agente se salga de los límites de la grilla
        #self.agent_pos = np.clip(self.agent_pos, 0, self.grid_size)

        if self.JUGADO0 and action == 0:
            reward = reward-100
        if self.JUGADO1 and action == 1:
            reward = reward-100
        if self.JUGADO2 and action == 2:
            reward = reward-100
        if self.JUGADO3 and action == 3:
            reward = reward-100
        if self.JUGADO4 and action == 4:
            reward = reward-100
        if self.JUGADO5 and action == 5:
            reward = reward-100
        if self.JUGADO6 and action == 6:
            reward = reward-100
        if self.JUGADO7 and action == 7:
            reward = reward-100
        if self.JUGADO8 and action == 8:
            reward = reward-100
        # Asignamos recompensa sólo cuando el agente llega a su objetivo
        # (recompensa = 0 en todos los demás estados)
        if self.check_win():
            reward = 1000
            done = True
        else:
            pass

        if self.check_lose():
            reward = -100
            done = True
        else:
            pass

        if self.check_draw():
            reward = -100
            done = True
        else:
            pass

        if self.check_win() or self.check_win() or self.check_draw():
            done = True
        else:
            done = False

        # gym también nos permite devolver información adicional, ej. en atari:
        # las vidas restantes del agente (no usaremos esto por ahora)
        info = {}

        return np.array([self.state]).astype(np.float32), reward, done, info

    def check_win(self):
        # filas
        if self.state[0] == 1 and self.state[1] == 1 and self.state[2] == 1:
            return True
        if self.state[3] == 1 and self.state[4] == 1 and self.state[5] == 1:
            return True
        if self.state[6] == 1 and self.state[7] == 1 and self.state[8] == 1:
            return True
        # columnas
        if self.state[0] == 1 and self.state[3] == 1 and self.state[6] == 1:
            return True
        if self.state[1] == 1 and self.state[4] == 1 and self.state[7] == 1:
            return True
        if self.state[2] == 1 and self.state[5] == 1 and self.state[8] == 1:
            return True
        # diagonal
        if self.state[0] == 1 and self.state[4] == 1 and self.state[8] == 1:
            return True
        if self.state[2] == 1 and self.state[4] == 1 and self.state[6] == 1:
            return True
        else:
            return False

    def check_lose(self):
        # filas
        if self.state[0] == 2 and self.state[1] == 2 and self.state[2] == 2:
            return True
        if self.state[3] == 2 and self.state[4] == 2 and self.state[5] == 2:
            return True
        if self.state[6] == 2 and self.state[7] == 2 and self.state[8] == 2:
            return True
        # columnas
        if self.state[0] == 2 and self.state[3] == 2 and self.state[6] == 2:
            return True
        if self.state[1] == 2 and self.state[4] == 2 and self.state[7] == 2:
            return True
        if self.state[2] == 2 and self.state[5] == 2 and self.state[8] == 2:
            return True
        # diagonal
        if self.state[0] == 2 and self.state[4] == 2 and self.state[8] == 2:
            return True
        if self.state[2] == 2 and self.state[4] == 2 and self.state[6] == 2:
            return True
        else:
            return False

    def check_draw(self):
        draw = False
        contador = 0
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if self.state[i] != 0:
                contador += 1

        if contador == 9:
            draw = True

        return draw

    def render(self, mode='console'):
        if mode != 'console':
            raise NotImplementedError()
        # en nuestra interfaz de consola, representamos el agente como una cruz, y
        # el resto como un punto
        for i in range(0, 9, 3):
            if i == 0:
                print(f"{self.state[i]} {self.state[i+1]} {self.state[i+2]} ")
            if i == 3:
                print(f"{self.state[i]} {self.state[i+1]} {self.state[i+2]} ")
            if i == 6:
                print(f"{self.state[i]} {self.state[i+1]} {self.state[i+2]} ")

    def close(self):
        pass


board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


def jugarCpu(board):
    model = PPO.load("model5millones")

    env = MyEnv()
    obs = board.flatten()

    fila = 0
    columna = 0
    repetido = True
    while repetido:
        action, _states = model.predict(obs)

        if action == 0:
            fila, columna = 0, 0
        if action == 1:
            fila, columna = 0, 1
        if action == 2:
            fila, columna = 0, 2
        if action == 3:
            fila, columna = 1, 0
        if action == 4:
            fila, columna = 1, 1
        if action == 5:
            fila, columna = 1, 2
        if action == 6:
            fila, columna = 2, 0
        if action == 7:
            fila, columna = 2, 1
        if action == 8:
            fila, columna = 2, 2

        if board[fila][columna] == 0:
            repetido = False

    return fila, columna


fila, columa = jugarCpu(board)
print(fila, columa)
