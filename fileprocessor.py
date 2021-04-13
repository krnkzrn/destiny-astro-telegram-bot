# import pandas
from datetime import date

# df = pandas.read_csv('resources/activations.csv',header=0)
# dc = pandas.read_csv('resources/client_base.csv',header=0)

# def week_activations():
today = date.today()
print('Today is ',today)


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
