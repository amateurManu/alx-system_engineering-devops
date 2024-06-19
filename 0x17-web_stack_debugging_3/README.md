# Web stack debugging #3

For this series of web stack debugging, we are supposed to fix the error resulting from Apache returning a 500 error.\
The 500 Internal Server Error results when `curl -sI 127.0.0.1` is run.\
`strace` is used to attach to a current running process.\
Error is fixed and automated using Puppet instead of using Bash scripts.
