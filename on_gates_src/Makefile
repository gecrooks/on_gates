
.DEFAULT_GOAL := help

# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


version: ## Extract version from git tag and write to version.tex
	git describe --tags  --abbrev=0 > version.txt || echo "No tags"
	@git describe --tags

build:  version  ## Build latex
	latexmk -xelatex -g on_gates.tex

edit:  ## Open all tex documents
	open *.tex


bib: ## Copy citations from master bibliogrpahy to local bibliogrpahy
	bibtool -s -d -x on_gates.aux ../../gec_bibliography/gec_bibliography.bib > on_gates_no_edit.bib


clean:	## Clean
	latexmk -C


circuits:  ## Build latex circuits
	cd circuits && ./latex_circuits.py


.PHONY: help
.PHONY: circuits
.PHONY: version version_check