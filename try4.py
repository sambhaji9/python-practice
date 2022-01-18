try:
    f = open("demofile.txt")
    try:
        f.write("Sambhaji Mane")
    except:
        print("Something went wrong when writing to this file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file.")