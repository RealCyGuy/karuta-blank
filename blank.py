import base64
import os

from dotenv import load_dotenv
import requests

load_dotenv()

# preset:
# [bottom, top, left, right]
presets = {
    "festivus": [350, 49, 37, 197],
    "carnations": [302, 97, 37, 197],
    "ed3": [302, 91, 37, 197],
    "explosion": [369, 30, 30, 213],
}

preset = presets[os.environ.get("frame", "explosion")]
colour = os.environ.get("colour", "#ffffff")

y = preset[0]
paths = []
while y > preset[1]:
    # print(f'<path d="M 37,{y} c 20,0 40,0 196,0" stroke="#fff" stroke-width="7"></path>')
    path = f'<path d="M{preset[2]},{y}c61.06667,0 122.13333,0 {preset[3]},0"></path>'
    print(path)
    paths.append(path)
    y -= 6
g = (
    f'<g fill="none" fill-rule="nonzero" stroke="{colour}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal">'
    + "".join(paths)
    + "</g>"
)
body = '{"data": "' + base64.b64encode(g.encode("ascii")).decode("ascii") + '"}'
print(body)

headers = {
  "Authorization": os.environ.get("AUTHORIZATION"),
  "content-type": "application/json"
}

response = requests.request("POST", os.environ.get("URL"), data=body, headers=headers)

print(response.text)
