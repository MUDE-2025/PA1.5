# Forking and pull requests

Let's practice forking and pull requests with an iceclassic prediction!

## Task 1.1 Open public repo

Open the public repository https://github.com/MUDE-2025/iceclassic. The repo already contains a figure that displays all of the historic breakup days and times, and the predictions of MUDE students will be added on top.

## Task 1.2 Fork repository

You cannot just edit this repository as you don't have editing rights. However, forking is a powerful GitHub feature which allows you to make your changes and propose them back to the original repository. Click `Fork` on the `Code` page of the public repository to create a fork in your own account.

![Fork repository](https://github.com/TUDelft-MUDE/source-files/raw/main/file/fork1.png)

## Task 1.3 Add prediction to fork
To add your prediction, add your student ID in the list in `data/predictions.txt` and enter a prediction in the format (YYYY-MM-DD HH:MM:SS) (year, month, day, hour, minute, seconds).

Keep the last line in `data/predictions.txt` empty. Git treats line endings carefully; if you accidentally add or remove the final empty newline, it may appear as if the previous line was deleted and re-added in your commit diff.

The repo is set up to automatically update the figure every time a commit is made. However, for your fork this is disabled for security reasons. If you want to see your prediction being added to the figure in your own repo, enable workflow under `Actions`.

## Task 1.4 Open Pull request to original repository

Open a pull request to the original repository by clicking `Contribute` or manually starting a Pull request from `Pull request` in the taskbar.

![Contribute button](https://github.com/TUDelft-MUDE/source-files/raw/main/file/contribute.png)

Create the pull request, and verify that you compare it to the original MUDE-2025/iceclassic repository

![Compare branches](https://github.com/TUDelft-MUDE/source-files/raw/main/file/fork_merge.png)

A workflow now starts to check whether your prediction is valid. If everything is correct, it will give a green checkmark and the MUDE Team will merge your pull request into the original repository.

## Task 1.5 Expect merge conflicts?

While waiting for the MUDE Team to approve your pull request, do you expect merge conflicts? Maybe they emerge while other pull requests are being merged. Try and fix the conflicts so that the MUDE Team doesn't have to do it ;)

![Fork repository](https://github.com/TUDelft-MUDE/source-files/raw/main/file/merge_conflicts_ice.png)

## Task 1.6 Request changes

If you didn't do this correctly, the MUDE Team will request changes. Fix these and push them to your fork. The pull request will automatically update.

> By Tom van Woudenberg and Robert Lanzafame, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).