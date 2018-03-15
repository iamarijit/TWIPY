import pandas as pd
import Place_data as tw
ch = input("Wish to update dataset (y/n)? \n")
if ch == 'y' or ch == 'Y':
 tw.place()
places = pd.read_csv('places.csv', encoding='utf-8')
Sorted = places.sort_values(['Country', 'Place'])
ids = Sorted.ID
dis_cout = []
for i in Sorted['Country']:
 if i not in dis_cout:
 dis_cout.append(i)
dic = {}
for i in dis_cout:
 dic[i] = Sorted['ID'][Sorted['Place'] == i]
flag = 0
nameofcountry=’ ’
while flag == 0:
 try:
 nameofcountry = input("Enter the country name : \n")
 l = dic[nameofcountry].iloc[0]
 flag = 1
 except:
 print('Invalid country !! Enter again !! \n')
trends = tw.api.trends_place(l)
print("\nThe most trending #hashtags of ", nameofcountry, " are :\n ")
for i in trends[0]['trends']:
 name = i['name']
 if name[0] == '#':
 print(name)
