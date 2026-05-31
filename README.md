Ansible NGINX Reverse Proxy Deployment

Project Overview

This project automates the deployment of a Python Flask application using Ansible with NGINX configured as a reverse proxy.

The deployment follows a role-based Ansible architecture and separates responsibilities into application, web, and common system roles.

---

Technologies Used

- Ansible
- NGINX
- Flask
- Python
- systemd
- Jinja2 Templates
- RHEL / Rocky Linux
- SELinux
- Firewalld

---

Architecture

Client Request
↓
NGINX Reverse Proxy
↓
Flask Application Backend

---

Project Structure

ansible-project/
├── ansible.cfg
├── collections/
├── inventory/
├── playbooks/
├── roles/
│   ├── app/
│   ├── common/
│   └── web/

---

Roles

app

Responsible for:

- Flask application deployment
- Python setup
- systemd service creation

web

Responsible for:

- NGINX installation
- Reverse proxy configuration

common

Responsible for:

- Common package installation
- Base system configuration

---

Deployment Command

ansible-playbook -i inventory/hosts playbooks/main.yml

---

Verification

systemctl status nginx
systemctl status myapp
curl http://localhost

---

Features

- Automated deployment
- Role-based architecture
- Reverse proxy implementation
- systemd service automation
- Infrastructure as Code

---

Author

Mahadev
