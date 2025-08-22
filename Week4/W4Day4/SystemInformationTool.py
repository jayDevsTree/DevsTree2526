import os
import datetime

def system_info():
    print("System Information:")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"User: {os.getlogin()}")
    print(f"Operating System Name: {os.name}")
    
    try:
        import platform
        print(f"Platform: {platform.system()} {platform.release()}")
    except ImportError:
        pass
    print("Machine :" ,platform.machine())
    print(f"Current Date and Time: {datetime.datetime.now()}")
    
    print(f"Number of Environment Variables: {len(os.environ)}")

if __name__ == "__main__":
    system_info()
