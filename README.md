## BREWMASTER! :beers:

Get info from a raspi about your homebrew setup.

#### featuring:

`Raspberry pi`
`Python3`
`Flask`

#### About

Brewmaster attempts to help you level up your homebrew game by giving you the info you need when you need it! It uses a simple http server (via [Flask](http://flask.pocoo.org)) and [Chart.js](http://www.chartjs.org) to show you the current temperature of your brew setup, and it logs all of the temperatures it has ever recorded.

You will need a temperature sensor (I use a waterproof DS18B20) and a raspberry pi to get this going! More instructions on temperature sensors are available [here](https://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi).

Simply set minimum temperature, maximum temperature, notification and refresh rate environment variables (otherwise default values will be used). To kick off the server use the provided script with `bash run.sh` then navigate over to http://localhost:5000 to view your graph!


#### Short Term goals:
- Temperature readout remotely  √
- Alerts for critical temps (too high/too low)
- Graph of temps  √


#### Wishlist / longterm:
- Remote temperature control
- Specific gravity readings
- Automated regulation

### Installation:

_I suggest using a [virtualenv](https://virtualenv.pypa.io/en/stable/) to manage your pip packages. To get started with virtualenv you can simply `pip3 install virtualenv` then create a virtualenv in your current direcetory with `python3 -m virtualenv venv`. Activation is as easy as `source venv/bin/activate`!_

0. Setup the mail linux command, there is a great tutorial [here](http://www.sbprojects.com/projects/raspberrypi/exim4.php). The important thing is the `mail` command works correctly, because that's how notifications are handled.

1. Clone this repo  
`git clone https://github.com/matthewpdias/brew-master.git`

2. Install the requirements (hopefully in a virtualenv !)  
`pip install -r reqirements.txt`

3. Setup your environment!  
`export NOTIFACTION_ADDRESS=you@email.com`  
`export MIN_TEMPERATURE=55`  
`export MAX_TEMPERATURE=72`

  You will also need to change the name of the temperature sensing device in log_temp.py to match your device's serial number (mine was 28-0516a4123aff) and any relevant file paths for your system unless they exactly match mine (I tried to use a vanilla raspbian install to make this easy).

4. Start the server  
`bash run.sh`

### Ideas
You _could_:
-  change the data being polled to show more points and get more detailed output

- Use an email adress associated with your phone number to get text alerts i.e. `5551234577@txt.att.net`,  `5551234577@vtext.com`, `5551234577@tmomail.net`, `5551234577@messaging.sprintpcs.com` depending on your carrier.

- setup port forwarding on your router to view your chart remotely (at your own network security risk!)
