from fastapi import FastAPI
from pydantic import BaseModel, constr
from uuid import UUID, uuid4
from enum import Enum
from starlette.status import HTTP_201_CREATED

class EstadosPossiveis(str, Enum):
    finalizado = "finalizado"
    nao_finalizado = "não finalizado"

class TarefaEntrada(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)
    estado: EstadosPossiveis = EstadosPossiveis.nao_finalizado

class Tarefa(TarefaEntrada):
    id: UUID

app = FastAPI()


TAREFAS = []

@app.get("/tarefas")
def listar():
    return TAREFAS

@app.post('/tarefas', response_model=Tarefa, status_code=HTTP_201_CREATED)
def criar(tarefa: TarefaEntrada):
    nova_tarefa = tarefa.dict()
    nova_tarefa.update({"id": uuid4()})
    TAREFAS.append(nova_tarefa)
    return nova_tarefa