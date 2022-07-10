from setuptools import setup

setup(
    name="redshift_module",
    version="0.1",
    packages=['redshift_module'],
    install_requires=['pyarrow','pandas','numpy','fastparquet','img2pdf']
)