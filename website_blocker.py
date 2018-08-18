import time
from datetime import datetime as dt

hosts_temp = "hosts_temp"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #the r means Suse row string to tell python not to use breaklines like \n
#you can use \\ as well

redirect = 	"127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
     #check time
     #if time is within our range, then we keep these urls in host file
     if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):  
        print("working hours..")
        with open(hosts_path, "r+") as file: #r+ lets you read and write
            content = file.read() #reads as a single string
            for website in website_list:
                if website in content:
                    pass #dont do anything
                else:
                    file.write(redirect + " " + website + "\n")

        time.sleep(5)
     else:
         with open(hosts_path, "r+") as file:
             content = file.readlines() #produces all the lines within a list
             file.seek(0) #place pointer before first character of file to insert new lines
             for line in content:
                 if not any(website in line for website in website_list): #any checks if the website name is in the website list
                     file.write(line)
             file.truncate() #removes everything below the new lines
         print('Fun hours...')
         time.sleep(5)

