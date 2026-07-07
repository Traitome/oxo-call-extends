---
name: ansible
category: utility
description: Open-source automation tool for configuration management, application deployment, and task execution
tags: [ansible, automation, configuration-management, devops, infrastructure-as-code, playbook]
author: oxo-call-community
source_url: "https://www.ansible.com"
---

## Concepts

- **Tool Overview**: Ansible - Open-source automation platform developed by Red Hat for IT infrastructure automation and configuration management.
- **Core Function**: Automates configuration management, application deployment, task execution, and orchestration across servers, cloud, and network devices.
- **Key Features**:
  - **Agentless Architecture**: Uses SSH for communication, no agents required on target nodes
  - **Declarative Language**: Uses YAML for writing playbooks that define desired system state
  - **Idempotent Operations**: Ensures consistent results regardless of execution count
  - **Modular Design**: Extensible with hundreds of built-in modules and support for custom modules
  - **Inventory Management**: Centralized management of target hosts and groups
- **Core Components**:
  - **Playbooks**: YAML files defining automation workflows and tasks
  - **Modules**: Reusable units for executing specific tasks (e.g., file management, package installation)
  - **Inventory**: List of managed hosts and groups
  - **Roles**: Structured collections of playbooks, tasks, templates, and variables for reuse
  - **Variables**: Manage system-specific configurations and differences
- **Installation**: `conda install -c bioconda ansible` or `pip install ansible`

## Pitfalls

- **SSH Connectivity**: Requires proper SSH access and key management across all target hosts
- **Variable Scoping**: Complex variable precedence rules can lead to unexpected behavior
- **Debugging Complexity**: Error messages can be cryptic for complex playbooks
- **Performance**: Large inventories may require optimization with forks and async execution
- **Idempotency Issues**: Not all modules are perfectly idempotent; requires careful playbook design
- **Windows Support**: Limited support compared to Linux/Unix systems

## Examples

### Test connectivity to all hosts
**Args:** `ansible all -m ping -i inventory.ini`
**Explanation:** Tests SSH connectivity to all hosts defined in inventory.ini using the ping module.

### Run a shell command on target hosts
**Args:** `ansible web_servers -m shell -a "uptime"`
**Explanation:** Executes the `uptime` command on all hosts in the web_servers group.

### Execute a playbook
**Args:** `ansible-playbook -i inventory.ini deploy_app.yml`
**Explanation:** Runs the deploy_app.yml playbook against hosts in inventory.ini.

### Check playbook syntax
**Args:** `ansible-playbook --syntax-check deploy_app.yml`
**Explanation:** Validates playbook syntax without executing it.

### Show module documentation
**Args:** `ansible-doc copy`
**Explanation:** Displays documentation for the copy module.

### Playbook example (deploy_app.yml)
**Args:**
```yaml
---
- name: Deploy web application
  hosts: web_servers
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Copy application files
      copy:
        src: ./app/
        dest: /var/www/html/

    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes
```
**Explanation:** A complete playbook that updates system packages, installs nginx, deploys application files, and starts the web server.