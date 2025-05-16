# 🧠 Estado de Bell com Qiskit

Este projeto demonstra como criar e simular um **estado de Bell** (emaranhado quântico) utilizando a biblioteca [Qiskit](https://qiskit.org/). O circuito é executado em simuladores locais (vetor de estado e QASM) e apresenta visualizações do vetor de estado e da distribuição de medições.

## ✨ O que é um Estado de Bell?

Um estado de Bell é um exemplo clássico de emaranhamento quântico. O circuito usado aqui aplica uma porta **Hadamard** seguida de uma **CNOT**, resultando em um dos quatro estados de Bell. Neste caso:

```python
|Φ⁺⟩ = (|00⟩ + |11⟩) / √2
```

## 🔧 Tecnologias

- [Qiskit](https://qiskit.org/)
- Python 3.x
- [Matplotlib](https://matplotlib.org/) (para visualização)

## 🧪 Funcionalidades

- Criação de circuito quântico para o estado de Bell.
- Simulação do vetor de estado (antes da medição).
- Execução de medições (1000 vezes) com simulação clássica.
- Visualização:
  - Vetor de estado na esfera de Bloch.
  - Histograma com os resultados das medições.

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/alfecjo/bell-state-qiskit.git
cd bell-state-qiskit
```

## Instale as dependências:

```python
pip install qiskit matplotlib
```

## Execute o script:
```python
python bell_state_qiskit.py
```

## 🖼️ Exemplos de saída

- Vetor de Estado
- Visualização do vetor de estado na esfera de Bloch para ambos os qubits antes da medição.

## Histograma de Medições

- Distribuição esperada: ~50% para 00, ~50% para 11 (devido ao emaranhamento).

## 🔁 Comparação com AWS Braket
- Este circuito também pode ser executado em simuladores ou hardwares reais usando Amazon Braket. A versão Braket está disponível neste repositório (quantum-bell-braket) para comparação de resultados entre plataformas quânticas.

## 📄 Licença
- Este projeto está licenciado sob a MIT License.