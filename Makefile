.POSIX:
PREFIX = ~/.local
CONFIG = ~/.config
PIPVER = `command -v pip3 || command -v pip`
install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f chameleon.py $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "chameleon.py has been installed to $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	mkdir -p $(DESTDIR)$(CONFIG)/chameleon
	cp -f config.yaml $(DESTDIR)$(CONFIG)/chameleon/config.yaml
	@echo "config file for chameleon.py created in $(DESTDIR)$(PREFIX)/config/config.yaml"
	@echo "installing $(PIPVER) dependencies"
	@$(PIPVER) install --user whichcraft || echo "dependencies couldn't be installed install pip and rerun"
uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "removed $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	rm -rf $(DESTDIR)$(CONFIG)/chameleon
	@echo "removed $(DESTDIR)$(CONFIG)/chameleon"
	$(PIPVER) uninstall whichcraft
.PHONY: install uninstall pipversion
