# QR Code Generator

A Python script to generate QR codes from a CSV file. Each QR code is saved as an image file named based on the specified input. This project uses a virtual environment for dependency management.

## Features
- Generates QR codes for a list of URLs/IPs.
- Reads input data from a CSV file.
- Automatically names the output images based on the `name` field in the input file.
- Saves dependencies in `requirements.txt` for easy setup in isolated environments.

## Requirements
- Python 3.6+
- A virtual environment for isolated dependency management.

## Setup

1. **Clone the repository**

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your input CSV file**:
   Place a CSV file named `ips_to_convert.csv` in the `data` folder with the following format:
   ```csv
   data,name
   http://192.168.1.100:8000,local_ip_1
   http://192.168.1.101:9000,local_ip_2
   http://192.168.1.102:8080,local_ip_3
   ```

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Output**:
   - QR code images are saved in the project directory.
   - Each image is named using the `name` field from the input file (e.g., `local_ip_1.png`).

## Virtual Environment Management
To deactivate the virtual environment after use:
```bash
deactivate
```

To reactivate the virtual environment:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

