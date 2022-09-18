
def SplitDate(date):
    months = {'JAN':1, 'FEB':2, 'MAR':3, 'APR': 4,'MAY':5, 'JUN':6, 'JUL': 7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    split_month = date[2:5]
    split_date = date[0]
    split_year = date[6:]
    m = months[split_month]
    return (split_date , m , split_year)

date = str(input('Enter the date in the format dd-mmm-yy:  '))
print (SplitDate(date))



