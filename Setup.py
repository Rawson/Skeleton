try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'M. Gardiner',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ar@mgardiner.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)


# http://learnpythonthehardway.org/book/ex46.html
# Make a copy of your skeleton directory. Name it after your new project.
# Rename (move) the NAME module to be the name of your project or whatever you want to call your root module.
# Edit your setup.py to have all the information for your project.
# Rename tests/NAME_tests.py to also have your module name.
# Double check it's all working using nosetests again.
# Start coding. 