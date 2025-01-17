# Save Race

A Python application that allows you to save information about races (name, duration, type) to a Firebase database using a graphical user interface built with `tkinter`.

---

## **Features**

- Simple and intuitive graphical user interface.
- Saves race data to a Firebase database.
- Input validation to ensure correct data entry.

---

## **Project Structure**

```plaintext
save_race/
├── main.py                  # Entry point of the application
├── ui/
│   └── ui_manager.py        # Handles the user interface
├── services/
│   └── firebase_service.py  # Handles Firebase database operations
├── utils/
│   └── validators.py        # Data validation functions
├── config/
│   └── firebase_config.json # Firebase configuration file
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## **Requirements**

- Python 3.11 or later  
- Firebase configured with the required credentials  
- `tkinter` module installed  
- Python dependencies (listed in `requirements.txt`)  

---

## **Installation**

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/salva-corsa.git
   cd salva-corsa
    ```
2. **Create a virtual environment (optional but recommended)**:
    ```bash
        python3 -m venv venv
        source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```
        pip install -r requirements.txt
    ```
4. **Add the Firebase config file:**
    - Download the ```firebase_config.json``` file from the Firebase console.
    - Save it in the ```config/``` directory.
5. **Run the application**
    ```bash
        python main.py
    ```