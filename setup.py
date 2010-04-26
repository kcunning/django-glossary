from distutils.core import setup
from setuptools import find_packages

setup(version="0.1.4",
    name='django-glossary',
    description="A simple glossary system for Django-powered sites",
    long_description="",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    author='Katie Cunningham',
    author_email='katie.fulton@gmail.com',
    url='http://github.com/kcunning/django-glossary',
    requires=[
        "django (>=1.1.1)",
    ],
    packages=find_packages(exclude="test_project"),
    zip_safe=False,
    include_package_data=True,
)
