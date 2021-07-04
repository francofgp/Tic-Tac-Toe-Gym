# Tic-Tac-Toe-Gym

This is the Tic-Tac-Toe game made with Python using the PyGame library and the Gym library to implement the AI.
In this game you could play against the AI that I have created using the Gym libray and StableBaselines3

_Little overview_

![Imgur](https://i.imgur.com/iCHxCJh.gif)

## Execute it in your editor

---

**Python 3.7 required**

<br>
_(I hardly recommend the conda enviroment in order to run all the files)_

Use the package manager [conda](https://docs.conda.io/projects/conda/en/latest/commands/install.html) to install the same virtual environment that I used, this command will create a new virtual environment with the same libraries that I used:
<br>
**The my_enviroment.yml is in this repo**

```bash
conda env create -f my_environment.yml
```

Then to execute the app to:

```bash
python tictactoe.py
```

## What files are in this repo?

In this repo you can find the following file:

-   tictactoe.py: the main file made with Pygame that you need to execute it in order to play the game
-   Tic_Tac_Toe_Gym.ipynb: the file that creates the IA for the oponent. You can execute this in Google Colab if you want <br>
    <a href="https://colab.research.google.com/drive/12ZBuTc2p0faVHnvV_25XENLHUuKDL7Rf?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
-   model5millonesFinal.zip: the file that I import in tictactoe.py file; in this file is where I saved the AI

## About the AI

---

The AI for this game was created using Reinforcement Learning using the Gym Library and StableBaselines3. For this AI I specified all the tic-tac-toe rules and the model itself learnt the rules, after 5 millions steps.

## Showcase

#### Example

![Imgur](https://i.imgur.com/iCHxCJh.gif)

![Imgur](https://i.imgur.com/M1elgTi.gif)

### License

[MIT](https://choosealicense.com/licenses/mit/)
