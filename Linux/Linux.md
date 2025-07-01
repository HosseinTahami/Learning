# Linux

## Definitions

- **Kernel**: The Core part of the OS and responsible for managing the hardware.


- **Shell**: An interface between the user and the kernel. The most popular shells are bash and zsh.


- ***GNU**: Stands for GNU's Not Unix. 
  - Basically Linux is the kernel and GNU provides many important additional tools.

---
## File Structure
- `/ (root dir)`

  - `/dev`: Contains information about devices.

    - `sda`: First hard drive.

    - `sdb`: Second hard drive.

    - `sda1`: First partition of the first hard drive.

    - `sdb3`: Third partition of the second hard drive.

  - `/etc`: Contains configurations.

  - `/home`: Contains users informations.

  - `/mnt`: Contains information of mounted devices like hard drives.

  - `/tmp`: Contains temporary files.

  - `/root`: Similar to the `/home` directory but for the root user.

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

- **history**: Shows the history of your commands (last 500). 
  
  - Use `![number]` to repeat a specific command, or `!!` to repeat the last command.
  
  - All of these commands are saved in `/home/[username]/.bash_history` or `/home/[username]/zsh_history` base on your shell.
  
  - if you want to run a previous command in your history use `![number of the command]` such as `!990`.
  
  - if you want to run the last command use `!!`.

- **echo**: Prints or inserts text into a file. 

  - Use `echo [text] >> [file name]`.
  
  - `echo $[variable name]` will show you the value of that variable.

- **whoami**: Shows the current user.

- **su**: Allows you to switch to another user.
  
  - `su` stands for *substitude user*.
  
  - Use `su [username]` such as `su root` or `su hossein`.

- **sudo passwd root**: Allows you to change password of the root user.

- **sudo -i**: Gives you the root user access.

- **head**: Shows the first 10 lines of a file. 
  - Use `head -n [number] [file name]`.

- **tail**: Shows the last 10 lines of a file. 
  - Use `tail -n [number] [file name]`.

- **less**: Shows a file page by page and allows you to navigate up and down. 
  - Use `less [file name]`.

- **printenv**: Print environment variables.

- **export**: Creates or change the current value an environment variable. 
  - Use `export [VARIABLE NAME]="[value]"`.

- **unset**: Deletes an environment variable. Use `unset [VARIABLE NAME]`.

- **which**: Show each command is installed in which path or directory.
  - Use `which [command]` to get a path or directory address.

- **grep**: Searches for something in a file. Use `grep [something] [file name]`. 
  - Use `-w` for an exact word match.
  - Us `-c` to count the occurrences.
  - Use `-i` to ignore case.
  - Use `-r` so it will be recursive and look inside the directories for files and search them for `[something]`.
    - `grep .svg -r /var/*` this `*` means look inside this directory and search everything.

- **tr**: Gets an char as input to replace another char inside a file.

  ```bash
  tr " " "," << one.txt
  ```

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

## Nano 

- ***New Buffer :*** New File

- ***^X :*** Exit ==> CNTRL + X

- ***^O :*** Write out and save changes ==> CNTRL + O

- ***^K :*** Cut the selected text ==> CNTRL + K

- ***M-U :*** Undo ==> ALT + U

- ***M-A :*** Select Text ==> ALT + A

## ENV

This is a environment which saves the variables inside it and you can call each of them or change them to your favaurite value.

```bash
>>> printenv

SYSTEMD_EXEC_PID=3897
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
SESSION_MANAGER=local/RMFC:@/tmp/.ICE-unix/3864,unix/RMFC:/tmp/.ICE-unix/3864
GNOME_TERMINAL_SCREEN=/org/gnome/Terminal/screen/c9327be0_024a_4fdc_98a8_2a5564580a13
LANG=en_US.UTF-8
XDG_CURRENT_DESKTOP=ubuntu:GNOME
PWD=/home/hossein/Desktop
WAYLAND_DISPLAY=wayland-0
QT_IM_MODULE=ibus
USER=hossein
DESKTOP_SESSION=ubuntu
XDG_MENU_PREFIX=gnome-
OLDPWD=/home/hossein
HOME=/home/hossein
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
_=/usr/bin/printenv
GTK_MODULES=gail:atk-bridge
VTE_VERSION=8000
XDG_SESSION_DESKTOP=ubuntu
GSM_SKIP_SSH_AGENT_WORKAROUND=true
QT_ACCESSIBILITY=1
GNOME_DESKTOP_SESSION_ID=this-is-deprecated
GNOME_SETUP_DISPLAY=:1
LOGNAME=hossein
GNOME_TERMINAL_SERVICE=:1.234
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MEMORY_PRESSURE_WRITE=c29tZSAyMDAwMDAgMjAwMDAwMAA=
XMODIFIERS=@im=ibus
SHELL=/usr/bin/zsh
MEMORY_PRESSURE_WATCH=/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/session.slice
XDG_SESSION_TYPE=wayland
GNOME_SHELL_SESSION_MODE=ubuntu
XDG_RUNTIME_DIR=/run/user/1000
USERNAME=hossein
COLORTERM=truecolor
XAUTHORITY=/run/user/1000/.mutter-Xwaylandauth.I0XD92
XDG_DATA_DIRS=/home/hossein/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share
XDG_SESSION_CLASS=user
TERM=xterm-256color
GDMSESSION=ubuntu
DISPLAY=:0
SHLVL=1
P9K_TTY=old
_P9K_TTY=/dev/pts/0
ZSH=/home/hossein/.oh-my-zsh
PAGER=less
LESS=-R
LSCOLORS=Gxfxcxdxbxegedabagacad
LS_COLORS=rs=0:di=01;34:ln=01;...

```

```bash
>>> printenv USER

hossein
```

```bash
>>> printenv LANG

LANG=en_US.UTF-8
```

```bash
>>> printenv PWD

PWD=/home/hossein/Desktop
```

### PATH

- This is a environment variable which shows the directories which we saved the commands which we run in the terminal.

```bash
>>> printenv PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/home/hossein/.local/bin:/home/hossein/.local/bin
```
- As you can see there are multiple paths and directories which each of them are seperated by  `:` to don't get mixup.
```bash
/usr/local/sbin
/usr/local/bin:/usr/sbin
/usr/bin:/sbin:/bin
/usr/games
/usr/local/games
/snap/bin:/snap/bin
/home/hossein/.local/bin
/home/hossein/.local/bin
```
- ***Which*** command will show you each command is installed in which path and directory.

```bash
>>> which python3

/usr/bin/python3
```

```bash
>>> which uv
/home/hossein/.local/bin/uv
```

## Redirecting

### >

- Rewrite the file from the begining.

  ```bash
  echo [something] > [file-name]
  ```

### >>

- Adds to the previous content of the file.

  ```bash
  echo [something] > [file-name]
  ```

### 2> or 2>>

- If there was an error write it in the file.

  ```bash
  [The command which you want] echo [something] 2> [file-name]
  ```
- Example:

    ```bash
    mdkir /one 2>> errors.txt
    ```
### |

- get the output of one command and send it to another command

```bash
cat /etc/passwd | grep root
```