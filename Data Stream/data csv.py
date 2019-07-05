import csv
import matplotlib.pyplot as plot
filename = 'goo.csv'
data = []
X, Y = [], []

try :
    with open(filename, 'r') as f :
        reader = csv.reader(f)
        header = next(reader)                                                             
        data = [row for row in reader]

except csv.Error as e:
    print("Error reading csv file %s : %s" % (reader.line_num, e))
if header :
    print(header)
    print('====================')
for datarow in data :
    print(datarow    )
    X.append(datarow[0])
    Y.append(int(datarow[1]))
plot.plot(X, Y)
plot.show()