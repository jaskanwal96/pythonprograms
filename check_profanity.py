import urllib
def read_text():
    quotes = open("E:\Study\Udacity\Movie Trailer\check profanity\movie_quotes.txt")
    content_of_file = quotes.read()
    ##print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if output == "true":
        print("Mind Your Language Brah!")
    else:
        print("Good To go Brah!")
    connection.close()
    
read_text()
