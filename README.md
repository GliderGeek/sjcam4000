# sjcam4000
I have an sjcam4000 action camera, which i want to use during cycling to record parts of the ride. It is positioned on my helmet, which makes it difficult to operate since the display is not accessible. In this project i build an iphone app which is able to control the camera from my phone, which is positioned on my handlebars.

## Goals / steps

- [x] Being able to start and stop video recording from script on laptop
- [ ] Test how long camera can idle with wifi active
- [x] Make basic python app with simple GUI
  - [ ] implement checking connection
- [ ] Make basic iphone app
  - [ ] beeware tutorial: https://docs.beeware.org/en/latest/tutorial/tutorial-0.html
  - [ ] make sure xcode old mac + new iphone combo works: https://chatgpt.com/share/67e6a12c-2ef0-8012-aed1-7f55c35ea605
- [ ] Combine all in iphone app

extra
[ ] Download movies/pictures from device

## How to use
- switch on sjcam4000
- turn on wifi
- connect laptop to sjcam wifi
- `python script.py` this will start recording, wait 5 seconds and stop recording

## Attribution
- https://how-i-did-that.blogspot.com/2014/11/reverse-engineering-sjcam4000-wifi-kind.html
- https://github.com/AdamLaurie/sjcam
