# Notes

## Functions
- In python this is considered a module without the need to export anything

## Packages
A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named __init__.py, which indicates that the directory should be treated as a package.

## Python Workspaces
Python workspaces refer to the environment in which you develop and run your Python code. They include the Python interpreter, installed libraries, and the current working directory. Understanding workspaces is essential for managing dependencies and code organization.

Python workspaces can be local or virtual environments. A local environment is the system-wide Python installation, while a virtual environment is an isolated environment for a specific project. You can create virtual environments using tools like `virtualenv` or `venv`.

> think of it like npm package.json in js world

```bash
    # install venv
    sudo apt install python3-venv
    # create a virtual env
    python3 -m venv my_test_environment
    # activate the veritual env
    source my_test_environment/bin/activate
    # deactivate the virtual env
    deactivate
```