# Gideon

This is the web2py app that will detect the reliability of a news.
This app will take news URL or Headline as input and output the score, related news and the conclusion. The headline here must be a headline of a news or use a formal(structural) sentence.
The score is given in between 0% to 100%, If the score is below 52.5%, we classify as a fake news otherwise not.
This model will not give a 100% accurate result, but it will give the related news that user can view and make further judgement. To see our conclusion, simply hover your cursor through the score written on the page after you submit the url or headline.


requirements:
download or clone web2py,
download chromedriver and set it to your path under db.py crawler function.

After you have done the requirements, move this gideon file in web2py/applications/, then you can run it locally through web2py server.
