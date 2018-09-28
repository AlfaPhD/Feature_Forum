from flask import Flask
from flask import jsonify, request, json
from Server import App
from Models import Forum, Resposta
from Services import ListaForum,CriarForum

@App.route("/forum", methods=["GET"])
def ListarForum():
    Resposta.Resposta["Status"] = "Sucesso"
    Resposta.Resposta["Dados"] = ListaForum.Listar()
    Resposta.Resposta["Mensagem"] = "Lista de Foruns"
    return jsonify(Resposta.Resposta)

@App.route("/forum", methods=["POST"])
def CriarForums():
    Resposta.Resposta["Status"] = "Sucesso"
    Resposta.Resposta["Dados"] = CriarForum.CriarForum()
    Resposta.Resposta["Mensagem"] = "Lista de Foruns"
    return jsonify(Resposta.Resposta)


@App.route("/forum/<id>", methods=["GET"])
def ConsultaForum():
    pass

@App.route("/forum/inactivate", methods=["POST"])
def InativarForum():
    pass

@App.route("/forum/activate", methods=["POST"])
def ActivateForum():
    pass

@App.route("/forum/register", methods=["POST"])
def InscreverForum():
    pass

@App.route("/forum/unregister", methods=["POST"])
def RemovarInscricaoForum():
    pass

@App.route("/forum/<id>/post", methods=["GET"])
def ConsultaPostagensForum():
    pass

@App.route("/forum/post", methods=["POST"])
def PostagemForum():
    pass


@App.route("/forum/post/<id>", methods=["GET"])
def LeituraPostagemForum():
    pass
    