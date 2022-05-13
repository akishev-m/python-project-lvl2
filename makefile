# Makefile

gendiff:
	poetry run gendiff

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/hexlet_code-0.2.0-py3-none-ane.whl

package-reinstall:
	rm dist/*
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

coverage:
	poetry run coverage xml

test-coverage:
	poetry run coverage run -m pytest -v
