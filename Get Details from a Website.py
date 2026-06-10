import re
import urllib.error
import urllib.request

url = 'https://satyadeo.com/goa-a-place-on-everybodys-list/'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

        print('Requested URL      :', response.geturl())
        print('Status Code        :', response.getcode())
        print('Header Values      :', response.getheaders())

        # Print the page text for reference
        print('\nPage Content Preview:')
        print(html[:1000])

        # Find image tags and extract their source URLs
        image_tags = re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)

        print('\nImages found on the page:', len(image_tags))
        if image_tags:
            for index, src in enumerate(image_tags, start=1):
                print(f'  {index}. {src}')
        else:
            print('  No image tags were found on this page.')

except urllib.error.URLError as e:
    print('URL Error:', e.reason)
except Exception as e:
    print('Error:', e)

