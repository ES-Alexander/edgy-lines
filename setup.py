import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='edgy-lines',
    version='0.0.1',
    author='ES-Alexander',
    auther_email='sandman.esalexander@gmail.com',
    description='A package for processing edges and lines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ES-Alexander/edgy-lines',
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
    ],
)
