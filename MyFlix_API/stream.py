import os
          
def initiate_stream(filename="Danger_River"):
    try:
        if os.path.exists("output.log"):
            os.remove("output.log") 
        
        os.system('ffmpeg -re -i http://rtmp-server/mp4/' + filename + '.mp4 -vcodec copy -loop -1 -c:a aac -b:a 160k -ar 44100 -strict -2 -f flv rtmp://rtmp-server/stream/' + filename + ' > output.log 2>&1 < /dev/null &')
        return "success"
    except:
        return "error"
    
if __name__ == '__main__':
    initiate_stream()