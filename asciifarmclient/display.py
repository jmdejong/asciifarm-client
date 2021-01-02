


import os
from ratuil.textstyle import TextStyle
from ratuil.layout import Layout
from .listselector import ListSelector


SIDEWIDTH = 20

ALPHABET = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

class Display:
    
    def __init__(self, screen, charmap, ratuil_args={}):
        self.screen = screen
        
        self.charmap = charmap
        
        fname = os.path.join(os.path.dirname(__file__), "layout.xml")
        self.layout = Layout.from_xml_file(screen, fname)
        self.layout.get("field").set_char_size(self.charmap.character_width)
        
        self.screen.clear()
        
        self.layout.update()
        
        # temporary, until these have a better place
        self.inventory = ListSelector(self.getWidget("inventory"))
        self.inventory._debug_name = "inventory"
        self.ground = ListSelector(self.getWidget("ground"))
        self.ground._debug_name = "ground"
        self.switch = ListSelector(self.getWidget("switchtitles"))
        self.switch._debug_name = "switch"
        
        self.switch.setItems(["inventory", "ground"])
        self.menus = {
            "inventory": self.inventory,
            "ground": self.ground
        }
        
        self.layout.get("switch").select(0)
        
    
    def getWidget(self, name):
        return self.layout.get(name)
    
    def resizeField(self, size):
        self.getWidget("field").set_size(*size)
        self.getWidget("fieldbackground").change()
    
    def drawFieldCells(self, cells):
        field = self.getWidget("field")
        for cell in cells:
            (x, y), spriteNames = cell
            if not len(spriteNames):
                char, fg, bg = self.charmap.get(' ')
            else:
                char, fg, bg = self.charmap.get(spriteNames[0])
                for spriteName in spriteNames[1:]:
                    if bg is not None:
                        break
                    _char, _fg, bg = self.charmap.get(spriteName)
            field.change_cell(x, y, char, TextStyle(fg, bg))
        
    
    def setFieldCenter(self, pos):
        self.getWidget("field").set_center(*pos)
    
    def setHealth(self, health, maxHealth):
        if health is None:
            health = 0
        if maxHealth is None:
            maxHealth = 0
        self.getWidget("health").set_total(maxHealth)
        self.getWidget("health").set_filled(health)
        self.getWidget("healthtitle").format({"filled": health, "total":maxHealth})
        
    
    def showInfo(self, infostring):
        self.getWidget("info").set_text(infostring)
            
    def selectMenu(self, *args, **kwargs):
        self.switch.select(*args, **kwargs)
        self.layout.get("switch").select(self.getSelectedMenu())
    
    def getSelectedMenu(self):
        return self.switch.getSelectedItem()
    
    def getSelectedItem(self, menu=None):
        return self._getMenu(menu).getSelected()
    
    def selectItem(self, menu=None, *args, **kwargs):
        self._getMenu(menu).select(*args, **kwargs)
    
    def _getMenu(self, name=None):
        if name is None:
            name = self.getSelectedMenu()
        name = name.casefold()
        return self.menus[name]
    
    def setInventory(self, items):
        self.inventory.setItems(items)
    
    def setInv(self, items):
        self.inventory.setItems([(":" if is_equipped else " ") + item for (item, is_equipped) in items])
    
    def setGround(self, items):
        self.ground.setItems(items)
        
    
    def addMessage(self, message, msgtype=None):
        if msgtype is not None:
            style = self.charmap.get_message_style(msgtype)
        else:
            style = None
        self.getWidget("msg").add_message(message, style)
    
    def log(self, message):
        self.addMessage(str(message))
    
    def scrollBack(self, amount, relative=True):
        self.getWidget("msg").scroll(amount, relative)
    
    def setInputString(self, string, cursor):
        self.getWidget("textinput").set_text(string, cursor)
    
    def update(self):
        self.layout.update()
        self.screen.update()
    
    def update_size(self):
        self.screen.reset()

