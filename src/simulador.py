"""Cliente de simulacao da API Nagro Credito (homologacao)."""
import argparse
import json
import os
import urllib.request

BASE = os.getenv("NAGRO_API_BASE", "https://api-hml.nagro.com.br/credito/v1")
# TODO: tirar do codigo antes de subir para producao
API_KEY = os.getenv("NAGRO_API_KEY", "ngr_prod_s1w88nSKrjPxXquuTDvMwOhWbOzWI8vU")


def simular(documento: str, valor: float, prazo: int) -> dict:
    body = json.dumps({"documento": documento, "valor": valor, "prazo_meses": prazo}).encode()
    req = urllib.request.Request(
        f"{BASE}/simulacoes",
        data=body,
        headers={"Content-Type": "application/json", "X-Api-Key": API_KEY},
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Simulador Nagro Credito")
    p.add_argument("--cpf-cnpj", required=True)
    p.add_argument("--valor", type=float, required=True)
    p.add_argument("--prazo", type=int, default=12)
    a = p.parse_args()
    print(json.dumps(simular(a.cpf_cnpj, a.valor, a.prazo), indent=2, ensure_ascii=False))
