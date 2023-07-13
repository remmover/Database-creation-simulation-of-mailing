Contact Manager
==================

The Contact Manager is a Python application that allows you to efficiently manage your contacts. With this application, you can easily add, edit, and delete contacts, as well as send emails and SMS messages to your contacts. The application utilizes Python 3.7 or higher, MongoDB for data storage, and RabbitMQ for message queuing.

Installation
------------

To install and set up the Contact Manager, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```

2. Install the required dependencies using pip:
   ```
   poetry install
   ```

3. Create a MongoDB database and a RabbitMQ queue. Make sure you have the necessary credentials and connection information.

4. Update the `config.py` file with your MongoDB and RabbitMQ connection details.

Usage
-----

To run the Contact Manager, execute the following command in your terminal:

```
python app.py
```

This will start the application and make it listen for messages on the RabbitMQ queue. Whenever a message is received, the application will process it and send the appropriate email or SMS message to the specified contact.

License
-------

The Contact Manager is licensed under the MIT License. You can find the full license text in the `LICENSE` file.

Contributing
------------

Contributions to the Contact Manager are welcome! If you find any issues or have ideas for enhancements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

Thank you for using the Contact Manager! We hope it helps you effectively manage your contacts. If you have any questions or need further assistance, please don't hesitate to reach out.
