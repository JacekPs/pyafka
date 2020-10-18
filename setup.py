import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='pyafka',
    packages=find_packages(include=['pyafkalib']),
    version='0.2.0',
    description='Kafka framework',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Jacek Kufel',
    license='Apache License 2.0 ',
    install_requires=['confluent-kafka==1.5.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest == 4.4.1', 'pytest-mock == 3.3.1'],
    test_suite='tests',
)