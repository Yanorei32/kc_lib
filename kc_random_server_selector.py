import random

class KCRandomServerSelector:
    @classmethod
    def select(cls):
        # list cerated by http://203.104.209.7/gadget/js/kcs_const.js
        return random.choice([
            'http://203.104.209.71/',
            'http://203.104.209.87/',
            'http://125.6.184.215/',
            'http://203.104.209.183/',
            'http://203.104.209.150/',
            'http://203.104.209.134/',
            'http://203.104.209.167/',
            'http://203.104.248.135/',
            'http://125.6.189.7/',
            'http://125.6.189.39/',
            'http://125.6.189.71/',
            'http://125.6.189.103/',
            'http://125.6.189.135/',
            'http://125.6.189.167/',
            'http://125.6.189.215/',
            'http://125.6.189.247/',
            'http://203.104.209.23/',
            'http://203.104.209.39/',
            'http://203.104.209.55/',
            'http://203.104.209.102/',
        ])

