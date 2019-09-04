# -*- coding: utf-8 -*-
import requests,random
import re,time

# 爬身份证信息
def idlit():
	idurl = 'http://id.8684.cn'
	reponse = requests.get(idurl)
	IDresult = re.findall('(<span class="table-td1">.*?span class="table-td4">)', reponse.text, re.S)
	idDict = dict()


	# 随机其中的一条数据
	while True:
		itemList = re.sub(r"</span>", "", re.sub(r'<span class="table-td\d">', "", IDresult[random.randint(0, len(IDresult)-1)])).split(" ")

		idDict['name'] = itemList[0]
		idDict['idNo'] = itemList[1]
		idDict['sex'] = itemList[2]
		idDict['age'] = itemList[4]
		if len(idDict['name'])%3 == 0:
			return idDict

def createBankNumber():
	#创建银行卡号
	"""
	#benginCode = [{"code":"622280","length":19,"name":u"建设银行","bankcode":"CCB"},
				  {"code":"622588","length":16,"name":u"招商银行","bankcode":"CMBCHINA"},
				  {"code":"622260","length":19,"name":u"交通银行","bankcode":"BOCO"},
				  {"code":"602969","length":16,"name":u"北京银行","bankcode":"BCCB"}]
	"""
	benginCode = [{"code": "622588", "length": 16, "name": u"招商银行", "bankcode": "CMBCHINA"}]

	bankCode = benginCode[random.randint(0, len(benginCode) - 1)]
	if bankCode["length"] == 16:
		BankNumber = bankCode["code"] + time.strftime("%d%H%M%S", time.localtime(time.time())) + str(
			random.randint(10, 99))
	else:
		BankNumber = bankCode["code"] + time.strftime("%m%d%H%M%S", time.localtime(time.time())) + str(
			random.randint(100, 999))

	bankCardInfo = {"BankNumber": BankNumber, "name": bankCode["name"], "bankcode": bankCode["bankcode"]}

	return bankCardInfo



if __name__ == "__main__":
	i = idlit()
	print i
	print i["name"]
	'''
	a= createBankNumber()
	print a
	print a['name']
	print type(a['name'])
	'''



