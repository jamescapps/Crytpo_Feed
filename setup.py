from setuptools import setup

setup(name='Crypto_Feed',
      version='0.1.0',
      packages=['project'],
      entry_points={
          'console_scripts': [
              'cryptofeed = project.__main__:main'
          ]
      },
      )