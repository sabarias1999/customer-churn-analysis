# Contributing to Customer Churn Analysis

Thank you for considering contributing!

## Reporting Bugs

Include:
1. Clear, descriptive title
2. Steps to reproduce
3. Your environment (Python version, OS)
4. Observed vs. expected behavior

## Suggesting Enhancements

Include:
1. Clear, descriptive title
2. Step-by-step description
3. Why this would be useful

## Getting Started with Development

\\\ash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR-USERNAME/customer-churn-analysis.git
cd customer-churn-analysis

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Create feature branch
git checkout -b feature/your-feature-name
\\\

## Development Workflow

\\\ash
# Make your changes
# Test them
python dashboard_automation.py

# Format code
black dashboard_automation.py --line-length 100

# Check style
flake8 dashboard_automation.py --max-line-length=100

# Commit
git commit -m "feat(core): add new feature"

# Push
git push origin feature/your-feature-name
\\\

## Pull Request Guidelines

Before submitting:
- [ ] Code follows PEP 8
- [ ] Tests pass locally
- [ ] Docstrings added/updated
- [ ] README updated (if needed)

## Commit Message Format

\\\
<type>(<scope>): <subject>

<body>

<footer>
\\\

Types: feat, fix, docs, style, refactor, perf, test, chore

---

**Thank you for contributing!**
