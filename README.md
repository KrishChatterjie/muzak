# MUZAK

A site to sell you classic rock albums. 😄

## About The Project

I was told to create an e-commerce website, with both frontend and backend developed, within 48 hours. I created a website called Muzak, to sell rock n roll albums from the 70s and 80s. 🤘 

Here's what I came up with:
* A login page for existing users, and a register page for new ones.
* A shop page, to display all the albums, with a feature for Led Zeppelin.
* A cart page, to see all the products that fit your fancy.

Of course, I assume this was meant to be done using databases, but since I've had no prior experience with SQL or MongoDB, along with a tight time constraint, I've used a makeshift solution here, using two .json files to store the user details, along with the details of all the products, to still make it as scalable as I could. In the future, once I learn how to use and manipulate data with databases, this will be done the right way.

The website is responsive, however hasn't been tested for width less than 600px. This too will be corrected soon!

### Built With

These are the languages and framework used to build this website:
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KrishChatterjie/muzak.git
   ```
2. Create a virtual environment and activate it
   ```sh
   python3 -m venv env
   ```
3. Install the required modules within the environments
   ```sh
   pip install -r requirements.txt
   ```
4. Run app.py
   ```sh
   py app.py
   ```
5. Open localhost:5050 in your browser of choice.
