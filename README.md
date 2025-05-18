# Gemini Code Generator Desktop App

A desktop code generation tool using Google Gemini 2.5 Turbo API and Tkinter.

## Features

- Input code generation queries in natural language
- Automatically generates code for all programming languages
- Powered by Gemini 2.5 Turbo model
- Simple GUI using Tkinter

## Requirements

- Python 3.8+
- Gemini API Key from Google

## Setup Instructions

1. Extract the zip file.
2. Open the folder in VS Code.
3. Install required packages:

```
pip install -r requirements.txt
```

4. Create a `.env` file and insert your Gemini API key:

```
GOOGLE_API_KEY=your-api-key-here
```

5. Run the app:

```
python main.py
```

## Usage

Type your code prompt (e.g., `# Generate a Python function to reverse a string`) in the query box and click "Generate Code". The generated code will appear in the output area.