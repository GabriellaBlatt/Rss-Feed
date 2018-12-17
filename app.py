from bottle import route, template, static_file, get, run
import feedparser
import json

feed = feedparser.parse('https://www.jpost.com/Rss/RssFeedsHeadlines.aspx')
entries = [{"title": i.title, "link": i.link} for i in feed["entries"]]


@route('/all')
def entry_list():
    return json.dumps(entries)


@route('/')
def index():
    return template("index.html", root='')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/img/<filename:re:.*\.(jpg|png)>')
def images(filename):
    return static_file(filename, root='img')


@get('/js/<filename:re:.*\.js>')
def logic(filename):
    return static_file(filename, root='js')


def main():
    run(host='localhost', port=7001, debug=True)


if __name__ == '__main__':
    main()
