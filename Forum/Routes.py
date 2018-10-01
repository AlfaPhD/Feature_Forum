from flask import Flask
from flask import jsonify, request, json
from Server import App
from Models import Forum, Resposta
from Services import ListaForum,CriarForum, ConsultaPorIdForum, MakeResponse, InativarForum, AtivarForum

@App.route("/forum", methods=["GET"])
def ListarForum():

    lista = ListaForum.Listar()

    if len(lista) > 0:
        MakeResponse.Response("Sucesso","Lista de Foruns", lista)
        return jsonify(Resposta.Resposta), 200
    else:
        MakeResponse.Response("Sucesso","Nenhum forum cadastrado","")
        return jsonify(Resposta.Resposta),404

@App.route("/forum", methods=["POST"])
def CriarForums():

    data = request.data
    data = json.loads(data)

    status = CriarForum.CriarForum(data)
    if status[1] == 200:
        MakeResponse.Response("Sucesso", "Forum criado com suscesso", status[0])
        return jsonify(Resposta.Resposta), 200
    else:
        MakeResponse.Response("Erro", "Forum não criado", '')
        return jsonify(Resposta.Resposta), 404

@App.route("/forum/<id>", methods=["GET"])
def ConsultaForum(id):

    forum = ConsultaPorIdForum.Consulta(id)
    if forum:
        MakeResponse.Response("Sucesso", "Forum encontrado", forum)
        return jsonify(Resposta.Resposta),200
    else:
        MakeResponse.Response("Erro", "Forum não encontrado", '')
        return jsonify(Resposta.Resposta), 404

@App.route("/forum/inactivate", methods=["POST"])
def InativarForuns():
    data = request.data
    data = json.loads(data)

    status = InativarForum.Inativar(data)

    if status:
        MakeResponse.Response("Sucesso", "Forum inativado com suscesso", status)
        return jsonify(Resposta.Resposta), 200
    else:
        MakeResponse.Response("Erro", "Erro", status)
        return jsonify(Resposta.Resposta), 404

@App.route("/forum/activate", methods=["POST"])
def ActivateForum():
    data = request.data
    data = json.loads(data)

    status = AtivarForum.Ativar(data)

    if status:
        MakeResponse.Response("Sucesso", "Forum ativado com suscesso", status)
        return jsonify(Resposta.Resposta), 200
    else:
        MakeResponse.Response("Erro", "Erro", status)
        return jsonify(Resposta.Resposta), 404

@App.route("/forum/register", methods=["POST"])
def InscreverForum():
    pass

@App.route("/forum/unregister", methods=["POST"])
def RemovarInscricaoForum():
    pass


#Postagens
@App.route("/forum/<id>/post", methods=["GET"])
def ConsultaPostagensForum():
    pass

@App.route("/forum/post", methods=["POST"])
def PostagemForum():
    pass


@App.route("/forum/post/<id>", methods=["GET"])
def LeituraPostagemForum():
    pass
    