from ._anvil_designer import UploadFormTemplate
from anvil import *
import anvil.server
from anvil_extras.logging import Logger, DEBUG
logging = Logger(level=DEBUG, format="UPLOADFORM: {msg}")


class UploadForm(UploadFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the screen"""
    self.layout.reset_links()
    self.layout.link_1.role = 'selected'

  @handle("file_loader_1", "change")
  def file_loader_1_change(self, file, **event_args):
    logging.debug("file_loader_1_change")  
    mask = anvil.server.call('create_contour', file)
    self.image_1.source = mask
