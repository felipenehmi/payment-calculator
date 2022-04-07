# payment-calculator
Coding exercice for ioet

This project was written using Python 3, so it's installation is required
for running the application.

<h3>Usage</h3>

Once inside paymentcalculator directory, commands available are:

Running application: <i>python3 main.py [input_file.txt]</i>

Running tests: <i>python3 tests.py</i>

<h3>About the development</h3>

The project structure was built over a combination of Facade and Command design
patterns,
mainly motivated by the sequence of actions necessary to process the file -
validation, processing and displaying results - each having it's own
complexity.
This structure allows these three steps to be isolated. So, if
it happens to  be necessary a  change in the input data format,
 in the payment calculation or in the results display, we need to change
only the command responsible for processing each task.
The Facade design keep the code clean and undestandable, making the
maintenance easy.
A black box testing approach was chosen for this project,
considering the project's structure and funcionality

