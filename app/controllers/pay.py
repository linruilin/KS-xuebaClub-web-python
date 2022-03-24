# coding=UTF-8
import json
import time
import requests
from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring, fromstring
from app.module.api import Api
from app.model.generalModel import GeneralModel
from app.model.transactionModel import TransactionModel
from app.model.weixinUser import WeixinUserModel
from weixin.pay import WeixinPay, WeixinPayError
from config import WEIXIN_APP_ID, WEIXIN_MCH_ID, WEIXIN_MCH_KEY, WEIXIN_NOTIFY_URL, WEIXIN_MCH_KEY_FILE, WEIXIN_MCH_CERT_FILE, WEIXIN_APP_SECRET, MONEY


# config = dict(WEIXIN_APP_ID=WEIXIN_APP_ID, WEIXIN_MCH_ID=WEIXIN_MCH_ID, WEIXIN_MCH_KEY=WEIXIN_MCH_KEY,
#               WEIXIN_NOTIFY_URL=WEIXIN_NOTIFY_URL, WEIXIN_MCH_KEY_FILE=WEIXIN_MCH_KEY_FILE, WEIXIN_MCH_CERT_FILE=WEIXIN_MCH_CERT_FILE)
# weixin = Weixin(config)

pay = WeixinPay(WEIXIN_APP_ID, WEIXIN_MCH_ID, WEIXIN_MCH_KEY,
                WEIXIN_NOTIFY_URL, WEIXIN_MCH_KEY_FILE, WEIXIN_MCH_CERT_FILE)


