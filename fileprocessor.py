import pandas
import datetime

df = pandas.read_csv('resources/activations.csv',header=0,parse_dates=['Дата','Время'])
# dc = pandas.read_csv('resources/client_base.csv',header=0)

today = datetime.date.today()
print('Today is ',today)

start = today - datetime.timedelta(days=today.weekday())
end = start + datetime.timedelta(days=6)
startD = pandas.to_datetime(start)
endD = pandas.to_datetime(end)
this_week_activations = df[(df['Дата']>startD)&(df['Дата']<endD)]

def 

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
