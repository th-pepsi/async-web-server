import concurrent.futures
import time

# 定义一个耗时任务
def long_running_task(task_id):
    print(f"Task {task_id} started")
    time.sleep(5)  # 模拟耗时操作
    print(f"Task {task_id} completed")
    return f"Result of task {task_id}"

if __name__ == "__main__":
    # 创建一个进程池，最大工作进程数为 4
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        # 提交多个任务
        futures = [executor.submit(long_running_task, i) for i in range(10)]

        # 等待所有任务完成并获取结果
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
