def job(scheduled_time):
    import os
    import shutil
    from News.news import scrape
    from Whatsapp.whatsapp import send_message

    os.mkdir("News/temp")
    scrape()
    contact_list = ["+91 60057 47938", "Harish Tomar AIT", "Ankit Yadav KV", "Adarsh Singh Comp AIT"]
    message = f"This message is autogenerated and is scheduled at {scheduled_time}. You will daily receive this message at the same time. Happy reading!"
    pdf_loc = "Whatsapp News/News/temp/"
    send_message(message, pdf_loc, contact_list)
    shutil.rmtree("News/temp/", ignore_errors = False)

def schedule_job():
    import schedule
    import time
    scheduled_time = "13:43"
    schedule.every().day.at(scheduled_time).minutes.do(job, scheduled_time)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    schedule_job()