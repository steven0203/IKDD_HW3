#codeing=utf-8
from django.shortcuts import render
from django.db import connection
from datetime import date

# Create your views here.
def index(request):
	context=dict()
	if 'longitude' in request.POST and 'latitude' in request.POST:
		longitude=float(request.POST['longitude'])
		latitude=float(request.POST['latitude'])
		cursor=connection.cursor()
		sql="SELECT date,zone1,zone2,road,longitude,latitude,\
 ST_Distance(\
 ST_GeogFromText(ST_AsText(ST_MakePoint(longitude,latitude)))\
 ,ST_GeogFromText(ST_AsText(ST_MakePoint(%s,%s)))\
 )as length\
 from denguedata\
 WHERE \
 ST_Distance(\
 ST_GeogFromText(ST_AsText(ST_MakePoint(longitude,latitude)))\
 ,ST_GeogFromText(ST_AsText(ST_MakePoint(%s,%s)))\
 )<=200;"
		cursor.execute(sql,(longitude,latitude,longitude,latitude,))
		data=cursor.fetchall()
		Data=list()
		tmp=dict()
		for eachData in data:
			tmp['date'],tmp['zone1'],tmp['zone2'],tmp['road'],tmp['longitude'],tmp['latitude'],tmp['length']=eachData
			tmp['date']=tmp['date'].__str__()
			Data.append(tmp.copy())
		context['Data']=Data
	return render(request,'get_data/index.html',context)
