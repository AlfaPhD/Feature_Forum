from Models import Resposta

def Response(status = '', mensagem = '', dados=''):
    Resposta.Resposta["Status"] = status
    Resposta.Resposta["Mensagem"] = mensagem
    Resposta.Resposta["Dados"] = dados