# pypi.org is the original source where you can find many packages that can be used to work for the real-life applications

# To install a package from pypi, we can use a tool called pip
# The versions are of the type x.y.z where x represents major, y represents minor, and z represents the patches

import requests # type: ignore

response = requests.get("https://shivangsuchak.demo.piano.io")
print(response)