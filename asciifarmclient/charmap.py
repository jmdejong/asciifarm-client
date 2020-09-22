

from .utils import get
from ratuil.textstyle import TextStyle
from ratuil import strwidth

ALPHABET = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def make_text_wide(char):
    if len(char) != 1:
        return char
    o = ord(char)
    if o >= ord('!') and o <= ord('~'): # printable ascii character
        return chr(o - ord("!") + ord('！')) # fullwidth ascii block
    if char == " ":
        return chr(12288) # ideographic space
    return char

def make_sprite_wide(sprite):
    (char, fg, bg) = sprite
    return (make_text_wide(char), fg, bg)


def parseSprite(sprite):
    if isinstance(sprite, str):
        return (sprite, None, None)
    char = get(sprite, 0, " ")
    fg = get(sprite, 1)
    bg = get(sprite, 2)
    return (char, fg, bg)

class CharMap:
    
    def __init__(self):
        self.mapping = {}
        self.default = ("?", None, None)
        self.message_styles = {}
        self.default_message_style = TextStyle()
        self.character_width = 1
        self.alphabet = ALPHABET
    
    def get(self, spritename):
        return self.mapping.get(spritename, self.default)
    
    def get_message_style(self, msgtype):
        return self.message_styles.get(msgtype, self.default_message_style)
    
    def apply_json(self, jsonmap):
        for name, sprite in jsonmap.get("mapping", {}).items():
            vals = parseSprite(sprite)
            self.mapping[name] = vals
        
        self.alphabet = jsonmap.get("alphabet", self.alphabet)
        
        for name, colours in jsonmap.get("writable", {}).items():
            fg = get(colours, 0)
            bg = get(colours, 1)
            for (letter, character) in zip(ALPHABET, self.alphabet):
                self.mapping[name + '-' + letter] = (character, fg, bg)
    
        if "default" in jsonmap:
            self.default = parseSprite(jsonmap["default"])
        for name, colour in jsonmap.get("msgcolours", {}).items():
            self.message_styles[name] = TextStyle(*colour)
        self.character_width = jsonmap.get("charwidth", self.character_width)
    
    def make_wide(self):
        self.default = make_sprite_wide(self.default)
        mapping = {}
        for key, sprite in self.mapping.items():
            mapping[key] = make_sprite_wide(sprite)
        self.mapping = mapping
        self.alphabet = "".join(make_text_wide(char) for char in self.alphabet)
        
