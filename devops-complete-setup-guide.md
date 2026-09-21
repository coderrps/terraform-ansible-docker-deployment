Bilkul. Maine tumhari uploaded `.md` file ke **same complete content** ko tumhare requested format mein convert kar diya hai: **har step ka explanation upar, aur us step ke saare commands ek hi code block mein niche**. 

````markdown
# DevOps Project - Complete Setup Guide

## Project

Infrastructure Automation & Multi-Server Deployment

## Tech Stack

- AWS EC2
- AWS IAM
- Terraform
- Ansible
- Docker
- Docker Hub
- Python
- Flask
- Ubuntu
- WSL
- SSH

---

# 1. Clone the Project

First pull the project from GitHub and move into the project directory.

### Commands

```bash
git clone <GITHUB_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
````

---

# 2. Build the Docker Image

Go to the application directory, build the Docker image, verify the image, login to Docker Hub, and push the image to the Docker Hub repository.

The Docker image will later be pulled by Ansible and deployed on both EC2 servers.

### Commands

```bash
cd application

docker build -t riturps/my-own-images:portfolio-app-v3 .

docker images

docker login

docker push riturps/my-own-images:portfolio-app-v3
```

---

# 3. AWS Account Setup

Create an AWS account and an IAM user for programmatic access.

Create an Access Key for the IAM user and configure AWS CLI locally.

After configuration, verify that the local machine can communicate with AWS.

### Commands

```bash
aws --version

aws configure

aws sts get-caller-identity
```

During `aws configure`, provide:

```text
AWS Access Key ID:     <ACCESS_KEY>
AWS Secret Access Key: <SECRET_KEY>
Default region name:  ap-south-1
Default output format: json
```

---

# 4. SSH Key Setup

Create an SSH key pair if one does not already exist.

The public key will be associated with EC2, while the private key will be used to connect to the EC2 servers.

### Commands

```bash
ssh-keygen -t rsa -b 4096 -f portfolio-key
```

This creates:

```text
portfolio-key
portfolio-key.pub
```

Keep the private key secure.

---

# 5. Terraform Setup

Move to the Terraform directory.

Initialize Terraform, validate the configuration, preview the infrastructure, and apply the configuration to AWS.

### Commands

```bash
cd terraform

terraform --version

terraform init

terraform validate

terraform plan

terraform apply
```

When Terraform asks for confirmation:

```text
yes
```

Terraform creates:

```text
2 EC2 Instances
Security Group
SSH Key Pair
```

---

# 6. Terraform Configuration

The EC2 resource uses `count = 2`, which creates two EC2 instances from the same resource definition.

### Example

```hcl
resource "aws_instance" "portfolio_server" {
  count = 2

  ami           = "AMI_ID"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.portfolio_sg.id]

  key_name = aws_key_pair.portfolio_key.key_name

  tags = {
    Name = "portfolio-server-${count.index + 1}"
  }
}
```

This creates:

```text
portfolio-server-1
portfolio-server-2
```

---

# 7. Get EC2 IP Addresses

After Terraform creates the infrastructure, get the public IP addresses of both EC2 instances.

These IP addresses will be used in the Ansible inventory.

### Commands

```bash
terraform output
```

Example:

```text
ec2_public_ips = [
  "13.204.88.69",
  "43.204.238.156"
]
```

---

# 8. Move to the Ansible Project

Move to the Ansible directory.

The Ansible project contains the configuration, inventory, and deployment playbook.

### Commands

```bash
cd ../ansible
```

Project files:

```text
ansible.cfg
inventory.ini
playbook.yml
```

---

# 9. Configure Ansible

Configure Ansible to use `inventory.ini` as the inventory file.

Disable host key checking so Ansible does not ask for SSH host-key confirmation during deployment.

### `ansible.cfg`

```ini
[defaults]
inventory = inventory.ini
host_key_checking = False
```

---

# 10. Update EC2 IP Addresses in Ansible Inventory

Get the EC2 public IPs from Terraform and add them to `inventory.ini`.

Both EC2 instances belong to the `webservers` group.

### Commands

```bash
nano inventory.ini
```

### `inventory.ini`

```ini
[webservers]
server1 ansible_host=<EC2_IP_1> ansible_user=ubuntu ansible_ssh_private_key_file=/home/ritu_priya_singh/.ssh/portfolio-key
server2 ansible_host=<EC2_IP_2> ansible_user=ubuntu ansible_ssh_private_key_file=/home/ritu_priya_singh/.ssh/portfolio-key
```

If the EC2 instances are recreated and their public IPs change, update the IPs here.

---

# 11. Test Ansible Connection

Before deploying the application, verify that Ansible can connect to both EC2 servers.

### Commands

```bash
ansible all -m ping
```

Expected:

```text
server1 | SUCCESS
server2 | SUCCESS
```

If both return `SUCCESS`, Ansible can connect to both EC2 servers.

---

# 12. Configure Docker Image in Ansible Playbook

The Docker image used by Ansible must match the image that was pushed to Docker Hub.

Update the image name and tag in `playbook.yml`.

### Commands

```bash
nano playbook.yml
```

### Docker image configuration

```yaml
- name: Pull application image
  community.docker.docker_image:
    name: riturps/my-own-images:portfolio-app-v3
    source: pull
