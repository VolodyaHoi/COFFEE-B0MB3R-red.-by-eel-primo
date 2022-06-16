import os, subprocess

# Errors
class LibInstallFailure(Exception):
    def __init__(self, lib_name, description):
        self.lib_name = lib_name
        self.description = description

    def __str__(self):
        return f"LibInstallFailure: Library {self.lib_name} wasn't installed! Cause: {self.description}"

class FileDownloadFailure(Exception):
    def __init__(self, filename, description):
        self.filename = filename
        self.description = description

    def __str__(self):
        return f"FileDownloadFailureFailure: File {self.filename} wasn't downloaded! Cause: {self.description}"

class FileUpdateFailure(Exception):
    def __init__(self, filename, description):
        self.filename = filename
        self.description = description

    def __str__(self):
        return f"FileUpdateFailureFailure: File {self.filename} wasn't updated! Cause: {self.description}"    

# Classes
class lib_installer:
    def __init__(self, libs):
        self.libs = libs

    def _download_lib_(self, lib_name):
        return os.system("py -m pip install " + lib_name)
    
    def install(self):
        #Just install all libs, no checking their avability
        print("Installing libs...")
        for lib in self.libs:
            result = self._download_lib_(lib)
            if result != 0:
                raise LibInstallFailure(lib, result)

        # Let's say for main program that we finished
        print("Finished!")
        return True

class file_updater:
    def __init__(self, files, path_on_github):
        self.files = files
        self.path = path_on_github

        li = lib_installer(['requests'])
        print("Upgrading requests lib...")
        li.install()      
        

    def _download_file_(self, filepath):
        import requests
        return requests.get(filepath, timeout=10).text
    
    def install(self):
        #Just install all libs, no checking their avability
        import hashlib
       
        should_restart_app = False
        is_windows = os.name == "nt"
        print("Updating files...")
        for file_id in range(len(self.files)):
            print("Updating file", file_id + 1, "out of", len(self.files))
            try:
                content = self._download_file_(self.path[file_id])
                content_hash_sha256 = hashlib.new('sha256')
                content_hash_sha256.update(content.encode('utf-8'))
                # check file hash, if hash != downloaded hash -> update!
                if is_windows:
                    # Windows sucks
                    print("Uh oh! Windows detected!")
                    print("ERROR! This lib is not supported for Windows")
                    print("File update cancelled")

                    hash_result = "-1"
                    '''
                    hash_result = subprocess.check_output("powershell Get-FileHash " + os.path.abspath(self.files[file_id])+ " -Algorithm sha256", shell=True).decode('utf-8').split(" ")
                    hash_result = list(dict.fromkeys(hash_result))             
                    '''               
                else:
                    # Linux/Darwin is OP!
                    with open(self.files[file_id], "r") as file:
                        file_hash_256 = hashlib.new('sha256')
                        file_hash_256.update(file.read().encode('utf-8'))
                        hash_result = file_hash_256.hexdigest()
                        file.close()
                print("Results of hashing:")
                print("Github content> ", content_hash_sha256.hexdigest())
                print("Local content > ", hash_result)
                if not content_hash_sha256.hexdigest() == hash_result.encode('utf-8') and not is_windows:
                    should_restart_app = True
                    try:
                        with open(self.files[file_id], "w", encoding='utf-8') as file:
                            file.write(content.replace('\n','').strip('\r'))
                            file.close()
                    except OSError as err:
                        raise FileUpdateFailure(self.files[file_id], err)
            # Too broad!
            except Exception as err:
                raise FileDownloadFailure(self.files[file_id], err)
            
        # Let's say for main program that we finished, and should user restart program
        print("Finished!")
        return should_restart_app

        
        
                
        
