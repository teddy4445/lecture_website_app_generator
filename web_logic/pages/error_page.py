from web_logic.pages.ipage import IPage


class ErrorPage(IPage):

    def __init__(self, seo_page):
        IPage.__init__(self, seo_page=seo_page)

