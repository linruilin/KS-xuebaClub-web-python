# coding=UTF-8

def net_nginx_ip(headers): # 获取nginx返回的ip
    ip_str = headers.get("X-Real-Ip") if not headers.get("X-Real-Ip") else headers.get("X-Forwarded-For")
    if not ip_str:
        return "0.0.0.0"
    else:
        return ip_str