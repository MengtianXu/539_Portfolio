#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        try:
            path=str(self.request.path)
            template = JINJA_ENVIRONMENT.get_template('templates' + path+'.html')
            self.response.write(template.render({'path':path[1:]}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'path':'index'}))
    def post(self):
        try:
            path=str(self.request.path)
            template = JINJA_ENVIRONMENT.get_template('templates' + path+'.html')
            self.response.write(template.render({'path':path[1:]}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'path':'index'}))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/index', HomeHandler),
    ('/resume', HomeHandler),
    ('/interest', HomeHandler),
    ('/timeline', HomeHandler),
], debug=True)