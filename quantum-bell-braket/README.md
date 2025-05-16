# 🧠 Quantum Bell States with Amazon Braket & Qiskit

Este app, apresenta uma simulação prática de emaranhamento quântico (estado de Bell) utilizando o **Amazon Braket SDK**. O objetivo é demonstrar a criação de circuitos quânticos simples, medição, visualização de estados e execução local ou em hardwares reais como **IonQ**, **D-Wave** ou **Rigetti**.

## ✨ Funcionalidades

- ✅ Criação de circuito quântico para estado de Bell
- ✅ Execução local com `LocalSimulator`
- ✅ Visualização do vetor de estado
- ✅ Geração de gráfico de distribuição de medidas
- ✅ Execução opcional em hardware real (QPU via AWS - pago)

---

## ⚙️ Tecnologias e Ferramentas

- [Amazon Braket SDK](https://docs.aws.amazon.com/braket/)
- [Python 3.x](https://www.python.org/)
- [Qiskit (opcional para comparação)](https://qiskit.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 🚀 Como executar

### 1. Clone o projeto

```bash
git clone https://github.com/alfecjo/quantum-bell-braket.git
cd quantum-bell-braket
```

## Instale as dependências

```bash
pip install amazon-braket-sdk
amazon-braket-schemas
matplotlib
```

## Execute o script principal
```bash
python bell_state.py
```
## 📊 Exemplo de saída

```bash
Medições do simulador local: {'00': 505, '11': 495}
Vetor de Estado (simulador local):
|00>: 0.707
|01>: 0.000
|10>: 0.000
|11>: 0.707
```

## 📁 Estrutura do Projeto

```bash
quantum-bell-braket/
│
├── bell_state.py           # Script principal com simulação
├── docs/
│   └── bell_plot.png       # Imagem do gráfico de exemplo
├── README.md
```

## 🤝 Contribuindo

- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou sugestões.
