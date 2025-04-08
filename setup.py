from setuptools import setup, find_packages

setup(
    name='TSP-Solver',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'bokeh>=2.4.0',
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'pytest>=6.2.5'
    ],
    author='TSP Solver Team',
    author_email='tsp-solver@example.com',
    description='A Python implementation of the Traveling Salesman Problem using various optimization algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aviennx/TSP-Solver',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'tsp-solver=TSPApp.main:main',
        ],
    },
)
