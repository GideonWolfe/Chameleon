.POSIX:
PREFIX = ~/.local
PIPVER = pip3
install:
	@cp -f chameleon.py $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "chameleon.py has been installed to $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	@echo "installing $(PIPVER) dependencies"
	@$(PIPVER) install --user whichcraft
uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/chameleon.py
	@echo "removed $(DESTDIR)$(PREFIX)/bin/chameleon.py"
	@$(PIPVER) uninstall --user whichcraft
.PHONY: install uninstall
