from flask import Flask
from flask.ext.cdn import CDN

app = Flask(__name__)

#cdn domain name 
app.config['CDN_DOMAIN'] = 'cdn.yourdomain.com'

#timestamp is by default set to True when using Flask-CDN. Therefore, it will be appended to the end of the asset's URL
app.config["CDN_TIMESTAMP"] = False
CDN(app)
