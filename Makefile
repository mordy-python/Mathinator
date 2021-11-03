setup:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements-dev.txt
fmt:
	python -m black mathinator/
clean:
	rm -rfv __pycache__
build:
	python -m build