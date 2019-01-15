import re
from lxml import etree
import requests
import time
from threading import Thread

from crawler import PostsCrawler
from mysql_manager import MysqlManager

max_threads = 10
interval = 20
mysql_mgr = MysqlManager(max_threads)

def post_crawl_task(topic):
    # Get 1st page of this topic
    post_crawler = PostsCrawler()
    post_crawler.get_content(topic['url'], 1)
    posts = post_crawler.get_posts()

    # Get number of pages of this topic
    page_count = post_crawler.get_max_page()

    print(topic['url'])
    print('page count', page_count)

    # Get the rest posts of this topic
    if page_count > 1:
        for i in range(2, page_count + 1):
            post_crawler.get_content(topic['url'], i)
            posts += post_crawler.get_posts()
    
    # Insert post of a topic
    i = 1
    for p in posts:
        # print(p)
        # print("=============================", i, "=============================")
        # print("")

        # Compose the post object
        post = {}
        post['topic_id'] = topic['id']
        post['content'] = p
        post['post_index'] = i
        mysql_mgr.insert_post(post)

        i += 1
    print('Post count:', i)
    # Mark this topic as finished downloading
    mysql_mgr.finish_topic(topic['id'])
    print("=============================", i, "=============================")

def wait_tasks_done(pool):
    for t in pool:
        if not t.alive():
            pool.remove(t)
        else:
            t.join()

if __name__ == "__main__":
    tick_start = time.time()
    while True:
        pool = []

        # Get a topic to grab its content
        topic = mysql_mgr.dequeue_topic()

        if topic is None:
            wait_tasks_done()
            exit(1)
        
        task = Thread(target=post_crawl_task, args=(topic,))
        task.start()
        pool.append(task)

        if len(pool) == max_threads:
            wait_tasks_done(pool)
            dur_task_run = time.time() - tick_start
            if dur_task_run < interval:
                time.sleep(interval - dur_task_run)
            tick_start = time.time()