class PayControllers(Api, GeneralModel, TransactionModel, WeixinUserModel):
    def __init__(self):
        Api.__init__(self)
        GeneralModel.__init__(self)
        TransactionModel.__init__(self)
        WeixinUserModel.__init__(self)
        self.currentVersion = "1.0.0"  # 最新版本号

    def validationData(self, request, name):  # 验证参数 返回验证状态码
        try:
            statusCode = "2000"
            # method = request.method
            if name == "jspay":
                if request.form.get("openid", False) is False:
                    statusCode = "3023"
                elif request.form.get("userid", False) is False:
                    statusCode = "3024"
                # elif request.form.get("openid", False) is False:
                #     statusCode = "3023"
            elif name == "getCode":
                if request.form.get("code", False) is False:
                    statusCode = "3022"
            else:
                statusCode = "3005"
            return statusCode
        except Exception as e:
            statusCode = "3000"
            return statusCode

    def getCode1_0_0(self, request):  # 获取用户openID 版本1.0.0
        # https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx6e27c1aed0d91117&redirect_uri=http%3a%2f%2fwww.hzfxjy.net%2flogin&response_type=code&scope=snsapi_userinfo#wechat_redirect   授权链接
        try:
            statusCode = self.validationData(request, "getCode")
            if statusCode == "2000":
                user_code = request.form.get("code")
                url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid="+WEIXIN_APP_ID + \
                    "&secret="+WEIXIN_APP_SECRET+"&code="+user_code+"&grant_type=authorization_code"
                res = requests.get(url)
                resjson = json.loads(res.text)
                # {'access_token': '25_8IOvXtP8pbSniG7XB2vHo6ZUemm-IE3x27Hu1J_i28skrAJBjjSuto_KIcDlTPYk-4-UAWD8JxsOJ5-b7mi7yQ', 'expires_in': 7200, 'refresh_token': '25_Un886tU6swW0D2jVra-bYj-flbvIKlk0zqcAAlAfZn6m8WeplEcQxH1Ql8Wv1yTp2q7r4YHbHO-6vs9N3DdFkA', 'openid': 'oq5IC1JF2PvQow1H0YzZ09u81DKM', 'scope': 'snsapi_userinfo'}
                self.postWeixinUser(resjson)

                codeType = self.get_code(statusCode)
                codeType["data"] = resjson
                return codeType
            else:
                codeType = self.get_code(statusCode)
                codeType["data"] = resjson
                return codeType
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType

    def jsPay1_0_0(self, request):  # 请求发起js支付 版本1.0.0
        try:
            statusCode = self.validationData(request, "jspay")

            # 订单号
            order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(
                time.time()))) + str(time.time()).replace('.', '')[-7:]

            data = request.form.to_dict()
            data["order_no"] = order_no
            data["money"] = MONEY
            resData = self.postGeneral(data)
            openid = request.form.get("openid")
            if resData["code"] == "2000":
                raw = pay.unified_order(trade_type="JSAPI", openid=openid, body="学霸注册" + str(resData["data"]),
                                        out_trade_no=order_no, total_fee=MONEY, attach="学霸注册" +
                                        str(resData["data"]))

                raw2 = pay.jsapi(openid=openid, body="学霸注册" + str(resData["data"]), out_trade_no=order_no, total_fee=MONEY, attach="学霸注册" +
                                 str(resData["data"]))
                codeType = self.get_code("2000")
                codeType["data"] = raw2
                return codeType
            else:
                return resData
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType

    def callback1_0_0(self, request):
        try:
            _xml = request.get_data()
            # 拿到微信发送的xml请求 即微信支付后的回调内容
            xml = str(_xml, encoding="utf-8")
            print("xml", xml)
            return_dict = {}
            tree = fromstring(xml)
            # xml 解析
            return_code = tree.find("return_code").text
            print(return_code)
            if return_code == 'FAIL':
                    # 官方发出错误
                return_dict['message'] = '支付失败'
                return ""
                # return Response(return_dict, status=status.HTTP_400_BAD_REQUEST)
            elif return_code == 'SUCCESS':
                print(xml)

                data = {
                    "cash_fee": tree.find("cash_fee").text,
                    "fee_type": tree.find("fee_type").text,
                    "openid": tree.find("openid").text,
                    "out_trade_no": tree.find("out_trade_no").text,
                    "result_code": tree.find("result_code").text,
                    "time_end": tree.find("time_end").text,
                    "total_fee": tree.find("total_fee").text,
                    "transaction_id": tree.find("transaction_id").text
                }

                resData = self.postTransaction(data)

                if resData["code"] == "2000":
                    # 生成根节点
                    root = Element('xml')
                    code = SubElement(root, 'return_code')
                    SubElement(code, '![CDATA[SUCCESS]]')
                    msg = SubElement(root, 'return_msg')
                    SubElement(msg, '![CDATA[OK]]')
                    xml_string = tostring(
                        root, 'utf-8', method="xml").decode('utf-8')
                    return xml_string
                    # return ""
                else:
                    return ""
                # <xml>
                #     <appid><![CDATA[wx6e27c1aed0d91117]]></appid>
                #     <attach><![CDATA[学霸注册74]]></attach>
                #     <bank_type><![CDATA[CFT]]></bank_type>
                #     <cash_fee><![CDATA[1]]></cash_fee>
                #     <fee_type><![CDATA[CNY]]></fee_type>
                #     <is_subscribe><![CDATA[Y]]></is_subscribe>
                #     <mch_id><![CDATA[1552983241]]></mch_id>
                #     <nonce_str><![CDATA[62EbRzo4aLgRLdy4HWCIzwQ55V5NW8lS]]></nonce_str>
                #     <openid><![CDATA[oq5IC1JF2PvQow1H0YzZ09u81DKM]]></openid>
                #     <out_trade_no><![CDATA[201909050621533784769]]></out_trade_no>
                #     <result_code><![CDATA[SUCCESS]]></result_code>
                #     <return_code><![CDATA[SUCCESS]]></return_code>
                #     <sign><![CDATA[1DBD772B35D22E145194BD000F1EF994]]></sign>
                #     <time_end><![CDATA[20190905062158]]></time_end>
                #     <total_fee>1</total_fee>
                #     <trade_type><![CDATA[JSAPI]]></trade_type>
                #     <transaction_id><![CDATA[4200000385201909055342743998]]></transaction_id>
                # </xml>

            # <xml>
            #     <return_code><![CDATA[SUCCESS]]></return_code>
            #     <return_msg><![CDATA[OK]]></return_msg>
            # </xml>
        except Exception as e:
            print(e)
            return ""
