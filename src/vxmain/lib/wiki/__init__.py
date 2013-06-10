import markdown
import mdx_macros
from vxmain.model import Image

class ImageMacro(mdx_macros.BaseMacro):
    """
    """
    name = "Image Macro"
    key = "Image"
    
    def handler(self, *args, **kwargs):
        total = 0
        for arg in args:
            try:
                total += arg
            except:
                pass
        
        if self.inline:
            return "<span class='sum'>%s</span>" % total
        return "<div class='sum'>%s</div>" % total

md = markdown.Markdown(
        extensions=['macros'],
        extension_configs={
            'macros': {
                'macros': [ImageMacro]
                }
        })