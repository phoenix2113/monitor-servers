import datetime
import urllib.request
import urllib.error

def server1(x):

    res = list(map(lambda ele: ele == "True", x[3]))
    if res:
        urls=x[1].split(';')
        for i, url in enumerate(urls):
            try:
                result = urllib.request.urlopen(url).getcode()
            except urllib.error.HTTPError as error:
                result = error.code
            except urllib.error.URLError as error:
                result= error.reason
            temp = {
                'response_code': result,
                'url': url,
                'time': str(datetime.datetime.now()).replace(" ","-")
            }
            print(" ".join([str(key)+"="+str(temp[key]) for key in sorted(temp.keys())]))
    else:
        print('if not working')
