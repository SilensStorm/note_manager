username = ("username")
print("имя пользователя",username)

title = ("title")
print("Заголовок заметки",title)

content = ("content")
print("Описание заметки",content)

status = ("status")
print("Сатус заметки",status)

from datetime import date
created_date = date.today()
print("дата создания заметки в формате день-месяц-год ",created_date.day,".",created_date.month,".",created_date.year,sep="")

issue_date = ("issue_date")
print("дата истечения заметки (дедлайн) в формате день-месяц-год",issue_date)
