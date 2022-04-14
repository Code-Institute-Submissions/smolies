![SMOLIES](/images/smolies.gif)

# **Smolies** - classic 90s pet game
## *by Katarzyna Zurawska*

### [Click here to play the game](https://smolies.herokuapp.com/)
### [Click here to view the repository](https://github.com/katzur/smolies)

# Table of Contents:
1. [Introduction](#introduction)
2. [UX](#ux)
    * [Target Audience](#target-audience)
    * [Strategy and Goals](#strategy-and-goals)
    * [Scope - Features & Future Fearures](#scope-features-&-future-features)
    * [Structure - Flow Chart](#structure)
    * [Surface](#surface)
    * [Game Screenshots](#game-screenshots)
3. [Testing](#testing)
    * [PEP8](#pep8)
    * [Manual Testing](#manual-testing)
    * [Game functions tests](#game-functions-tests)
    * [Bugs and Fixes](#bugs-and-fixes)
4. [Deployment](#deployment)
5. [Used technologies and credits](#used-technologies-and-credits)
    * [Used technologies](#used-technologies)
    * [Used Libraries](#used-libraries)
    * [Media](#media)
    * [Other technologies](#other-technologies)
    * [Content and credits](#content-and-credits)

# Introduction
*Smolies* is a fun, simple text based game created fully in Python.
It was inspired by popular in the 90s pet games called *Tamagotchi*, where player was resposible for keeping their virtual pet happy and alive.
As *Smolies* is not trying to be a copy of it, it still brings the 90s nostalgia back!

# UX
## Target Audience
* Younger users - play fun, involving pet game, learn the concept of owning a pet and need of caring for it
* CLI games enthusiasts
* Users looking for quick entertainment game
* Mature users - nostalgia for the past games created in 80s and 90s

## Strategy and goals
The main goal was to create a simple, fun game based on Command Line Interface concept (terminal). 
The game page provides consistent styling, bringing back the memory of popular in 90s *Tamagotchi*. 
Game's terminal runs without any issues, and prompts users with bolded, colored mesages in response to their inputs. 
Button on the top of the terminal is clearly visible and allows the user to start/ restart the game at any time. 
Created code is easy to navigate thanks to numerous docstrings and comments, and allows implementation of future features.

## Scope - Features & Future Features
The scope of *Smolies - pet game* is currently defined by the following features:
* Functioning terminal based pet style game, inspred by 90s *Tamagotchi*.
* Visual banners and ASCII art graphics for more pleasant user experience.
* User can choose 1 of the 5 following types of animals: cat, dog, hamster, fish, bird.
* User can create a name for their chosen pet.
* Game allows the player to take one of the 6 following actions: 
    - give food to the pet
    - play with the pet
    - get new toys for the pet
    - teach new words to the pet
    - talk with the pet
    - quit the game
* Game has an inbuild timer that runs pet's age, hunger, and happiness levels in the background of each turn.
* Player needs to keep pet happy and well fed in order to keep it alive.
* Player can decide what words should the pet learn and talk with the pet, to check if the virtual pet remembers it (randomly chosen each time out of all learned words).
* Player can get new toys for the pet. Toys are unique for each type of animal.
* User can feed the pet and lower its hunger.
* User can play with the pet and raise the level of its joy.
* Player can quit the game at any time.
* In case of pet starving or reaching old age - pet can naturally pass away - like in original Tamagotchi games.

Features that are to be considered for future releases:
* Different types of ASCII arts based on chosen type of animal - for now more generic ones are in use.
* More changing background statistics.
* Mood function based on animal level of happiness and hunger - prompting user with messages.
* Additional game functions - care for animals hygene, sleep, etc.

## Structure
The structure of *Smolies* on the visual page level has been using gif animation in the background on the right side of the page, and
the game terminal on the left side. Above the terminal there's a clearly visible button, that allows the player to start/ restart the game.
It all provides an easy and intuitive access to the game itself and good user experience thanks to minimalistic, bold design. 
![PAGE LOOK](/images/page.png)

On the deeper level the game structure required planning the logic of game's functions flow, in order to provide clear and easy to navigate product.
Flow chart was used to secure game's natural logic and avoid unnecessary errors.
## [CLICK TO VIEW THE FLOW CHART](/images/flowchart.png)

## Surface
### Colors
The colors choice selected for the game's page is based on the rule of simplicity and minimalism. 
The black background is complimented by simple, white gif of a sleeping pet, white frame for the terminal, and cyan colored button. 
The whole page have a clean look and is easy to navigate. All the colors were intentionally picked to keep the clean design and great elements contrast.
Terminal prompts are displayed in various colors for pleasant user experience.
## [COLOR PALETTE](/images/colors.jpg)

### Images and favicon
* Favicon comes from [this page](https://www.pikpng.com/pngl/m/55-557559_toby-fox-undertale-annoying-dog-transparent-clipart.png)
* Background gif images comes from [Pixilart page](https://www.pixilart.com/art/annoying-dog-nap-time-4a79686562715e8)
* Banner for README was created by me on [VistaCreate page](https://create.vista.com/home/)
* ASCII arts used for the game come from [ASCII ART Archive](https://www.asciiart.eu/)

## Game Screenshots
Selected screenshots presenting different game options and outputs in the terminal:
* [Wrong input](/images/invalid-input.jpg)
* [Main menu](/images/menu.jpg)
* [Feeding](/images/feeding.jpg)
* [Playing](/images/playing.jpg)
* [Getting toys](/images/getting-toys.jpg)
* [Teaching new words](/images/teaching.jpg)
* [Talking with the pet](/images/talking.jpg)
* [Death](/images/dead.jpg)
* [Quit the game](/images/quit.jpg)

# Testing
## PEP8
Test using PEP8 validator to avoid conventions errors.
Pass without any errors.
![pep8](/images/pep8.jpg)

## Manual Testing
* Checked for incorrect type of data provided into the terminal. Ensured that the program triggers error messages for the users asking for correct input.
![Wrong input](/images/invalid-input.jpg)
* Tested various data input scenarios to ensure that user prompts won't break the game functionality:
    * entering numbers, spaces, special characters instead of letters, 
    * entering wrong pet type, making sure that capital/small letters wont break the functionality
    * entering wrong number type, letters, special characters in menu options to make sure it provides an error message
    * entering wrong number type, letters, special characters in functions for getting toys to make sure it won't let the user break the functionality
* I also performed tests when each new function was implemented in the process of game creation (additional print statements, constant terminal checks)
* Tested program as well in VSCode and regularly pushed deployments through GitHub and Heroku.
* Asked a few additinal people (game testers) to test the game and look for potential bugs.

## Game functions tests
* Wrong pet type input test
![wrong pet type](/images/test1.jpg)
* Wrong pet name input test 
![wrong name](/images/test2.jpg)
* Wrong menu option choice 
![wrong menu](/images/test3.jpg)
* Wrong word input type in teaching function
![wrong word](/images/test4.jpg)

## Bugs and Fixes
### **Fixed Bugs**
* Infinity loop problem with early menu options at the beginning of process of creating menu. 
*choice = input* broke the loop:
![infinity loop](/images/infinity-loop.jpg)

* Removing the @property decorator helped to fix the TypeError and run choice 2:
![property decorator](/images/property%20decorator.jpg)

* Fixed typos that were breaking the functions.
In this example - missing colon fixed the issue of main function functionality:
![typo](/images/typo.jpg)

* Name error fixed - using name of the functions that weren't yet defined
It was enough to put them temporary as a comment to be able to test the game's functionality of other functions.
![name error](/images/name-error.jpg)

* Biggest game bug that took a lot of time to fix:
Values of hunger and fun decreasing to minus values. (Due to user's action and working timer in the backround)
Reached out for mentor help, tutor support and thanks to the help of group member (Elvira, huge thank you to you and Dan!) - I was
able to fix the problem.
It was enough to remove "==" and add regular "=" in case of integers, as well as add additional if/ else statement for joy in timer.
![negative values](/images/negative%20values.jpg)

### **Remaining Bugs**
As much as the issue with negative values was fixed - it happens at times that joy value reaches -1. 
The game corrects itself in the following turn taken by the player, and turns the value to 0, as intended.
All the possible solutions to fix fully the issue were undertaken (reached out to my mentor, tutor support and additional help),
and it seems that the logic blocks the negative values for the hunger properly, but in case of joy this issue seems to be correcting itself with a slight delay.

# Deployment

## Forking The GitHub Repository
To use this code and make changes without affecting the original code you can do what is called 'Forking the repository'. 
By forking this repository you are given a copy of the code at that moment in time that you can use freely. 
To fork this repository you need to follow the following few steps:

1. Create an account or log into your existing GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/smolies), you are wanting to fork.
3. In the upper-right of the repository, click the 'Fork' button.
4. A copy of the Repository will now be available within your repositories.

You will now have a copy of the code available to clone and work on without affecting the original code.

## Cloning the Project.
To make a local clone of the project follow these steps:

1. Log into your GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/smolies).
3. In the upper section of the repository click the drop-down option: 'Code'.
4. Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it.
5. Open a new workspace in GitPod.
6. Open GitBash. In the bash terminal type 'git clone [copy url here from step 4]'
7. Press enter - the IDE will clone and download the repo.
8. GitBash will clone the repository into this directory.
9. Optionally type: 'python3 -m http.server' to host the website locally - it won't run the python file, only allow you see how it looks.
10. If you want to create a web-app from the repo, follow the instructions in "Heroku App Deployment".

## GitHub Desktop App
1. Log in to your GitHub account or create an account.
2. Navigate to the [Repository](https://github.com/katzur/smolies).
3. Select the 'Code' button above the file list on the right had side.
4. Select 'Open with GitHub Desktop'
5. Install GitHub Desktop Application.
6. The repo will be copied locally onto your machine.
7. If you want to create a web-app from the repo please follow the instructions in "Heroku App Deployment"

## Heroku App Deployment.
1. Create the GitPod repo from the [CI Template](https://github.com/Code-Institute-Org/python-essentials-template) via the GitPod button in GitHub.
2. Create an account or log into your existing Heroku account.
3. Click on: NEW in the top right corner and choose create a new app.
4. Enter a unique name for the Heroku app.
5. Click on: Create App.
6. Once the app is built, navigate to "Settings" and scroll down to "Config Vars". 
7. In the KEY input field enter PORT and in the VALUE input field enter 8000. Click ADD.
7. Scroll down and click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
3. Ensure that the python buildpack is above the node.js buildpack. You can click and drag the packs to re-arrange them.
1. Navigate to the "Deploy" section.
2. Scroll down to "Deployment Method" and select "GitHub".
3. Authorize the connection of Heroku to GitHub.
4. Search for your GitHub repository name, and select the correct repository.
5. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so. 
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.

# Used Technologies and Credits
## Languages
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)
+ a little bit of two below (for getting the heroku page final look):
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)

## Used Libraries
Puthon Libraries:
    * pyfiglet - to use ASCII fonts for game's banner
    * termcolor - to use colors and styling for fonts

## Media
* Favicon comes from [this page](https://www.pikpng.com/pngl/m/55-557559_toby-fox-undertale-annoying-dog-transparent-clipart.png)
* Background gif images comes from [Pixilart page](https://www.pixilart.com/art/annoying-dog-nap-time-4a79686562715e8)
* Banner for README was created by me on [VistaCreate page](https://create.vista.com/home/)
* ASCII arts used for the game come from [ASCII ART Archive](https://www.asciiart.eu/)

## Other technologies
* Flow chart was created online using [Diagrams website](https://app.diagrams.net/)
* VSCode and Notepad++ were additionally used for rewriting the code, when needed.
* [GitHub](https://github.com/) provided a repository for the game.
* [Heroku](https://dashboard.heroku.com/) provided deployment for the game.

## Content and credits
* GitHub Python Template from [Code Institute](https://codeinstitute.net/ie/)
* The inspiration for this project came from the 90s nostalgia and my love for old games like *Tamagotchi*.
* Python pet game functions flow inspiration and guidance came from two absolutely great tutorials:
    * [YT tutorial from MJ Codes](https://www.youtube.com/watch?v=7m6O9zqZFZ8). This video helped me to understand better the concept of pet game, and Python classes. I dodn't use the code itself, but took an inspiration for some of my own game functions. Huge thank you!
    * [Gabriel's video How to Make a Pet Simulator](https://junilearning.com/blog/coding-projects/python-pet-simulator/) - absolutely great source, that at the end turned into a base of my pet game. WOnderfully explained dictionaries, function flow, game testing in the process of creating and shown best habits of commenting and docstringing code. Couldn't be more greatful for this resource!
* [Stack Overflow](https://stackoverflow.com/) helped me in many situations with small and big Python issues. Very grateful for the knowledgeable community of Stack Overflow.
*  [Code Intitute's Slack](https://slack.com/) CI community provided all necessary help throughout the project development. 
Huge thank you to all the Slack CI fellow students, especially my MSLETB group, [Elvira](https://github.com/Elvira-94) and Dan for their time and help with code issue no one could solve, my mentor [Chris Quinn](https://github.com/10xOXR), my CI msletb-nov-2021 cohort facilitator [Kasia Bogucka](https://github.com/bezebee), and my boyfriend Dino, who provided great help and supported me even in the most stressful moments of developing this project. Thank you all!!!



