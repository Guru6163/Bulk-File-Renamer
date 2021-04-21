import os


def main():
  i=0
  path=input("Enter the Path of the Folder: ")
  path=path.replace("\\","/")
  for filename in os.listdir(path):
    my_dest="img"+str(i)+".jpg"
    soruce_file=path+filename
    my_dest=path+my_dest
    os.rename(soruce_file,my_dest)
    i+=1

if __name__ =="__main__":
  main()
