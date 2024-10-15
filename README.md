# Hyperbolic Text-to-Speech App

Convert your text or uploaded `.txt` files into speech using the Hyperbolic API with this Streamlit-powered web application.

## Features

- **Text Input**: Enter text directly into the text area.
- **File Upload**: Upload a `.txt` file to convert its content to speech.
- **Language Selection**: Choose from multiple languages including English (EN), Spanish (ES), French (FR), Chinese (ZH), Japanese (JP), and Korean (KR).
- **Speaker Selection**: Select a speaker based on the chosen language.
- **Adjustable Parameters**:
  - **SDP Ratio**: Adjust the SDP ratio between 0.0 and 1.0.
  - **Noise Scale**: Adjust the noise scale between 0.0 and 1.0.
  - **Noise Scale W**: Adjust the noise scale width between 0.0 and 1.0.
  - **Speed**: Adjust the speech speed between 0.1 and 5.0.
- **Audio Generation**: Generate and download the synthesized speech as an MP3 file.
- **Error Handling**: Provides feedback for missing inputs or API issues.

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from https://www.python.org/downloads/
- **pip**: Python package installer. It usually comes with Python. Verify by running `pip --version` in your terminal.

### Clone the Repository
git clone https://github.com/yourusername/MeloTTS-Hyperbolic.git
cd MeloTTS-Hyperbolic/app

### Create a Virtual Environment (Optional but Recommended)
python -m venv venv

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies
pip install -r requirements.txt

## Setup

### Configure Environment Variables

The application requires a Hyperbolic API key to function. This key should be stored securely in a `.env` file.

1. **Create a `.env` File**

   In the root directory of your project (`MeloTTS-Hyperbolic/app/`), create a file named `.env`.

2. **Add the API Key**

   Open the `.env` file in a text editor and add the following line:

   ```env
   HYPERBOLIC_API_KEY=your_hyperbolic_api_key_here
   ```

   - Replace `your_hyperbolic_api_key_here` with your actual Hyperbolic API key.
   - **Important**: Do not commit the `.env` file to version control to keep your API key secure.

### Obtain Hyperbolic API Key

If you don't have a Hyperbolic API key, follow these steps:

1. **Sign Up / Log In**

   Visit the https://www.hyperbolic.xyz/ and sign up for an account or log in if you already have one. You will get $10 credit for free trial after your first API call.

2. **Generate an API Key**

   Navigate to the developer section in Settings and generate a new API key.

3. **Copy the API Key**

   Copy the generated API key and paste it into your `.env` file as shown above.

## Running the Application

Navigate to the `app` directory and run the Streamlit application:
streamlit run app.py

This command will launch the app in your default web browser. If it doesn't open automatically, check the terminal output for the local URL (usually `http://localhost:8501`) and open it manually in your browser.

## Usage

1. **Enter Text or Upload a File**

   - **Text Input**: Type your desired text into the provided text area.
   - **File Upload**: Click on the "Upload a .txt file" button to upload a text file. The content of the file will populate the text input area.

2. **Select Language and Speaker**

   - Choose a language from the dropdown menu.
   - Based on the selected language, choose a speaker from the corresponding options.

3. **Adjust Parameters**

   - **SDP Ratio**: Adjust the ratio using the slider.
   - **Noise Scale**: Adjust the noise scale using the slider.
   - **Noise Scale W**: Adjust the noise scale width using the slider.
   - **Speed**: Adjust the speech speed using the slider.

4. **Generate Audio**

   - Click the "Generate Audio" button.
   - The app will process your request and generate an MP3 file.
   - Once processing is complete, a download button will appear. Click it to download and listen to your synthesized speech.

## Error Handling

- **Missing Text/Input**: The app will prompt you to enter text or upload a `.txt` file if none is provided.
- **Missing API Key**: If the API key is not found in the `.env` file, an error message will prompt you to set it.
- **API Errors**: Any issues with the API request will be displayed with the corresponding status code and error message.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, feel free to reach out at info@digimoblabs.com

