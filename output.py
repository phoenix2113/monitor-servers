import pandas as pd
import fetch_status_code
import multiprocessing
  
# reading two csv files
data1 = pd.read_csv('table1.csv')
data2 = pd.read_csv('table2.csv')
  
# using merge function by setting how='inner'
output1 = pd.merge(data1, data2, 
                   on='Server Name', 
                   how='inner')
  
# displaying result
x = output1.to_numpy()

proc1 = multiprocessing.Process(target=fetch_status_code.server_response, args=(x[0], ))
proc2 = multiprocessing.Process(target=fetch_status_code.server_response, args=(x[1], ))
proc3 = multiprocessing.Process(target=fetch_status_code.server_response, args=(x[2], ))

proc1.start()
proc2.start()
proc3.start()

