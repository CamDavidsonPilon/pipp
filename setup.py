from setuptools import setup, find_packages

setup(
    name='pipp',
    version='0.0.1',
    description='pip install with recommendations',
    author='Cameron Davidson-Pilon',
    author_email='cam.davidson.pilon@gmail.com',
    license='MIT',
    keywords=['pip'],
    url='',
    packages=find_packages(),
    package_data={
        'pip': ['data/recommendations.json',]
    },
    install_requires=[
        'pip',
    ],
    entry_points = {
        'console_scripts': [
            'pipp = pipp.pipp:main',
        ],
    }
)