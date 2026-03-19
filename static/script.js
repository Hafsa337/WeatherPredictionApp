async function getWeather() {
    const city = document.getElementById("city").value.trim();
    const resultDiv = document.getElementById("result");

    if (!city) {
        resultDiv.innerHTML = "<p style='color:red;'>Please enter a city name</p>";
        return;
    }

    try {
        const response = await fetch('/get_weather', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city: city })
        });

        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
            return;
        }

        // Display weather
        resultDiv.innerHTML = `
            <h2>${data.city}, ${data.region}, ${data.country}</h2>
            <p>🌡 Temp: ${data.temperature}°C</p>
            <p>☁ ${data.condition} <img src="https:${data.icon}" alt="icon"></p>
            <p>💧 Humidity: ${data.humidity}%</p>
            <p>🌬 Wind: ${data.wind} kph</p>
        `;

    } catch (err) {
        console.error(err);
        resultDiv.innerHTML = "<p style='color:red;'>Error fetching weather data</p>";
    }
}