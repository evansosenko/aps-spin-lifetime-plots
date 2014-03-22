all: plots

plots:
	@python plots >> stdout.log 2>> stderr.log
	@$(foreach x,$(wildcard plots/plot_*.py),python $(x) >> stdout.log 2>> stderr.log;)

clean:
	@rm -rf build
	@rm stdout.log
	@rm stderr.log

.PHONY: build plots
