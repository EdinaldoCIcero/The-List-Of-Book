from pprint import pprint, pformat
from ast import literal_eval



class DataSaveLoad():
    def __init__(self , path ):

        self.path = path

        pass

    def saveDataList( self ,list_datas , name_data_file , extension_file = ".dtsl"):
        with open( self.path + name_data_file + extension_file , 'w' ) as save_file:
            save_file.write( pformat( list_datas ) )

            #print("Saved_data_file_to " + save_file.name)

    def loadDataList(self , name_data_file , extension_file):
        data = None

        with open( self.path  + name_data_file + extension_file , 'r' ) as load_file:
            data = load_file.read()
            load_data = literal_eval(data) 
            #print("Load_data_file" + load_file.name)
            return load_data

    def loadDataListExtencioJoin(self , name_data_file ):
        data = None

        with open( self.path  + name_data_file, 'r' ) as load_file:
            data = load_file.read()
            load_data = literal_eval(data) 
            #print("Load_data_file" + load_file.name)
            return load_data


    def appendItenListSave(self , append_value_list , name_data_file , extension_file=".dtsl"):

        load_data_value = self.loadDataList(name_data_file = name_data_file , 
                                          extension_file   = extension_file
                                          )
        
        load_data_value.append(append_value_list)

        self.saveDataList(list_datas    = load_data_value, 
                        name_data_file  = name_data_file, 
                        extension_file  = extension_file
                        )


    def removeItenListSave(self , remove_value_list , name_data_file , extension_file=".dtsl"):

        load_data_value = self.loadDataList(name_data_file = name_data_file , 
                                          extension_file   = extension_file
                                          )
        try:
            load_data_value.remove(remove_value_list)

            self.saveDataList(list_datas    = load_data_value, 
                            name_data_file  = name_data_file, 
                            extension_file  = extension_file
                            )

        except Exception as e:
            pass

    def LoadDataDict(self , name_data_file , extension_file=".dtsl"):
        load_dict = None

        with open( self.path  + name_data_file + extension_file , 'r' ) as opened_dict:
            data = opened_dict.read()
            load_dict = literal_eval(data) 
            #print("Load" + opened_dict.name)

            
            return load_dict





            
                

                

