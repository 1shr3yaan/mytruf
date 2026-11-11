
# MYTRUF - Password Security Analyzer

MYTRUF is an interactive password analysis application built using Python and Streamlit. It evaluates basic password characteristics and provides feedback to help users understand common password weaknesses.

## Features

- Password length analysis
- Uppercase and lowercase character detection
- Number and special character detection
- Common password detection
- Repeated character detection
- Theoretical entropy estimation
- Security score and rating
- Improvement recommendations
- Interactive dashboard

## Technologies Used

- Python
- Streamlit
- Regular Python libraries

## Project Structure

```text
mytruf-password-analyzer/
|
|-- app.py
|-- analyzer.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project

```bash
cd mytruf-password-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

## Important Note

MYTRUF is an educational project. Its scoring system and entropy calculation are heuristic estimates, not professional security guarantees or a substitute for established password-security tools.

The application processes password input locally and does not intentionally store or transmit it.

## Author

SHREYAAN MALAKAR
