from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent overflow

    # Encrypting the image by adding the key to each pixel value
    encrypted_array = (img_array + key) % 256

    # Converting the array back to uint8 and then to an image
    encrypted_array = encrypted_array.astype('uint8')
    encrypted_img = Image.fromarray(encrypted_array)

    # Saving the encrypted image
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
   
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent overflow

    # Decrypting the image by subtracting the key from each pixel value
    decrypted_array = (img_array - key) % 256

    # Converting the array back to uint8 and then to an image
    decrypted_array = decrypted_array.astype('uint8')
    decrypted_img = Image.fromarray(decrypted_array)

    # Saving the decrypted image
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").strip().lower()
    
    image_path = input("Enter the path to the image: ").strip()
    
    output_path = input("Enter the path to save the output image: ").strip()
    
    key = int(input("Enter the encryption/decryption key (an integer): ").strip())

    # Perform the chosen operation
    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice == 'd':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please select 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
