
.DEFAULT_GOAL := help

# Kudos: Adapted from Auto-documenting default target
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


build: ## Build on_gates
	git tag --points-at HEAD > version.txt
	latexmk -xelatex on_gates.tex


edit:  ## Open all tex documents
	open *.tex


clean:	## Clean
	latexmk -C


circuits:  ## Build latex circuits
	cd circuits && ./latex_circuits.py


version: _version_check build ## Build and tag new version `>make version TAG=0.6`
	git add on_gates.pdf
	git commit -m "New version ${TAG}"
	git tag -a ${TAG} -m "v${TAG}"
	@echo "To complete push: git push origin ${TAG}"

_version_check:
	@echo "Checking for clean git repo..."
	echo ${TAG} > version.tex


.PHONY: help
.PHONY: circuits
.PHONY: version version_check