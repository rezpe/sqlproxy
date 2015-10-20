from distutils.core import setup

requirements = [
    'flask',
    'flask-cors',
    'flask-restful',
    'pandas'
]

setup(
  name = 'SimpleSQLProxy',
  packages = ['SimpleSQLProxy'], # this must be the same as the name above
  install_requires=requirements,
  entry_points = {
        'console_scripts': ['simplesqlproxy=simplesqlproxy.sqlproxyws:main'],
    },
  version = '0.7',
  description = 'A simple sqlproxy for SQL LITE databases based on flask',
  author = 'Sebastien Perez',
  author_email = 'sebastien.perezvasseur@gmail.com',
  url = 'https://github.com/rezpe/sqlproxy', # use the URL to the github repo
  download_url = 'https://github.com/rezpe/sqlproxy/tarball/0.7', # I'll explain this in a second
  keywords = ['Web Service', 'SQL', 'sqlite'], # arbitrary keywords
  classifiers = [],
)
