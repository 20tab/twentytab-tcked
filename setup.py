from setuptools import setup, find_packages
import tab_translation

setup(name='twentytab-tcked',
      version=tab_translation.__version__,
      description='A django application that use cked as texteditor. It update RichTextField with config parameter',
      author='20tab S.r.l.',
      author_email='info@20tab.com',
      url='https://github.com/20tab/twentytab-tcked',
      license='MIT License',
      install_requires=[
          'Django >=1.6',
          'django-appconf>=0.6',
          'hg+https://bitbucket.org/ssbb/django-cked#egg=django-cked'
      ],
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
      }
)
