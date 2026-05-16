import urllib.request
try:
    with urllib.request.urlopen('https://satyadeo.com/goa-a-place-on-everybodys-list/') as f:
        #with urllib.request.urlopen('https://satyadeo.com/') as f:
        print(f.read().decode('utf-8'))
        print("Header Values are :",f.getheaders())
        print("Requested url is :",f.geturl())

except urllib.error.URLError as e:
    print(e.reason)
