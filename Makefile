test:
	poetry run pytest --cov=resolver --cov-report=term --cov-report=xml --junitxml=test-reports/junit.xml

lint:
	poetry run pre-commit run --all-files --show-diff-on-failure

dist: clean
	poetry build

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf .cache/ test-reports/
	rm -f .coverage coverage.xml
