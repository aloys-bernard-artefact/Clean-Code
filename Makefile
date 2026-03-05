
# Makefile for Clean Code 2 project
.PHONY : help hello load_data process_data save_data run tests

help :
	@echo "Available targets:"
	@echo "  hello        - Print 'Hello, World!'"
	@echo "  load_data    - Simulate loading data"
	@echo "  process_data - Simulate processing data"
	@echo "  save_data    - Simulate saving data"
	@echo "  run           - Execute the full data pipeline"

hello :
	@echo "Hello, World!"

load_data :
	@echo "📥 Loading data..."

process_data :
	@echo "🔥 Processing data..."

save_data :
	@echo "💾 Saving data..."

run : load_data process_data save_data
	echo "🚀 All steps completed successfully!"

tests :
	@echo "Running tests..."
	PYTHONPATH=. pytest -v tests/
