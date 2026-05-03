import webbrowser
import urllib.parse

def search_youtube(query):
    try:
        search_query = urllib.parse.quote(query)
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
        return f"Sir, searching YouTube for {query}"
    except Exception as e:
        print("YouTube Error:", e)
        return "Sorry Sir, I could not open YouTube right now."

def play_youtube(query):
    try:
        search_query = urllib.parse.quote(query)
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
        return f"Sir, opening YouTube for {query}"
    except Exception as e:
        print("YouTube Error:", e)
        return "Sorry Sir, I could not open YouTube right now."