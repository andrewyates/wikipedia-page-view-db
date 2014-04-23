wikipedia-page-view-db
===============

Downloads [Wikipedia page view statistics](http://dumps.wikimedia.org/other/pagecounts-raw/) and imports them into a DB.
Code is licensed under the GNU GPL v2.

Configuration
-------------
* Edit *orm/settings.py* (see comments in file)
* Initialize DB: *python manage.py syncdb*

Usage
-----
These commands may be repeated to find and import new page count files.
Files are deleted after they have been downloaded and imported, but
files that have already been imported will not be re-downloaded.
* Find page count files to download: *python find_urls.py*
* Import page view counts into the DB: *TODO*
