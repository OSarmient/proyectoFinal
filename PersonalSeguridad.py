# Importando las librerías necesarias para la simulación basada en agentes
import random

# Clase para el Personal de Seguridad de Transmilenio
class PersonalSeguridad:
    def __init__(self, efectividad):
        self.efectividad = efectividad

    def detectar_evasion(self, usuario):
        # Determinar si el personal de seguridad detecta la evasión
        return random.random() < self.efectividad