
.DEFAULT_GOAL := help

# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


version: ## Extract version from git tag and write to version.txt
	git tag --points-at HEAD > version.txt


build: ## Build on_gates
	latexmk -xelatex on_gates.tex


clean:	## Clean
	latexmk -C


circuits:  ## Build latex circuits
	cd circuits && ./latex_circuits.py


.PHONY: help
.PHONY: circuits