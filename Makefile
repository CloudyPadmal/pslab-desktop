DESTDIR =

# Variable CUSTOM will be 'true' if we are not in the context of building a debian package (you must be root or use
# fakeroot, the directory .. is supposed to be the root directory of the package FOSSASIA PSLab
CUSTOM = $(shell cd ..; if [ -x /usr/bin/dh_testroot -a -x /usr/bin/dh_testdir ] && dh_testroot && dh_testdir; then echo false; else echo true; fi)

# Find library installation path
INSTALL_PATH = $(patsubst Location:,,$(shell python3 -m pip show PSL_Apps | grep Location))
INSTALL_PATH_LEN = $(shell echo $(INSTALL_PATH) | wc -c)

# Finds every UI file in the repository
UI_SOURCES = $(shell find . -name "*.ui")
# Generates a list of UI files with `auto_` prefix to denote that the python GUI files are autogenerated
UI_FILES = $(shell for f in $(UI_SOURCES); do path=$$(dirname $$f); g=$$(basename $$f); echo $$path/auto_$$g | sed 's/.ui/.py/'; done)
# Store old UI file names
OLD_UI_FILES = $(patsubst %.ui, %.py, $(UI_SOURCES))

# Build all sources with Python3
all: $(UI_FILES)
	python3 setup.py build

# Rule to generate UI python files from UI source
auto_%.py: %.ui
	@echo Generating UI file for $@
	@pyuic5 $< > $@

# Debug method to test if make is listing the new UI files
showUIFiles:
	@echo $(UI_FILES) | tr " " "\n"
# Debug method to test if make is listing the old UI files
showOldUIFiles:
	@echo $(OLD_UI_FILES) | tr " " "\n"

clean:
	# Remove build resources from repo directory
	@rm -rf PSL_Apps.egg-info build
	@if $(CUSTOM); then rm -rf /usr/share/pslab/; fi
	@find . -name "*~" -o -name "*.pyc" -o -name "__pycache__" | xargs rm -rf
	@if $(CUSTOM); then make uninstall_custom; fi

uninstall_custom:
	# Remove PSLab UI python package
	@if [ ${INSTALL_PATH_LEN} -gt 2 ]; then sudo rm -rf $(INSTALL_PATH)/PSL_* ; fi
	# Remove PSLab UI resources
	@sudo rm -rf $(DESTDIR)/usr/share/pslab/PSL_Resources
	# Remove the executable script
	@sudo rm -f /usr/local/bin/Experiments

install:
	# Install PSLab UI resources to a local directory
	mkdir -p $(DESTDIR)/usr/share/pslab/PSL_Resources
	cp -r PSL_Resources/* $(DESTDIR)/usr/share/pslab/PSL_Resources/
	# create distributions for current python distribution
	python3 setup.py install

cleanUIFiles:
	@find . -name "auto_*" | xargs rm -rf
	@echo Removed auto-generated UI .py files
