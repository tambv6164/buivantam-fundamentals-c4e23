from gmail import GMail, Message
from random import choice
from datetime import datetime
from threading import Timer

gmail = GMail("tambuitechkids@gmail.com", "techkidstambui1@")
template = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay em ngủ dậy, thấy {{symptom}}, b&aacute;c sĩ bảo em bị {{sick}}.</p>
<p>Sếp cho em nghỉ l&agrave;m nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" />.</p>
<p>Nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" />.</p>
'''
sickness_list = ["thương hàn", "kiết lỵ", "tiêu chảy"]
sickness = choice(sickness_list)
symptom = "đau bụng"

def job():
    content = template.replace("{{symptom}}", symptom).replace("{{sick}}", sickness)
    message = Message("Đơn xin nghỉ làm", to="tambv6164@gmail.com", html=content)
    gmail.send(message)

x = datetime.today()
y = x.replace(day=x.day+1, hour=7, minute=0, second=0, microsecond=0)
delta = y - x
secs = delta.seconds + 1

t = Timer(secs, job)
t.start()
