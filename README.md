#### install pytest
```
$ sudo apt install python3-pytest
```

#### run test
run the command under the test project directory
```
$ python3 -m pytest
$ python3 -m pytest --verbose
$ python3 -m pytest --quiet
$ python3 -m pytest --exitfirst
$ python3 -m pytest --maxfail=1
$ python3 -m pytest --junit-xml report.xml

$ python3 -m pytest tests
$ python3 -m pytest tests/test_math.py
$ python3 -m pytest tests/test_math.py::test_one_plus_one
$ python3 -m pytest -k "one"

$ python3 -m pytest -m "math"
!!! ensure "markers" configured in pytest.ini

# show manual
$ python3 -m pytest --help
```

#### install some useful plugins
```
$ pip3 install pytest-html
$ python -m pytest --html=report.html
```

measuring coverage
```
$ pip3 install pytest-cov
# or
$ apt install python3-pytest-cov

$ python3 -m pytest --cov=tests
$ python3 -m pytest --cov=tests --cov=test_class
$ python3 -m pytest --cov=tests --cov-report html
```

distributed testing and loop-on-failing modes
```
$ pip3 install pytest-xdist
# or
$ apt install python3-pytest-xdist

$ python3 -m pytest -n 3
```

for behavioral driven development (bdd)
```
$ pip3 install pytest-bdd
```

modules for api testing
```
$ pip3 install assertpy lxml jsonpath-ng cerberus
```

#### reference
https://testautomationu.applitools.com/
https://docs.pytest.org/en/7.1.x/
https://pypi.org/project/pytest/
https://github.com/AndyLPK247/tau-intro-to-pytest
https://github.com/AndyLPK247/tau-pytest-bdd

further reading
https://tavern.readthedocs.io/en/latest/
https://hypothesis.readthedocs.io/en/latest/

pytest plugins
https://pypi.org/project/pytest-html/
https://pypi.org/project/pytest-xdist/
https://pypi.org/project/pytest-cov/
https://pypi.org/project/pytest-bdd/

https://github.com/assertpy/assertpy
https://docs.python-cerberus.org/en/stable/
