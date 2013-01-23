
PYTEST_OPTIONS = -v
PYTEST_JENKINS = --junitxml=./result.xml

.PHONY: test jenkins

test:
	py.test $(PYTEST_OPTIONS)

jenkins:
	py.test $(PYTEST_JENKINS)
