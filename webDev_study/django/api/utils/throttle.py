from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

# import time
# """
# # 访问频率控制
# """

# VISIT_RECORD = {}  #这东西最好放DJANGO 的缓存里

# class VisitThrottle(BaseThrottle):
#     def __init__(self):
#         self.history = None  # 类内全局变量

#     # 60s内只能访问3次
#     def allow_request(self, request, view):
#         # 1 获取IP地址
#         #remote_addr = request.META.get('REMOTE_ADDR')
#         remote_addr = self.get_ident(request)  #替换上面那句话 获取用户唯一标识
#         ctime = time.time()
#         print('IP:', remote_addr, ' time:', ctime)

#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [
#                 ctime,
#             ]
#         history = VISIT_RECORD.get(remote_addr)
#         self.history = history
#         while history and history[-1] < ctime - 10:  # 10秒内访问3次
#             history.pop()  #大于一分钟就删除
#         if len(history) < 3:
#             history.insert(0, ctime)
#             return True
#         else:
#             return False

#     def wait(self):
#         """
#         # 还需要等多少秒
#         """
#         ctime = time.time()
#         return 10 - (ctime - self.history[-1])


class VisitThrottle(SimpleRateThrottle):
    """
    对匿名用户的限制
    """
    scope = "Luffy"  # 随便写的 当KEY用的

    def get_cache_key(self, request, view):
        return self.get_ident(request)  # 使用IP判断


class UserThrottle(SimpleRateThrottle):
    """
    对已登录的用户的限制
    """
    scope = "LuffyUser"  # 随便写的 当KEY用的

    def get_cache_key(self, request, view):
        return self.request.user.username  # 改用用户名判断
