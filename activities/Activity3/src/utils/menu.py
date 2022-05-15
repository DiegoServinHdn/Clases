from utils.s3_utils import S3Utils

class MenuException (Exception):
    pass

class Menu():

    @staticmethod
    def principal():
        print("Selecciona una opción: ")
        print("Opcion 1:  Subir archivo")
        print("Opcion 2:  Borrar archivo")
        print("Opcion 3:  Crear archivo")
        print("Opcion 4:  Listar archivos")
        opcion= int(input(">>" ))

        if opcion == 1:
            filename = input("Introduce la ruta del archivo local: ")
            bucket = input("Introduce bucket del archivo: ")
            key = input("Introduce el nombre del objeto: ") #mx-corp-landing <- Bucket #agregadores/uber/*parquet <- Key
            S3Utils.put_s3_files(filename, bucket, key)

        if opcion == 2:
            bucket = input("Introduce el bucket que deseas borrar: ")
            key = input("Introduce el nombre del objeto: ")
            S3Utils.delete_s3_file(bucket, key)

        if opcion == 3:
            bucketname = input("Introduce el bucket que deseas crear: ")
            S3Utils.create_bucket(bucketname)

        if opcion == 4:
            bucket = input("Introduce el bucket que deseas listar: ")
            folder = input("Introduce el nombre del folder: ")
            print(S3Utils.list_s3_folder(bucket, folder))
