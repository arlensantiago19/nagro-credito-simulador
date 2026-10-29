# nagro-credito-simulador

Serviço de simulação de crédito rural (Nagro Crédito) — API interna de homologação.

## Rodando local

```bash
cp .env .env.local   # ajustar se necessário
docker compose up -d
python -m src.simulador --cpf-cnpj 00000000000191 --valor 250000 --prazo 12
```

Endpoints usados:

| Ambiente | Base URL |
|---|---|
| Homologação | `https://api-hml.nagro.com.br/credito/v1` |
| Portal | `https://credito-hml.nagro.com.br` |

Suporte: time de plataforma — `plataforma-hml@nagro.com.br`
