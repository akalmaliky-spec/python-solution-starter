# Contributing Guidelines

Thank you for your interest in contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your changes
5. Commit and push to your fork
6. Submit a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-solution-starter.git
cd python-solution-starter

# Create virtual environment
make install

# Run tests
make test
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and returns
- Write docstrings for all functions and classes
- Run `make format` to format code automatically
- Run `make lint` to check for style violations

## Testing

- Write unit tests for new functionality
- Ensure all tests pass: `make test`
- Aim for good test coverage

## Commit Messages

Write clear and descriptive commit messages:
- Use imperative mood ("Add feature" not "Added feature")
- Keep messages concise
- Reference relevant issues if applicable

## Pull Request Process

1. Update documentation as needed
2. Add/update tests for new functionality
3. Ensure all tests pass
4. Ensure code is formatted with `make format`
5. Submit PR with clear description

## Questions?

Feel free to open an issue for questions or discussions.
