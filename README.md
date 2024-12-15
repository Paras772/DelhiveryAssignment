# AWS Environment and Kubernetes Deployment with Monitoring

## Overview

This project demonstrates the provisioning of an AWS environment using Terraform, deploying a containerized application to Kubernetes (Minikube), and setting up monitoring and observability with Prometheus and Grafana. The project is divided into three parts:

1. **AWS Environment Provisioning with Terraform**  
2. **Kubernetes Deployment with Minikube**  
3. **Monitoring and Observability**  

---

## Part 1: AWS Environment Provisioning with Terraform

The AWS environment is provisioned using Infrastructure as Code (IaC) with Terraform. The resources created include:

- **VPC** with public and private subnets.
- **Internet Gateway** and **NAT Gateway** for network traffic.
- An **EC2 Instance** for hosting a mock application in a private subnet.
- An **S3 Bucket** for static file storage.
- **Security Groups** for restricted access.

### Steps:
1. Installed Terraform and verified its setup.
2. Created an S3 bucket to store the Terraform state as a best practice.
3. Designed and applied the Terraform plan to create the infrastructure.
4. Verified the creation of resources on AWS and terminated them when no longer required.


---

## Part 2: Kubernetes Deployment with Minikube

This section involves deploying a containerized Python application to Kubernetes using Minikube and Kubernetes manifests. **Kops** is used for managing the cluster due to its cost-effectiveness and industrial standards.

### Key Features:
- Minikube setup on an EC2 instance.
- Deployment of a Python application with Kubernetes manifests.
- DNS routing via Route53 for the application.

### Steps:
1. Created an EC2 instance and installed required tools (Kops, kubectl, AWS CLI, Helm, and ArgoCD).
2. Created a Kops bucket to store the cluster state.
3. Mapped DNS using Route53 for external access to the application.
4. Deployed and validated the Kubernetes cluster using Kops commands.
5. Hosted the application accessible via LoadBalancer DNS.

---

## Part 3: Monitoring and Observability

Monitoring and observability were implemented using **CloudWatch**, **Prometheus**, and **Grafana**.

### Steps:
1. Created a CloudWatch dashboard to monitor the AWS resources.
2. Deployed Prometheus on Kubernetes:
   - Set up a monitoring namespace and RBAC rules.
   - Configured Prometheus to scrape Kubernetes pod metrics.
3. Deployed Grafana on Kubernetes:
   - Integrated Prometheus as a data source.
   - Visualized cluster metrics using pre-built Grafana dashboards.

---

## Deployment Commands

### Kops Commands for Cluster Management:
- Create Cluster:
  ```bash
  kops create cluster --name=kubeparas.proddeploy.xyz --state=s3://kopsparasbucket \
  --zones=us-east-1a,us-east-1b --node-count=1 --node-size=t3.small --master-size=t3.medium \
  --dns-zone=kubeparas.proddeploy.xyz --node-volume-size=8 --master-volume-size=8
  ```
- Update Cluster:
  ```bash
  kops update cluster --name kubeparas.proddeploy.xyz --state=s3://kopsparasbucket --yes --admin
  ```
- Validate Cluster:
  ```bash
  kops validate cluster --state=s3://kopsparasbucket
  ```
- Delete Cluster:
  ```bash
  kops delete cluster --name kubeparas.proddeploy.xyz --state=s3://kopsparasbucket --yes
  ```

---

## Technologies Used

- **Terraform** for AWS provisioning
- **Docker** for containerizing applications
- **Kubernetes (Minikube, Kops)** for orchestration
- **Prometheus** for metrics collection
- **Grafana** for visualization
- **CloudWatch** for AWS monitoring

---
