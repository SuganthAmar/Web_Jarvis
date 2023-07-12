import sys
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import pyautogui
import psutil
import pyjokes


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        sys.stdout.write('Listening...\n')
        sys.stdout.flush()
        recognizer.pause_threshold = 1
        voice = recognizer.listen(source)

        try:
            sys.stdout.write('Recognizing...\n')
            sys.stdout.flush()
            command = recognizer.recognize_google(voice, language='en-US')
            sys.stdout.write(f'You said: {command}\n')
            sys.stdout.flush()
            return command
        except Exception as e:
            sys.stderr.write(str(e) + '\n')
            sys.stdout.write('Unable to recognize your voice.\n')
            sys.stdout.flush()
            return ''


def search_wikipedia(query):
    try:
        sys.stdout.write('Searching Wikipedia...\n')
        sys.stdout.flush()
        results = wikipedia.summary(query, sentences=2)
        sys.stdout.write(results + '\n')
        sys.stdout.flush()
        speak(results)
    except wikipedia.exceptions.PageError:
        sys.stdout.write('Sorry, no results found.\n')
        sys.stdout.flush()
        speak('Sorry, no results found.')
    except wikipedia.exceptions.DisambiguationError:
        sys.stdout.write('There are multiple matches. Please be more specific.\n')
        sys.stdout.flush()
        speak('There are multiple matches. Please be more specific.')


def send_email(to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email_address', 'your_email_password')
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail('your_email_address', to, message)
        server.quit()
        sys.stdout.write('Email sent successfully.\n')
        sys.stdout.flush()
        speak('Email sent successfully.')
    except Exception as e:
        sys.stderr.write(str(e) + '\n')
        sys.stdout.write('Sorry, an error occurred while sending the email.\n')
        sys.stdout.flush()
        speak('Sorry, an error occurred while sending the email.')


def open_website(url):
    webbrowser.open_new_tab(url)
    sys.stdout.write('Website opened successfully.\n')
    sys.stdout.flush()
    speak('Website opened successfully.')


def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    sys.stdout.write('Screenshot taken successfully.\n')
    sys.stdout.flush()
    speak('Screenshot taken successfully.')


def get_battery_info():
    battery = psutil.sensors_battery()
    percent = battery.percent
    sys.stdout.write(f'Battery percent: {percent}%\n')
    sys.stdout.flush()
    speak(f'Battery percent: {percent}%')


def tell_joke():
    joke = pyjokes.get_joke()
    sys.stdout.write(joke + '\n')
    sys.stdout.flush()
    speak(joke)


if __name__ == '__main__':
    while True:
        sys.stdout.write('Enter a command: ')
        sys.stdout.flush()
        command = sys.stdin.readline().strip()

        if 'wikipedia' in command:
            sys.stdout.write('What do you want to search for?\n')
            sys.stdout.flush()
            query = sys.stdin.readline().strip()
            search_wikipedia(query)
        elif 'website' in command:
            sys.stdout.write('What website do you want to open?\n')
            sys.stdout.flush()
            url = sys.stdin.readline().strip()
            open_website(url)
        elif 'screenshot' in command:
            take_screenshot()
        elif 'battery' in command:
            get_battery_info()
        elif 'joke' in command:
            tell_joke()
        elif 'exit' in command:
            sys.stdout.write('Goodbye!')
            speak('Goodbye!')
            break
        else:
            sys.stdout.write('Sorry, I did not understand that command.')
            speak('Sorry, I did not understand that command.')

