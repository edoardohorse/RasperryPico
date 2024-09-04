import lib.sh1107 as sh1107
import time
import sys
from types.types import Sizes
from lib.stringPoly import ljust

COLORS={
  "BLACK":0,
  "WHITE":1
}

class Test:
   display: sh1107.SH1107_SPI
   sizes: Sizes

   def __init__(self, display:sh1107.SH1107_SPI, sizes: Sizes) -> None:
     super().__init__()

     self.display  = display
     self.sizes    = sizes
    
   def run(self):
     pass

   def clear(self):
    self.display.fill(0)
    self.display.show()

   def log(self, nameTest: str, prefix: str = "-- Test: ", suffix:str = "."):
      nameTest = ljust(nameTest, 20, suffix)
      text: str = f"{prefix} {nameTest}"
      print(text, end='')

   def endLog(self, suffix:str = "DONE"):
      print(suffix, end='\n')

   def exit(self, code = 0):
    sys.exit(code)

class TestComplex(Test):
  
  def __init__(self, display: sh1107.SH1107_SPI, sizes: Sizes) -> None:
     super().__init__(
        display=display,
        sizes=sizes
        )

  def simple(self):
    self.log('Simple')
    self.display.sleep(False)
    self.display.fill(0)
    self.display.text('SH1107', 0, 0, 1)
    self.display.text('driver', 0, 8, 1)
    self.display.show()
    time.sleep(1)
      
    self.endLog()    
    return self
   
  def count0to10(self):
    global COLORS
    self.log('CountToTen')
    for i in range(10):
        self.display.large_text(s=str(i % 10), x=0,y=0, m=max(i,1), c=COLORS['WHITE'], r=90*i)
        self.display.show()
        time.sleep(0.1)
        self.display.fill(0)

    self.endLog()    

    return self

  def bigText(self):
    global COLORS
    self.log('BigText')
    for i in range(4):
      for j in range(5):
          """
          large text drawing function uses the standard framebuffer font (8x8 pixel characters)
          writes text, s,
          to co-cordinates x, y
          size multiple, m (integer, eg: 1,2,3,4. a value of 2 produces 16x16 pixel characters)
          colour, c [optional parameter, default value COLORS['WHITE']]
          optional parameter, r is rotation of the text: 0, 90, 180, or 270 degrees
          optional parameter, t is rotation of each character within the text: 0, 90, 180, or 270 degrees
          """
          self.display.large_text(s=str("big text"), x=(i) % 2 *56, y=(i+1) % 2 *32, m=2, c=COLORS['WHITE'], r=90*i, t=90*j)
          self.display.show()
          time.sleep(.2)
          self.display.fill(0)


    self.endLog() 
    return self
  
  def drawTrianglesAndCircles(self):
    global COLORS

    self.log('Triangles and Circles')
    for i in range (0, 32, 4):
      self.display.triangle(0+3*i, i, 127-i, i, 127-i, 127-3*i, c=COLORS['WHITE'])
      self.display.show()
      for i in range (0, 32, 4):
          self.display.triangle(i, 0+3*i, i, 127-i, 127-3*i, 127-i, c=COLORS['WHITE'])
          self.display.show()
      time.sleep(2)
      self.display.fill(0)
  #     display.show()
  #     display.triangle(0, 0, 0, 127, 127, 127, c=COLORS['WHITE'], f=True) 
  #     display.show()
  #     time.sleep(2)
      self.display.fill(0)
      self.display.show()
      for i in range (0, 64, 4):
          self.display.circle(64, 64, 64-i , c=COLORS['WHITE'])
          self.display.show()
      time.sleep(2)
      self.display.fill(0)
      self.display.show()
      for i in range (0, 128, 32):
          for j in range (0, 128, 32):
              self.display.rect(i, j, 32, 32, c=(i+j)//32 % 2, f=True)
              self.display.show()
              self.display.circle(i+16, j+16, 15 , c=((i+j)//32 +1) % 2, f=True)
              self.display.show()
      time.sleep(2)

    self.endLog() 
    return self

  def runTests(self):
    self.simple()
    self.count0to10()
    self.bigText().exit()
    self.drawTrianglesAndCircles()
    return self
