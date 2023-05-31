//import news from 'gnews';
/*const news = require('gnews');

const candidateNews = async(name) => {
    const c_news = await news.search(name);

    for (let article of c_news) {
        $(".news").text(article.pubDate + ' | ' + article.title);
    }
};

candidateNews('Kathy C. Hochul');*/
const candidateNews = (name) => {
    let article = "hi";
    $(".news").append(article + name);

};
candidateNews('Kathy C. Hochul');
