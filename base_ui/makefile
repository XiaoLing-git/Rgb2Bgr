THIS_DIR = $(CURDIR)

THIS_DIR_TEMP_FILE = $(THIS_DIR)/*.log

BK_CMD = $(CURDIR)/bk_loader.exe

CURRENT_DIR_NAME = $(notdir $(shell pwd))

SUB_FOLDER =

clean:
	rm -f $(THIS_DIR_TEMP_FILE)

format:
	black $(THIS_DIR)/
	mypy $(THIS_DIR)/

test:clean
	$(BK_CMD) download -p $(PORT) -i $(CONFIG)
	rm -f $(THIS_DIR_TEMP_FILE)

flash: clean
	python $(UNIT_TEST_FILE_PATH) lock-pro-wifi COM7 --product-id W1114000 --mac B0E9FE7357D6
	rm -f $(THIS_DIR_TEMP_FILE)

debug:clean
	python $(UNIT_TEST_FILE_PATH) lock-pro-wifi $(PORT) --product-id $(PRODUCT_ID) --mac $(MAC)
	rm -f $(THIS_DIR_TEMP_FILE)

shell_create_folder:
ifdef TARGET
	mkdir -p $(TARGET)
	@for dir in $(SUB_FOLDER); do \
        mkdir -p $(TARGET)/$$dir|| exit 1; \
    done
endif

shell:shell_create_folder
ifdef TARGET
	@for dir in $(SUB_FOLDER); do \
  		cp -r $(THIS_DIR)/$$dir/* $(TARGET)/$$dir \
  		|| exit 1; \
    done
endif