### **1 Log File Analyzer**
**Objective**: Develop a Python script to analyze log files, extract meaningful information, and generate a summary report.

**Key Concepts and APIs**:
- String parsing and manipulation (`split()`, `find()`, `strip()`, `replace()`)
- Regular expressions (`re` module) for pattern matching in strings
- File handling (`open()`, reading/writing files)
- String formatting (`f-strings`, `format()`)
- Command-line arguments (`argparse` module)

**Steps**:
1. **Input Handling**:
   - Use `argparse` to accept a log file as an input from the command line.
   - Optional: Accept filters or keywords as arguments to focus the analysis on specific log entries.

2. **Log Parsing**:
   - Read the log file line by line.
   - Use regular expressions to extract important information such as timestamps, error levels (e.g., INFO, ERROR), and messages.
   - Store relevant data in a structured format (e.g., dictionary or list of dictionaries).

3. **Data Analysis**:
   - Count the occurrences of different error levels (e.g., number of ERRORs, WARNs).
   - Extract and count occurrences of specific keywords if provided.
   - Identify the most frequent errors or warnings.

4. **Generate Summary Report**:
   - Summarize the findings and generate a report with key metrics.
   - Format the report with appropriate headings, counts, and detailed information.

5. **Output**:
   - Print the report to the console.
   - Optionally, save the report to a text file.

**Example Output**:
```
Log File Analysis Report:
-------------------------
Total Entries: 500
Errors: 15
Warnings: 30
Most Frequent Error: "Database connection failed"
```

### **2: Automated Email Formatter and Sender**
**Objective**: Create a Python script to automate the process of formatting and sending emails with personalized content.

**Key Concepts and APIs**:
- String manipulation (`split()`, `join()`, `replace()`, `format()`)
- Email handling (`smtplib` module, `email` module for MIME types)
- File handling (reading CSV/JSON files for recipient data)
- Environment variables or configuration files for storing credentials
- Command-line arguments (`argparse` module)

**Steps**:
1. **Input Handling**:
   - Use `argparse` to accept a CSV/JSON file containing recipient details (e.g., name, email address) and a template file for the email body.

2. **Email Template**:
   - Read the email template from a file. The template should contain placeholders (e.g., `{name}`) for personalization.
   - Replace placeholders with actual recipient data using string formatting methods.

3. **SMTP Setup**:
   - Configure the script to use an SMTP server for sending emails.
   - Use environment variables or a configuration file to securely store email credentials.

4. **Sending Emails**:
   - Loop through the recipient list, personalize the email for each recipient, and send the email using the `smtplib` module.
   - Handle potential errors (e.g., connection issues, invalid email addresses) and log them for later review.

5. **Output**:
   - Print a success message for each email sent.
   - Log failed attempts with the reason for failure.

**Example Email Template**:
```
Subject: Monthly Report for {name}

Dear {name},

Please find attached the monthly report for {month}.

Best regards,
Your Company
```

**Example Output**:
```
Sent email to john.doe@example.com
Sent email to jane.smith@example.com
Failed to send email to invalid.email@domain (Invalid email address)
```

