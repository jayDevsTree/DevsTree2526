from setuptools import setup, find_packages

setup(
    name='mypackagejay',  # unique package name (lowercase, no spaces)
    version='0.0.1',
    packages=find_packages(),
    description='A simple greeting package',
    author='Jay Patil',
    author_email='your-email@example.com',
    url='https://github.com/yourusername/mypackagejay',  # Optional, can be your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
