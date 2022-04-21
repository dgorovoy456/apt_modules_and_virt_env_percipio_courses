from setuptools import setup

setup(
    name='calc',
    version='1.0',
    description='My new Python module',
    author='Denys',
    author_email='dgorovoy456@gmail.com',
    url='some.come',
    py_modules=['calc']

)

# python3 setup.py sdist // to convert calc package to distribution file
# pip install calc-1.0.tar.gz // to install package inside virtual environment
