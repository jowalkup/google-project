from pygooglenews import GoogleNews

def get_news(search):
    gn = GoogleNews(country = 'US')
    search = gn.search(search)
    newsitem = search['entries']

    title = []
    link = []

    for item in newsitem:
        title.append(item.title)
        link.append(item.link)

    news = list(zip(title, link))

    for item in news:
        print(item)
        print()
    print(len(newsitem))
    return

get_news('Kathy C. Hochul')
