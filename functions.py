import requests
import pywhatkit as kit
import wikipedia
import smtplib
import json

# Function to find your IP address
def find_my_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

# Function to get the latest news
def get_latest_news():
    api_key = 'e845bb8b20194ace8cc94e640fae6b2f'
    news_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    news_data = requests.get(news_url).json()
    articles = news_data['articles'][:5]
    return [article['title'] for article in articles]

# Function to get random advice
def get_random_advice():
    response = requests.get('https://api.adviceslip.com/advice').json()
    return response['slip']['advice']

# Function to get a random joke
def get_random_joke():
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers).json()
    return response['joke']

# Function to get trending movies
def get_trending_movies():
    api_key = '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'
    url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}'
    response = requests.get(url).json()
    movies = [movie['title'] for movie in response['results'][:5]]
    return movies

# Function to get weather report
def get_weather_report(city):
    api_key = '3041e9a702c0c17d17f9160e961f57b2'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    weather = response['weather'][0]['description']
    temp = response['main']['temp']
    return f"{city}: {weather}, {temp}°C"

# Function to play video on YouTube
def play_on_youtube(video):
    kit.playonyt(video)

# Function to search on Google
def search_on_google(query):
    kit.search(query)

# Function to search on Wikipedia
def search_on_wikipedia(query):
    return wikipedia.summary(query, sentences=2)

# Function to send an email
def send_email(to_email, subject, message):
    your_email = 'your_email@gmail.com'
    your_password = 'your_password'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(your_email, your_password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(your_email, to_email, email_message)

# Function to send a WhatsApp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+{number}", message, wait_time=15)

# Example usage
if __name__ == "__main__":
    print("Your IP Address:", find_my_ip())
    print("Latest News:", get_latest_news())
    print("Random Advice:", get_random_advice())
    print("Random Joke:", get_random_joke())
    print("Trending Movies:", get_trending_movies())
    print("Weather Report:", get_weather_report('New York'))
    play_on_youtube('Python programming')
    search_on_google('OpenAI')
    print(search_on_wikipedia('Python programming language'))
    # send_email('recipient@example.com', 'Test Subject', 'This is a test email')
    # send_whatsapp_message('1234567890', 'Hello from your voice assistant!')
