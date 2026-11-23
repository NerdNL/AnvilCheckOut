from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator
from anvil_extras import logging


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def link_home_click(self, **event_args):
    open_form('Home')
    self.link_1_click()
  
  def link_1_click(self, **event_args):
    open_form('UploadForm')

  def link_2_click(self, **event_args):
    open_form('FormItem2')

  def link_3_click(self, **event_args):
    open_form('FormItem3')


  def reset_links(self):
    self.link_1.role = ''
    self.link_2.role = ''
    self.link_3.role = ''






  