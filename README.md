# instaAutomate 🚀

**instaAutomate** is a Python-based automation tool designed to help Instagram users easily manage their followers. It automates the process of comparing your "followers" and "following" lists on Instagram by controlling the mouse cursor to navigate through your profile, extracting the necessary data, and then comparing the two lists to show who is not following you back.

## 🛠️ How it Works:
instaAutomate uses the `pyautogui` library to simulate mouse movements and clicks on your screen, as well as `pyperclip` to copy text from your browser. It automates the following process:
1. Navigates through your "followers" list.
2. Extracts the list of accounts you're following.
3. Compares both lists and generates a list of people who aren't following you back.
4. The final list of users not following you back is saved to a file named **Bandits.txt**.

## 🚀 Features:
- 🔍 **Automated Profile Navigation**: Uses mouse control to scroll through your Instagram followers and following lists.
- 📝 **Real-Time Data Extraction**: Extracts data directly from your Instagram page in your desktop browser.
- ⚖️ **Comparison of Lists**: Compares the two lists and identifies who isn’t following you back.
- 💾 **Saves Results**: Outputs the list of non-followers to a file called `Bandits.txt`.
- 💻 **Runs on Your Local Machine**: No need to upload your credentials or share data with third-party servers.

## 📋 Requirements:
- Python 3.x

## 🖥️ Usage:
1. Clone the repository and navigate to the folder
   - ```git clone https://github.com/sabilashang/instaAutomate```
   - ```cd instaAutomate```
2. Install the required dependencies by running:
   - ```pip install -r requirements.txt```
3. Log in to your Instagram account on the desktop in a browser.
4. Run the program and switch to the Instagram Window
   - ```python instaAutomate.py```

## ⚠️ License:
This project is under No License: This code is for personal use only. Copying, modifying, or using this code for academic, commercial, or other purposes is not permitted.

## 📫 Contact:
Feel free to reach out if you have any questions!
**Instagram**: [@sabilashan_g](https://www.instagram.com/sabilashan_g/)
