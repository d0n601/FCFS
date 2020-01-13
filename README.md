# Sacramento Area Rental Scraper
This little script scrapes rental listings from a few property management companies in the greater Sacramento area. The script is very basic, it doesn't log anything in the database besides the link to the property listing to determine if the scraper has already seen the property. It's really basic, and I've tried to keep myself from over engineering it. It sends an email/text message when a new link is found, so that **you'll be first** in the first come first serve game.

#### Property Management Companies
* [RNB Property Management](https://www.rnbrentals.com/) 
* [Lyon Property Management](https://www.golyonpm.com/)
* [Vienna Property Management](https://www.viennapm.com/)
* [Ferguson Property Management](https://fergusonpm.com/)
* [Cornette Property Management](https://www.cornettemanagement.com/)
* [Action Property Management](https://actionproperties.net/)
* [Sacramento Delta Property Management](http://sacdelt.com/)


## Why?  
I was searching for a home and had compiled a list of property managers in the Sacramento region that took applications on a first come first serve basis. After speaking with a few of the companies I was told that they don't list their homes on [Zillow](https://zillow.com) right away. It can take two days to list on Zillow after listing the property on their own website. This means by the time you see it posted on Zillow, you're likely not going to be the FIRST applicant.

I built this for myself, not you. So you need to make the modifications that you need to make. I posted it for other home hunting hackers to modify at their will.  

*Are you sick of checking listings yourself every day? So was I.*  

*Do you know Python and want to use your skills to get a house over those that aren't hackers? So do/did I.*  

This is a good starting point, I doubt enough people will use it in my area to actually compete with me for homes, so happy house hunting!


## Installation
* Clone this repository or download the zip file. 
* Fill-in the email variables in `config.py.example` and rename it to `config.py`.
* Modify RNB's url to match your particular preferences (pets, location, etc)
* Install required dependencies `pip3 install mongo` and `pip3 install bs4`.
* Install MongoDB and configure your database.
* Setup cronjob to run on your server (if you aren't linux you fail) `# Setup your cron as such: */15 * * * * /usr/bin/python3 /PATH TO FILE/fcfs.py`. Don't forget to set the correct path to the script.


## To Do's  
**Note:** I'm not looking for homes anymore, but if and when I do, I'll get to these.  
* Track changes on RNB as they build new website.
* Combine all Rently, Appfolio and Showmojo companies into one function that has a url parameter.
* Modify configuration file for RNB instead of hard coded url.
* Write a better install description with a `requirements.txt` and MongoDB directions.
