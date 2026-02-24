import requests
import os
import sys
import re

if __name__ == "__main__":
    os.makedirs("videos/segments", exist_ok=True)
    print(sys.argv[1])
    if (sys.argv[1] == "-u"):
        url = sys.argv[2]
    elif (sys.argv[1] == "-n"):
        FileName = sys.argv[2]
    else:
        print(f"Usage: python {sys.argv[0]} -u [URL] -n [nameFile]")
        exit(1)
    
    if (sys.argv[3] == "-u"):
        url = sys.argv[4]
    elif (sys.argv[3] == "-n"):
        FileName = sys.argv[4]
    else:
        print(f"Usage: python {sys.argv[0]} -u [URL] -n [nameFile]")
        exit(1)
    
    match = re.sub("seg-[0-9]+-", "seg-{video}-", url)
    
    if(url == match):
        print(f"[!] Url invalid. Please check the url")
        exit(1)
    else:
        url = match
        
    FileName = re.sub(" ", "-", FileName)
    
    print("URL:", url)    
    print("FileName:", FileName)    
    os.makedirs("video/final", exist_ok=True)
    video = 1
    while(True):
        #os.system("cls")
        #url = f"https://iv-h.phncdn.com/xrygo-FhSgRtkaVjA7Dvf_jOj9M=,1755239470/hls/videos/202503/06/465390915/720P_4000K_465390915.mp4/seg-{video}-v1-a1.ts"
        #url = f"https://kv-h.phncdn.com/hls/c6251/videos/202508/14/19230845/720P_4000K_19230845.mp4/seg-{video}-v1-a1.ts?hdnea=st=1755578582~exp=1755582182~hdl=-1~hmac=9b1ce983146a5d4df6db7947441d2ac42e3ae762"

        response = requests.get(eval(f"f'''{url}'''"))
        #response = requests.get(url)
        
        if(response.status_code == 404):
            if(video > 10):
                print("All segments downloaded succesfully!")
                exit(0)
            else:
                print("Resource not found!")
                exit(1)
        if(response.status_code == 410):
            print("Link is gone! chek for new one")
            exit(1) # or break
        
        if response.status_code != 200:
            print(f"Status code: {response.status_code}, Response: {response.text}")
            exit(1)
            
        #print(f"{video} files saved") 
        print(f"Segment: {video} with status_code: {response.status_code}") 
        binaryData = response.content

        if(response.status_code == 200):
            #with open(f'videos/segments/{video}.ts', 'wb') as file:
                #file.write(binaryData)
            with open(f'videos/final/{FileName}.ts', 'ab') as file:
                file.write(binaryData)
                
        video += 1
    
    #print("Merging all video segments..")
    #os.makedirs("videos/final", exist_ok=True)
    #
    #with open("videos/final/video.ts", "wb") as video:
    #    video.write
    
