import news from 'gnews';

const candidateNews = async(name) => {
    const c_news = await news.search(name);

    for (let article of c_news) {
        $(".news").text(article.pubDate + ' | ' + article.title);
    }
};

candidateNews('Kathy C. Hochul');
