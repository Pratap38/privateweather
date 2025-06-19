# 🌤️ Weather Storm - A Dynamic Weather and City Visualization App

## 📖 Overview

**Weather Storm** is a full-stack Django web application that provides real-time weather updates and city-specific background images. Users can input the name of a city to receive current weather data, including temperature, weather conditions, and an iconic representation. The app dynamically displays visually appealing backgrounds related to the queried city for an enhanced user experience.

---

## 🛠️ Features

* **Real-Time Weather Updates:** Fetches live weather data using the OpenWeatherMap API.
* **Dynamic Backgrounds:** Displays city-specific images using Google Custom Search API.
* **User-Friendly Interface:** Minimalist and responsive design for a seamless experience.
* **Error Handling:** Gracefully handles errors with fallback messages and visuals.
* **Weather Icons:** Includes dynamic weather condition icons for visual representation.

---

## 🧑‍💻 Technologies Used

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Weather Icons
* **APIs Integrated:**

  * [OpenWeatherMap API](https://openweathermap.org/api) for weather data.
  * [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction) for city images.
* **Styling:** Custom CSS with Google Fonts (Poppins)
* **Deployment:** (Optional: Mention your deployment platform if hosted, e.g., Heroku, AWS, etc.)

---

## 🚀 How It Works

1. User enters the name of a city in the input field.
2. The app fetches weather details from the OpenWeatherMap API.
3. Simultaneously, it retrieves a background image for the city using the Google Custom Search API.
4. The application dynamically displays:

   * Current temperature
   * Weather description
   * Icon representing the weather condition
   * A stunning background image of the city
5. If the city is invalid or data is unavailable:

   * Shows a fallback image and error message.

---

## 📷 Screenshots

**Homepage with Weather Data:**
![Uploading Screenshot from 2025-06-19 18-03-58.png…]()



---

## 🛠️ Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-storm.git
   cd weather-storm
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your API keys:

   * **OpenWeatherMap API Key**
   * **Google Custom Search API Key** and Search Engine ID
   * Add these keys to your `settings.py` or `.env` file.

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🎨 Future Enhancements

* Add hourly and weekly weather forecasts.
* Include geolocation-based weather updates.
* Save user preferences and recently searched cities.
* Deploy the app online for public access.

---

## 💡 Contribution

Contributions are welcome! Feel free to fork the project, create a new branch, and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
