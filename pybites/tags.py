import os
import re
from collections import Counter
import urllib.request

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

#tempfile = os.path.join('/tmp', 'feed')
tempfile = os.path.join('c:\jupyter\work', '') + 'test.xml'
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    'use Counter to get the top 10 PyBites tags'
    all = re.findall(TAG_HTML, content)
    c = Counter(all)
    return c.most_common(n)