```

---

# 13. Ansible Playbook Deployment Flow

The Ansible playbook performs the complete server configuration and application deployment.

It:

1. Installs Docker.
2. Starts Docker.
3. Pulls the application image from Docker Hub.
4. Removes the old container if it exists.
5. Starts the new application container.

### Playbook

```yaml
- name: Configure EC2 server
  hosts: webservers
  become: true

  tasks:

    - name: Install Docker
      apt:
        name: docker.io
        state: present
        update_cache: true

    - name: Start Docker
      service:
        name: docker
        state: started
        enabled: true

    - name: Pull application image
      community.docker.docker_image:
        name: riturps/my-own-images:portfolio-app-v3
        source: pull

    - name: Remove old container
      community.docker.docker_container:
        name: portfolio-app
        state: absent

    - name: Start application container
      community.docker.docker_container:
        name: portfolio-app
        image: riturps/my-own-images:portfolio-app-v3
        state: started
        restart_policy: unless-stopped
        ports:
          - "5000:5000"
```

The application uses:

```text
Docker Image:
riturps/my-own-images:portfolio-app-v3

Container:
portfolio-app

Port:
5000
```

Port mapping:

```text
EC2 Port 5000
      |
      v
Container Port 5000
      |
      v
Flask Application
```

---

# 14. Deploy Application to Both EC2 Instances

Run the Ansible playbook.

Because both servers belong to the `webservers` group, the playbook runs against both EC2 instances.

### Commands

```bash
ansible-playbook playbook.yml
```

Deployment flow:

```text
                  Ansible
                     |
           +---------+---------+
           |                   |
           v                   v
        EC2 #1              EC2 #2
           |                   |
        Docker              Docker
           |                   |
       Flask App           Flask App
```

---

# 15. Check Running Containers

Check the running containers on both EC2 instances.

You can also check stopped containers.

### Commands

```bash
ansible webservers -m shell -a "docker ps"

ansible webservers -m shell -a "docker ps -a"
```

Expected container:

```text
portfolio-app
```

The container should be running on both servers.

---

# 16. Check Docker Images

Check which Docker images have been pulled onto the EC2 servers.

### Commands

```bash
ansible webservers -m shell -a "docker images"
```

Expected image:

```text
riturps/my-own-images:portfolio-app-v3
```

---

# 17. Check Docker Service

Check whether Docker is running on both EC2 servers.

### Commands

```bash
ansible webservers -m shell -a "sudo systemctl status docker --no-pager"
```

Expected status:

```text
active (running)
```

---

# 18. Check Application Logs

If there is an application or container error, check the Docker container logs.

### Commands

```bash
ansible webservers -m shell -a "docker logs portfolio-app"
```

Useful for checking:

```text
Application errors
Python errors
Flask startup errors
Container startup errors
Dependency errors
```

---

# 19. Check Application Internally

Test the Flask application from inside both EC2 servers.

This verifies that the application is responding on port `5000` before testing it from the browser.

### Commands

```bash
ansible webservers -m shell -a "curl -s http://localhost:5000"
```

If the application is running correctly, the Flask application's response should be returned.

---

# 20. Check Individual EC2 Server

You can also connect directly to an EC2 server using SSH.

After connecting, check the container, logs, and application.

### Commands

```bash
ssh -i ~/.ssh/portfolio-key ubuntu@<EC2_IP>

docker ps

docker logs portfolio-app

curl http://localhost:5000
```

---

# 21. Verify Application from Browser

Use the public IP addresses returned by Terraform and access the application on port `5000`.

### Example

```text
http://<EC2_IP_1>:5000
http://<EC2_IP_2>:5000
```

Both EC2 servers should display the Flask application.

---

# 22. Troubleshooting Commands

Use these commands when something does not work.

### Commands

```bash
# Check Ansible connectivity
ansible all -m ping

