# Forking and pull requests

*[CEGM1000 MUDE](http://mude.citg.tudelft.nl/)*

*Written by: Tom van Woudenberg & Robert Lanzafame*

Let's practice forking and pull requests with an iceclassic prediction!

## Task 1.1 Open public repo

Open the public repository https://github.com/MUDE-2025/iceclassic. The repo already contains a figure that displays all of the historic breakup days and times, and the predictions of MUDE students will be added on top.

## Task 1.2 Fork repository

You cannot just edit this repository as you don't have editing-rights. However, forking is a powerful GitHub feature which allows you to make your changes and propose them back to the original repository. Click `Fork` on the `Code` page of the public repository to create a fork in your own account.

![Fork repository](https://files.mude.citg.tudelft.nl/fork1.png)

## Task 1.3 Add prediction to fork
To add your prediction, add your GitHub username in the list in `data/predictions.txt` and enter a prediction in the format (YYYY-MM-DD HH:MM:SS) (year,month, day, hour minute, seconds). 

The repo is set up to automatically update the figure every time a commit is made. However, for your fork this is disabled for security reasons. If you want to see your prediction being added to the figure in your own repo, enable workflow under `Actions`.

## Task 1.4 Open Pull request to original repository

Open a pull request to the original repository by clicking `Contribute` or manually starting a Pull request from `Pull request` in the taskbar.

![Contribute button](https://files.mude.citg.tudelft.nl/contribute.png)

Create the pull request, and verify that you compare it to the original MUDE-2025/iceclassic repository

![Compare branches](https://files.mude.citg.tudelft.nl/fork_merge.png)

## Task 1.5 Expect merge conflicts?

While waiting for the MUDE-team to approve your pull request, do you expect merge conflicts? Maybe they emerge while other pull requests are being merged. Try and fix the conflicts so that the MUDE-team doesn't have to do it ;)

![Fork repository](https://files.mude.citg.tudelft.nl/merge_conflicts_ice.png)

> Copyright 2025 MUDE, Delft University of Technology. This work is licensed under a CC BY 4.0 License