.PHONY: build test
default: build

build:
	docker build -t eshackathon/keywords .

test:
	-rm -rf /tmp/i3-keywords
	mkdir /tmp/i3-keywords
	cp input.json /tmp/i3-keywords/input.json
	docker run -e LANG=C.UTF-8 --volume /tmp/i3-keywords:/app/work eshackathon/keywords work/input.json 10 > /tmp/i3-keywords/output.json
	@echo --- START OUTPUT ---
	@cat /tmp/i3-keywords/output.json
	@echo --- END OUTPUT ---
	-rm -rf /tmp/i3-keywords

shell:
	docker run -it --entrypoint=/bin/sh eshackathon/keywords
