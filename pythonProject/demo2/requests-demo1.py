import requests
import random
import string

url = "http://8.148.31.14:8081/"
url2 = "http://sealong.yyboxdns.com:13811/"
#1.登录接口
session=requests.Session()
url1="%sphone_shop/user/login"%url2

data={
    "userName":"zhanlan",
    "userPass":"654321"
}

response1=session.post(url=url1,data=data)

# print(response1.text)

assert response1.status_code == 200,"第一个登录接口请求失败,状态码不是200"
assert response1.text == "success","登录接口返回的值不是success"
print("登录接口成功")

#2.获取商品接口
url2="http://sealong.yyboxdns.com:13811/phone_shop/goodsType/findAll"
response2=session.post(url=url2,data=data)
print(response2.json())


#3.用户收货地址查询
url3="http://sealong.yyboxdns.com:13811/phone_shop/address/findAddrByUserId"
response3=session.post(url=url3,data=data)
print(response3.text)
addrId=response3.json()[0]['addrId']
print(addrId)

#4.查询收藏商品接口
url4="http://sealong.yyboxdns.com:13811/phone_shop/guess/findFavorite"
response4=session.post(url=url4,data=data)
print(response4.text)


#5.添加收货地址接口
phone = random.randint(13000000000,18600000000)
print(phone)

name=string.ascii_letters
length=4
random_name=''.join(random.choices(name,k=length))
print(random_name)

name2="张李柳刘德非到付件啊卡的"
name3="".join([random.choice(name2) for _ in range(3)])
print(name3)

url5="http://sealong.yyboxdns.com:13811/phone_shop/address/addAddress"

data={
    "addrNickname":random_name,
    "addrPhone":phone,
    "addrProvince":"110000",
    "addrCity":"110200",
    "addrArea":"110228",
    "addrDetail":"翻斗花园101",
    "addrZipcode":"443000"
}
response5=session.post(url=url5,data=data)
print(response5.text)


#6.删除地址接口
url6="http://sealong.yyboxdns.com:13811/phone_shop/address/deleteAddress"
data={
    "addrId":"22"
}
response6=session.post(url=url6,data=data)
print(response6.text)


#7.加入购物车接口
url7="http://sealong.yyboxdns.com:13811/phone_shop/cart/addCart"
data={
    "num":"1",
    "goodsId":"3"
}
response7=session.post(url=url7,data=data)
print(response7.text)


#8.购物车查询接口
url8="http://sealong.yyboxdns.com:13811/phone_shop/cart/findCartByUser"
response8=session.post(url=url8,data=data)
print(response8.text)
cartId=response8.json()[0]['cartId']
print(cartId)

#9.提交订单接口
url9="http://sealong.yyboxdns.com:13811/phone_shop/order/takeOrder"
data={
    "addr":addrId,
    "goodslist":cartId
}
response9=session.post(url=url9,data=data)
print(response9.text)


#10.我的待支付订单接口
url10="http://sealong.yyboxdns.com:13811/phone_shop/order/findReadPayOrder"
response10=session.post(url=url10,data=data)
print(response10.text)
orderId=response10.json()[0]['orderId']


#11.订单支付接口
url11="http://sealong.yyboxdns.com:13811/phone_shop/order/toPay"
params={
    "orderId":orderId
}
response11=session.post(url=url11,params=params)
print(response11.text)