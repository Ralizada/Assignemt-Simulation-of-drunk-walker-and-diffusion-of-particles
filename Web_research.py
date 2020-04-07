

import numpy as np
import re
import requests

"""
MOLECULE is https://webbook.nist.gov/cgi/cbook.cgi?Name=MOLECULE
Molecular weight</a>:</strong> ??????</li>
Formula</a>:</strong> ??????</li>

"""

response = requests.get('https://webbook.nist.gov/cgi/cbook.cgi?Name=ethanol')
content = response.text
weight_line = re.findall(r'Molecular weight</a>:</strong> \d+.\d+</li>', content)
weight = re.findall(r'\d+.\d+', weight_line[0])[0]
formula_line = re.findall(r'Formula</a>:</strong> (\w(<sub>\d+</sub>\w*)+)+', content)[0]





