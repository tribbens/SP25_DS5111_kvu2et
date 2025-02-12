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
# VM Setup

# Installing Requirements

# Setting up Headless Browser
