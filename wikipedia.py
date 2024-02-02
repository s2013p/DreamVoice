import requests
from bs4 import BeautifulSoup

def search_wikipedia(search_query):
    endpoint = "https://pl.wikipedia.org/w/api.php"

    params_search = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_query
    }

    response = requests.get(endpoint, params=params_search)

    if response.status_code != 200:
        return {"error": "Nie udało się uzyskać odpowiedzi od serwera Wikipedii."}

    data = response.json()

    if "query" in data and "search" in data["query"]:
        search_results = data["query"]["search"]
        results = {}

        for result in search_results:
            title = result["title"]
            pageid = result["pageid"]

            # Zapytanie o treść strony
            params_extract = {
                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro": True,
                "explaintext": True,
                "pageids": pageid,
                "exchars": 1200,  # Liczba znaków wyciągu, możesz dostosować według potrzeb
            }

            response_extract = requests.get(endpoint, params=params_extract)
            if response_extract.status_code != 200:
                snippet = "Nie udało się uzyskać szczegółów strony."
            else:
                extract_data = response_extract.json()
                snippet = extract_data['query']['pages'][str(pageid)]['extract'][:300].rsplit(' ', 1)[0] + "..."

            results[title] = {"snippet": snippet, "pageid": pageid}

        return results
    else:
        return {"error": "Nie znaleziono wyników dla podanego zapytania."}

