#!/bin/bash

INSTANCE_IP=$(terraform output -raw instance_ip)
PRIVATE_KEY_PATH="~/.ssh/id_rsa" # ssh key path

export INSTANCE_IP
export PRIVATE_KEY=${PRIVATE_KEY_PATH}

ansible-playbook -i inventory.yaml playbook.yml
