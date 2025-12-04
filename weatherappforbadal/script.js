// DOM references
const searchBtn = document.getElementById('searchBtn');
const cityInput = document.getElementById('cityInput');
const weatherInfo = document.getElementById('weatherInfo');
const errorEl = document.getElementById('error');
const loading = document.getElementById('loading');

function getWeatherIcon(weatherCode) {
    const icons = {
        '01d': '☀️', '01n': '🌙',
        '02d': '⛅', '02n': '☁️',
        '03d': '☁️', '03n': '☁️',
        '04d': '☁️', '04n': '☁️',
        '09d': '🌧️', '09n': '🌧️',
        '10d': '🌦️', '10n': '🌧️',
        '11d': '⛈️', '11n': '⛈️',
        '13d': '❄️', '13n': '❄️',
        '50d': '🌫️', '50n': '🌫️'
    };
    return icons[weatherCode] || '🌤️';
}

function showError(message) {
    errorEl.textContent = message;
    errorEl.style.display = 'block';
}

function clearError() {
    errorEl.textContent = '';
    errorEl.style.display = 'none';
}

async function getWeather(city) {
    // Explicit API key validation
    if (!API_KEY) {
        showError('No API key set. Add your OpenWeatherMap API key to `index.html` as `const API_KEY = "your_key"` or run `localStorage.setItem("OWM_API_KEY", "your_key")` in the console. Get a key at https://openweathermap.org/api');
        return;
    }

    clearError();
    weatherInfo.style.display = 'none';
    loading.style.display = 'block';

    try {
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&units=metric&appid=${API_KEY}`;
        const response = await fetch(url);

        if (response.status === 401) {
            // Unauthorized - bad key
            throw new Error('invalid_key');
        }

        if (response.status === 404) {
            throw new Error('not_found');
        }

        if (!response.ok) {
            throw new Error('network');
        }

        const data = await response.json();

        const temp = data.main && typeof data.main.temp === 'number' ? Math.round(data.main.temp) : '--';
        const feels = data.main && typeof data.main.feels_like === 'number' ? Math.round(data.main.feels_like) : '--';
        const humidity = data.main && typeof data.main.humidity === 'number' ? `${data.main.humidity}%` : '--%';
        const windKmh = data.wind && typeof data.wind.speed === 'number' ? `${Math.round(data.wind.speed * 3.6)} km/h` : '-- km/h';
        const desc = data.weather && data.weather[0] && data.weather[0].description ? data.weather[0].description : '';
        const icon = data.weather && data.weather[0] && data.weather[0].icon ? data.weather[0].icon : '';

        document.getElementById('temperature').textContent = `${temp}°C`;
        document.getElementById('cityName').textContent = data.name || city;
        document.getElementById('description').textContent = desc;
        document.getElementById('humidity').textContent = humidity;
        document.getElementById('windSpeed').textContent = windKmh;
        document.getElementById('feelsLike').textContent = `${feels}°C`;
        document.getElementById('weatherIcon').textContent = getWeatherIcon(icon);

        loading.style.display = 'none';
        weatherInfo.style.display = 'block';
    } catch (err) {
        console.error('getWeather error:', err);
        loading.style.display = 'none';
        weatherInfo.style.display = 'none';

        if (err.message === 'invalid_key') {
            showError('Invalid API key. Check your OpenWeatherMap API key and try again.');
        } else if (err.message === 'not_found') {
            showError('City not found. Please check the city name and try again.');
        } else {
            showError('Unable to retrieve weather. Check your network and API key.');
        }
    }
}

// Wiring up event listeners
if (searchBtn && cityInput) {
    searchBtn.addEventListener('click', () => {
        const city = cityInput.value.trim();
        if (city) getWeather(city);
    });

    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const city = cityInput.value.trim();
            if (city) getWeather(city);
        }
    });
}