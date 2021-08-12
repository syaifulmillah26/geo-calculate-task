SHELL:=/usr/bin/env bash

coverage:
	python -m coverage run -m unittest discover -v
