import streamlit as st
import requests
import base64
import os
from dotenv import load_dotenv  # Import dotenv to handle environment variables

def main():
    # Load environment variables from the .env file
    load_dotenv()
    
    # Set the title of the Streamlit app
    st.title("Hyperbolic Text-to-Speech App")
    st.write("Convert your text or uploaded `.txt` files into speech using the Hyperbolic API.")

    # Create a text area for user input
    text_input = st.text_area("Enter text", height=200)

    # Create a file uploader for .txt files
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

    # If a file is uploaded, read its content and use it as the text input
    if uploaded_file is not None:
        try:
            text_input = uploaded_file.read().decode('utf-8')
        except Exception as e:
            st.error(f"Error reading the uploaded file: {e}")
            return

    # Create a dropdown for language selection
    language = st.selectbox("Select Language", options=["EN", "ES", "FR", "ZH", "JP", "KR"])

    # Define available speakers for each language
    speaker_dict = {
        "EN": ["EN-US", "EN-BR", "EN-INDIA", "EN-AU"],
        "ES": ["ES"],
        "FR": ["FR"],
        "ZH": ["ZH"],
        "JP": ["JP"],
        "KR": ["KR"]
    }

    # Create a dropdown for speaker selection based on the chosen language
    speaker = st.selectbox("Select Speaker", options=speaker_dict.get(language, []))

    # Create sliders for optional parameters with default values
    sdp_ratio = st.slider("SDP Ratio", 0.0, 1.0, 0.5)
    noise_scale = st.slider("Noise Scale", 0.0, 1.0, 0.5)
    noise_scale_w = st.slider("Noise Scale W", 0.0, 1.0, 0.5)
    speed = st.slider("Speed", 0.1, 5.0, 1.0)

    # Create a button to generate the audio
    if st.button("Generate Audio"):
        # Check if the text input is empty
        if not text_input.strip():
            st.error("Please enter text or upload a `.txt` file.")
            return

        # Retrieve the API key from environment variables
        api_key = os.getenv("HYPERBOLIC_API_KEY")
        if not api_key:
            st.error("API key not found. Please set the HYPERBOLIC_API_KEY environment variable.")
            return

        # Define the API endpoint URL
        url = "https://api.hyperbolic.xyz/v1/audio/generation"

        # Set up the headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Construct the payload with required and optional parameters
        payload = {
            "text": text_input,
            "language": language,
            "speaker": speaker,
            "sdp_ratio": sdp_ratio,
            "noise_scale": noise_scale,
            "noise_scale_w": noise_scale_w,
            "speed": speed
        }

        try:
            # Send a POST request to the API
            response = requests.post(url, headers=headers, json=payload)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while making the API request: {e}")
            return

        # Check if the response status is successful
        if response.status_code == 200:
            try:
                # Parse the JSON response and extract the audio data
                audio_base64 = response.json().get("audio")
                if not audio_base64:
                    st.error("No audio data found in the API response.")
                    return

                # Decode the base64 audio data
                audio_bytes = base64.b64decode(audio_base64)

                # Save the decoded audio as an MP3 file
                with open("result.mp3", "wb") as f:
                    f.write(audio_bytes)

                st.success("Audio generated successfully!")

                # Provide a download button for the generated audio
                with open("result.mp3", "rb") as f:
                    st.download_button(
                        label="Download Audio",
                        data=f,
                        file_name="result.mp3",
                        mime="audio/mp3"
                    )
            except (ValueError, KeyError, base64.binascii.Error) as e:
                st.error(f"Error processing the API response: {e}")
        else:
            # Display an error message if the API request was unsuccessful
            st.error(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()