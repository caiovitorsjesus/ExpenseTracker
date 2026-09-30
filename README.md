# Expense Tracker

Aplicativo simples de linha de comando para registrar e gerenciar despesas. Cada despesa recebe um ID e uma data automática, além da descrição e do valor informados pelo usuário.

## Funcionalidades

- Adicionar uma despesa
- Listar as despesas cadastradas
- Atualizar uma despesa pelo ID
- Remover uma despesa pelo ID
- Validar descrições e valores informados

## Requisitos

- Python 3.10 ou superior
- Nenhuma dependência externa

## Como executar

Abra um terminal na pasta do projeto e execute:

```bash
python main.py
```

No Windows, também é possível usar:

```powershell
py main.py
```

Escolha uma opção no menu e siga as instruções exibidas no terminal. Para encerrar, escolha `5. Exit`.

## Armazenamento

As despesas ficam apenas na memória enquanto o programa está aberto. Ao encerrar a execução, os registros são perdidos.
