# fabricaNode

## Setup

```
pdm install
pdm run python manage.py migrate
pdm run python manage.py seed_demo_data     # popula áreas/keywords + base geográfica
pdm run python manage.py seed_professores   # importa os professores reais do portal da Fábrica
pdm run dev
```

Copie `.env.example` para `.env` e ajuste conforme o ambiente.
