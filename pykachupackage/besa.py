from datetime import datetime
import pytz

def show_manila_time():
    manila = pytz.timezone('Asia/Manila')
    time_now = datetime.now(manila)
    print(f"Besa's date and time in Manila, Philippines: {
            time_now.strftime('%Y-%m-%d %H:%M:%S')}")