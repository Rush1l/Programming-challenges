def check_file_exists(csv_file): 
    return csv_file.is_file()

csv_file = Path("south.csv")

def read_csv(csv_file):
      csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

    # read the specified csv file just like Challenge 10

html_file = Path('south.html')
    
def read_html(html_file):
  file  = codecs. open('south.html', 'r', 'utf-8')
  r = file.read()
  file.close()
  return file
  
    
        
    
    ## read a html file as a regular file
            
def process(csv, html):
    ## replace link1...link5 in html with corresponding values fronm csv
    ## Similarly do for initials1...intitials5 and name1...name5

def write_html(path, html):
    ## write the new contents into an html file


if __name__ == "__main__":
    csv = read_csv("south.csv")
    html = read_html("south.html")
    html = process(csv, html)
    write_html("south_final.html", html)
