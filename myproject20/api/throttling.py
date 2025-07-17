from rest_framework.throttling import UserRateThrottle 

class EmanRateThrottle(UserRateThrottle):
    scope= 'eman'