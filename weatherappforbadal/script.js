const API_KEY = '6fe69938c43a12f1556631ede9c3883f'; // You need to add your OpenWeatherMap API key here
        const searchBtn = document.getElementById('searchBtn');
        const cityInput = document.getElementById('cityInput');
        const weatherInfo = document.getElementById('weatherInfo');
        const error = document.getElementById('error');
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

        async function getWeather(city) {
            if (!API_KEY) {
                alert('Please add your OpenWeatherMap API key to use this app.\n\nGet a free key at: https://openweathermap.org/api');
                return;
            }

            weatherInfo.style.display = 'none';
            error.style.display = 'none';
            loading.style.display = 'block';

            try {
                const response = await fetch(
                    `https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid=${API_KEY}`
                );

                if (!response.ok) {
                    throw new Error('City not found');
                }

                const data = await response.json();

                document.getElementById('temperature').textContent = `${Math.round(data.main.temp)}°C`;
                document.getElementById('cityName').textContent = data.name;
                document.getElementById('description').textContent = data.weather[0].description;
                document.getElementById('humidity').textContent = `${data.main.humidity}%`;
                document.getElementById('windSpeed').textContent = `${Math.round(data.wind.speed * 3.6)} km/h`;
                document.getElementById('feelsLike').textContent = `${Math.round(data.main.feels_like)}°C`;
                document.getElementById('weatherIcon').textContent = getWeatherIcon(data.weather[0].icon);

                loading.style.display = 'none';
                weatherInfo.style.display = 'block';
            } catch (err) {
                loading.style.display = 'none';
                error.style.display = 'block';
            }
        }

        searchBtn.addEventListener('click', () => {
            const city = cityInput.value.trim();
            if (city) {
                getWeather(city);
            }
        });

        cityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const city = cityInput.value.trim();
                if (city) {
                    getWeather(city);
                }
            }
        });

        // Demo mode with sample data when API key is not provided
        if (!API_KEY) {
            setTimeout(() => {
                document.getElementById('temperature').textContent = '22°C';
                document.getElementById('cityName').textContent = 'London';
                document.getElementById('description').textContent = 'partly cloudy';
                document.getElementById('humidity').textContent = '65%';
                document.getElementById('windSpeed').textContent = '15 km/h';
                document.getElementById('feelsLike').textContent = '20°C';
                document.getElementById('weatherIcon').textContent = '⛅';
                weatherInfo.style.display = 'block';
            }, 500);
        }