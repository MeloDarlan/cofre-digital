# Cofre Digital - Sistemas Distribuidos

Aplicação cliente/servidor em Python que simula um cofre digital compartilhado. Cada cliente tenta adivinhar um número secreto gerado pelo servidor e a cada tentativa errada, o prêmio acumulado cresce. Quem acertar leva 60% do fundo!

## Como funciona

- O cliente envia seu **nome** e um **número de 0 a 999**
- O servidor sorteia um número aleatório para aquele cliente
- **Errou?** O fundo aumenta e o cliente recebe uma mensagem com o valor acumulado
- **Acertou?** O cliente recebe 60% do fundo e o cofre zera

A comunicação é feita via **Sockets TCP**. O servidor é **multithreaded**, cada cliente é atendido em uma thread separada, com acesso sincronizado ao fundo compartilhado.

---

## Pré-requisitos

- Python 3.8 ou superior
- `pip` instalado

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MeloDarlan/cofre-digital.git
cd cofre-digital
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar o venv
python -m venv venv

# Ativar no Linux/macOS
source venv/bin/activate

# Ativar no Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
PORT=5000
```

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `PORT` | Porta de comunicação TCP | `5000` |

---

## Executando

### Servidor

Abra um terminal, ative o venv e execute:

```bash
python server.py
```

O servidor ficará aguardando conexões:

```
Cofre Digital iniciado: 0.0.0.0:5000 …
```

### Cliente

Em outro terminal, ative o venv e execute:

```bash
python client.py
```

Informe seu nome e um número:

```
Seu nome: Maria
Seu número (0 a 999): 342
Código Errado, Maria. O cofre tem R$ 110.00 acumulados.
```

## Observações

- O fundo inicial do servidor começa em **R$ 100,00**
- Cada tentativa adiciona **R$ 10,00** ao fundo

### Agentes Utilizados

**Sonnet 4.6 (Claude AI)**: Utilizado como ferramenta de apoio para:
  - Esclarecimento de conceitos de lock dentro da biblioteca de threads;
  - Auxílio na elaboração de documentação como esse README;
  - Suporte na identificação e correção de erros.

### Responsabilidade Acadêmica

A Inteligência Artificial foi empregada exclusivamente como ferramenta de suporte ao processo de aprendizagem e desenvolvimento. Todas as decisões de projeto, implementações finais, validações e integrações foram realizadas e revisadas pelos autores do trabalho.