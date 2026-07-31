import urllib.request
import os

raw_urls = os.environ.get("DEB_URLS_INPUT", "")
urls = raw_urls.strip().splitlines()

index = 1
for url in urls:
    url = url.strip()
    if not url:
        continue
    filename = f"tweak_{index}.deb"
    print(f"Đang tải tweak {index} từ: {url}")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filename, "wb") as out_file:
            out_file.write(response.read())
        print(f"Đã lưu thành công: {filename}")
        index += 1
    except Exception as e:
        print(f"Lỗi khi tải {url}: {e}")
