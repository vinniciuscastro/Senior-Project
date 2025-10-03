Mutest

⚡ Mutest is a mutation testing tool designed to evaluate the effectiveness of your test suites. It introduces small, controlled changes (mutations) into the source code and checks whether existing tests can detect them. This helps you identify weak spots in your testing strategy.

📖 Table of Contents

About

Features

How It Works

Configuration

Examples

Roadmap

Contributing

🔍 About

Mutest was created to make test quality visible. Unlike traditional coverage tools that measure what code is executed, mutation testing evaluates whether tests can detect real bugs.

This project is also a senior capstone project, combining QA principles with software engineering best practices like CI/CD integration, automated test generation, and extensibility.

🚀 Features

Mutation engine to generate code variations

Test runner integration to detect surviving mutants

Metrics and reporting (mutation score, killed vs surviving mutants)

CI/CD pipeline compatibility

Extensible design for new mutation operators

(Optional) Visual regression or accessibility testing hooks

⚙️ How It Works

Mutest parses your source code

Applies mutation operators (for example: changing == to !=, removing branches)

Re-runs your test suite against the mutated code

Records whether the tests fail (mutant killed) or pass (mutant survived)

Generates a mutation score report

⚡ Configuration

Customize behavior using a config file, for example mutest.config.json:

{
  "source": "src",
  "tests": "tests",
  "mutators": ["arithmetic", "conditional", "logical"],
  "report": "html"
}

📊 Examples

Example Project

CI/CD Integration Guide

🛠 Roadmap

Mutest is currently in active development as part of a senior project. The planned timeline of milestones is:

 Weeks 1–2: Research mutation testing concepts and Abstract Syntax Tree (AST) basics
Goal: Research foundation and parsing prototype

 Weeks 3–4: Build basic mutant generator with three operator types (arithmetic, conditional, logical)
Goal: Core mutation engine prototype

 Weeks 5–6: Implement test execution and kill/survive tracking
Goal: First end-to-end test run

 Week 7: Add mutation score calculation
Goal: Mutation scoring integrated

 Weeks 8–9: Develop basic CLI and simple reporting (text or HTML output)
Goal: Usable CLI with reporting

 Weeks 10–11: Add minimal CI/CD integration (for example: GitHub Actions)
Goal: Pipeline-ready prototype

 Week 12: Write user and developer documentation
Goal: Complete documentation

 Week 13: Perform tool testing and bug fixing
Goal: Stable release candidate

 Week 14: Final polish and presentation preparation
Goal: Demo-ready and project presentation

🤝 Contributing

Contributions, issues, and feature requests are welcome.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request