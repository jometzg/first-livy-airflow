from setuptools import setup, find_packages

setup(
    name='airflow-custom-livy-operator',
    version='0.2.0',
    author='John Metzger',
    author_email='john.metzger@microsoft.com',
    description='A custom Apache Airflow operator that fixes Livy for Microsoft Fabric',
    packages=find_packages(),
    install_requires=[
        'apache-airflow>=2.0.0',
        'apache-airflow-providers-apache-livy>=2.0.0',
        'apache-airflow-providers-microsoft-fabric>=2.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)