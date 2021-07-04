from distutils.core import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(name='mobilechelonian',
      version='0.5',
      description='Turtles in the Jupyter Notebook',
      long_description = readme,
      author='Thomas Kluyver',
      author_email='',
      url='https://github.com/fkiaru/mobilechelonian',
      packages=['mobilechelonian'],
      package_data={'mobilechelonian': ['mobilechelonianjs/*.js']},
      classifiers=[
          'Framework :: IPython',
          'Intended Audience :: Education',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Artistic Software',
          'Topic :: Education',
      ],
      install_requires=['IPython', 'ipywidgets>=7.0.0'],
)
