from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():

    """
        1 - Conta Digital,
        2 - /contas,
        3 - /contas/id/credito,
        4 - /contas/id/debito,
        5 - /contas/id/saldo,

    """
    return {
        "Conta Digital"
    }

class Cliente(BaseModel):
    id: int
    banco: int
    agencia: int
    conta: int
    valor: float

base_de_dados = [
    #Cliente(id= 1, banco= 1, agencia= 1738, conta = 10789, valor= 0.00)
]

@app.post("/contas")
def Cadastrar_conta_corrente(cliente: Cliente):
    base_de_dados.append(cliente)
    return cliente

@app.put("/contas/{id_cliente}/credito")
def Creditar_na_conta_corrente(id_cliente: int):
    for cliente in base_de_dados:
        if(cliente.id == id_cliente):
            cliente.valor = 10.75
            return {"Saldo em conta de R$": cliente.valor}
   
@app.put("/contas/{id_cliente}/debito")
def Debitar_da_conta_corrente(id_cliente: int):
    for cliente in base_de_dados:
        if(cliente.id == id_cliente):
            cliente.valor -= 9.75
            return {"Saldo em conta de R$": cliente.valor}

@app.get("/contas/{id_cliente}/saldo")
def Consultar_o_saldo_da_conta_corrente(id_cliente: int):
    for cliente in base_de_dados:
        if(cliente.id == id_cliente):
            return {"Saldo em conta de R$": cliente.valor}

    return {"Status": 404, "Mensagem": "Cliente não encontrado"}

@app.get("/contas/todas")
def Todos_clientes():
    return base_de_dados
