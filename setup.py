from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      install_requires=['psutil','platform','socket','multiprocessing','timeit','math'],
      author="Aonghus Lawlor",
      author_email="aonghus.lawlor@ucd.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )
