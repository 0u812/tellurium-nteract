from setuptools import setup

setup(name             = 'tellurium-nteract',
      version          = "2.0.0",
      description      = 'Metapackage for installing Tellurium nteract deployment',
      license          = 'Apache 2.0',
      author           = 'J Kyle Medley',
      url              ='https://github.com/0u812/tellurium-nteract' ,
      packages         = [],
      install_requires = [
      # tellurium
      'tellurium>=2.0.0',
      # core packages
      'libroadrunner>=1.4.16', 'rrplugins>=1.1.8',
      'tesbml>=5.15.0', 'tesedml>=0.4.2', 'tecombine>=0.2.0',
      'antimony>=2.9.1', 'phrasedml>=1.0.5', 'sbml2matlab>=0.9.1',
      # cust
      'temagics>=1.0.0',
      # jupyter
      'jupyter-core>=4.3.0', 'jupyter-client>=4.4.0',
      'ipython>=5.2.2', 'ipykernel>=4.5.2',
      # aux
      'plotly>=2.0.5',
      'Jinja2>=2.9.5',
      'appdirs>=1.4.3',
      # should be inherited
      'numpy>=1.12.0', 'matplotlib>=2.0.0',
      # misc
      'lmfit>=0.9.5',
      ],
)
