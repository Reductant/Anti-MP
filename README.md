# Anti-MP
A program to find the best and the worst of English politics

The program was written in Python 3.5. 

On running the first time, it checks for the presence in its folder of a file called antimp.csv. If the file does not exist, it creates one. This involves accessing the website theyworkforyou.com, which takes some time (usually around 5 minutes). This only needs to be done once. (A later update might be added to do this on a weekly or monthly basis, to keep the data fresh).

The program then asks for a username. 

Next, the program asks 85 policy questions, and ranks all British MPs based on agreement with the user's opinions.

The final step is to display the MPs ranked in order of agreement with the user. The output is also saved as a new file, username.csv.
