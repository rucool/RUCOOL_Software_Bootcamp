# Instructions to install: Miniconda
Please go to: https://docs.conda.io/en/latest/miniconda.html

Follow these instructions to set up miniconda on your Mac or Windows computer according to https://docs.conda.io/en/latest/miniconda.html


Select/download the installer for your operation system that has Python 3.11. Follow the prompts for the installation. (Note: be careful to select the correct operating system. For MacOS the "pkg" installers are easier and be careful to select the "intel" or "M1" link depending on the type of processor you have, if you're not sure click on the 'Apple' in the upper left corner of your screen and 'About This Mac' ).

For Windows this should automatically install the 'Anaconda Powershell Prompt' to your start menu. For MacOS when you open a 'terminal' either by typing 'terminal' in the spotlight or navigating to Applications -> Utilities in 'Finder.' When you open a Powershell or Terminal you should now see (base) at the prompt. To confirm type at the prompt:

    conda env list

And you should get something like:

     base                  *  /Users/tnmiles/miniconda3
