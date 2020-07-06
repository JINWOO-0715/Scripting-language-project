from distutils.core import setup

setup(name='Seoul Movie',
      version='1.0',
      py_modules=['Gmail','make_graph','Map','Naver_Crowling',
                  'ReadFile','UI'],
      package_data = {
          'Seoul Movie':
              [
               'map.html',
               'osm.html',
               'sample.csv',
                'selectBG.c',
               'selectBG.pyd',
               'theater.xlsx']},

      )
