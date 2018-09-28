from flask import jsonify,request,json
from Models import Forum
import uuid
import datetime

def CriarForum():
    data = request.data
    data = json.loads(data)

    idForum = str(uuid.uuid1())
    idCriador = data['id']
    titulo = data['titulo']
    descricao = data['descricao']
    dataCriacao = datetime.datetime.now()
    dataUltimoPost  = datetime.datetime.now()
    Ativo = True

    novo_Forum = {}
    novo_Forum["idForum"] = idForum 
    novo_Forum["idCriador"] = idCriador 
    novo_Forum["titulo"] = titulo 
    novo_Forum["descricao"] = descricao 
    novo_Forum["dataCriacao"] = dataCriacao 
    novo_Forum["dataUltimoPost"] = dataUltimoPost 
    novo_Forum["Ativo"] = Ativo 

    Forum.Forum.append(novo_Forum)