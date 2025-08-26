from ..main import celery_app
import time

@celery_app.task(name="start_crawl_task")
def start_crawl_task(shop_id: str):
    """
    一个模拟的爬虫任务。
    未来会替换为真正的 Scrapy 爬虫。
    """
    print(f"正在为店铺 {shop_id} 启动爬虫任务...")
    time.sleep(10) # 模拟爬取耗时
    print(f"爬取任务为店铺 {shop_id} 完成。")
    return {"shop_id": shop_id, "status": "completed"}
