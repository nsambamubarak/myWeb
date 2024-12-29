# Medication Reminder Application

This project is a simple medication reminder application that helps users remember to take their medications at scheduled times.

## Project Structure

```
medication-reminder
├── src
│   ├── schedule.py        # Contains the logic for scheduling medication reminders
│   └── main.py           # Main driver for the application
├── requirements.txt       # Lists the dependencies required for the project
└── README.md              # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medication-reminder
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python src/main.py
   ```

2. The application will print reminders at the scheduled times (09:00, 13:00, and 18:00).

## Dependencies

- `schedule`: A Python library for scheduling tasks.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.