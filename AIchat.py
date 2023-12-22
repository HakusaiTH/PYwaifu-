from characterai import PyCAI
from googletrans import Translator
from VoicevoxTTS import text_to_voice

client = PyCAI("1b01c1086980a7ac4ccba7d0bfed5e67087c791d")

char = "Wqcpqfh-x_oWqHJJFi4noysofgpDs1zaJAPnle2vII0"

chat = client.chat.get_chat(char)

participants = chat['participants']

def translate_text(text,traget_la):
    translator = Translator()
    translation = translator.translate(text, dest=traget_la)
    return translation.text

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

def callAI(message):
    data = client.chat.send_message(chat['external_id'], tgt, translate_text(message,"en"))
    text = data['replies'][0]['text']

    message_result = translate_text(text,"th")
    message_result_voice = translate_text(text,"ja")
    text_to_voice(message_result_voice)  

    return message_result