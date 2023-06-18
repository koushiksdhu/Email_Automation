# Birthday Email Automation

This project is a Birthday Email Automation tool built using Python and the `smtplib` library. It allows you to automatically send birthday greetings via email to your friends, family, or colleagues on their special day. The tool reads a CSV file containing the list of birthdays and sends personalized emails to the respective recipients.

## Features

1. CSV Input: The tool reads a CSV file containing the list of birthdays and recipient information. The CSV file should include columns for names, email addresses, and birthdays.

2. Email Generation: The tool generates personalized email messages for each recipient based on their name and birthday. You can customize the email template to suit your needs.

3. SMTP Configuration: The tool uses the Simple Mail Transfer Protocol (SMTP) to send emails. You need to provide the SMTP server details and your email credentials for the tool to send the emails on your behalf.

4. Date Matching: The tool matches the current date with the birthdays in the CSV file to identify recipients who have a birthday on the current day. It then sends an email to wish them a happy birthday.

5. Logging: The tool logs the email sending process, including successful deliveries and any errors encountered. This helps you keep track of the emails sent and identify any issues that may arise.

## Prerequisites

To use the Birthday Email Automation tool, ensure you have the following:

- Python (version 3.7 or higher) installed on your computer.
- Access to an SMTP server to send the emails.
- Basic knowledge of Python and the `smtplib` library.

## Usage

1. Clone the GitHub repository or download the project files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies by running the following command:
   ```
   $ pip install smtplib
   ```

4. Open the `birthdays.csv` file in a text editor or spreadsheet software and populate it with the names, email addresses, and birthdays of the recipients. Save the file.

5. Open the `config.py` file and update the SMTP server details and your email credentials in the respective fields.

6. Customize the email template in the `letter.txt` file. You can modify the subject line, message body, and any other details according to your preference.

7. Run the following command to start the Birthday Email Automation tool:
   ```
   $ python automated_birthday_wisher.py
   ```

8. The tool will check the current date and compare it with the birthdays in the `birthdays.csv` file.

9. If there are any birthdays on the current day, the tool will send personalized emails to the respective recipients.

10. Check the console output for the email sending process and any errors encountered.

11. Repeat the process daily or as desired to automatically send birthday greetings.

## Customization

You can customize the Birthday Email Automation tool by modifying the code in the `automated_birthday_wisher.py`, `birthday.csv`, and `letter.txt` files. You can change the CSV file format, email template, SMTP server details, or add additional features to enhance the automation.