# Check all containers
ansible webservers -m shell -a "docker ps -a"

# Check application logs
ansible webservers -m shell -a "docker logs portfolio-app"

# Check Docker service
ansible webservers -m shell -a "sudo systemctl status docker --no-pager"

# Check Docker images
ansible webservers -m shell -a "docker images"

# Check application internally
ansible webservers -m shell -a "curl -s http://localhost:5000"

# Check port 5000
ansible webservers -m shell -a "sudo ss -lntp | grep 5000"

# Connect directly to EC2
ssh -i ~/.ssh/portfolio-key ubuntu@<EC2_IP>
```

---

# 23. Complete Project Flow

```text
GitHub
   |
   v
Clone Project
   |
   v
Build Docker Image
   |
   v
Push Image to Docker Hub
   |
   v
AWS Account
   |
   v
IAM User
   |
   v
Access Key
   |
   v
aws configure
   |
   v
Terraform
   |
   +--> terraform init
   |
   +--> terraform validate
   |
   +--> terraform plan
   |
   +--> terraform apply
   |
   +--> terraform output
   |
   v
Two EC2 Instances
   |
   v
Get Public IPs
   |
   v
Update inventory.ini
   |
   v
Update Docker Image in playbook.yml
   |
   v
ansible all -m ping
   |
   v
ansible-playbook playbook.yml
   |
   +-----------------------+
   |                       |
   v                       v
EC2 Instance 1         EC2 Instance 2
   |                       |
Docker                  Docker
   |                       |
Flask                   Flask
   |                       |
   +-----------+-----------+
               |
               v
        Application :5000
```

---

# 24. Important Commands - Quick Revision

## AWS

```bash
aws --version
aws configure
aws sts get-caller-identity
```

## Docker

```bash
docker build -t riturps/my-own-images:portfolio-app-v3 .
docker images
docker login
docker push riturps/my-own-images:portfolio-app-v3
```

## Terraform

```bash
terraform --version
terraform init
terraform validate
terraform plan
terraform apply
terraform output
terraform destroy
```

## Ansible

```bash
ansible all -m ping
ansible-playbook playbook.yml
ansible webservers -m shell -a "docker ps"
ansible webservers -m shell -a "docker ps -a"
ansible webservers -m shell -a "docker logs portfolio-app"
ansible webservers -m shell -a "docker images"
ansible webservers -m shell -a "sudo systemctl status docker --no-pager"
ansible webservers -m shell -a "curl -s http://localhost:5000"
```

## SSH

```bash
ssh -i ~/.ssh/portfolio-key ubuntu@<EC2_IP>
```

---

# 25. Concepts Covered

## AWS

* AWS Account
* IAM User
* Access Keys
* AWS CLI
* EC2
* Security Groups
* Key Pairs
* Public IP
* SSH

## Terraform

* Infrastructure as Code
* AWS Provider
* Terraform Resources
* `terraform init`
* `terraform validate`
* `terraform plan`
* `terraform apply`
* `terraform output`
* `terraform destroy`
* Terraform `count`
* Terraform Outputs

## Ansible

* Configuration Management
* Inventory
* `ansible.cfg`
* Playbooks
* Tasks
* Modules
* `become`
* SSH-based automation
* Remote command execution
* Multi-server deployment

## Docker

* Dockerfile
* Docker Image
* Docker Container
* Docker Hub
* Docker Registry
* Port Mapping
* Container Logs
* Container Lifecycle
* Restart Policy

## Application

* Python
* Flask
* Flask Application
* Application Port
* Containerized Application

---

# Final Architecture

```text
                         AWS
                          |
              +-----------+-----------+
              |                       |
              v                       v
          EC2 Server 1            EC2 Server 2
              |                       |
              |<------ Ansible -------|
              |                       |
           Docker                  Docker
              |                       |
              v                       v
        Flask Container         Flask Container
              |                       |
              +-----------+-----------+
                          |
                       Port 5000
```

## Core Idea

```text
Terraform   -> Creates Infrastructure

Ansible     -> Configures Servers

Docker      -> Packages Application

Docker Hub  -> Stores Application Image

Flask       -> Application

AWS EC2     -> Runs Application
```

---

# Cleanup

When the project is no longer required, destroy the Terraform-managed AWS infrastructure.

### Commands

```bash
cd terraform

terraform destroy
```

Confirm:

```text
yes
```

This removes the Terraform-managed AWS resources and prevents unnecessary AWS resources from continuing to run.

```
```
