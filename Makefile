all: analysis

analysis:
	@python plots >> stdout.log 2>> stderr.log

clean:
	@rm -rf build
	@rm stdout.log
	@rm stderr.log

.PHONY: build plots
