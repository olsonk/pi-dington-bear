from twython import Twython, TwythonStreamer
from picamera import PiCamera
from time import sleep
from datetime import datetime
import explorerhat

APP_KEY = 'REPLACE WITH YOUR TWITTER APP DETAILS'
APP_SECRET = 'REPLACE WITH YOUR TWITTER APP DETAILS'
OAUTH_TOKEN = 'REPLACE WITH YOUR TWITTER APP DETAILS'
OAUTH_TOKEN_SECRET = 'REPLACE WITH YOUR TWITTER APP DETAILS'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            tweet_text = data['text']
            tweeter = data['user']['screen_name']
            if tweet_text.find('pic') != -1:
                try:
                    with PiCamera() as camera: # The part that takes pictures and tweets them
                        timestamp = datetime.now().isoformat()
                        photo_path = "/home/pi/pidington-img/%s.jpg" % timestamp
                        camera.capture(photo_path)

                        message = "Here's what I'm looking at, @%s! Taken %s" % (tweeter, timestamp)
                        with open(photo_path, 'rb') as photo:
                            twitter.update_status_with_media(status=message, media=photo)
                except:
                    print("Camera Error")
            elif tweet_text.find('forward') != -1:
                explorerhat.motor.one.forward()
                explorerhat.motor.two.forward()
                sleep(5)
                explorerhat.motor.one.stop()
                explorerhat.motor.two.stop()
            elif tweet_text.find('backward') != -1:
                explorerhat.motor.one.backward()
                explorerhat.motor.two.backward()
                sleep(5)
                explorerhat.motor.one.stop()
                explorerhat.motor.two.stop()
            elif tweet_text.find('left') != -1:
                explorerhat.motor.one.forward()
                sleep(2)
                explorerhat.motor.one.stop()
            elif tweet_text.find('right') != -1:
                explorerhat.motor.two.forward()
                sleep(2)
                explorerhat.motor.two.stop()
            else:
                message = "@%s Mention 'pic' in your tweet to take a picture" % tweeter
                twitter.update_status(status=message)
    def on_error(self, status_code, data):
        print (status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def main():

    sleep(30) #make sure USB wi-fi dongle is set up

    explorerhat.light.red.on()
    explorerhat.light.blue.on()
    explorerhat.light.green.on()
    explorerhat.light.yellow.on()
    sleep (2)
    explorerhat.light.red.off()
    explorerhat.light.blue.off()
    explorerhat.light.green.off()
    explorerhat.light.yellow.off()
    stream.statuses.filter(track='@PidingtonBear')
    
    """
    with PiCamera() as camera: # The part that takes pictures and tweets them
        camera.start_preview()
        sleep(3)
        timestamp = datetime.now().isoformat()
        photo_path = "/home/pi/pidington-img/%s.jpg" % timestamp
        camera.capture(photo_path)
        camera.stop_preview()

        message = "Here's a PiCamera picture! - Take 2!"
        with open('/home/pi/twitter-image.jpg', 'rb') as photo:
            twitter.update_status_with_media(status=message, media=photo)
"""
if __name__ == '__main__':
    main()
