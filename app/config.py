from re import DEBUG


class Config:  # contains configuration that are used in both production and development stages....
    '''
    General configuration parent class
    '''
class  ProdConfig(Config): # contains configuration that are used in production stages 
    '''
    Production configuration child class

    Args:
         Config: The parent configuration class with General configuration settings
         '''
class   DevConfig(Config): #contains configuation that are used in development stages
    '''
    Development configuration child case
    Args:
        Config: The parents configuration class with General configuration settings
        '''
    DEBUG = True # enables debug mode in our application..