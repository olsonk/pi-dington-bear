# pi-dington-bear

Tweet-controlled, picture-taking mobile robot controlled by Raspberry Pi

## Installation

On your pi, clone or download this repository. Edit the Twitter API keys by creating a Twitter app on your desired account and inserting the keys provided. Make sure you edit the twitter stream line in the `main()` function to reflect whatever Twitter account you're using

## Usage

1. In LXTerminal, edit your `rc.local` file by typing `sudo nano /etc/rc.local` and adding `python3 path/to/python/script &`
2. Hook up your ExplorerHatPro to wheels and DC motors; connect to pi
3. Install camera module
3. Boot your pi and make sure you have internet access
4. Tweet `pic`, `forward`, `backward`, `left`, or `right` to your twitter account to interact!

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

This project was created as part of the final project for Picademy USA, February 2016 at the Computer History Museum in Mountain View, CA. We came up with the idea after learning about using the `picamera` module and `gpiozero` modules.

## Credits

HUGE thanks to the @Raspberry_Pi team for inspiring and teaching us so much in two days!
- Kevin Olson (@olsonk408)
- Heather McLean (@hmcleanwp)
- Mark Meyers (@meywong)
- Qumisha Goss (@QatalystGoss)
- Blair Mishleau (@blairtheblur)

## License

MIT License
