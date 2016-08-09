#!/usr/bin/python
## Designed by Exorcist

db_name = 'IVI_'
#Year

list_year = []
for y in range(2014,2017):
	list_year.append(y)

#Month
list_month = []
for m in range(1,13):
	if m < 10:
		m_new = '0'+str(m)
		list_month.append(m_new)
	else:
		list_month.append(m)

#Day
list_day = []
for d in range(1,32):
        if d < 10:
                d_new = '0'+str(d)
                list_day.append(d_new)
        else:
                list_day.append(d)

#Hour
list_hour = []
for h in range(0,24):
        if h < 10:
                h_new = '0'+str(h)
                list_hour.append(h_new)
        else:
                list_hour.append(h)

#Minute
list_min = []
for min in range(0,60):
        if min < 10:
                min_new = '0'+str(min)
                list_min.append(min_new)
        else:
                list_min.append(min)

#Second
list_sec = []
for sec in range(0,60):
        if sec < 10:
                sec_new = '0'+str(sec)
                list_sec.append(sec_new)
        else:
                list_sec.append(sec)

for y1 in list_year:
	for m1 in list_month:
		for d1 in list_day:
			for h1 in list_hour: 
				for min1 in list_min:
					for sec1 in list_sec:
						print db_name+str(y1)+'-'+str(m1)+'-'+str(d1)+'_'+str(h1)+'-'+str(min1)+'-'+str(sec1)+'.sql.gz'
					

