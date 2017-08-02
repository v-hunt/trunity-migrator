from setuptools import setup, find_packages


setup(
    name='trunity_migrator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'git+git://github.com/v-hunt/trunity-3-api-client.git',
      ],
    url='',
    license='MIT',
    author='hunting',
    author_email='VicHunting@yandex.ua',
    description='Library for migrating content from Trunity 2 to Trunity 3 learning platform.'
)
