# terraform-ansible-docker-deployment
Infrastructure automation project using Terraform, AWS EC2, Ansible, Docker, and Flask to provision and deploy a containerized application across multiple EC2 instances.


# Infrastructure Automation & Multi-Server Deployment

A hands-on DevOps project demonstrating Infrastructure as Code and automated application deployment using Terraform, AWS EC2, Ansible, Docker, Docker Hub, and Flask.

Terraform provisions two AWS EC2 instances, while Ansible configures both servers and deploys the same Dockerized Flask application to each instance.

## Tech Stack

- AWS EC2
- Terraform
- Ansible
- Docker
- Docker Hub
- Python
- Flask
- Ubuntu/Linux
- SSH


## Architecture

```text
                    Terraform
                        │
                        ▼
                  AWS Infrastructure
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          EC2 Server 1        EC2 Server 2
              │                   │
              └─────────┬─────────┘
                        │
                     Ansible
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
           Docker              Docker
              │                   │
              ▼                   ▼
        Flask Container      Flask Container
              │                   │
              └─────────┬─────────┘
                        │
                   Port 5000


```
### What the project demonstrates

## What I Learned

- Provisioning AWS infrastructure using Terraform
- Managing multiple EC2 instances with Terraform
- Configuring Linux servers using Ansible
- Creating reusable Ansible playbooks
- Building Docker images
- Publishing images to Docker Hub
- Deploying containers remotely using Ansible
- Deploying the same application across multiple servers
- Managing SSH-based server automation
- Understanding the relationship between IaC, configuration management, and containerization



## Deployment Flow

1. Terraform provisions two EC2 instances on AWS.
2. Terraform outputs the public IP addresses.
3. The IP addresses are added to the Ansible inventory.
4. Ansible connects to both EC2 instances through SSH.
5. Ansible installs and configures Docker.
6. Docker pulls the application image from Docker Hub.
7. Ansible starts the Flask container on both servers.
8. The application becomes accessible on port `5000` on both instances.

