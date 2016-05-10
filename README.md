# Python-Retry

**Synopsis**

This python script runs the command given in the arguments every second until it successfully exits.

**Examples**

For example running ./retry.py ls -l tries to run the ls -l command, and if it's
exit code is other than 0 then it tries to run it again every second until it runs
successfully, otherwise it will provide the same output as if you ran ls -l. You can also
launch other scripts with it, for example running ./retry ./try.py will run the try.py
until the exit code will be 0, which happens if the random number is 3, otherwise
the exit code will be 1.
