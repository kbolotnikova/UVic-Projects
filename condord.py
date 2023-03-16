import sys
import re

class condcord:
  def __init__(self, input_file=None, output_file=None):
    self.input_file = input_file
    self.output_file = output_file
    
    if(self.input_file_ != None and self.output_file != None):
      concordance = self.full_concordance()
      self.__write_to_output(concordance)
