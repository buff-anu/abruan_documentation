Install
========

AbRuAn provides a Dockerfile for easier installation on any machine.
Please ensure that you have Docker installed on your system.
Then follow the steps below:

- Clone the repository and open the project directory in a terminal.
- Execute the following command:

    ::

        ./build_abruan.sh

- Start the container.

Installing python libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For dveloping your own scripts, you may want to install more python libraries.
There are two ways to accomplish this - modifying Dockerfile or installing directly in container.

The Dockerfile can be customzied. Any changes made to this file are reflected in all containers.
You can appned the libraries and associated installation command
in the Dockerfile directly; however, if you are not familiar with Docker then you may modify your working container.
Simply install libraries in the container as you would on a linux machine. Remember that these installations are specific to your container.
These installations will not reflect in other containers.