import markdown
import mdx_macros
#from vxmain.model.primitives import Image

class SummationMacro(mdx_macros.BaseMacro):
    """
    A trivial macro that attempts to sum up a series of numbers.  Example
    usage::
    
        [[Sum(4,6,2,9)]]
    """
    name = 'Summation macro'
    key  = 'Sum'
    
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

class ImageMacro(mdx_macros.BaseMacro):
    """
    [[Image(name)]]
    """
    name = "Image Macro"
    key = "Image"
    
    def handler(self, name):
        #return "<img id=\"image_{0}\" src=\"/image/{0}asdf\" />".format(name)
        return "Name: {0}".format(name)

md = markdown.Markdown(
        extensions=['macros'],
        extension_configs={
            'macros': {
                'macros': [ImageMacro, SummationMacro]
                }
        })