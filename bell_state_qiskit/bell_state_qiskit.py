from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito Bell (emaranhado)
qc = QuantumCircuit(2, 2)
qc.h(0)               # Hadamard no qubit 0
qc.cx(0, 1)           # CNOT com controle no qubit 0 e alvo no qubit 1
qc.barrier()
qc.measure([0, 1], [0, 1])

# Simulador de vetor de estado (antes da medição)
sv_simulator = Aer.get_backend('statevector_simulator')
circuit_no_meas = qc.remove_final_measurements(inplace=False)
sv_result = sv_simulator.run(circuit_no_meas).result()
statevector = sv_result.get_statevector()

print("\nVetor de Estado:")
print(statevector)

# Plot do vetor de estado
plot_bloch_multivector(statevector)
plt.title("Vetor de Estado (Qiskit)")
plt.show()

# Simulador de medições
simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
qobj = assemble(compiled, shots=1000)
result = simulator.run(qobj).result()
counts = result.get_counts()

print("\nResultados da Medição:")
print(counts)

# Histograma
plot_histogram(counts)
plt.title("Distribuição de Medidas (Qiskit)")
plt.show()
