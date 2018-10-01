from Models import Forum

def Consulta(id):
    for item in Forum.Forum:
        if item["idForum"] == id:
            return item
    return False



