# Linux
---

## Definitions

- **Shell**: An interface between the user and the kernel. The most popular shells are bash and zsh.

---
## File Structure
- `/ (root)`
  - `/dev`: Contains information about devices.
    - `sda`: First hard drive.
    - `sdb`: Second hard drive.
    - `sda1`: First partition of the first hard drive.
    - `sdb3`: Third partition of the second hard drive.
  - `/etc`: Contains configurations.
  - `/home`: Contains user information.
  - `/mnt`: Contains information of mounted devices like hard drives.
  - `/tmp`: Contains temporary files.
  - `/root`: Similar to the home directory but for the root user.

---

## Shortcuts

- **CTRL + ALT + T**: Opens a terminal.
- **exit** or **CTRL + D**: Closes the terminal.

---

## Commands

- **pwd**: Print Working Directory.

- **clear**: Clears the terminal.

- **ls**: Lists everything in the current directory.

  - **ls -a**: Lists hidden files and directories. `-a` stands for all

  - **ls -l**: Lists files and directories with more detailed information and `-l` stands for long.

  - **ls -i**: Shows the inode of files.

- **mkdir**: Creates a directory. (Make Directory)

- **cd**: Changes the current directory.
  Use `cd ..` to move backward and `cd .` means the current directory.

- **uname -a**: Shows information about the operating system. `-a` stands for "all".

- **man**: Shows the manual for a command. Use `man [command]`.

- **type**: Tells if a command is a third-party or built-in command.

- **touch**: Creates a file.

- **rm**: Deletes a file. Use `rm [file name]`.

- **rm -r**: Deletes a directory. Use `rm -r [directory name]`. The `-r` means *recursive*.

- **cat**: Concatenates files. Use `cat -n [file name]` to show the contents of the file with line numbers.

- **nl**: Works like `cat -n`, but blank lines will not have numbers.

- **history**: Shows the history of your commands (last 500). Use `![number]` to repeat a specific command, or `!!` to repeat the last command. All of these commands are saved in `/home/[username]/.bash_history` or `/home/[username]/zsh_history` base on your shell.
  - if you want to run a previous command in your history use `![number of the command]` such as `!990`.
  - if you want to run the last command use `!!`.

- **echo**: Prints or inserts text into a file. Use `echo [text] >> [file name]`.

- **whoami**: Shows the current user.

- **sudo su**: Allows you to switch to another user. Use `su [username]`.

- **head**: Shows the first 10 lines of a file. Use `head -n [number] [file name]`.

- **tail**: Shows the last 10 lines of a file. Use `tail -n [number] [file name]`.

- **less**: Shows a file page by page and allows you to navigate up and down. Use `less [file name]`.

- **printenv**: Prints environment variables.

- **export**: Creates an environment variable. Use `export [VARIABLE NAME]="[value]"`.

- **unset**: Deletes an environment variable. Use `unset [VARIABLE NAME]`.

- **grep**: Searches for something in a file. Use `grep [something] [file name]`. Use `-w` for an exact word match, `-c` to count the occurrences, and `-i` to ignore case.

- **add-apt-repository**: Adds a repository to `/etc/apt/sources.list`, allowing you to install packages from that repository.

- **dpkg**: The underlying technology behind `apt-get`.
  - **dpkg -i**: Installs a package. Use `dpkg -i [app-name.deb]`.
  - **dpkg -r**: Removes a package. Use `dpkg -r [app-name.deb]`.
  - **dpkg -s**: Shows the status of a package. Use `dpkg -s [app-name.deb]`.
- **dpkg-reconfigure**: Resets a package to its default settings. Use `dpkg-reconfigure [package_name]`.

- **ps**: Shows processes. Use `ps -ef` to show all processes with detailed information.

- **top**: Shows processes interactively, similar to `ps` but live.

- **uptime**: Shows details about the system's uptime.

- **free**: Shows free space in memory and swap. Use `free -h` to show memory in gigabytes.

- **sleep**: Puts the terminal to sleep. Use `sleep [number] &` to run the command in the background. If you forget the `&`, you can use `CTRL+Z`.

- **jobs**: Shows background jobs.

- **fg**: Brings a background command to the foreground. Use `fg %[id]`.

- **bg**: Puts a foreground command in the background. Similar to `fg`, use `bg %[id]`.

- **kill**: Sends aI apologize for the incomplete response. It seems that the content got cut off. Could you please provide more details about the file you would like me to create? What specific information or topic would you like the file to cover?