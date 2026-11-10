# Azure DevOps CI Practical Project

## Overview

This project demonstrates a Python order calculation application developed and managed using Azure DevOps.

The application calculates the total cost of an order using its unit price and quantity. It includes input validation to prevent negative values and automated tests written with pytest.

The project demonstrates practical experience with Git, Azure Repos, Azure Boards, Azure Pipelines, feature branching, pull requests and Continuous Integration (CI).

## Technologies

- Python 3.12
- pytest
- Git
- Azure Repos
- Azure Boards
- Azure Pipelines
- YAML

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

## Application Functionality

The application provides an order total calculation function.

It includes validation to reject negative prices and quantities.

Example:

```python
calculate_total(25.00, 3)
```

Expected output:

```text
75.0
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

## Automated Testing

Run the test suite:

```bash
pytest -v
```

The four automated tests cover:

- Normal order calculations.
- Zero quantity.
- Negative price validation.
- Negative quantity validation.

All four tests passed in the final Azure Pipelines run.

## Azure DevOps CI Workflow

The project uses Azure Pipelines to automate testing.

The pipeline:

1. Uses a Microsoft-hosted Ubuntu agent.
2. Sets up Python 3.12.
3. Installs project dependencies.
4. Executes the pytest test suite.

The pipeline runs when changes are pushed to the `main` branch.

## Branching and Pull Request Strategy

Development changes are made in feature branches and submitted through pull requests.

The `main` branch has the following policies configured:

- Required Python CI build validation.
- Automatic pipeline execution for pull requests.
- Optional linked-work-item checking.

The pull request was successfully validated, approved and merged into `main`. A subsequent pipeline run also completed successfully, with all four automated tests passing.

## Azure Boards

Azure Boards was used to track the project work through issues and the Kanban board.

Work items were also linked to relevant development evidence, including a commit and a successful pipeline build.

## Key Learning Outcomes

This project provided practical experience in:

- Managing source code with Git and Azure Repos.
- Creating and working with feature branches.
- Managing work items with Azure Boards.
- Configuring YAML-based CI pipelines.
- Automating Python tests with pytest.
- Configuring branch protection and build validation.
- Creating, reviewing and completing pull requests.
- Verifying successful post-merge CI execution.

## Project Scope

This is a CI-focused practical project. It demonstrates automated testing and source-control workflows; it does not include a production deployment pipeline.
