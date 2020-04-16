=======
bldtool
=======

bldtool is a Django app to that adds management commands to support
developers with standard quality and build support.  These buildtools
assume python django server side, and TypeScript/react client side.

Quick start
-----------

1. Build the bldtool installer from srouce
   - cd <source>
   - python setup.py sdist

2. Create your django site and vm
   - virtualenv -p python3.8 env
   - . env/bin/activate
   - pip install django
   - django-admin startproject <site>
   - cd site
   - pip install <src>dist/django-bldtool-X.Y.tar.gz
   - Add "bldtool" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bldtool',
    ]

5. Run "python manage.py qc" and update the errors until it runs
   clean.  In particular update the manage.py so that the setting
   import exception does not need to be covered:
      except ImportError as exc: # pragma: no cover

6. When creating new apps be sure to:
   - Remove the generated files you will not be using.
   - Update the generated files with docstrings to pass lint.

Project Requirements
------------------

This tool assumes:
1. django
2. django_rest_framework
3. typescript for js-react components.
4. The client side is not a single page react application, but is
   served with typical django templates that may have react components
   as the body of some pages.

Management Commands
----------------

lint
^^^^
This runs pylint on all python files on all the modules.
It also runs jslint on all typescript files.


coverage
^^^^^^^^
This runs tests and generates a coverage report on all apps.

qc
^^^

This runs both lint and coverage.
