from fastapi import FastAPI
from celery import Celery
import os

# 初始化 FastAPI 应用
app = FastAPI(title="广告合规审核系统")

# 初始化 Celery
celery_app = Celery("tasks", broker=os.getenv("REDIS_BROKER_URL"))

@app.get("/")
def read_root():
    return {"message": "广告合规审核系统后端 API 运行中！"}

# 接下来我们会在这里添加路由
# @app.post("/tasks/submit_crawl")
# async def submit_crawl_task(shop_id: str):
#     from .tasks.crawl_task import start_crawl_task
#     task = start_crawl_task.delay(shop_id)
#     return {"task_id": task.id, "status": "processing"}
