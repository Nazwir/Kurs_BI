import pyodbc

def get_connection():
    conn = pyodbc.connect(
    #conn_str = (
            'DRIVER="Your Database Driver";'
            'SERVER="Your Server";'
            'DATABASE="Your Database";'
            'UID="Your Username";'
            'PWD="Your Password"'
        )
    return conn
    #return pyodbc.connect(conn_str)
