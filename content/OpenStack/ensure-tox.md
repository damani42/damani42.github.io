Title: Presentation of ensure-tox role.
Date: 2020-08-08 16:15
Tags: python, openstack, zuul, tox
Summary: The ensure-tox is a simple playbook for zuul.
status: draft

# Introduction

The [ensure-tox](https://opendev.org/zuul/zuul-jobs/src/branch/master/roles/ensure-tox/README.rst)
is simple. It's a ansible playbook for zuul to check if tox is install. It
looks for tox, and if it can't found it, it install it via pip into a virtual
environment for the current user. It can be very useful sometimes and
particulary with the usage of ``ensure_global_symlinks`` variable.

# Example with a bug fix

Recently with a colleague **Bernard Cafarelli**, we've fixed the
[upstream CI](https://review.opendev.org/#/c/745304/) for
[oslo-cookiecutter](https://github.com/openstack/oslo-cookiecutter). It
is a project that makes it easy to create an oslo project. The problem came
from a test script that tried to run the tox command in the newly created
project. The tox command was therefore not visible in the virtualenv created by
the new project. I could not reproduce the bug in local, because couldn't
immediately identify the problem because I had tox installed on my machine.
In such cases, ensure-tox comes in handy. With the use of the
``ensure_global_symlinks`` variable which allows to make a symlink into
``/usr/local/bin`` path. It is needed in this case, because the script
expects to have tox in a more standard location. The ensure-tox role was
already in use by the parent job. So we just had to add the use of the variable
to fix the bug.

# Zuul jobs

The oslo-cookiecutter project uses [zuul-jobs](https://opendev.org/zuul/zuul-jobs).
It is a project that contains a set of Zuul jobs and Ansible roles suitable for
use by any Zuul system. This allows in one of his projects to be able to reuse
already existing job, role and not to reinvent the wheel. In our case,
oslo-cookiecutter uses the
[tox job](https://zuul-ci.org/docs/zuul-jobs/python-jobs.html#job-tox) from the
zuul-jobs project. The tox job uses the ensure-tox role, as can be
[seen here](https://opendev.org/zuul/zuul-jobs/src/branch/master/playbooks/tox/pre.yaml#L4).
The tox playbook first performs the ensure-tox role. As explained previously,
ensure-tox makes sure that tox is installed. If it is not installed, the role
will install it in a virtualenv using the
[ensure-pip-virtualenv](https://opendev.org/zuul/zuul-jobs/src/branch/master/roles/ensure-tox/tasks/main.yaml#L21-L33)
role. In our case, we had to use the ``ensure_global_symlinks`` variable. To
have the tox command accessible in a
[path](https://opendev.org/zuul/zuul-jobs/src/branch/master/roles/ensure-tox/tasks/main.yaml#L38-L46)
of the ``$PATH`` which allowed us to correct our problem. The zuul-jobs project
contains many roles and playbooks. I will write an article soon to introduce
zuul and zuul-jobs.

# Conclusion

In conclusion, ensure-tox is very useful to ensure that the job has tox
installed and to have a symlink on the host system for scripts that need it.
This is quite specific to OpenStack, because few projects use zuul. But if you
are using zuul for a python project. I recommend you to use zuul-jobs and
ensure-tox too. To enjoy a multitude of jobs, playbooks and ansible roles for
zuul already written.
