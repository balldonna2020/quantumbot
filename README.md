# QuantumBot

## Overview
QuantumBot is a Python-based tool designed to perform a deep clean of the Windows registry. It helps to remove unused and obsolete entries, which can potentially boost system performance. This tool automates the cleaning process, ensuring that your Windows registry is free from clutter which might be slowing down your machine.

## Features
- Removes unused and obsolete registry entries.
- Automatically identifies and deletes empty registry keys.
- Logs all actions, errors, and exceptions for easy debugging and review.

## Requirements
- Windows Operating System
- Python 3.x

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/QuantumBot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd QuantumBot
   ```

## Usage
To start the registry cleaning process, run the following command in your terminal:

```bash
python quantumbot.py
```

QuantumBot will automatically scan specified registry paths and clean them. Default paths include:
- `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
- `SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

You can modify the `registry_paths` list in `quantumbot.py` to include additional registry paths you wish to clean.

## Logging
QuantumBot logs all its actions in a file named `quantumbot.log`. This log includes:
- Information about which registry paths are being cleaned.
- Details of any registry keys that are deleted.
- Errors encountered during the process.

## Disclaimer
**Warning:** Editing the Windows Registry can cause system instability if not done correctly. Make sure to back up your registry before using this tool, and use it at your own risk.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.