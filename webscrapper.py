from newspaper import Article
url= "Link url"

my_article=Article(url,language="en")
my_article.download()
#print(my_article.html)

my_article.parse()
print("Title: ",my_article.title)
print("Author:",my_article.authors)
print("Publishing date:",my_article.publish_date)


my_article.nlp()

print("summary: ",my_article.summary)
print("keywords: ",my_article.keywords)
