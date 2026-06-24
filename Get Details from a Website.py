import os
import re
import urllib.error
import urllib.parse
import urllib.request


def download_images_from_webpage(url, save_dir='downloaded_images'):
    os.makedirs(save_dir, exist_ok=True)

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except urllib.error.URLError as e:
        print('URL Error:', e.reason)
        return []
    except Exception as e:
        print('Error while fetching the webpage:', e)
        return []

    image_tags = re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    downloaded_files = []

    print('\nImages found on the page:', len(image_tags))
    if image_tags:
        for index, src in enumerate(image_tags, start=1):
            image_url = urllib.parse.urljoin(url, src)
            filename = os.path.basename(urllib.parse.urlsplit(image_url).path) or f'image_{index}.jpg'

            if not os.path.splitext(filename)[1].lower():
                filename = f'{index}{os.path.splitext(filename)[0]}.jpg'

            save_path = os.path.join(save_dir, filename)

            try:
                urllib.request.urlretrieve(image_url, save_path)
                downloaded_files.append(save_path)
                print(f'  {index}. Downloaded -> {save_path}')
            except Exception as e:
                print(f'  {index}. Failed to download {image_url}: {e}')
    else:
        print('  No image tags were found on this page.')

    return downloaded_files


if __name__ == '__main__':
    url = 'https://satyadeo.com/goa-a-place-on-everybodys-list/'

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8', errors='ignore')

            print('Requested URL      :', response.geturl())
            print('Status Code        :', response.getcode())
            print('Header Values      :', response.getheaders())

            print('\nPage Content Preview:')
            print(html[:1000])

    except urllib.error.URLError as e:
        print('URL Error:', e.reason)
    except Exception as e:
        print('Error:', e)

    downloaded_files = download_images_from_webpage(url)
    print('\nDownloaded images count:', len(downloaded_files))

