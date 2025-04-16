[![Feature Validation](https://github.com/tribbens/SP25_DS5111_kvu2et/actions/workflows/validations.yml/badge.svg)](https://github.com/tribbens/SP25_DS5111_kvu2et/actions/workflows/validations.yml)

# Setup GitHub Credentials
Enter the following code to create new SSH credentials but substitute with the email associated with your GitHub account.
```
ssh-keygen -t ed25519 -C "<your_github_email>"
```
* Use the default file name and press "enter" to avoid using a passkey when prompted.
* On GitHub go to your profile > "Settings" > "SSH and GPG Keys" > Add a new SSH key
* Name it to match the name of your vm
* Type ```cat id_ed25519.pub``` and copy/paste this key into the field on GitHub > "Save"
* Confirm on your VM with ```ssh -T -i ed25519 git@github.com``` > response should include "You've successfully authenticated..."
# Clone GitHub repository
Navigate into the folder you want to clone this repository into. Likely your home folder.
Next, enter the following command:
```
git clone git@github.com:tribbens/SP25_DS5111_kvu2et.git
```
You now have the repository on your VM and can run scripts directly.
# Initial Setup of VM
Navigate into the folder for the repository you just cloned. Then type the following code into the command line. It will setup the VM.
```
bash init.sh
```
# Install Chrome Headless Browser
Type the following code to run the script to install Chrome headless browser:
```
bash scripts/install_chrome_headless.sh
```
# Further Setup of Virtual Environment
* Type this code to setup the env
```
make env
```
* The requirements.txt file includes any packages that we want to have installed. Type this code to install all packages included in the requirements file:
```
make update
```
# Activating, Linting, & Testing Code
* Activate the env with this code:
```
source env/bin/activate
```
* Lint the gainers module with pylint:
```
make lint
```
You should get a score above 9.0 but likely not 10.0
* Test the gainers module with pytest:
```
make test
```
# Running the Gainers Module to Test It
* Let's try to download some data from Yahoo Finance:
```
make gainers SRC=yahoo
```
* It should show up in your directory with the current date with this command:
```
ls
```
The format of the file should be: ygainers_yyyy-mm-dd_at_hh-mm.csv
If a file shows up with a date and time close to when you typed the command, it should have worked!
* Just to confirm, type the following command where file_name is the file that just showed up:
```
cat <file_name>
```
# Confirming Structure
Let's check the structure to confirm everything worked. Type this code, replacing the bracketed part with the full path to your project repository:
```
tree <your project-repo> -I env
```
You should have an output similar to mine shown here:
```
/home/ubuntu/SP25_DS5111_kvu2et
├── README.md
├── google-chrome-stable_current_amd64.deb
├── init.sh
├── makefile
├── requirements.txt
├── sample_data
│   └── ygainers.csv
├── scripts
│   └── install_chrome_headless.sh
└── ygainers.html
```

### If your output looks similar to mine (paying special attention to "ygainers.csv" showing up), everything is setup properly!
