from Models import Forum


def Ativar(data):

    idForum = data['idForum']
    idCriador = data['idCriador']
    i = 0
    for item in Forum.Forum:
        i = i + 1
        if item['idForum'] == idForum:
            if item['idCriador'] == idCriador:
                Forum.Forum[i-1]['Ativo'] = True
                return item
            else:
                return "Id do criador diferente do que criou o forum"
        return ""
