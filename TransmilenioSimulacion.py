from PersonalSeguridad import PersonalSeguridad
from SistemaTransmilenio import SistemaTransmilenio
from UsuarioTransmilenio import UsuarioTransmilenio
import simpy
import random
import pandas as pd
import matplotlib.pyplot as plt

class TransmilenioSimulacion:
    def __init__(self, env, num_usuarios, efectividad_seguridad):
        self.env = env
        self.usuarios = [UsuarioTransmilenio(random.choice(['bajo', 'medio', 'alto']), 
                                             random.choice(['positiva', 'negativa'])) 
                         for _ in range(num_usuarios)]
        self.personal_seguridad = PersonalSeguridad(efectividad_seguridad)
        self.datos = []

    def run(self):
        while True:
            for usuario in self.usuarios:
                evasor = usuario.decidir_evasion()
                detectado = False
                if evasor:
                    detectado = self.personal_seguridad.detectar_evasion(usuario)
                    self.registrar_evento(usuario, evasor, detectado)
                else:
                    self.registrar_evento(usuario, evasor, detectado)
            yield self.env.timeout(1)

    def registrar_evento(self, usuario, evasor, detectado):
        self.datos.append({
            'dia': self.env.now,
            'nivel_socioeconomico': usuario.nivel_socioeconomico,
            'percepcion_servicio': usuario.percepcion_servicio,
            'evasor': evasor,
            'detectado': detectado
        })

    def guardar_datos(self):
        df = pd.DataFrame(self.datos)
        df.to_csv('datos_transmilenio.csv', index=False)
        
    # Al final de la simulación
    def visualizar_datos(self):
        df = pd.DataFrame(self.datos)

        # Ejemplo: Gráfico de barras de la frecuencia de evasión por nivel socioeconómico
        evasion_por_nse = df[df['evasor']].groupby('nivel_socioeconomico').size()
        evasion_por_nse.plot(kind='bar')
        plt.title('Frecuencia de Evasión por Nivel Socioeconómico')
        plt.xlabel('Nivel Socioeconómico')
        plt.ylabel('Frecuencia de Evasión')
        plt.show()
        
         # Gráfico de barras de la frecuencia de evasión por percepción del servicio
        evasion_por_percepcion = df[df['evasor']].groupby('percepcion_servicio').size()
        evasion_por_percepcion.plot(kind='bar', color='green')
        plt.title('Frecuencia de Evasión por Percepción del Servicio')
        plt.xlabel('Percepción del Servicio')
        plt.ylabel('Frecuencia de Evasión')
        plt.show()


# Configuración y ejecución de la simulación
env = simpy.Environment()
simulacion = TransmilenioSimulacion(env, num_usuarios=100, efectividad_seguridad=0.7)
env.process(simulacion.run())
env.run(until=30)  # Simular por 30 días

# Guardar los datos en un archivo CSV
simulacion.guardar_datos()
# Llamada a la función de visualización
simulacion.visualizar_datos()
