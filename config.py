class Config:
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_BROKER_URL = 'pyamqp://admin:admin-pass@rabbit:5672//'
    DEBUG = True
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True


config = {
    'default': Config
}
