# gives a single float value



def getDates(date,month,year,week):
	file1 = open("testing.csv","w")
	for k in range(3):
		#st=str(date)+','+str(month)+','+str(year)+','+str(week)
		
		date=date+1
		if date==31:
			date=1
			month=month+1
		if date==1 and month==13:
			month=1
			year=year+1

		week=(week+1)%7
		st=str(date)+','+str(week)
		file1.write(st+"\n")
		print(str(date)+"    "+str(month)+"    "+str(year)+"    "+str(week))
	file1.close()
