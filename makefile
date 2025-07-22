FILE_NAME = FACTORY_TEST_SW

CURRENT_DATETIME := $(shell date +%Y%m%d_%H%M%S)

PACKAGE_FOLDER_NAME := $(CURDIR)/$(FILE_NAME)$(CURRENT_DATETIME)

RM = rm -rf
RUN = poetry run


SUB_FOLDER = lnk_screen_picture RGB2GBR


sub_clean:
	@for dir in $(SUB_FOLDER); do \
        echo "Cleaning $$dir..."; \
        $(MAKE) -C $$dir clean || exit 1; \
    done


clean:sub_clean
	$(RM) $(CURDIR)/dist
	$(RM) $(CURDIR)/build
	$(RM) $(CURDIR)/$(FILE_NAME)*

.PHONY: test

test:
	$(RUN) python main.py

create_package_folder:
	mkdir -p $(PACKAGE_FOLDER_NAME)

	@for dir in $(SUB_FOLDER); do \
        make -C $$dir shell TARGET=$(PACKAGE_FOLDER_NAME)/$$dir|| exit 1; \
    done


package:clean create_package_folder

	pyinstaller main.spec
	cp $(CURDIR)/dist/main $(CURDIR)/$(FILE_NAME)$(CURRENT_DATETIME)
