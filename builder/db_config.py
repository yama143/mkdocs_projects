from sqlalchemy import create_engine
from configparser import ConfigParser, RawConfigParser
import os
from sqlalchemy.engine import URL



class DbConfig:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.config_ini = 'db_config.ini'        
        self.section = 'osint_sqlmodel'


    def write_file(self):
        self.config.write(open(self.config_ini, 'w'))


    def generate_db_ini(self):
        # parser = ConfigParser()
        if not os.path.exists(self.config_ini):
            # config['postgresql'] = {'host': 'localhost', 'database': 'nadc', 'user': 'yourusername', 'password': 'yourpassword'}
            # write_file()
            config = RawConfigParser()

    # Please note that using RawConfigParser's set functions, you can assign
    # non-string values to keys internally, but will receive an error when
    # attempting to write to a file or when you get it in non-raw mode. Setting
    # values using the mapping protocol or ConfigParser's set() does not allow
    # such assignments to take place.
            section = 'postgresql'
            config.add_section(section)
            config.set(section, 'host', 'localhost')
            config.set(section, 'database', 'nadc_bravo')
            config.set(section, 'user', 'yourusername')
            config.set(section, 'password', 'yourpassword')


    # Writing our configuration file to 'example.cfg'
        with open(self.config_ini, 'w') as configfile:
            config.write(configfile)


    def config(self):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section, self.filename))
        return db

    def config_postgres(self):
        # print('###################################################')
        # print('###################################################')
        # print('###################################################')        
        # print(self.config_ini)
        # print(self.section)
        # section = 'database\\' + section
        # create a parser
        parser = ConfigParser()
        # read config file
        try:
            parser.read(self.config_ini)
        except Exception as e:
            print(e)
            print(self.config_ini)
            raise Exception("Something else happened")

        # get section, default to postgresql
        db = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            # print(type(params))
            for param in params:
                if param[0] == 'user':
                    # print('found user ' + param[1])
                    user = param[1]
                if param[0] == 'password':
                    # print('found host ' + param[1])
                    password = param[1]
                if param[0] == 'host':
                    # print('found host ' + param[1])
                    host = param[1]
                if param[0] == 'database':
                    # print('found database ' + param[1])                                                
                    database = param[1]
            db = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
        else:
            raise Exception(f"""Section {self.section} not found in the {self.config_ini} file""")

        return db    



    def get_central_engine():
        cfg = DbConfig()
        engine_string = cfg.config_postgres()    
        db_engine = create_engine(engine_string, isolation_level="AUTOCOMMIT")    
        return db_engine



def main():
    configuration = DbConfig()
    db = configuration.config_postgres()
    print(db)
    

if __name__ == "__main__":
    main()
    # print(current_dir)

    # print(config_ini)
    
    # # generate_db_ini()
    # filename  = config_ini 
    # section = 'localhost_pg'
    # # Using readlines()
    # file1 = open(filename, 'r')
    # lines = file1.readlines()  
    # [print(x) for x in lines]  
    
    
    # section = 
    # db = config_postgres(filename, section)
    # print(db)
    
    # print(db)


   
   
# def config_mssql(filename='db_config.ini', section='mssql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)

#     # get section, default to postgresql
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         # print(type(params))
#         for param in params:
#             if param[0] == 'user':
#                 # print('found user ' + param[1])
#                 user = param[1]
#             if param[0] == 'password':
#                 # print('found host ' + param[1])
#                 password = param[1]
#             if param[0] == 'host':
#                 # print('found host ' + param[1])
#                 host = param[1]
#             if param[0] == 'database':
#                 # print('found database ' + param[1])                                                
#                 database = param[1]
#         # db = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
#         # db = f"""mssql+pyodbc://{user}:{password}@{host}/{database}"""
#         # db = f"""mssql+pyodbc://{user}:{password}@{host}/{database}"""
#         # db = f"""mssql+pyodbc://{host}*\\SQLEXPRESS/{database};trusted_connection=yes"""
#         # db = f"""mssql+pymssql:/{user}:{password}@{host}/{database}"""
#         # db = f"""mssql+pymssql://{user}:{password}@{host}\\\\SQLEXPRESS/{database}"""
#         # db = f"""mssql+pyodbc://osint:osint@localhost:port/databasename?driver=ODBC+Driver+17+for+SQL+Server"""
#         # db = f"""mssql+pymssql://{host}\\SQLEXPRESS/{database}?trusted_connection=yes"""

#         # connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-AIJMJAR\SQLEXPRESS;DATABASE=nadc_flatwater;UID=osint;PWD=osint"
#         connection_string = "DRIVER={ODBC Driver 17 for SQL Server};" + f"""SERVER={host};DATABASE={database};UID={user};PWD={password}"""
#         db = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         # print()
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))

#     return db    
   