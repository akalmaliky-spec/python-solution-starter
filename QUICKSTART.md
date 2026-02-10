# Quick Start Guide

## 5-Minute Setup

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/python-solution-starter.git
cd python-solution-starter
make install
```

### 2. Edit Your Solution

Open `main.py` and replace the `solve()` function:

```python
def solve():
    """Your solution logic here."""
    # Read input
    lines = read_input()
    data = parse_input(lines)
    
    # Process your solution
    result = process_data(data)
    
    return format_output(result)
```

### 3. Run Your Solution

```bash
make run
```

### 4. Test It

```bash
make test
```

## Key Utilities

### Decorators

```python
from utils import timer, memoize

@timer
def my_function():
    """Execution time will be logged."""
    pass

@memoize
def fibonacci(n):
    """Results are cached."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Logging

```python
from logger import logger

logger.info("Processing started")
logger.debug("Debug information")
logger.error("An error occurred")
```

### Configuration

Set environment variables in `.env`:

```bash
cp .env.example .env
# Edit .env with your values
```

Then use in your code:

```python
from config import DEBUG, LOG_LEVEL

if DEBUG:
    print("Debug mode enabled")
```

## Common Workflows

### Format Code
```bash
make format
```

### Check Code Quality
```bash
make lint
```

### View Available Commands
```bash
make help
```

## Project Structure

- `main.py` - Your solution code
- `utils.py` - Helper functions and decorators
- `config.py` - Configuration management
- `logger.py` - Logging setup
- `tests.py` - Unit tests
- `requirements.txt` - Dependencies
- `Makefile` - Development commands

See `README.md` for full documentation.
