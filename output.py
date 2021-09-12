from multiprocessing import process
import pandas as pd
import fetch_status_code
import multiprocessing

duration=int(input("Enter the duration:- ", ))
# reading two csv files
data1 = pd.read_csv('table1.csv')
data2 = pd.read_csv('table2.csv')
  
# using merge function by setting how='inner'
outputTable = pd.merge(data1, data2, 
                   on='Server Name', 
                   how='inner')
  
# displaying result
mergeTable = outputTable.to_numpy()

proc1 = multiprocessing.Process(target=fetch_status_code.server_response, args=(mergeTable[0],duration ))
proc2 = multiprocessing.Process(target=fetch_status_code.server_response, args=(mergeTable[1],duration ))
proc3 = multiprocessing.Process(target=fetch_status_code.server_response, args=(mergeTable[2],duration ))

proc1.start()
proc2.start()
proc3.start()

