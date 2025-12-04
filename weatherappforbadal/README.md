# Weather App (weatherappforbadal)

A small static weather app that uses the OpenWeatherMap current weather API.

## Setup

1. Obtain an API key
   - Create a free account at https://openweathermap.org/ and get an API key (APPID).

2. Add the API key to the app

You have two options:

- Option A — Add to `index.html` (quick):

  Open `index.html` and add a global variable before `script.js` is loaded, for example inside the `<head>`:

  ```html
  <script>
    const API_KEY = 'your_api_key_here';
  </script>
  <script src="script.js" defer></script>
  ```

- Option B — Use browser localStorage (nice for testing without editing files):

  Open the browser console (F12) on the page and run:

  ```js
  localStorage.setItem('OWM_API_KEY', 'your_api_key_here');
  ```

  The app will read the key from `localStorage` if it doesn't find a global `API_KEY` variable.

## Run locally

Serve the folder using a simple HTTP server (recommended) so CORS and fetch work correctly.

Windows (cmd.exe):

```bat
cd /d C:\Users\piyus\EverythingCode2\weatherappforbadal
python -m http.server 8000
```

Then open: http://localhost:8000

## Behavior & Error messages

- If no API key is set: the app shows a clear message telling you to add a key or set `localStorage`.
- If the API key is invalid: the app shows `Invalid API key. Check your OpenWeatherMap API key and try again.`
- If the city is not found: the app shows `City not found. Please check the city name and try again.`
- Other network/server errors show a generic message: `Unable to retrieve weather. Check your network and API key.`

## Troubleshooting

- Confirm the API key is active and has not exceeded its quota.
- Open the browser console to see detailed errors logged by the app.

If you'd like, I can add an on-page input to set the API key (so you don't need to edit files or use the console).