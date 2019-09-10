## Gideon

This is the web2py app that will detect the reliability of a news.
This app will take news URL or Headline as input and output the score, related news and the conclusion. The headline here must be a headline of a news or use a formal(structural) sentence.
The score is given in between 0% to 100%, If the score is below 52.5%, we classify as a fake news otherwise not.
This model will not give a 100% accurate result, but it will give the related news that user can view and make further judgement. To see our conclusion, simply hover your cursor through the score written on the page after you submit the url or headline.


## Requirements:
download or clone web2py,
download chromedriver and set it to your path under db.py crawler function, in the variable "CHROME_PATH".

For python library, please install the following packages as these are used:
string, sklearn, numpy, pandas, google-search, beautifulsoup4, requests, html2text, readability-lxml, tqdm, urllib.request, selenium, PIL, wordcloud, matplotlib


After you have done the requirements, move this gideon file in web2py/applications/, then you can run it locally through web2py server.


## About the Algorithm:
Gideon fake news detector will take input news headline or URL and output the percent of confidence and conclusion of the calculation (fake news or not).
The algorithm is as follows:
1. take input from user
2. if the input is url -> scrape the url and return the sentence to search using google search. if the input is headline -> search the headline in google search.
3. taking top 8 news from the google search, we will compare if the news searched is actually correlated to the headline/url.
4. If it is related, we will consider the news website and score them accordingly.
5. we will compute the score and return the result.
