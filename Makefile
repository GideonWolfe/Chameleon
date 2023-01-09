PREFIX 			= ~/.local
CONFIG 			= ~/.config
PIPVER 			= `command -v pip3 || command -v pip`
CONF_FILE 	= $(XDG_CONFIG_HOME)/chameleon/config.yaml
CURRENT_DIR = $(PWD)

install:
	mkdir -p $(PREFIX)/bin
	cp -f chameleon.py $(PREFIX)/bin/chameleon.py
	@echo "chameleon.py has been installed to $(PREFIX)/bin/chameleon.py"
	mkdir -p $(CONFIG)/chameleon
	-mv $(CONF_FILE) $(CONF_FILE)-backup 2>/dev/null
	-cp -r $(CURRENT_DIR)/config-template.yaml $(CONF_FILE)
	@echo "installing $(PIPVER) dependencies"
	@$(PIPVER) install whichcraft || echo "dependencies couldn't be installed install pip and rerun"
	@$(PIPVER) install pywal || echo "dependencies couldn't be installed install pip and rerun"
uninstall:
	-rm -f $(PREFIX)/bin/chameleon.py
	@echo "removed $(PREFIX)/bin/chameleon.py"
	-rm -rf $(CONFIG)/chameleon
	@echo "removed $(CONFIG)/chameleon"
