# Carford

## Executar o projeto
Suba o BD, no projeto eu usei o Postgres

```docker-compose up```

Crie uma env para o projeto, eu usei venv

```python3 -m venv nome_env```

Depois ative

```source env/bin/activate```

Instale as bibliotecas

```pip install requirements.txt```

Rode as Migrations

```alembic revision --autogenerate -m "Migrations"```

```alembic upgrade head```

Depois é só executar o projeto

Como no projeto tem um launch, pode ser executado usando o botão de run se estiver usando o VS Code

## Tarefas
- Modelar BD ✔
- Desenvolver API ✔
  - Criar Rotas ✔
    - Rotas de Proprietário ✔
    - Rotas de  Carro ✔
- Fazer os Testes ❌
  - Unitários ❌
  - Integração ❌
- Desenvolver Front ❌
  - Cadastro de Proprietário ❌
  - Cadastro de Carro ❌
- Tornar as rotas seguras ❌