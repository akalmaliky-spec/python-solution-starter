# Python Solution Starter

A clean, professional Python scaffold for coding problems—fast to start, easy to test, consistent structure.

## Features

- **Clean structure**: Well-organized project layout with pytest
- **Type hints**: Full type annotations for clarity
- **Docstrings**: Clear documentation following docstring conventions
- **stdin/stdout**: Ready for competitive programming input/output
- **Testing**: pytest setup with sample tests
- **Code quality**: black, ruff configuration included
- **CI/CD**: GitHub Actions workflow for automated testing and linting
- **Git-ready**: Pre-configured `.gitignore` for Python projects

## Project Structure

```
python-solution-starter/
├── main.py                      # Main solution module with solve() function
├── requirements.txt             # Project dependencies (development)
├── pyproject.toml              # Project config: pytest, black, ruff settings
├── tests/
│   ├── __init__.py
│   └── test_main.py            # pytest test suite (placeholder + sample tests)
├── README.md                    # This file
├── .gitignore                   # Git ignore rules for Python
└── .github/
    └── workflows/
        └── tests.yml           # GitHub Actions CI/CD workflow
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akalmaliky-spec/python-solution-starter.git
   cd python-solution-starter
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Solution

Execute the solution with a simple command:

```bash
python main.py < input.txt
```

Or pipe input directly:

```bash
echo -e "3\n1 2 3" | python main.py
```

### Example

**Input** (input.txt):
```
3
1 2 3
```

**Run:**
```bash
python main.py < input.txt
```

**Output:**
```
6
```

## Testing

### Run All Tests

```bash
pytest
```

### Verbose Output

```bash
pytest -v
```

### Run Specific Test

```bash
pytest tests/test_main.py::TestSolve::test_solve_sample_input_1 -v
```

### Run Tests with Coverage

```bash
pytest --cov=main tests/
```

## Code Quality

### Format Code with Black

```bash
black main.py tests/
```

### Check Code with Ruff

```bash
ruff check main.py tests/
```

### Check Formatting (without changes)

```bash
black --check main.py tests/
```

## Development

### Editing the Solution

1. Open `main.py`
2. Implement your solution logic in the `solve(input_data: str) -> str` function
3. Parse the input string as needed
4. Return the result as a string

**Example template in `main.py`:**
```python
def solve(input_data: str) -> str:
    """
    Main solution function.
    
    Args:
        input_data: Raw input string from stdin
    
    Returns:
        The solution result as a string
    """
    lines = input_data.strip().split('\n')
    # TODO: Parse input and implement solution
    result = "your solution here"
    return str(result)
```

### Adding Tests

Edit `tests/test_main.py` to add your own tests:

```python
def test_my_case(self):
    """Describe what this test checks."""
    input_data = "your input"
    expected = "expected output"
    result = solve(input_data)
    assert result == expected
```

### Adding Dependencies

1. Install a package:
   ```bash
   pip install package-name
   ```

2. Add to `requirements.txt`:
   ```bash
   pip freeze | grep package-name >> requirements.txt
   ```

3. Use in your code:
   ```python
   import package_name
   ```

## Continuous Integration

The repository includes a GitHub Actions workflow (`.github/workflows/tests.yml`) that:
- Runs tests with pytest
- Checks code formatting with black
- Lints code with ruff
- Tests on multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)

All checks run automatically on:
- Push to main
- Pull requests to main

## Common Commands

| Command | Purpose |
|---------|---------|
| `python main.py < input.txt` | Run solution |
| `pytest` | Run all tests |
| `pytest -v` | Run tests with details |
| `black main.py tests/` | Format code |
| `ruff check main.py tests/` | Lint code |
| `source .venv/bin/activate` | Activate venv (Linux/macOS) |
| `.venv\Scripts\activate` | Activate venv (Windows) |

## Tips

- Keep the `solve()` function pure—use only the input parameter
- Add helper functions as needed above or below `solve()`
- Write tests as you develop—they help verify correctness
- Use type hints for clarity: `def helper(x: int) -> int:`
- Comment complex logic with `# TODO:` for solution areas

## License

This project is open source and available under the MIT License. See [LICENSE](LICENSE) for details.

## Resources

- [Python docs](https://docs.python.org/3/)
- [pytest documentation](https://docs.pytest.org/)
- [black code formatter](https://github.com/psf/black)
- [ruff linter](https://docs.astral.sh/ruff/)

