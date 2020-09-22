
import os

from .paths import keybindingsPath, charmapPath
from .charmap import CharMap
import json


standardKeyFiles = {
    "default": os.path.join(keybindingsPath, "default.json"),
    "azerty": os.path.join(keybindingsPath, "azerty.json")
}

def loadKeybindings(name):
    fname = None
    if name in standardKeyFiles:
        fname = standardKeyFiles[name]
    else:
        fname = name
    with open(fname) as f:
        data = json.load(f)
    bindings = {}
    help = ""
    for ftemplate in data.get("templates", []):
        if ftemplate.partition(os.sep)[0] in {".", ".."}:
            ftemplate = os.path.relpath(ftemplate, fname)
        template = loadKeybindings(ftemplate)
        bindings.update(template.get("actions", {}))
        help = template.get("help", help)
    bindings.update(data.get("actions", {}))
    help = data.get("help", help)
    return {"actions": bindings, "help": help}


standardCharFiles = {name: os.path.join(charmapPath, file) for name, file in {
    "default": "fullwidth.json",
    "halfwidth": "halfwidth.json",
    "hw": "halfwidth.json",
    "fullwidth": "fullwidth.json",
    "fw": "fullwidth.json",
    "emoji": "emoji.json"
}.items()}

def loadCharmapJson(name):
    
    fname = None
    if name in standardCharFiles:
        fname = standardCharFiles[name]
    else:
        fname = name
    with open(fname) as f:
        data = json.load(f)
    
    templates = []
    for ftemplate in data.get("templates", []):
        if ftemplate.partition(os.sep)[0] in {".", ".."}:
            ftemplate = os.path.relpath(ftemplate, fname)
        templates.extend(loadCharmapJson(ftemplate))
    
    templates.append(data)
    return templates

def loadCharmap(name):
    
    templates = loadCharmapJson(name)
    charmap = CharMap()
    for template in templates:
        charmap.apply_json(template)
    
    return charmap
