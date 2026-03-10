.PHONY: tests


collect:
	./scripts/collect.sh

preprocess:
	./scripts/preprocessed.sh

train:
	./scripts/train.sh

bash:

	./scripts/collect.sh && \
	 ./scripts/preprocessed.sh && \
	./scripts/train.sh

tests:
	pytest tests/test_collect.py && \
	pytest tests/test_preprocessed.py && \
	pytest tests/test_model.py

all: