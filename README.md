# Simple-Challonge-Ticker
Very simple program that pushes Challonge matches to text file for an OBS ticker.

Created for Python 2.7. You'll have to install pychallonge and dateutil as they are dependencies. If you're only interested in running the program, you can just grab the compiled .exe of the ticker for Windows.

This program hooks a Challonge bracket and publishes a given recently completed or upcoming match to a text file.

It has both normal and subdomain support. For subdomains, simply enter the subdomain first followed by a dash (-), then the tournament name.

For example: "moal-MoaL41MeleeSingles" would pull from http://moal.challonge.com/MoaL41MeleeSingles

You can vary how many upcoming or completed matches you'd like to publish to the text file. You then hook the text file to an OBS ticker object, and you're all set to go.

Hope you enjoy, this was a really simple fast project for something that can be really unique for your competitive stream.
