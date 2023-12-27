install:
	pip install -r requirements.txt

tests:
	pytest -v tests/ cov-fail-under=100

lint-diffs:
	flake8 $$(git diff --nameonly master | egrep *.py)

lint:
	flake8
