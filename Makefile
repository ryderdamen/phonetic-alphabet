.PHONY: publish-dev
publish-dev:
	@echo "Publishing Dev"; \
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* --skip-existing

.PHONY: publish
publish:
	@echo "Publishing"
	twine upload dist/* --skip-existing

.PHONY: build
build:
	@echo "Building Dist..."; \
	python setup.py sdist bdist_wheel