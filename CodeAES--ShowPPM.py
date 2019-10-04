from Crypto.Cipher import AES
from Crypto import Random
import matplotlib.pyplot as plt
from PIL import Image

def main():
    key = Random.new().read(AES.block_size) #Creates key
    IV = Random.new().read(AES.block_size) #Initialization vector
    mode = AES.MODE_CFB #Sets encryption mode to CFB mode; CFB is great in avoiding the hassle of padding
    
    encryptor = AES.new(key, mode, IV) # Encryptor
    decryptor = AES.new(key, mode, IV) # Decryptor

    encrypt(key, mode, IV, encryptor) #Calls encryption function
    decrypt(key, mode, IV, decryptor) #Calls decryption function
    
    return 1

def encrypt(key, mode, IV, encryptor):

    input_data = Image.open("TestImage.jpg") #Reads image
    img_bytes = open("TestImage.jpg", "rb").read() #Reads image bytes
    plt.imshow(input_data) #Show image in console
    plt.show()
    img_data = Image.Image.getdata(input_data) #Image byte data
    
    encData = encryptor.encrypt(img_bytes) #Encryption line
    
    encFile = open("Encrypted.ppm", "wb") #creates encrypted file in directory
    encFile.write(b'P6 1499 1499 255\n')
    encFile.write(encData)
    encFile.close()

    return 1

def decrypt(key, mode, IV, decryptor):

    encFile2 = open("Encrypted.enc", "rb") #Opens encrypted file created earlier
    encData2 = encFile2.read()
    encFile2.close()

    decData = decryptor.decrypt(encData2) #Decryption line

    output_file = open("output.jpeg", "wb") #Creates decrypted file in directory
    output_file.write(decData)
    output_file.close()

    return 1

if __name__=="__main__":
    main()