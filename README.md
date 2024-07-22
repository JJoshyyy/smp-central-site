# SMP Central Site


This repository contains the code for the SMPCentral website. You will find the profile pictures of each person in static/assets/ , and the logo in /static/assets/logo

/templates/ contains each .html file, along side with static/assets/css/
You can run the site by running `gunicorn -w 4 -b 0.0.0.0:8080 main:app` in the directory. Change `0.0.0.0` to the listening address (0.0.0.0 for listening on all addresses) and `8080` for the port the site will listen on. If using `8080`, I highly recommend using a reverse proxy like nginx

If you need any help, feel free to send me a DM either on [twitter](https://twitter.com/@yeahjenni_) or on [discord](https://discord.gg/maQQmb8Ycj)