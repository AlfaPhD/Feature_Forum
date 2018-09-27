from flask import jsonify
from Models import Resposta
from Server import App


@App.errorhandler(400)
def TratarRequisicaoInvalida(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "O pedido nao pôde ser entregue devido a sintaxe incorreta."
    Resposta.Resposta["Dados"] = ""
    return(jsonify(Resposta.Resposta))

@App.errorhandler(403)
def TratarErrorProibido(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "O pedido nao deve ser requisitado novamente."
    Resposta.Resposta["Dados"] = ""
    return(jsonify(Resposta.Resposta))

@App.errorhandler(404)
def TratarNotFound(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "O recurso requisitado nao foi encontrado"
    Resposta.Resposta["Dados"] = ""
    return(jsonify(Resposta.Resposta))

@App.errorhandler(500)
def TratarErroServidor(error):
    Resposta.Resposta["Status"] = "Erro"
    Resposta.Resposta["Mensagem"] = "Deu ruim. O erro foi {0}.".format(error)
    Resposta.Resposta["Dados"] = ""
    return(jsonify(Resposta.Resposta))