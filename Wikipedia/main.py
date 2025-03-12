import wikipediaapi

def search_wikipedia(query):
    user_agent = "MyWikipediaParser/1.0"
    wiki_wiki = wikipediaapi.Wikipedia(
      language='en',
      user_agent=user_agent
      )
    page = wiki_wiki.page(query) # Get the page for the query

    if page.exists(): # Check if the page exists
        print(f'Title: {page.title}')
        print(f"Summary: {page.summary}")
        print(f"URL: {page.fullurl}")
    else: # If the page does not exist, print an error message
        print("Page does not exist")


if __name__ == "__main__":
    while True:
        query = input("Enter a query: ")
        search_wikipedia(query)
        print("="*30) # Divider