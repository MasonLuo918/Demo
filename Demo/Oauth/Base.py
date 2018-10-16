import json
import urllib
import re

class Oauth_Base(object):
    #绑定对应第三方应用的App_id,App_key和redireci_url
    def __init__(self,client_id,cliend_key,redireci_url):
        self.client_id = client_id
        self.client_key = cliend_key
        self.redireci_url = redireci_url

    def _get(self,url,data):
        request_url = "%s?%s" %(url,urllib.parse.urlencode(data))
        response = urllib.request.urlopen(request_url)
        return response.read()

    def _post(self,url,data):
        request = urllib.request.Request(url=url,data=urllib.parse.urlencode(data).encode("UTF8"))
        response = urllib.request.urlopen(request)
        return response.read()

    def get_auth_url(self): #获取code,授权页面
        pass

    def get_access_token(self):
        pass

    def get_open_id(self):
        pass

    def get_user_info(self):
        pass

    def get_email(self):
        pass

class Oauth_yiban(Oauth_Base):
    def get_auth_url(self):
        url = "https://openapi.yiban.cn/oauth/authorize"
        params = {
            "client_id":self.client_id,
            "redirect_uri":self.redireci_url,
            "state":1
        }
        url = "%s?%s" % (url,urllib.parse.urlencode(params))
        return url

    def get_access_token(self,code):
        params = {
            "client_id":self.client_id,
            "client_secret":self.client_key,
             "code":code,
             "redirect_uri":self.redireci_url
        }
        url = 'https://openapi.yiban.cn/oauth/access_token'
        response = self._post(url,params)
        result = json.loads(response.decode('utf-8'))
        self.access_token = result['access_token']
        self.openid = result['userid']
        return self.access_token

    def get_open_id(self):
        return self.openid

    def get_user_info(self):
        url = 'https://openapi.yiban.cn/user/me'
        params = {
            "access_token":self.access_token
        }
        response = self._get(url,params)
        result = json.loads(response.decode("utf-8"))
        info = result['info']
        self.nickname = info['yb_username']
        return info

    def get_username(self):
        return self.nickname

