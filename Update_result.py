import csv
def update_result(a):
    with open('result.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)
                
        # write a row to the csv file
        return writer.writerows(a)