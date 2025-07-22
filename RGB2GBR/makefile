THIS_DIR = $(CURDIR)

THIS_DIR_TEMP_FILE = $(THIS_DIR)/*.log

CURRENT_DIR_NAME = $(notdir $(shell pwd))

SUB_FOLDER = bin

clean:
	rm -rf $(THIS_DIR)/temp/*.jpg
	rm -rf $(THIS_DIR)/temp/*.png
	rm -rf $(THIS_DIR)/save/*.jpg
	rm -rf $(THIS_DIR)/save/*.png

format :
	black $(THIS_DIR)/
	mypy $(THIS_DIR)/

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