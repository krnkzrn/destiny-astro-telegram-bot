import datetime

class User:
    name=''
    birthdate=datetime.date.today()
    userid=''
    active=False

    def reset(self):
        name = ''
        birthdate = datetime.date.today()
        userid = ''
        active = False

    def asdict(self):
        return {'id':self.userid, 'Активная подписка': self.active,'Имя':self.name, 'Дата рождения':self.birthdate.strftime('%d.%m.%Y')}