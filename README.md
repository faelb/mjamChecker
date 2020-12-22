# mjamChecker

mjamChecker is a Python program that helps you to find out when your restaurant is available for an order again.

## Installation

### I'm just a normal user

First make sure to install python version 3.9 on your PC/Linux/MAC.
To do so just open the command line in windows (you press the windows home button
and type in "shell" or "cmd" or "Eingabeaufforderung" and open it) and type in python.
If its not installed yet, the windows store will pop up and give you the opportunity to install it.
Of course you could also download and install it from the official website.
If it was already installed, it will look like this:

C:\Users\username>python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

just type quit() and press enter to quit the python shell.

After installing python the next thing you have to do open the command line (if its not already opened).
Get the folder path of where all the files are in (main.py, README, requirements.txt) and copy it (just get it from the windows explorer).
It could look like this: C:\GitHub\mjamChecker
Back in the commandline type: cd pathYouJustCopied
so in my case it would be: cd C:\GitHub\mjamChecker
press Enter - the command line now switched the directory path to the path of our program.
Type in: pip install -r requirements.txt
wait for all the dependencies to install
DONE!

now you can just type in main.py and press enter - the program will start.
You can also just doubleclick the main.py file in the folder and it will run.


### I know what I'm doing

Just use pip with the requirements.txt for your own python installation or for a venv to get the missing packages,
and then run the python script.

## Usage


After Installation run the main.py file and follow the orders on the terminal.
You will first have to tell the program the URL of your restaurant.
To get this URL visit mjam.net - login there or just type in your address and go to the search bar to find your restaurant.
When you found your restaurant and it says "Momentan keine Lieferung" - still click onto its widget to enter the restaurants page.
And there you have the URL of the restaurants page, that you have to copy paste to the input of the program.
Commit the URL by pressing enter and the program will start polling Mjam (if your URL was right).
The mjamChecker will check the Mjam website every 7 seconds to find out wether your restaurant is available again.
If it is available it will play an awfull annoying alarm sound you wont miss (So volume up on the speakers!)

## Contributing
Project is finished - no contributions planned

## License
GNU GPLv3