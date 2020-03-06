python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install -i https://test.pypi.org/simple/ ccreport
pip install -i https://test.pypi.org/simple/ ccreport --upgrade

twine upload dist/*
pip install ccreport
pip install ccreport --upgrade
