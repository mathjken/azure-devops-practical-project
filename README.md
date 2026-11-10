
# Azure DevOps Practical Project

## Overview

This project demonstrates a basic Python application with automated testing and Continuous Integration using Azure DevOps.

The application calculates the total cost of an order using its unit price and quantity. It includes input validation and automated tests written with pytest.

## Technologies

- Python 3.12
- pytest
- Git
- Azure Repos
- Azure Pipelines

## Project Structure

```text
azure-devops-practical-project/
├── app.py
├── test_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── azure-pipelines.yml
```

## Local Setup

Clone the repository:

```bash
git clone <repository-url>
cd azure-devops-practical-project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Expected output:

```text
Order total: £75.00
```

## Run Automated Tests

```bash
pytest -v
```

The test suite checks:
- Normal order calculations.
- Zero quantity.
- Negative price validation.
- Negative quantity validation.

## Continuous Integration

Azure Pipelines will be configured to install dependencies and execute the automated test suite whenever changes are pushed to the main branch.

## Project Objective

To gain practical experience with Azure DevOps, source control management, automated testing, CI pipelines and work item tracking.

