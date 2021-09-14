import telepot
from src.db.mysql_connection import connection,cursor
from src.charts.generate_charts import relat_diario, relat_historico
bm= telepot.Bot('822361090:AAEyKBqmmyytRa5BqmpbfGm-ord7yc9v9UY')
def recebeMSG(msg):
    chat_id=msg['chat']['id']
    mens=msg['text'].upper()

    if(mens.__contains__('/START')):
        bm.sendMessage(chat_id, 'Ola, para te ajudar preparamos um menu:')
        bm.sendMessage(chat_id, '/cadastro \n/diario \n/historico ')

    if(mens.__contains__('/CADASTRO')):
        bm.sendMessage(chat_id, "Para se cadastrar, preciso que informe seu email")

    if (msg['text'].__contains__('@')):
        email=msg['text'].upper()
        chat_id=(msg['chat']['id'])
        nome=msg['chat']['first_name'].upper()
        try:
            cursor.execute("INSERT INTO bvzfdagnfqepipz70gyw.Clientes(nome, email, id_chat,gold) VALUES('%s', '%s', %d,NULL)"%(nome , email , chat_id))
            connection.commit()
            bm.sendMessage(chat_id,"Usuario cadastrado com sucesso")
        except:
            bm.sendMessage(chat_id,"Usuario ja possui cadastro")

    if(mens.__contains__('/DIARIO')):
        relat_diario()
        bm.sendMessage(chat_id,"Fique por dentro da movimentacao! ")
        bm.sendPhoto(chat_id,photo=open('../../charts/diario.png', 'rb'))

    if (mens.__contains__('/HISTORICO')):
        relat_historico()
        bm.sendMessage(chat_id, "Fique por dentro da movimentacao! ")
        bm.sendPhoto(chat_id, photo=open('../../charts/historico.png', 'rb'))

bm.message_loop(recebeMSG)
while True:
    pass