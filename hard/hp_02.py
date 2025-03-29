
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง

"""
    import multiprocessing
    import threading

    def worker():
        print("Working")

    if __name__ == "__main__":
        for _ in range(5):
            t = threading.Thread(target=worker)
            p = multiprocessing.Process(target=worker)
            
            t.start()
            p.start()
            
            t.join()
            p.join()

"""

# คำตอบ:
