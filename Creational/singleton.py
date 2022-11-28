# Simple implementation of the Singleton Pattern

class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    
# main method   
if __name__ == '__main__':   
  
   logger_one, logger_two = Logger(), Logger()
  
   assert logger_one is logger_two   
  
   print('Logger One : ', logger_one)   
   print('Logger Two : ', logger_two)   