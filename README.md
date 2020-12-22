# mjamChecker

mjamChecker is a Python program that helps you to find out when your restaurant is available for an order again.

## Installation

### I'm just a normal user

First make sure to install python version 3.9 on your PC/Linux/MAC.
While installing python, the program may asks if it should update the system/environment variable. If so, tell it to update it.
After installing python the next thing you have to do open the command line. For that,in Windows, you press the windows home button
and type in "shell" or "cmd" or "Eingabeaufforderung" and open it.
You type in "python --version".
If it tells you the version of python everything is alright. If there is a error message check google for "How to add python
to environment variable windows" or "Python in Umgebungsvariable windows".

If that worked now you have to type in "

### I know what I'm doing

If you want to you can just use the requirements.txt for your own python installation or for a venv,
and then run the python script there.

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