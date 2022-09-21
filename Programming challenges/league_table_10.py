import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    for row in rows:
        home,away,homegoals,awaygoals,winner=rows[1],rows[2],rows[3],rows[4],rows[5]
        if home not in dictionary:
            dictionary[home]=[0,0,0,0,0] ##win,draw,loss,goal diff,points

        if away not in dictionary:
            dictionary[away]=[0,0,0,0,0]


            ##check if it's a draw

        if winner=='D':
            dictionary[home][4]+=1
            dictionary[away][4]+=1

            dictionary[home][1]+=1
            dictionary[away][1]+=1

            ##if winner is away

        if winner=='A':
            dictionary[home][2]+=1
            dictionary[away][0]+=1

            dictionary[away][4]+=1

            ##if winner is home

        if  winner=='H':
            dictionary[home][0]+=1
            dictionary[away][2]+=1

            dictionary[home][4]+=1











if __name__ == "__main__":
    file_contents = read_csv(csv_file)
 
