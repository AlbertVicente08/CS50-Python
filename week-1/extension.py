

text = input("Introduzca un nombre de archivo ===> ").lower()

if text.find(".gif") != -1:
    print(f"image/{text}")
    
elif text.find(".jpg") != -1:
    print(f"image/{text}")
    
elif text.find(".jpeg") != -1:
    print(f"image/{text}")
    
elif text.find(".png") != -1:
    print(f"image/{text}")
    
elif text.find(".pdf") != -1:
    print(f"application/{text}")
    
elif text.find(".txt") != -1:
    print(f"application/{text}")
    
elif text.find(".zip") != -1:
    print(f"application/{text}")
    
else:  
    print("application/octet-stream")
