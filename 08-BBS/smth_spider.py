from boards import BoardsCrawler
from topics import TopicsCrawler
from posts import PostsCrawler

boards_crawler = BoardsCrawler()
topics_crawler = TopicsCrawler()
posts_crawler = PostsCrawler()

boards = []

def get_article_posts(url):
    c = posts_crawler.get_pagination_content(url, 1)
    total_pages = posts_crawler.get_total_pages(c)
    posts = posts_crawler.get_posts(c)
    print(total_pages)
    if total_pages > 1:
        for i in range(2, total_pages + 1):
            c = posts_crawler.get_pagination_content(i)
            posts.append(posts_crawler.get_posts(c))

# Get all boards
for i in range(0,10):
    c = boards_crawler.get_board_of_section(i)
    boards += boards_crawler.get_board_list(c)

    # Get article list of board
    for board in boards:
        url = boards['board_url']
        content = topics_crawler.get_content(url, 1)
        articles = topics_crawler.get_post_list()
        total_pages_of_board = topics_crawler.get_max_page()
        for article in articles:
            get_article_posts(article['article_url'])
        for i in range(2, total_pages_of_board+1):
            articles = topics_crawler.get_article_list(content)
            for article in articles:
                get_article_posts(article['article_url'])