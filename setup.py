from setuptools import setup

setup(name='memedensity',
      version='0.0.2',
      description='Tells you the amount of memes in your facebook feed',
      url='https://github.com/lakshaykalbhor/MemeDensity',
      author='Lakshay Kalbhor',
      author_email='lakshaykalbhor@gmail.com',
      license='MIT',
      packages =['MemeDensity'],
      install_requires=[
          'requests',
          'argparse',
          'selenium',
        ],
      entry_points={
        'console_scripts': ['memedensity=MemeDensity.command_line:main'],
      }
      )