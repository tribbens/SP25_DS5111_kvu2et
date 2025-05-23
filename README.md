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
# Activating and Testing
* Activate the env with this code:
```
. env/bin/activate
```
* Let's test the headless browser by typing the following code:
```
make ygainers.csv
```
* Move the file "ygainers.csv" to "sample_data" by typing:
```
mv ygainers.csv sample_data/
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
