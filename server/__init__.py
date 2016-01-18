# -*- coding: utf-8 -*-
from flask import Flask
from coffesploit.core.coffesplot import Coffesploit

csfserver = Flask(__name__)

csfserver.config.from_object('config')
main = Coffesploit()

#csfserver.config.update(
#    CELERY_BROKER_URL='redis://localhost:6379',
#    CELERY_RESULT_BACKEND='redis://localhost:6379')


#def task_run(plugin_name, status):
#    #print plugin_name, status
#    main.use(plugin_name)
#    main.pluginmanager.current_plugin.run(status)
#    return main.pluginmanager.current_plugin.result()


from server import views, models
