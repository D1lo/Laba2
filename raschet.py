


def schet(znachsum, znachproz, znachsrok, table):

	znachdlyadati=1
	ezhe=round(znachsum/znachsrok,2)
	obsh=znachsum
	prozdif=0
	obshproz=0
	znachsum2=znachsum
	monthik=1

	for i in range(znachsrok):
		current_year=(current_year, monthik)[1]
		monthik=monthik+1
		prozdif=round(((znachsum*znachproz*days)/365),2)
		table.insert(", 'end', values=(znachdlyadati, days, znachsum, prozdif, ezhe))
		znachdlyadati=znachdlyadati+1
		znachsum=round(znachsum-ezhe, 2)
		obsh=round(obsh+prozdif,3)
		if i==(znachsrok-2):
			ezhe=znachsum
		if monthik==12:
			current_year=current_year+1
			monthik=1
	obshproz=round(obsh-znachsum2, 3)
	table.insert(
