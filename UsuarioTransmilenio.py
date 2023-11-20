# Importando las librerías necesarias para la simulación basada en agentes
import random

# Clase para los Usuarios de Transmilenio
class UsuarioTransmilenio:
    def __init__(self, nivel_socioeconomico, percepcion_servicio):
        self.nivel_socioeconomico = nivel_socioeconomico
        self.percepcion_servicio = percepcion_servicio
        self.probabilidad_evasion = self.calcular_probabilidad_evasion()

    def calcular_probabilidad_evasion(self):
        # La probabilidad de evasión podría basarse en el nivel socioeconómico y la percepción del servicio
        base_probabilidad = {'bajo': 0.3, 'medio': 0.1, 'alto': 0.05}
        ajuste_percepcion = -0.05 if self.percepcion_servicio == 'positiva' else 0.05
        return base_probabilidad[self.nivel_socioeconomico] + ajuste_percepcion

    def decidir_evasion(self):
        # El usuario decide evadir o no basado en su probabilidad de evasión
        return random.random() < self.probabilidad_evasion