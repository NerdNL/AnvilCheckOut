from ._anvil_designer import HomeTemplate
from ..FormItem1 import FormItem1
from ..FormItem2 import FormItem2
from ..FormItem3 import FormItem3
from ..FormItem4 import FormItem4
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import data_access


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run when the form opens.

  def load_component(self, cmpt):
    print(">> homeform", cmpt)
    self.content_panel.clear()
    self.content_panel.add_component(cmpt)
    
  def link_1_click(self, **event_args):
    self.set_active_link("link_1")
    self.load_component(FormItem1())

  def link_2_click(self, **event_args):
    self.set_active_link("link_2")
    self.load_component(FormItem2())
  
  def link_3_click(self, **event_args):
    self.set_active_link("link_3")
    self.load_component(FormItem3())
  
  def link_4_click(self, **event_args):
    self.set_active_link("link_4")
    self.load_component(FormItem4())

  def set_active_link(self, link):
    self.link_1.role = "selected" if link == "link_1" else None
    self.link_2.role = "selected" if link == "link_2" else None
    self.link_3.role = "selected" if link == "link_3" else None
    self.link_4.role = "selected" if link == "link_4" else None

  def primary_color_1_click(self, **event_args):
    var = "variable"
    text = f"test {var}"
    x=Notification("nieuw",  style="danger", title="titel", timeout=6).show()
    alert(text,  title="TEST", role="submit")
    x.hide()
