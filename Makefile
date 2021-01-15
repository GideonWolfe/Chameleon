.POSIX:
PREFIX = ~/.local
PIPVER = `command -v pip3 || command -v pip`
install:
	cp -f chameleon.py $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "chameleon.py has been installed to $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	@echo "installing $(PIPVER) dependencies"
	@$(PIPVER) install --user whichcraft || echo "dependencies couldn't be installed install pip and rerun"
uninstall:
	rm -rf $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "removed $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	$(PIPVER) uninstall whichcraft
.PHONY: install uninstall pipversion
