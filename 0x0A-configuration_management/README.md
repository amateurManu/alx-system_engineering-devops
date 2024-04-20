Configuration Management

This project serves as an introduction to the process of systematically handling changes to a system in a way that it maintains integrity over at time as learned in the ALX SE Program.

All files are interpreted on Ubuntu 20.04 LTS

Puppet manifests pass puppet-lint version 2.1.1 without any errors


Tasks:
0. Create a file
mandatory
Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet


1. Install a package
mandatory
Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0


2. Execute a command
mandatory
Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
