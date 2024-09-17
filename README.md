# WhatsApp Notification Script

This Python script is designed to read an Excel file containing user data, identify any missing information in the records, and send WhatsApp notifications to the users with incomplete data. It uses the pandas library to handle the Excel file and the pywhatkit library to send WhatsApp messages.

Requirements:

Python 3.x
pandas library
pywhatkit library
An active internet connection
WhatsApp web logged in
Setup:

1° Install the required Python libraries by running:
pip install pandas pywhatkit

2° Ensure that your WhatsApp Web is logged in before running the script.

Usage:
1° Modify the path in the pd.read_excel() function to point to your Excel file.
2° Ensure the column names in the script match those in your Excel file:

TELEFONE for the phone number column
NOME for the name column
Run the script using Python:
python script.py

Functionality:

1° Reads the Excel file into a DataFrame.
2° Iterates through each row to check for missing data.
3° For each record with missing data, generates a notification message.
4° Sends the notification message via WhatsApp to the phone number provided.
Note:
Ensure your phone number column format includes the country code (e.g., +55 for Brazil).
The script will attempt to send messages immediately after checking the data. Adjust the 15 in kit.sendwhatmsg_instantly to set the delay time in seconds before sending the message.
Troubleshooting:

If messages are not sent, check if WhatsApp Web is properly logged in and accessible.
Ensure all necessary libraries are installed and up to date.

