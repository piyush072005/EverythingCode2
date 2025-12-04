async function getWeather(city) {
                if (!API_KEY) {
                    alert('Please add your OpenWeatherMap API key to use this app.\n\nGet a free key at: https://openweathermap.org/api');
                    return;
                }

                weatherInfo.style.display = 'none';
                error.style.display = 'none';
                loading.style.display = 'block';

                try {
                    // Use the current weather endpoint and request metric units
                    const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&units=metric&appid=${API_KEY}`;
                    const response = await fetch(url);

                    if (!response.ok) {
                        // If the city is not found the API returns 404
                        throw new Error('City not found');
                    }

                    const data = await response.json();

                    // Safely read fields and update the UI
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
                    error.style.display = 'block';
                }
            }