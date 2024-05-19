# Frontend Development Notes

## React & TypeScript

The frontend of our Movie Picture application is written in TypeScript and utilizes the React framework. This ensures strict type checking and follows a component-based architecture.

## eslint

This project utilizes eslint for maintaining code quality. It's crucial to adhere to the rules specified in our `.eslintrc` file. The linter automatically checks code for style issues, potential bugs, and enforces design principles.

## React Testing Library

Our application employs the React Testing Library for unit testing. This testing library focuses on the user's perspective, crafting tests that resemble user interactions with the app.

## GitHub Actions

GitHub Actions automate our software development workflows. They handle linting, testing, and building the app upon a `pull_request` to the `main` branch. Additionally, deployments occur upon a `push` to the `main` branch.

## Docker

We containerize our frontend application using Docker, facilitating consistency and ease of deployment.

## Kubernetes

Deployment to our existing Kubernetes cluster is automated through GitHub Actions workflows.

## AWS & Terraform

AWS hosts our Kubernetes cluster, managed via Terraform for infrastructure as code. Follow the provided Terraform scripts to create AWS infrastructure, ensuring proper permissions.

---
As you engage with this project, prioritize understanding each aspect of the pipeline. Verify that workflows are correctly configured and trigger as anticipated. Embrace best practices, maintaining clean, well-tested code.
