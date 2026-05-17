import urllib.request
try:
    with urllib.request.urlopen('https://satyadeo.com/goa-a-place-on-everybodys-list/') as f:
        #with urllib.request.urlopen('https://satyadeo.com/') as f:
        f2 = urllib.request.urlopen('https://satyadeo.com/goa-a-place-on-everybodys-list/')
        print(f.read().decode('utf-8'))
        print("Header Values are :",f.getheaders())
        print("Requested url is :",f.geturl())
        print("Contents of the url are  :",f2.read())

except urllib.error.URLError as e:
    print(e.reason)
