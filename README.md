# asciifarm-client
The client for Asciifarm

[Asciifarm rust server](https://github.com/jmdejong/rustifarm)  
[Asciifarm python server](https://github.com/jmdejong/asciifarm)

![asciifarm screenshot](https://github.com/jmdejong/rustifarm/blob/master/img/Screenshot_2020-04-12_11-31-20.png)

## About Asciifarm

Asciifarm is a multiplayer RPG/farming game that is played in the terminal.

The intended use is to play this servers with a shared login (through ssh) but it can be played in other contexts too.

Players can fight enemies and plant crops to gather resources.

## Installation/Running

_a better installation with pip will be added in the future_

The asciifarm client requires [ratuil](https://github.com/jmdejong/ratuil) version 0.3.0 (at least) to run.
To install ratuil run:

    python3 -m pip install --user ratuil

To install the client download or clone this repository.
Make sure the current working directory is the root folder of the repository.
Then run `python3 -m asciifarmclient`.

## Controls

The controls can be customised by giving a new keybindings file.
Assuming that you haven't done this the most important controls are as follows:

- `wasd`, `hjkl` or arrow keys: move around
- `e`: pick up an item from the same tile
- `q`: drop the currently selected item from the inventory
- `c` or `+`: select the next item in the inventory
- `x` or `-`: select the previous item in the inventory
- `b` or `*`: switch between viewing the ground and the inventory
- `E`: Use the selected inventory item. Using an item can have mean several things depending on the item. For example eat it (for food), plant it (for seeds) or equip it (for weapons and armour) or unequip it (if the item was equipped already)
- `f`: attack something attackable on the same or adjacent tiles
- `r`: interact with something on the same or adjacent tiles. Interact could mean harvest a plant, open/close a door, read a sign or talk with an npc
- `pageup`: scroll the chat messages up
- `pagedown`: scroll the chat messages down
- `t` or `enter`: send a message or command in the chat. Commands start with `/`
- `/`: send a message or command in the chat and fill in a `/` already. This is the same as first pressing `t` and then pressing `/`

When entering a message or command `enter` will send the message / execute the command, `escape` will trow away the message and `tab` will take you back to the game input, but leave the message so you can continue it the next time you start send a message/command.


## Command line arguments

Run `python3 -m asciifarmclient --help` to see the list of command line arguments.

    $ python3 -m asciifarmclient --help
    usage: __main__.py [-h] [-n NAME] [-a ADDRESS] [-s {abstract,unix,inet}] [-k KEYBINDINGS] [-c CHARACTERS] [-o LOGFILE] [--reset-style] [--blink-bright-background]
                    [-l | -b]

    The client to AsciiFarm. Run this to connect to to the server.

    optional arguments:
    -h, --help            show this help message and exit
    -n NAME, --name NAME  Your player name (must be unique!). Defaults to username on inet sockets and tildename on unix socket (including abstract). Apart from the tilde in a tildename all characters must be unicode letters, numbers or connection puctuation. The maximum size of a name is 256 bytes when encoded as utf8
    -a ADDRESS, --address ADDRESS
                            The address of the socket. When the socket type is 'abstract' this is just a name. When it is 'unix' this is a filename. When it is 'inet' is should be in the format 'address:port', eg 'localhost:8080'. Defaults depends on the socket type
    -s {abstract,unix,inet}, --socket {abstract,unix,inet}
                            the socket type. 'unix' is unix domain sockets, 'abstract' is abstract unix domain sockets and 'inet' is inet sockets.
    -k KEYBINDINGS, --keybindings KEYBINDINGS
                            The file with the keybinding configuration. This file is a JSON file.
    -c CHARACTERS, --characters CHARACTERS
                            The file with the character mappings for the graphics. If it is either of these names: ['default', 'halfwidth', 'hw', 'fullwidth', 'fw', 'emoji'] it will be loaded from the charmaps directory.
    -o LOGFILE, --logfile LOGFILE
                            All game messages will be written to this file.
    --reset-style         Reset the style when it changes. Useful on some terminals
    --blink-bright-background
                            Use blink attribute to make background brighter. Useful for terminals that don't have bright backgrounds usually. Implies --reset-style
    -l, --colours, --colors
                            enable colours! :)
    -b, --nocolours, --nocolors
                            disable colours! :)

        Gameplay information:
            Walk around and explore the rooms.
            Kill the goblins and plant the seeds.

        ~troido
