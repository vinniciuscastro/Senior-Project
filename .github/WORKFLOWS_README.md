# GitHub Actions Workflows for Mutest

This document describes the CI/CD workflows set up for the Mutest mutation testing tool.

## Workflows Overview

### 1. CI/CD Pipeline (`ci.yml`)
**Triggers:** Push and Pull Requests to `main` branch

**What it does:**
- Tests the codebase across **4 Python versions** (3.9, 3.10, 3.11, 3.12)
- Runs pytest with timeout protection (10 seconds per test)
- Generates **test coverage reports** using pytest-cov
- Uploads coverage to **Codecov** for tracking over time
- Creates test result artifacts for each Python version
- Generates HTML coverage report (viewable in artifacts)

**Benefits:**
- Ensures compatibility across multiple Python versions
- Tracks code coverage metrics to identify untested code
- Provides detailed test reports for debugging failures

**How to view coverage:**
1. Check the Codecov integration on your GitHub repo
2. Download the `coverage-report` artifact from workflow runs
3. Open `htmlcov/index.html` in your browser

---

### 2. Code Quality (`code-quality.yml`)
**Triggers:** Push and Pull Requests to `main` branch

**What it does:**
- Checks code formatting with **Black** (your existing formatter)
- Runs **flake8** linting to catch:
  - Python syntax errors
  - Undefined names and variables
  - Code complexity issues
  - Style violations

**Benefits:**
- Maintains consistent code style across contributions
- Catches common Python errors before they reach production
- Enforces best practices automatically

**Note:** If Black finds formatting issues, run locally:
```bash
black Mutest/
```

---

### 3. Security Scanning (`security.yml`)
**Triggers:**
- Push and Pull Requests to `main` branch
- **Weekly schedule** (Sundays at midnight UTC)

**What it does:**
- Checks dependencies for **known security vulnerabilities** using Safety
- Runs **Bandit** security linter to find security issues in your code
- Performs **CodeQL** static analysis for advanced vulnerability detection
- Uploads security reports to GitHub Security tab

**Benefits:**
- Proactive security monitoring
- Identifies vulnerable dependencies before deployment
- Detects common security anti-patterns (SQL injection, hardcoded secrets, etc.)

**Weekly scans** ensure you're notified of newly discovered vulnerabilities.

---

### 4. Release Automation (`release.yml`)
**Triggers:** When you push a **version tag** (e.g., `v1.0.0`)

**What it does:**
- Builds Python distribution packages (wheel and source)
- Creates a GitHub Release with auto-generated release notes
- Attaches distribution files to the release
- (Optional) Publishes to PyPI when enabled

**How to create a release:**
```bash
git tag v1.0.0
git push origin v1.0.0
```

**Benefits:**
- Automated release process
- Professional release notes
- Distribution packages ready for installation
- Optional PyPI publishing (disabled by default)

**To enable PyPI publishing:**
1. Create a PyPI account and get an API token
2. Add `PYPI_TOKEN` to GitHub Secrets
3. Change `if: false` to `if: true` in the workflow

---

## Quick Reference

| Workflow | Purpose | Runs On | Artifacts |
|----------|---------|---------|-----------|
| `ci.yml` | Test & Coverage | Every push/PR | Test results, Coverage HTML |
| `code-quality.yml` | Linting & Formatting | Every push/PR | None |
| `security.yml` | Security Scanning | Push/PR + Weekly | Bandit report |
| `release.yml` | Create Releases | Version tags | Distribution packages |

## Status Badges

Add these to your README.md to show workflow status:

```markdown
![Python Tests](https://github.com/YOUR_USERNAME/Senior-Project/workflows/Python%20Tests/badge.svg)
![Code Quality](https://github.com/YOUR_USERNAME/Senior-Project/workflows/Code%20Quality/badge.svg)
![Security Scan](https://github.com/YOUR_USERNAME/Senior-Project/workflows/Security%20Scan/badge.svg)
```

Replace `YOUR_USERNAME` with your GitHub username.

## Next Steps

1. **Push these workflows** to your GitHub repository
2. **Enable GitHub Actions** in your repository settings (if not already enabled)
3. **Set up Codecov:**
   - Visit https://codecov.io
   - Sign in with GitHub
   - Enable coverage for your repository
4. **Optional:** Set up PyPI tokens for automated publishing
5. **Monitor** the Actions tab to see workflows running

## Troubleshooting

### Tests failing?
- Check the test results artifact in the workflow run
- Review the pytest output in the workflow logs
- Ensure all dependencies are in `requirements.txt`

### Code quality checks failing?
- Run `black Mutest/` locally to fix formatting
- Review flake8 warnings and fix identified issues

### Security warnings?
- Review the Bandit report artifact
- Update vulnerable dependencies
- Fix security issues identified by CodeQL

## Support

For issues with these workflows, check:
- GitHub Actions documentation: https://docs.github.com/actions
- Pytest documentation: https://docs.pytest.org
- Black documentation: https://black.readthedocs.io
