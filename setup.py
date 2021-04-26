from setuptools import setup, find_packages

setup(
    name='demo_multilabel_classification',
    version='1.1',
    packages=find_packages(),
    package_data={
        '': ['trained_models', 'trained_models/*.pkl']
    },
    url='',
    license='bsd',
    author='aurelien.massiot & lea.naccache',
    author_email='amassiot@octo.com, lnaccache@octo.com',
    description='Demo for multilabel classification article',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'plotly.express',
        'streamlit',
        'watchdog'
    ],
    extras_require={
        'test': ['pytest',
                 'mock']
    }
)
