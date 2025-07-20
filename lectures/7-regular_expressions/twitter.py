import re

url = input("URL: ").strip()
# username = re.match(r"/.+$", url)
# username = url.replace("https://twitter.com/", '')
# username = url.removeprefix("https://twitter.com/")
# username = re.sub(r"^((https?://)?(www\.)?)?twitter\.com/", '', url)  # re.sub(pattern, replace, string, coung, flags)
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")