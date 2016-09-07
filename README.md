# Propeller WebIDE
A web based IDE for the Parallax Propeller


## Requirements
**Propeller WebIDE** is a Python 2.7 web-application, while it might work with Python 2.6 this is untested and unsupported. The same is valid for python 3.x.

Any required Python libraries will be installed with the installation of **Propeller WebIDE**.

For storage of data **Propeller WebIDE** depends on a MySql server, either on the same host or on a different system. 
While other database systems could be used, they are not supported. 
And libraries to communicate with the database will need to be installed manually, as they will not be installed by following the installation guide.

## Installation
Start with checking out the code from the git repository.

We recommend running in a virtual environment. If you have never used it look at the [installation and user guide](https://virtualenv.pypa.io/en/stable/).

To install a library, activate the virtual environment (if used) and then run the given commands.

Install the OS dependant libraries:

#### Windows
Move to the setup/windows directory

- `pip install MySQL_python-1.2.5-cp27-none-win32.whl`

#### All platforms
After the installation of the OS dependant libraries, if any, continue with installing the rest of the required python libraries.

`pip install -r requirements.txt`
