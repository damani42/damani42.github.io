Title: Presentation of ensure-tox role.
Date: 2020-08-08 16:15
Tags: python, openstack, zuul, tox
Summary: The ensure-tox is a simple playbook for zuul.
status: draft

# Introduction

The [ensure-tox](https://opendev.org/zuul/zuul-jobs/src/branch/master/roles/ensure-tox/README.rst)
is simple. It's a ansible playbook for zuul to be sure tox is install. It's
look for tox, and if not found, install it via pip into a virtual environment
for the current user. It can be very useful sometimes and particulary with the
usage of ``ensure_global_symlinks`` variable.

# Usage

Recently with a colleague **Bernard Cafarelli**, we have fix the
[upstream CI](https://review.opendev.org/#/c/745304/) for oslo-cookiecutter. It
is a project that makes it easy to create an oslo project. The problem came
from a test script that tried to run the tox command in the newly created
project. The tox command was therefore not visible in the virtualenv created by
the new project. I could not reproduce the bug in local, because I did not
immediately have to identify the problem and that for my part, I had tox
installed on my machine. In such cases, ensure-tox comes in handy. With the use
of the ``ensure_global_symlinks`` variable which allows to make a symlink into
``/usr/local/bin`` path. What is needed in this case, because the script
expects to have tox in a more standard location. The ensure-tox role was
already in use by the parent job. So we just had to add the use of the variable
tox fix the bug.

# Conclusion

In conclusion, ensure-tox is very useful to ensure that the job has tox
installed and to have a symlink on the host system for scripts that need it.
This is quite specific to OpenStack, because few projects use zuul. But if you
are using zuul for a python project. I recommend you to use ensure-tox too.
