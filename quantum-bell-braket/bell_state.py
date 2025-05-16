# Instalar dependências caso esteja em notebook local
# !pip install amazon-braket-sdk amazon-braket-schemas matplotlib

from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# 1. Criar circuito de emaranhamento (Bell State)
# ------------------------------
bell_circuit = Circuit()\
    .h(0)\
    .cnot(0, 1)\
    .measure(0, 1)

# ------------------------------
# 2. Simular localmente (clássico)
# ------------------------------
local_simulator = LocalSimulator()

# Executar com 1000 disparos (shots)
result = local_simulator.run(bell_circuit, shots=1000).result()

# Exibir contagem de medições
counts = result.measurement_counts
print("Medições do simulador local:", counts)

# ------------------------------
# 3. Visualizar as medições
# ------------------------------
labels, values = zip(*counts.items())
plt.bar(labels, values)
plt.title("Distribuição de Medidas - Estado Bell")
plt.xlabel("Estados Medidos")
plt.ylabel("Contagens")
plt.show()

# ------------------------------
# 4. Vetor de estado (sem medição)
# ------------------------------
circuit_state = Circuit().h(0).cnot(0, 1)  # sem .measure() para ver vetor puro

state_vector = local_simulator.run(circuit_state, shots=0).result().result_types[0].value
print("Vetor de Estado (simulador local):")
for i, amp in enumerate(state_vector):
    print(f"|{i:02b}>: {amp:.3f}")

# ------------------------------
# 5. (Opcional) para rodar no hardware real da AWS (IonQ) apenas...
# ------------------------------
# Descomente as linhas abaixo se quiser rodar no QPU IonQ (cuidado, pois tem custo e demora)

# ionq_device = AwsDevice("arn:aws:braket:::device/qpu/ionq/Harmony")
# task = ionq_device.run(bell_circuit, shots=100)
# hardware_result = task.result()
# print("Resultados no hardware (IonQ):", hardware_result.measurement_counts)
