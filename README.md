swampdemo
=========

SwampDragon simple demo app

Create a virtual environment

    mkvirtualenv myproject
    
Install Swamp Dragon

    pip install swampdragon
    
Create a database (and add an admin user)

    python manage.py syncdb
    

To start the project open two terminals 

Terminal 1:

    python manage.py runserver
    
Terminal 2:
    
    python manage.py socketserver
    
Open a browser to ```http://localhost:8000```

Open a second browser window to ```http://localhost:8000/admin/```

You can now add instances of the Foo model and see data populate as you add or edit models.

## Note

Tornado 4.0

If you experience Error during WebSocket handshake: Unexpected response code: 403 you might have to run the latest dev version of sockjs-tornado.

pip uninstall sockjs-tornado

pip install -e git+https://github.com/mrjoes/sockjs-tornado.git#egg=sockjs-tornado

This should solve the error message.

