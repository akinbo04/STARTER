async function getWeatherData(city) {
    const apiKey = 'cbf7de6ff9b2fd62119d0fbc13840870';
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (response.ok) {
            updateWeatherDisplay(data);
        } else {
            console.error('Error:', data.message);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function updateWeatherDisplay(data) {
    // Update current weather display with data
    // Update forecast display with data
}

document.getElementById('search-button').addEventListener('click', () => {
    const city = document.getElementById('search-bar').value;
    getWeatherData(city);
});