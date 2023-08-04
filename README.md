# Rutgers University Center for Ocean Observing Leadership Software Bootcamp
Jupyter Notebooks, data, and lecture notes 

Lectures are based on:

- Online textbook (Abernathey): https://earth-env-data-science.github.io/intro (Links to an external site.)
- Software Carpentry: http://swcarpentry.github.io/
  
# Instructions to install Miniconda
Please go to: https://docs.conda.io/en/latest/miniconda.html

Select/download the installer for your operation system that has Python 3.11. Follow the prompts for the installation.

# Instructions to install Create Conda Environment

  To create an environment with the yml:
## Windows:
Download the win_swbc2023.yml file, open it and at the very bottom there is a line that says prefix.

    prefix: C:\Users\JuliaEngdahl\miniconda3\envs\swbc2023

change it to your username

    prefix: C:\Users\UserName\miniconda3\envs\swbc2023

Once you edit and save the win_swbc2023.yml file, open the Anaconda Powershell Prompt from your start menu and change directories to where you saved the win_swbc2023.yml file. Then type the following as shown:

        conda env create -f win_swbc2023.yml
    If a prompt appears that says Proceed ([y/n])? Type y and hit enter.
Once it successfully installs, type the following as shown:

        conda activate swbc2023
To deactivate your environment:

	      conda deactivate
## Mac:

# If for whatever reason creating an environment from the yml does NOT work. Follow these steps:
For windows, open the anaconda powershell prompt or for mac open your terminal and type the following as shown:

        conda create --name swbc2023 python=3.11
If a prompt appears that says Proceed ([y/n])? Type y and hit enter.
Then type:

        conda activate swbc2023
Once the environment is activated, type or copy and paste the following as is:

	        conda install -c anaconda pandas numpy xarray urllib3
    If a prompt appears that says Proceed ([y/n])? Type y and hit enter.

Once that finishes installing, type or copy and paste the following as is:

	      conda install -c conda-forge cmocean matplotlib jupyterlab glob2 cartopy netcdf4 dask
    If a prompt appears that says Proceed ([y/n])? Type y and hit enter.
    
Once that is done, you have successfully created an environment from scratch!

# Instructions to install Bash Shell
## Windows:
    1.	Download the Git for Windows installer.
    2.	Run the installer and follow the steps below:
        1.	Click on "Next" four times (two times if you've previously installed Git). You don't need to change anything in the Information, location, components, and start menu screens.
        2.	From the dropdown menu, "Choosing the default editor used by Git", select "Use the Nano editor by default" (NOTE: you will need to scroll up to find it) and click on "Next".
        3.	On the page that says "Adjusting the name of the initial branch in new repositories", ensure that "Let Git decide" is selected. This will ensure the highest level of compatibility for our lessons.
        4.	Ensure that "Git from the command line and also from 3rd-party software" is selected and click on "Next". (If you don't do this Git Bash will not work properly, requiring you to remove the Git Bash installation, re-run the installer and to select the "Git from the command line and also from 3rd-party software" option.)
        5.	Select "Use bundled OpenSSH".
        6.	Ensure that "Use the native Windows Secure Channel Library" is selected and click on "Next".
        7.	Ensure that "Checkout Windows-style, commit Unix-style line endings" is selected and click on "Next".
        8.	Ensure that "Use Windows' default console window" is selected and click on "Next".
        9.	Ensure that "Default (fast-forward or merge) is selected and click "Next"
        10.	Ensure that "Git Credential Manager" is selected and click on "Next".
        11.	Ensure that "Enable file system caching" is selected and click on "Next".
        12.	Click on "Install".
        13.	Click on "Finish" or "Next".
    3.	If your "HOME" environment variable is not set (or you don't know what this is):
        1.	Open command prompt (Open Start Menu then type cmd and press Enter)
        2.	Type the following line into the command prompt window exactly as shown:
              setx HOME "%USERPROFILE%"
        3.	Press Enter, you should see SUCCESS: Specified value was saved.
        4.	Quit command prompt by typing exit then pressing Enter

## MacOS:
The default shell in some versions of macOS is Bash, and Bash is available in all versions, so no need to install anything. You access Bash from the Terminal (found in /Applications/Utilities). See the Git installation video tutorial for an example on how to open the Terminal. You may want to keep Terminal in your dock for this workshop.
To see if your default shell is Bash type echo $SHELL in Terminal and press the Return key. If the message printed does not end with '/bash' then your default is something else and you can run Bash by typing bash
If you want to change your default shell, see this Apple Support article and follow the instructions on "How to change your default shell".

## Linux:

The default shell is usually Bash and there is usually no need to install anything.
To see if your default shell is Bash type echo $SHELL in a terminal and press the Enter key. If the message printed does not end with '/bash' then your default is something else and you can run Bash by typing bash.


