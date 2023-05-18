#!/usr/bin/env python
from datetime import date
from string import Template
import re
import sys
try:
    import textile
except ImportError:
    print """ERROR: You need to install the textile library ("pip install textile")\n"""
    exit()

def usage():
    print """
Usage: python build_page.py textile_file [textile_file ...]

Read each textile file, and write a corresponding HTML file.
HTML files are written into the same directory as the textile files, with a .html
extension.  If the input file has a .textile extension, it is removed first.

The first line of the input file is taken as the title, and written into the
page title and a leading <h1></h1> tag.

Example:
python build_page.py html/index.textile   # Writes html/index.html
"""

TEMPLATE = 'template.html'
TEXTILE_SUFFIX = '.textile'

def base_filename(textile_filename):
    if textile_filename[-8:] == '.textile':
        return textile_filename[0:-8]
    else:
        return textile_filename

def build(textile_filename):
    f = open(textile_filename)
    try:
        (title, raw_content) = f.read().split('\n', 1)
        # Any line starting with "p(updated)." will have "Updated: [today]" set as its content
        p = re.compile(r'^(p\(updated\)\.).*$', re.M)
        raw_content = re.sub(p, r'\1 Updated: %s' % date.today(), raw_content)
        content = textile.textile(raw_content)
    finally:
        f.close()

    t = open(TEMPLATE)
    try:
        template = Template(t.read())
    finally:
        t.close()

    output = template.substitute({
        'title': title,
        'content': content,
    })

    output_filename = base_filename(textile_filename) + '.html'
    o = open(output_filename, 'w')
    o.write(output)
    o.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        exit()
    for f in sys.argv[1:]:
        build(f)
