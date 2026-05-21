.PHONY: install test simulate status clean

install:
	pip install -e .

install-dev:
	pip install -e .[dev]

test:
	python -m pytest tests/

simulate:
	python -m simulator.network_sim

status:
	python cli/10g.py status

topology:
	python cli/10g.py topology

clean:
	rm -rf __pycache__ *.pyc build/ dist/ *.egg-info
