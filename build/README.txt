
The HTML pages are built from textile using a Python script.
All content is contained in the textile scripts.
Do not edit the HTML files.

Building HTML from textile is done like so:
(generally) $ python build_page.py html/index.textile

(specifically) - to get the anaconda version
$ /opt/dmc/anaconda/64bit/bin/python build_page.py html/index.textile

On cube1, in /earthscope/geows-www:
find . -type f -name *.textile -print |xargs /opt/dmc/anaconda/64bit/bin/python build_page.py

------------
Subversion is accessed with the default, earthcube user id.
reminder --> check svn status possibly commit before starting a series of changes

svn status -u

update if needed, commit if needed
push new html files back to svn
