# Contact Manager Project

This is a simple contact manager application that allows users to add, view, and delete contacts. The application is structured in a modular way, making it easy to maintain and extend.

## Features

- Add new contacts with name, email, and phone number.
- View a list of all contacts.
- Delete contacts from the list.
- Data is stored in a JSON file for persistence.

## Project Structure

```
contact-manager
├── src
│   ├── models
│   │   └── contact.py
│   ├── controllers
│   │   └── contact_controller.py
│   ├── views
│   │   └── contact_view.py
│   ├── utils
│   │   └── validation.py
│   └── main.py
├── tests
│   └── test_contact_manager.py
├── data
│   └── contacts.json
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd contact-manager
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the contact manager application, execute the following command:
```
python src/main.py
```

Follow the prompts in the user interface to manage your contacts.

## Testing

To run the unit tests for the contact manager, use the following command:
```
python -m unittest tests/test_contact_manager.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.