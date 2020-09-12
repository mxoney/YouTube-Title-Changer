# YouTube-Title-Changer
Repeatedly edits your YouTube video title to its current views.

## Information
This tool edits your YouTube video title to "This video has X views" every 30 seconds, checking for the live views count. It is not using YouTube's official API, making it more user-friendly — no need to register API keys nor worry about cookies. I would recommend hosting the bot as it has to be constantly running to be kept up to date. Please refrain from using this YouTube bot as automating without the consent of the YouTube team is against their Terms of Service. Nevertheless, if you use this, you are doing it at your own risk. You have been warned.

I am aware this is extremely simple, but my friend requested this tool and I figured why not upload it to Github. ¯\\\_(ツ)\_/¯

## Preview
![](https://i.imgur.com/xK5rlQT.png)<br>
![](https://i.imgur.com/QXotaec.png)

## Usage
- Python 3.6 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.
- If you do not already have the **Requests** or **Selenium** libraries installed, run setup.py — make sure PIP is added to PATH.
1. Check your Google Chrome version. If you have V.85, you can keep the included chromedriver.exe. If you have any other Google Chrome version, download chromedriver.exe with the matching version [here](https://chromedriver.chromium.org/downloads) to main.py's file directory.
2. Run main.py.
3. Enter your YouTube video ID — e.g. https://www.youtube.com/watch?v=ABCDEFGHIJK
4. Log in to your YouTube account using your e-mail and password — solve captcha if required.
4. All set!

## Check Google Chrome version
1. Navigate to the three dots at the top right corner of Google Chrome.
2. Select "Help", and click "About Google Chrome".<br>
![](https://i.imgur.com/PiL1MEy.png)<br>
![](https://i.imgur.com/aluXidt.png)

## Legal Notice
This was developed for educational purposes only. I am not accountable for any of your actions; this was merely a speedrun to demonstrate how bots work. Please do not misuse this tool.
