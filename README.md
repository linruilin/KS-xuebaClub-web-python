# KS-xuebaClub-web-python

学霸club - python版本

## 创建虚拟环境

virtualenv env

## 启动虚拟环境

```sh
source env/bin/activate
```

## 生产环境启动

### 正常启动

```sh
./env/bin/gunicorn --config=gunicorn.py setup:app
```

### 后台启动

```sh
./env/bin/gunicorn --config=gunicorn.py setup:app --daemon
```

## 开发环境启动

需要修改启动文件(非python开发人员是用正式版本正常启动即可)

```sh
python setup.py runserver -d -p 31100
```

## 测试

### 测试指令

运行自动化测试

```sh
coverage run test.py
```

### 测试覆盖查询

```sh
coverage report
```
  
### 测试覆盖生成html

```sh
coverage html -d covhtml --omit=env/*,tests/*
```

### api 接口

接口名称:请求省市县接口

请求类型:get

请求url http:hzfxjy.net/api/area

请求参数

响应参数列表

| 变量名 | 含义       | 类型   |
|--------|------------|--------|
| code   | 状态代码   | string |
| msg    | 状态消息   | string |
| data   | 省市县数据 | Array  |

---

接口名称:验证手机号码

请求类型:post

请求url http:hzfxjy.net/api/isphone

请求参数

| 变量名 | 含义     | 类型   |
|--------|----------|--------|
| phone  | 电话号码 | string |

响应参数列表

| 变量名 | 含义     | 类型   |
|--------|----------|--------|
| code   | 状态代码 | string |
| msg    | 状态消息 | string |

---

接口名称:注册接口

请求类型:post

请求url http:hzfxjy.net/api/logup

请求参数

| 变量名         | 含义     | 类型   | 是否必填 |
|----------------|----------|--------|----------|
| phone          | 电话号码 | string | 是       |
| password       | 电话号码 | string | 是       |
| name           | 电话号码 | string | 是       |
| parentName     | 电话号码 | string | 是       |
| education      | 电话号码 | string | 否       |
| parentPhone    | 电话号码 | string | 是       |
| job            | 电话号码 | string | 否       |
| address        | 电话号码 | string | 是       |
| school         | 电话号码 | string | 是       |
| schoolArea     | 电话号码 | int    | 是       |
| grade          | 电话号码 | string | 是       |
| className      | 电话号码 | string | 是       |
| schoolRoll     | 电话号码 | string | 是       |
| schoolRollArea | 电话号码 | int    | 否       |

响应参数列表

| 变量名 | 含义                   | 类型   |
|--------|------------------------|--------|
| code   | 状态代码               | string |
| msg    | 状态消息               | string |
| data   | 注册账户ID（支付使用） | int    |

---

接口名称:登录接口

请求类型:post

请求url http:hzfxjy.net/api/login

请求参数

| 变量名   | 含义     | 类型   | 是否必填 |
|----------|----------|--------|----------|
| phone    | 电话号码 | string | 是       |
| password | 电话号码 | string | 是       |

响应参数列表

| 变量名 | 含义     | 类型   |
|--------|----------|--------|
| code   | 状态代码 | string |
| msg    | 状态消息 | string |

---

接口名称:获取支付参数

请求类型:post

请求url http:hzfxjy.net/api/pay/code

请求参数

| 变量名 | 含义     | 类型   | 是否必填 |
|--------|----------|--------|----------|
| code   | 用户code | string | 是       |

响应参数列表

| 变量名 | 含义         | 类型   |
|--------|--------------|--------|
| code   | 状态代码     | string |
| msg    | 状态消息     | string |
| data   | 微信返回消息 |        |

---

接口名称:发起js支付

请求类型:post

请求url http:hzfxjy.net/api/pay/order

请求参数

| 变量名 | 含义               | 类型   | 是否必填 |
|--------|--------------------|--------|----------|
| openid | openid             | string | 是       |
| userid | 用户注册后返回的id | string | 是       |

响应参数列表

| 变量名 | 含义     | 类型   |
|--------|----------|--------|
| code   | 状态代码 | string |
| msg    | 状态消息 | string |
| data   | 订单参数 |        |

---

接口名称:获取用户信息

请求类型:get

请求url http:hzfxjy.net/api/user/info

响应参数列表

| 变量名     | 含义                         | 类型   |
|------------|------------------------------|--------|
| code       | 状态代码                     | string |
| msg        | 状态消息                     | string |
| data.image | 用户头像如果为""使用默认头像 | string |
| data.name  | 用户名称                     | string |

---

接口名称:获取用户订阅

请求类型:get

请求url http:hzfxjy.net/api/user/info

响应参数列表

| 变量名     | 含义            | 类型   |
|------------|-----------------|--------|
| code       | 状态代码        | string |
| msg        | 状态消息        | string |
| data.money | 订单金额 单位分 | string |
| data.name  | 订阅名称        | string |
| data.time  | 支付时间        | string |
