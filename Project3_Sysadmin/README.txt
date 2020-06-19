BEFORE START: Note that words between '<>' are intended to be replaced for something else, including those characters.
              Commands are intended to enter right after '$' symbol


CONFIGURATION AND INSTALATION

- Install virtualbox and Debian and configure it.
- Get ip address from virtual machine with command:

  $ip address

- Install ansible.




ANSIBLE CONFIGURATION

- Open file:

  /etc/ansible/hosts

- Write in the first lines:
  
  [<name for the virtual machine>]               # name for the virtual machine group 
  <alias> ansible_host=<ip addres>               # alias for the vm, in this case [vbox] and the ip address of the vm
                                                 # you can add as many vm as you want adding different aliases
  [<name for the virtual machine>:vars]
  ansible_python_interpreter=/usr/bin/python3    # in case python2 run by default

- Open: 

  <file>.yaml                                    # in this case shield-playbook.yaml

- Change:

  hosts: <alias>                                 # alias you put on hosts file
  user: <user>                                   # user you register on the vm




PASSWORD CONFIGURATION

- There are three ways:
  1. Automated. This is the least secure, but it runs automatically:
     - Open /etc/ansible/hosts
     - Write down the [<name for virtual machine>:vars] box:

       ansible_become_pass=<password>            # in <password> you have to write the user password of the vm

  2. Asking for password automatically. This is more secure. When you run the program, it will ask you your user password of the vm automatically:
     - Open /etc/ansible/ansible.cfg and here there are 2 options:
     - In [privilege_escalation] box, uncomment and modify the line 'become_ask_pass' so it will end like this:

       become_ask_pass=True


     - The second option is similar but do not recomended because it will be deleted in Ansible 2.6 (sudo) and Ansible 2.8 (ask_sudo_pass).
       In [defaults] box, uncomment and modify the line 'ask_sudo_pass' so it will end like this:

       ask_sudo_pass = True 

  3. Asking for password manually. This is more secure than 1 and equal to 2. It is a command line parameter.
     It will ask you your user password of the vm. You do not have to do anything until running the program.




RUN THE PROGRAM
  
- If configuration password (previous block) was 1 or 2, run as:

  $ansible-playbook <file.yaml>                  # in this case ansible-playbook shield-playbook.yaml  
  

- If configuration password (previous block) was 3, run as:

  $ansible-playbook <file.yaml> -K               # in this case ansible-playbook shield-playbook.yaml


- If configuration password (previous block) was 2 or 3, you will be asked for your vm password. Write it.

- Wait until finish.




VISUALIZATION OF WEBSITE

- You can see the website at:
  - vm: on localhost
  - local machine: on <ip address>               # ip address you put in hosts




ATTENTION

- If the machine give you an error related to permissions (sudo, password, users), try this and run again:

  $su -
  $apt update && apt install sudo
  $usermod -aG sudo <user>                       # in <user> enter the vm user
  $exit
  $newgrp sudo
