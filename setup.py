from setuptools import setup, find_packages

requires = [
        'django',
        'pillow',
        'gunicorn',
        'django-heroku'
        ]


setup(
    name='djangoCryptoSolve',
    version='',
    install_requires=['django'],
    packages=find_packages(),
    url='',
    license='',
    author='marcio.sobral',
    author_email='',
    description=''
)


#from setuptools import setup, find_packages

#setup(
   # name='djangoCryptoSolve',
    #version='',
    #install_requires=['django'],
    #packages=find_packages(),
    #url='',
    #license='',
    #author='marcio.sobral',
    #author_email='',
    #description=''
#)
