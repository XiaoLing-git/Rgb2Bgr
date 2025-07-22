RM = rm -rf
RUN = poetry run


clean:
	$(RM) $(CURDIR)/dist

.PHONY: test

test:
	$(RUN) python main.py