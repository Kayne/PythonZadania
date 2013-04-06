#encoding: utf-8
"""
Wprawka 6 (środa, PR)
"""
import datetime
import re

def odwrocDate(data):
  data = list(str(data).split("-"))
  data.reverse()
  return "".join(data)

def szukajPodciagi(data):
  data = odwrocDate(data)
  datatemp = data
  for i in range(7):
    p = re.compile(data[i:i+2])
    if len(p.findall(data)) == 3:
      return True
  return None

def sprawdzDaty():
  start_date = datetime.date(2001, 01, 01)
  end_date = datetime.date(2999, 12, 31)
  wynik = []
  for i in range(((end_date+datetime.timedelta(days=1)-start_date).days)):
    if szukajPodciagi(odwrocDate(start_date+datetime.timedelta(days=i))) != None:
      wynik.append((start_date+datetime.timedelta(days=i)))
  return wynik

for i in sprawdzDaty():
  print i.strftime("%d-%m-%Y")