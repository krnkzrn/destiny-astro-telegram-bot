import pandas
# import datetime
import user
import ya

# today = datetime.date.today()
# print('Today is ',today)
#
# start = today - datetime.timedelta(days=today.weekday())
# end = start + datetime.timedelta(days=6)
# startD = pandas.to_datetime(start)
# endD = pandas.to_datetime(end)
# this_week_activations = df[(df['Дата']>startD)&(df['Дата']<endD)]

# todo if initial load has failed need to load on next var access
# todo do we need to schedule upload in case of failed attempt?
# todo add methof getDC() where check flag if load success, if not - load again
# todo probably do same for saveDC

def add_client(client):
    ya.load_clients()
    clients = pandas.read_csv('resources/client_base.csv', header=0)
    if isinstance(client, user.User) :
        clients = clients.append(client.asdict(), ignore_index=True)
        clients.to_csv('resources/client_base.csv')
        ya.save_clients()

# todo remove?
def print_all_clients():
    ya.load_clients()
    clients = pandas.read_csv('resources/client_base.csv', header=0)
    print(clients)

def get_client(userid):
    ya.load_clients()
    clients = pandas.read_csv('resources/client_base.csv', header=0)
    return clients[clients['id'] == userid].reset_index(drop=True)

# for index, row in dc.iterrows():
#     print(row['НС дня рождения'], row['НС года рождения'], row['ЗВ дня рождения'], row['ЗВ года рождения'])
#     clientActivationsNS = df.loc[df['Для кого(НС)'].isin([row['НС дня рождения'], row['НС года рождения']])]
#     clientActivationsZV = df.loc[df['Для кого(ЗВ)'].isin([row['ЗВ дня рождения'], row['ЗВ года рождения']])]
#     clientActivations = pandas.concat([clientActivationsNS, clientActivationsZV]).drop_duplicates
#
#     file = open('personal_message_template.html')
#     s = file.read()
#     with open('personal_message_example.html', 'w') as result:
#         result.write(s.format(name='Karina',activations=clientActivations.style.render()))
